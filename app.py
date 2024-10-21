from flask import Flask, render_template, jsonify
import json

app = Flask(__name__)

@app.route('/')
def home():
    with open('data/Patients.json') as f:
        patients = json.load(f)
    return render_template('home.html', patients=patients)

@app.route('/details/<int:patient_id>')
def details(patient_id):
    with open('data/Patients.json') as f:
        patients = json.load(f)
    patient = next((p for p in patients if p['id'] == patient_id), None)
    return render_template('details.html', patient=patient)

if __name__ == '__main__':
    app.run(debug=True)
