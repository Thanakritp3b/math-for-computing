from flask import Flask, request, jsonify
from flask_cors import CORS
import numpy as np
import matplotlib.pyplot as plt
import matplotlib 
matplotlib.use('Agg')
import sympy as sp
import json
import io
import base64

app = Flask(__name__)
CORS(app)

def generate_uniform_points(a, b, n):
    return np.linspace(a, b, n)

def evaluate_polynomial(coefficients, x_values):
    n = len(coefficients)
    y_values = np.zeros_like(x_values)
    for i in range(n):
        y_values += coefficients[i] * np.power(x_values, i)
    return y_values

def get_matrix(x):
    matrix = []
    for i in range(len(x)):
        row = []
        for j in range(len(x)):
            row.append(x[i] ** j)
        matrix.append(row)
    return np.array(matrix)

def evaluate_function(function_str, x):
    x_sym = sp.Symbol('x')
    func = sp.sympify(function_str)
    f = sp.lambdify(x_sym, func, 'numpy')
    return f(x)

def sle_interpolation(x, y, eval_points):
    matrix = get_matrix(x)
    coefficients = np.linalg.solve(matrix, y)
    y_interpolated = evaluate_polynomial(coefficients, eval_points)
    return y_interpolated, coefficients

def lagrange_interpolation(x, y, eval_points):
    n = len(x)
    y_interpolated = np.zeros_like(eval_points)
    
    for i in range(n):
        basis = np.ones_like(eval_points)
        for j in range(n):
            if i != j:
                basis *= (eval_points - x[j]) / (x[i] - x[j])
        y_interpolated += basis * y[i]
    
    return y_interpolated

def parametric_interpolation(x, y, num_points=100):
    t = np.linspace(0, 1, len(x))
    t_interp = np.linspace(0, 1, num_points)
    
    matrix = get_matrix(t)
    x_coeffs = np.linalg.solve(matrix, x)
    y_coeffs = np.linalg.solve(matrix, y)
    
    x_interp = evaluate_polynomial(x_coeffs, t_interp)
    y_interp = evaluate_polynomial(y_coeffs, t_interp)
    
    return x_interp, y_interp, x_coeffs, y_coeffs

def create_plot(original_points, interpolation_results, title):
    plt.figure(figsize=(10, 6))
    
    plt.scatter(original_points['x'], original_points['y'], color='black', label='Original Points', zorder=5)
    
    if 'sle' in interpolation_results:
        plt.plot(interpolation_results['x'], interpolation_results['sle']['y'], 'b-', label='SLE Interpolation')
    
    if 'lagrange' in interpolation_results:
        plt.plot(interpolation_results['x'], interpolation_results['lagrange']['y'], 'g--', label='Lagrange Interpolation')
    
    if 'parametric' in interpolation_results:
        plt.plot(interpolation_results['parametric']['x'], interpolation_results['parametric']['y'], 'r:', label='Parametric Interpolation')
    
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.title(title)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    
    buf = io.BytesIO()
    plt.savefig(buf, format='png', dpi=300, bbox_inches='tight')
    buf.seek(0)
    plt.close()
    
    return base64.b64encode(buf.getvalue()).decode('utf-8')

@app.route('/interpolate', methods=['POST'])
def interpolate():
    try:
        data = request.get_json()
        input_type = data['type']
        methods = data['methods']
        
        if input_type == 'function':
            function_str = data['function']
            a = float(data['interval_start'])
            b = float(data['interval_end'])
            degree = int(data['degree'])
            
            x = generate_uniform_points(a, b, degree + 1)
            y = evaluate_function(function_str, x)
            
            eval_x = np.linspace(a, b, 100)
            
        else:
            points = np.array(data['points'])
            x = points[:, 0]
            y = points[:, 1]
            
            eval_x = np.linspace(np.min(x), np.max(x), 100)
        
        original_points = {'x': x.tolist(), 'y': y.tolist()}
        
        results = {
            'x': eval_x.tolist(),
            'original_points': original_points
        }
        
        if 'sle' in methods:
            y_sle, coeffs_sle = sle_interpolation(x, y, eval_x)
            results['sle'] = {
                'y': y_sle.tolist(),
                'coefficients': coeffs_sle.tolist()
            }
            
        if 'lagrange' in methods:
            y_lagrange = lagrange_interpolation(x, y, eval_x)
            results['lagrange'] = {
                'y': y_lagrange.tolist()
            }
            
        if 'parametric' in methods:
            x_param, y_param, x_coeffs, y_coeffs = parametric_interpolation(x, y)
            results['parametric'] = {
                'x': x_param.tolist(),
                'y': y_param.tolist(),
                'x_coefficients': x_coeffs.tolist(),
                'y_coefficients': y_coeffs.tolist()
            }
        
        title = f"Interpolation Results ({'Function' if input_type == 'function' else 'Points'} Input)"
        plot_base64 = create_plot(original_points, results, title)
        results['plot'] = plot_base64
        
        if 'evaluation_point' in data:
            point = float(data['evaluation_point'])
            evaluation_results = {}
            
            if 'sle' in methods:
                idx = np.abs(eval_x - point).argmin()
                evaluation_results['sle'] = results['sle']['y'][idx]
            
            if 'lagrange' in methods:
                idx = np.abs(eval_x - point).argmin()
                evaluation_results['lagrange'] = results['lagrange']['y'][idx]
            
            if 'parametric' in methods:
                param_x = results['parametric']['x']
                param_y = results['parametric']['y']
                idx = np.abs(param_x - point).argmin()
                evaluation_results['parametric'] = param_y[idx]
            
            results['evaluation'] = evaluation_results
        
        return jsonify(results)

    except Exception as e:
        return jsonify({
            'error': str(e)
        }), 400

if __name__ == '__main__':
    app.run(debug=True)