from flask import Flask, render_template, Response
import requests
import json

app = Flask(__name__)

API_KEY = "CVGjNdJjj1qG8RGXNjetbEFsCtXTpzq2"
BASE_URL = "https://eu.private5g.ericsson.net/public/v2/organization/ntt-brazil/site/ntt-br-lab/"

def format_json_response(data):
    return Response(json.dumps(data, indent=4), mimetype='application/json')

def get_api_response(endpoint):
    url = BASE_URL + endpoint
    try:
        response = requests.get(url, headers={"x-api-key": API_KEY})
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        return {"error": str(e)}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/latency')
def latency():
    return format_json_response(get_api_response('kpi/latency'))

@app.route('/topdevices')
def topdevices():
    return format_json_response(get_api_response('kpi/topdevices'))

@app.route('/apn')
def apn():
    return format_json_response(get_api_response('nc/apn'))

@app.route('/cidr')
def cidr():
    return format_json_response(get_api_response('apn/nextcidr'))

@app.route('/imsi')
def imsi():
    return format_json_response(get_api_response('nc/imsi'))

@app.route('/nextimsi')
def nextimsi():
    return format_json_response(get_api_response('nc/imsi/nextimsi'))

@app.route('/vlan')
def vlan():
    return format_json_response(get_api_response('nc/vlan'))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
