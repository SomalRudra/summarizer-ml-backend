from datetime import date
from flask import Flask, request, make_response
from summarizer_processor import fetchDataFromUrl

app = Flask(__name__)

@app.route('/',methods = ['GET'])
def hello():
    return "Testing get";

@app.route('/content-from-url',methods = ['GET'])
def getContentFromUrl():
    url = request.args.get('url');

    data = fetchDataFromUrl(url);

    todayDate = date.today()

    response_body = {'data':data, 'contentDate': todayDate }
    return response_body, 200, {'Access-Control-Allow-Origin':'*'}

# @app.route('/summarization-from-content',methods = ['GET'])
# def summarizationFromContent():
#     request_data = request.get_json(force=True)
#     content = request_data.get('content')

#     summary = summarizeFromContent(content)

#     todayDate = date.today()

#     response_body = {'summary':summary,'fromContent':True,'fromUrl':False, 'contentDate': todayDate }
#     return response_body, 200, {'Access-Control-Allow-Origin':'*'}

# @app.route('/summarization-from-URL',methods = ['GET'])
# def summarizationFromURL():
#     request_data = request.get_json(force=True)
#     url = request_data.get('url')

#     summary = summarizeFromURL(url)

#     todayDate = date.today()

#     response_body = {'summary':summary,'fromContent':False,'fromUrl':True, 'contentDate': todayDate}
#     return response_body, 200, {'Access-Control-Allow-Origin':'*'}
