from flask import Flask, jsonify, request
from flask_cors import CORS
import pandas as pd
from src import data_processing as dp

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

def find_articles(to_do, k):
    list_articles = dp.find_relevant_articles(to_do, k)
    # save relevant list of articles into a temporary csv file
    df_list_articles=pd.DataFrame(list_articles)
    df_list_articles.to_csv('./src/temp_list.csv',index=False)

# sanity check route

TASKS= []

# route instance to get the task (user's query), process it and find the related articles
@app.route('/task', methods=['POST','GET'])
def all_tasks():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        TASKS.append({
            'task': post_data.get('task'),
            'numberArticles': post_data.get('numberArticles')
        })
        to_do = post_data.get('task')
        nb_articles=int(post_data.get('numberArticles'))
        find_articles(to_do,nb_articles)
        response_object['message'] = 'task added!'
    else:
        response_object['tasks'] = TASKS
    return jsonify(response_object)

# route instance to retrieve list of articles
@app.route('/articles', methods=['GET'])
def articles():
    df_new_list=pd.read_csv('./src/temp_list.csv')
    new_list=df_new_list.to_dict('records')
    return jsonify(new_list)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')