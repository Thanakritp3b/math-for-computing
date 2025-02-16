import React, { useState } from 'react';

const InterpolationApp = () => {
  const [inputType, setInputType] = useState('function');
  const [functionInput, setFunctionInput] = useState('x*sin(x) - x^2 + 1');
  const [intervalStart, setIntervalStart] = useState('0');
  const [intervalEnd, setIntervalEnd] = useState('2');
  const [degree, setDegree] = useState('5');
  const [points, setPoints] = useState([]);
  const [selectedMethods, setSelectedMethods] = useState({
    sle: true,
    lagrange: false,
    parametric: false
  });
  const [results, setResults] = useState(null);
  const [error, setError] = useState(null);
  const [evaluationPoint, setEvaluationPoint] = useState('');
  const [evaluationResults, setEvaluationResults] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleFileUpload = (event) => {
    const file = event.target.files[0];
    if (file) {
      const reader = new FileReader();
      reader.onload = (e) => {
        const text = e.target.result;
        const rows = text.split('\n');
        const parsedPoints = rows
          .map(row => row.split(',').map(Number))
          .filter(point => point.length === 2 && !isNaN(point[0]) && !isNaN(point[1]));
        setPoints(parsedPoints);
      };
      reader.readAsText(file);
    }
  };

  const handleSubmit = async () => {
    try {
      setLoading(true);
      setError(null);
      
      const selectedMethodsList = Object.entries(selectedMethods)
        .filter(([_, selected]) => selected)
        .map(([method]) => method);

      if (selectedMethodsList.length === 0) {
        throw new Error('Please select at least one interpolation method');
      }

      const requestData = {
        type: inputType,
        methods: selectedMethodsList,
        ...(inputType === 'function' ? {
          function: functionInput,
          interval_start: parseFloat(intervalStart),
          interval_end: parseFloat(intervalEnd),
          degree: parseInt(degree)
        } : {
          points: points
        }),
        ...(evaluationPoint ? { evaluation_point: parseFloat(evaluationPoint) } : {})
      };

      const response = await fetch('http://localhost:5000/interpolate', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(requestData),
      });

      if (!response.ok) {
        const errorData = await response.json();
        throw new Error(errorData.error || 'Failed to calculate interpolation');
      }

      const data = await response.json();
      setResults(data);
      
      if (data.evaluation) {
        setEvaluationResults(data.evaluation);
      }
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={{ maxWidth: '800px', margin: '0 auto', padding: '20px' }}>
      <h1 style={{ marginBottom: '20px' }}>Interpolation Calculator</h1>

      <div style={{ marginBottom: '20px' }}>
        <div style={{ marginBottom: '10px' }}>
          <button 
            onClick={() => setInputType('function')}
            style={{ 
              marginRight: '10px',
              padding: '5px 10px',
              backgroundColor: inputType === 'function' ? '#007bff' : '#f8f9fa',
              color: inputType === 'function' ? 'white' : 'black',
              border: '1px solid #dee2e6',
              borderRadius: '4px'
            }}
          >
            Function
          </button>
          <button 
            onClick={() => setInputType('points')}
            style={{ 
              padding: '5px 10px',
              backgroundColor: inputType === 'points' ? '#007bff' : '#f8f9fa',
              color: inputType === 'points' ? 'white' : 'black',
              border: '1px solid #dee2e6',
              borderRadius: '4px'
            }}
          >
            Points
          </button>
        </div>

        {inputType === 'function' ? (
          <div>
            <div style={{ marginBottom: '10px' }}>
              <label style={{ display: 'block', marginBottom: '5px' }}>Function:</label>
              <input
                type="text"
                value={functionInput}
                onChange={(e) => setFunctionInput(e.target.value)}
                placeholder="e.g. x*sin(x) - x^2 + 1"
                style={{ width: '100%', padding: '5px' }}
              />
            </div>
            <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr 1fr', gap: '10px' }}>
              <div>
                <label style={{ display: 'block', marginBottom: '5px' }}>Start:</label>
                <input
                  type="number"
                  value={intervalStart}
                  onChange={(e) => setIntervalStart(e.target.value)}
                  style={{ width: '100%', padding: '5px' }}
                />
              </div>
              <div>
                <label style={{ display: 'block', marginBottom: '5px' }}>End:</label>
                <input
                  type="number"
                  value={intervalEnd}
                  onChange={(e) => setIntervalEnd(e.target.value)}
                  style={{ width: '100%', padding: '5px' }}
                />
              </div>
              <div>
                <label style={{ display: 'block', marginBottom: '5px' }}>Degree:</label>
                <input
                  type="number"
                  value={degree}
                  onChange={(e) => setDegree(e.target.value)}
                  min="1"
                  style={{ width: '100%', padding: '5px' }}
                />
              </div>
            </div>
          </div>
        ) : (
          <div>
            <label style={{ display: 'block', marginBottom: '5px' }}>Upload Points (CSV):</label>
            <input
              type="file"
              onChange={handleFileUpload}
              accept=".csv,.txt"
              style={{ marginBottom: '10px' }}
            />
            {points.length > 0 && (
              <div style={{ fontSize: '14px', color: '#666' }}>
                Loaded {points.length} points
              </div>
            )}
          </div>
        )}

        <div style={{ marginTop: '20px' }}>
          <label style={{ display: 'block', marginBottom: '5px' }}>Methods:</label>
          <div style={{ display: 'flex', gap: '20px' }}>
            <label>
              <input
                type="checkbox"
                checked={selectedMethods.sle}
                onChange={(e) => setSelectedMethods(prev => ({...prev, sle: e.target.checked}))}
              /> SLE
            </label>
            <label>
              <input
                type="checkbox"
                checked={selectedMethods.lagrange}
                onChange={(e) => setSelectedMethods(prev => ({...prev, lagrange: e.target.checked}))}
              /> Lagrange
            </label>
            <label>
              <input
                type="checkbox"
                checked={selectedMethods.parametric}
                onChange={(e) => setSelectedMethods(prev => ({...prev, parametric: e.target.checked}))}
              /> Parametric
            </label>
          </div>
        </div>

        <button
          onClick={handleSubmit}
          disabled={loading}
          style={{ 
            width: '100%',
            padding: '10px',
            backgroundColor: loading ? '#ccc' : '#007bff',
            color: 'white',
            border: 'none',
            borderRadius: '4px',
            marginTop: '20px',
            cursor: loading ? 'not-allowed' : 'pointer'
          }}
        >
          {loading ? 'Calculating...' : 'Calculate'}
        </button>
      </div>

      {error && (
        <div style={{ 
          padding: '10px', 
          backgroundColor: '#f8d7da', 
          color: '#721c24', 
          borderRadius: '4px',
          marginBottom: '20px'
        }}>
          {error}
        </div>
      )}

      {results && (
        <div style={{ marginTop: '20px' }}>
          <h2 style={{ marginBottom: '10px' }}>Results</h2>
          
          <img 
            src={`data:image/png;base64,${results.plot}`}
            alt="Interpolation Plot"
            style={{ 
              width: '100%', 
              marginBottom: '20px',
              border: '1px solid #dee2e6',
              borderRadius: '4px'
            }}
          />

          <div>
            <div style={{ display: 'flex', gap: '10px', marginBottom: '10px' }}>
              <input
                type="number"
                value={evaluationPoint}
                onChange={(e) => setEvaluationPoint(e.target.value)}
                placeholder="Enter x value"
                style={{ flex: 1, padding: '5px' }}
              />
              <button
                onClick={handleSubmit}
                style={{ 
                  padding: '5px 10px',
                  backgroundColor: '#007bff',
                  color: 'white',
                  border: 'none',
                  borderRadius: '4px'
                }}
              >
                Evaluate
              </button>
            </div>
            
            {evaluationResults && (
              <div style={{ 
                padding: '10px', 
                backgroundColor: '#f8f9fa',
                borderRadius: '4px'
              }}>
                {Object.entries(evaluationResults).map(([method, value]) => (
                  <div key={method} style={{ 
                    display: 'flex', 
                    justifyContent: 'space-between',
                    marginBottom: '5px'
                  }}>
                    <span style={{ fontWeight: 500, textTransform: 'capitalize' ,color:'black'}}>{method}:</span>
                    <span style={{color: 'black'}}>{value.toFixed(4)}</span>
                  </div>
                ))}
              </div>
            )}
          </div>
        </div>
      )}
    </div>
  );
};

export default InterpolationApp;