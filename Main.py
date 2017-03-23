'''
Created on 15.03.2017

@author: Administrator
'''

import urllib
import json
import os

from flask import Flask
from flask import request
from flask import make_response


# Flask app should start in global layout
app = Flask(__name__)


@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)

    print("Request:")
    print(json.dumps(req, indent=4))

    res = makeWebhookResult(req)

    res = json.dumps(res, indent=4)
    print(res)
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r

def makeWebhookResult(req):
    if req.get("result").get("action") != "Kunden.Übersicht":
        return {}
    result = req.get("result")
    parameters = result.get("parameters")
    ID = parameters.get("IDKunde")
    
    w=4
    h=10
    a=[[0 for x in range(w)] for y in range(h)] ;
    
    a [0][0]= "11111"
    a [0][1]= "Max Mustermann"
    a [0][2]= "KFZ- Haftpflicht"
    a [0][3]= "Rentenversicherung"
    a [1][0]= "11112"
    a [1][1]= "Lisa Mustermann"
    a [1][2]= ""
    a [1][3]= "Rentenversicherung"  
    
        
    gefunden = False
    for i in range(len(a)): 
        if a[i][0]== ID :
            speech="Kunde:"   
            gefunden= True
            for j in range(len(a[i])-1):
                speech=speech + " " +a[i][j+1]+","   
        if gefunden == True:  
            break           
        else:
            speech="Du hast kein Kundenkonto bei uns."
         

    print("Response:")
    print(speech)

    return {
        "speech": speech,
        "displayText": speech,
        #"data": {},
        # "contextOut": [],
        "source": "apiai-onlinestore-shipping"
    }


if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))

    print "Starting app on port %d" % port

    app.run(debug=True, port=port, host='0.0.0.0')

