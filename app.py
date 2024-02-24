import os
from LLMModel import LLMModel
from flask import (Flask, redirect, render_template, request,
                   send_from_directory, url_for)

app = Flask(__name__)

@app.route('/')
def index():
   print('Request for index page received')
   return "Hi"


@app.route('/recommendationfromopenai', methods=['GET'])
def getRecommendations():
   query = request.args.get('ask')
   print(query)
   llm_model=LLMModel()
   llm_items = llm_model.get_llm_items(query)
   if query:
       print('Request for hello page received with name=%s' % query)
       return llm_items
   else:
       print('Request for hello page received with no name or blank name -- redirecting')
       return "No results found"


if __name__ == '__main__':
   app.run()
