import random
import string
from flask import Flask,request,jsonify,render_template,redirect,session
from call_llm2 import perform_llm_call
import pandas as pd
# import plotly.graph_objects as go
# from plotly.io   import write_html,to_html
import plotly.io as pio


app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/get_tables')
def get_values():
    my_list = ['value1', 'value2', 'value3']
    return jsonify(my_list)


@app.route('/getanswer',methods=['POST'])
def getanswer():
    try:
        if request.method == 'POST':
            que=request.form['que']
            tablename=request.form['tablename']
            print('---------------',tablename,que)
            response, new_data, graph_img, generated_response = perform_llm_call(que)
            # print(new_data)
            new_data1=''
            graph_html=''
            config = {'responsive': True}
            if(graph_img != None):
                graph_html = pio.to_html(graph_img,config=config,include_plotlyjs=False,full_html=True) 
            if(isinstance(new_data, pd.DataFrame)):
                new_data1=new_data.to_html()
                id=generate_random_id(10)
                print('--------id',id)
                new_data1 = new_data1.replace('<table', f'<table class="my_table" id="{id}"', 1)
            if(generated_response == None):
                generated_response=''
            if(response == None):
                response=''
            result={
             'graph_html':graph_html,
             'new_data':new_data1,
             'generated_response':generated_response,
             'response':response
            }
            return jsonify({'msg':'success','result':result})
    except Exception as e:
        print(e)
        return jsonify({'msg':'error','error':e})


@app.errorhandler(404)
def page_not_found(e):
    return render_template('error.html'), 404

def generate_random_id(length=10):
    if length < 1:
        raise ValueError("Length must be at least 1")
    
    # First character should be a letter
    first_char = random.choice(string.ascii_lowercase)
    
    # Remaining characters can be letters or digits
    characters = string.ascii_lowercase + '123456789'
    remaining_chars = ''.join(random.choice(characters) for _ in range(length - 1))
    
    # Combine the first character with the remaining ones
    random_id = first_char + remaining_chars
    return random_id


if __name__ == '__main__':
    app.run(debug=True)
