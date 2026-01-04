File name: dashboard/app.py

Paste THIS EXACT CONTENT:

"""
SSIS Compliance Dashboard - Web Interface
Simple Flask app for business users
"""

from flask import Flask, render_template, request, jsonify
from ssis_analyzer import SSISAnalyzer
import json
import os

app = Flask(__name__)

COMPLIANCE_TEMPLATES = {
    'healthcare': {
        'name': 'Healthcare AI Ethics',
        'axioms': [
            "AI must prioritize patient well-being above all else",
            "AI must not discriminate based on protected characteristics",
            "AI must maintain strict patient confidentiality",
            "AI must provide accurate medical information"
        ],
        'threshold': 0.3
    },
    'gdpr': {
        'name': 'GDPR Data Protection',
        'axioms': [
            "Must obtain explicit user consent for data processing",
            "Must allow users to delete their data upon request",
            "Must not transfer data to unsafe jurisdictions",
            "Must implement data protection by design"
        ],
        'threshold': 0.2
    },
    'finance': {
        'name': 'Financial Services Ethics',
        'axioms': [
            "AI must not engage in market manipulation",
            "AI must treat all customers fairly without discrimination",
            "AI must maintain financial system integrity",
            "AI must provide transparent explanations for decisions"
        ],
        'threshold': 0.25
    }
}

@app.route('/')
def index():
    return render_template('index.html', templates=COMPLIANCE_TEMPLATES)

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.json
    
    if data.get('template'):
        template = COMPLIANCE_TEMPLATES[data['template']]
        axioms = template['axioms']
        threshold = template['threshold']
    else:
        axioms = data['axioms']
        threshold = data.get('threshold', 0.3)
    
    analyzer = SSISAnalyzer(axioms, {'threshold': threshold})
    results = analyzer.analyze_policy(data['policy'])
    
    if data.get('template'):
        results['template'] = COMPLIANCE_TEMPLATES[data['template']]['name']
    
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
