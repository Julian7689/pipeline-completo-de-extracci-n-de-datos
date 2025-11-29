from flask import Flask, render_template, request, redirect, url_for, session, flash, jsonify
import requests
import sys
import os

# Add the static directory to the path to import modules
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'static'))

from login import logeado_credenciales
from scrapper import scrape_data
from processor import save_to_excel, save_to_csv, save_to_json

app = Flask(__name__)
app.secret_key = 'your-secret-key-here-change-in-production'  # Change this in production!

# Store scraped data temporarily
scraped_data = []

@app.route('/')
def index():
    """Main dashboard page"""
    if 'logged_in' not in session:
        return redirect(url_for('login'))
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    """Login page and authentication"""
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        # Create a session for authentication
        with requests.Session() as req_session:
            if logeado_credenciales(req_session, username, password):
                session['logged_in'] = True
                session['username'] = username
                session['password'] = password
                flash('Login exitoso!', 'success')
                return redirect(url_for('index'))
            else:
                flash('Credenciales incorrectas', 'error')
                return redirect(url_for('login'))
    
    return render_template('login.html')

@app.route('/logout')
def logout():
    """Logout user"""
    session.clear()
    flash('Has cerrado sesión', 'info')
    return redirect(url_for('login'))

@app.route('/scrape', methods=['POST'])
def scrape():
    """Execute scraping process"""
    global scraped_data
    
    if 'logged_in' not in session:
        return jsonify({'error': 'No autenticado'}), 401
    
    try:
        with requests.Session() as req_session:
            # Re-authenticate
            if logeado_credenciales(req_session, session.get('username'), session.get('password')):
                # Scrape data
                scraped_data = scrape_data(req_session)
                
                if scraped_data:
                    # Save to files
                    save_to_excel(scraped_data)
                    save_to_csv(scraped_data)
                    save_to_json(scraped_data)
                    
                    flash(f'Scraping exitoso! {len(scraped_data)} registros obtenidos', 'success')
                    return jsonify({
                        'success': True, 
                        'count': len(scraped_data),
                        'redirect': url_for('results')
                    })
                else:
                    flash('No se encontraron datos', 'warning')
                    return jsonify({'error': 'No se encontraron datos'}), 404
            else:
                flash('Error de autenticación', 'error')
                return jsonify({'error': 'Error de autenticación'}), 401
                
    except Exception as e:
        flash(f'Error durante el scraping: {str(e)}', 'error')
        return jsonify({'error': str(e)}), 500

@app.route('/results')
def results():
    """Display scraped results"""
    if 'logged_in' not in session:
        return redirect(url_for('login'))
    
    return render_template('results.html', data=scraped_data)

@app.route('/api/data')
def get_data():
    """API endpoint to get scraped data as JSON"""
    if 'logged_in' not in session:
        return jsonify({'error': 'No autenticado'}), 401
    
    return jsonify(scraped_data)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
