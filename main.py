from flask import Flask
from subprocess import Popen, PIPE

import json

app = Flask(__name__)

# curl -u ce0e1055-7d7d-478b-b8f5-7b0776a7f6e1:9J564LQ19MZJViKN1ciSRRK8LFJsOCy4mzwHrLnIZCOhj6B4GNQLLCsNG9BFIEdS -X POST https://eu-gb.functions.cloud.ibm.com/api/v1/namespaces/andreas.kaas.johansen%40ibm.com_dev/actions/matemate?blocking=true

@app.route('/')
def hello():

    p = Popen(['curl', '-u', 'ce0e1055-7d7d-478b-b8f5-7b0776a7f6e1:9J564LQ19MZJViKN1ciSRRK8LFJsOCy4mzwHrLnIZCOhj6B4GNQLLCsNG9BFIEdS', '-X', 'POST',
               'https://eu-gb.functions.cloud.ibm.com/api/v1/namespaces/andreas.kaas.johansen%40ibm.com_dev/actions/matemate?blocking=true'], stdout=PIPE, stderr=PIPE)
    (output, err) = p.communicate()
    rc = p.returncode

    json_res = json.loads(output)
    the_poster = json_res['response']['result']['poster']

    return "<img src=\"data:image/png;base64, "+the_poster+"\" alt=\"Red dot\"/></div>"

