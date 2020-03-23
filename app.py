from flask import Flask, jsonify, request
from datetime import datetime
import os

data = []
skip = True
for line in open('covidpy.csv'):
    if skip:
        skip = False
        continue
    date, cases, deaths, tests, recoveries = line.strip().split(',')
    data.append({
        'date':date, 
        'cases':int(cases), 
        'deaths':int(deaths), 
        'tests':int(tests), 
        'recoveries':int(recoveries)
    })

app = Flask(__name__)

@app.route('/')
def main():
    return jsonify(data), 200

# @app.route('/recharts')
# def recharts():
#     return 

if __name__ == "__main__":
    app.run()