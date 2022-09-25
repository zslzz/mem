from flask import Flask
import pandas as pd
from calcul import cal
from calcul import getall

app = Flask(__name__)


@app.route('/api')
def hello_world():  # put application's code here
    # calCheap(210)
    return "hello"
    # return calresult(200).to_json(orient = 'split', force_ascii = False)

@app.route('/api/all')
def all():
    # index中的num需要和<int:num>完全一致
    s=getall()
    return pd.concat(s).to_json(orient="records", force_ascii = False)

@app.route('/api/badget/<int:num>/')
def badget(num):
    # index中的num需要和<int:num>完全一致
    s,v1,v2,v3=cal(num)
    return pd.concat(v1).to_json(orient="records", force_ascii = False)

@app.route('/api/ability/<int:num>/')
def ability(num):
    # index中的num需要和<int:num>完全一致
    s,v1,v2,v3=cal(num)
    return pd.concat(v2).to_json(orient="records", force_ascii = False)

@app.route('/api/score/<int:num>/')
def score(num):
    # index中的num需要和<int:num>完全一致
    s,v1,v2,v3=cal(num)
    return pd.concat(v3).to_json(orient="records", force_ascii = False)

if __name__ == '__main__':
    app.run()
