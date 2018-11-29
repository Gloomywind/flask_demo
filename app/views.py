from flask import jsonify, request
from models import *
from flask import render_template
import time
import json


@app.route('/', methods=['GET'])
def hello():
    return render_template('index.html')

@app.route('/api/post/status', methods=['POST'])
def status():
    if request.method == 'POST':
        data = json.loads(request.data)
        ports = data['port_usage']
        ports = ','.join(ports)
        timestamp = data['time'][:13]
        status = honeypot(time=timestamp, disk=data['disk_usage'],
                                  host=data['host'], cpu=data['cpu_usage'],
                                  memory=data['mem_usage'], port=ports)
        db.session.add(status)
        db.session.commit()
        return "ok"
		
    

@app.route('/api/get/usage', methods=['GET'])
def usage():
    status = getstatus()
    datas = {'data': status}
    print datas
    return jsonify(datas)

def getstatus():
    status_list = []
    timestamp = time.strftime('%Y-%m-%d %H', time.localtime(time.time()))
    data = honeypot.query.filter_by(time=timestamp).all()
    for i in data:
        status = {}
        status['host'] = i.host.replace('-', '.')
        status['memory'] = i.memory
        status['cpu'] = i.cpu
        status['disk'] = i.disk
        status['port'] = i.ports
        status_list.append(status)
    return status_list

