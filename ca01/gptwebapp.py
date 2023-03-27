'''
gptwebapp shows how to create a web app which ask the user for a prompt
and then sends it to openai's GPT API to get a response. You can use this
as your own GPT interface and not have to go through openai's web pages.

We assume that the APIKEY has been put into the shell environment.
Run this server as follows:

On Mac
% pip3 install openai
% pip3 install flask
% export APIKEY="......."  # in bash
% python3 gptwebapp.py

On Windows:
% pip install openai
% pip install flask
% $env:APIKEY="....." # in powershell
% python gptwebapp.py
'''
from flask import request,redirect,url_for,Flask
from gpt import GPT
import os

app = Flask(__name__)
gptAPI = GPT(os.environ.get('APIKEY'))

# Set the secret key to some random bytes. Keep this really secret!
app.secret_key = b'_5#y2L"F4Q789789uioujkkljkl...8z\n\xec]/'

@app.route('/')
def index():
    ''' display a link to the general query page '''
    print('processing / route')
    return f'''
        <h1>chefGPT</h1>
        <a href="{url_for('connor')}">Connor's GPT prompt: Make a recepie to fit your needs</a>
        <a href="{url_for('gptdemo')}">Ask questions to GPT</a>
    '''


@app.route('/connor', methods=['Get', 'POST'])
def connor():
    ''' Connor's prompt engineering page, work in progress
    '''
    if request.method == 'POST':
        prompt = request.form['prompt']
        passalong = "Give me a recepie that meets the following parameters: " + prompt
        answer = gptAPI.connorResponse(passalong)
        return f'''
        <h1>Connor's GPT Demo</h1>
        <pre style="bgcolor:yellow">{"Your keywords were: " + prompt}</pre>
        <hr>
        Here is the answer in text mode:
        <div style="border:thin solid black">{answer}</div>
        Here is the answer in "pre" mode:
        <pre style="border:thin solid black">{answer}</pre>
        <a href={url_for('connor')}> Make another recepie?</a>
        <p> </p>
        <a href={url_for('index')}> Go back home</a>
        '''
    else:
        return '''
        <h1>Connor's GPT Demo App</h1>
        Enter a list of keywords (up to 10, seperated by commas) that you'd like to 
        make a recepie out of! For example, try "fast, cheap, vegetarian, dinner"
        <form method="post">
            <textarea name="prompt"></textarea>
            <p><input type=submit value="get response">
        </form>
        '''

@app.route('/gptdemo', methods=['GET', 'POST'])
def gptdemo():
    ''' handle a get request by sending a form 
        and a post request by returning the GPT response
    '''
    if request.method == 'POST':
        prompt = request.form['prompt']
        answer = gptAPI.getResponse(prompt)
        return f'''
        <h1>GPT Demo</h1>
        <pre style="bgcolor:yellow">{prompt}</pre>
        <hr>
        Here is the answer in text mode:
        <div style="border:thin solid black">{answer}</div>
        Here is the answer in "pre" mode:
        <pre style="border:thin solid black">{answer}</pre>
        <a href={url_for('gptdemo')}> make another query</a>
        '''
    else:
        return '''
        <h1>GPT Demo App</h1>
        Enter your query below
        <form method="post">
            <textarea name="prompt"></textarea>
            <p><input type=submit value="get response">
        </form>
        '''

if __name__=='__main__':
    # run the code on port 5001, MacOS uses port 5000 for its own service :(
    app.run(debug=True,port=5001)
    