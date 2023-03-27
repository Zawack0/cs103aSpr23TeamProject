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
        <h1>ChefGPT</h1>
        <a href="{url_for('about')}">About ChefGPT</a><br>
        <a href="{url_for('team')}">About the team</a><br>
        <a href="{url_for('connor')}">Connor's GPT prompt: Make a recepie to fit your needs</a><br>
        <a href="{url_for('sam')}">Sam's GPT prompt: Get a recepie that uses the ingredients you have</a><br>
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
        <h1>Connor's GPT Demo App</h1>
        Enter a list of keywords (up to 10, seperated by commas) that you'd like to 
        make a recepie out of! For example, try "fast, cheap, vegetarian, dinner"
        <form method="post">
            <textarea name="prompt"></textarea>
            <p><input type=submit value="get response">
        </form>
        '''
    
@app.route('/sam', methods=['Get', 'POST'])
def sam():
    ''' Sam's prompt engineering page
    '''
    if request.method == 'POST':
        prompt = request.form['prompt']
        passalong = "Give me a recepie that includes the following ingredients: " + prompt
        answer = gptAPI.samResponse(passalong)
        return f'''
        <h1>Sam's GPT Demo</h1>
        <pre style="bgcolor:yellow">{prompt}</pre>
        <hr>
        Here is the answer in text mode:
        <div style="border:thin solid black">{answer}</div>
        Here is the answer in "pre" mode:
        <pre style="border:thin solid black">{answer}</pre>
        <a href={url_for('sam')}> make another query</a>
        '''
    else:
        return '''
        <h1>Sam's GPT Demo App</h1>
        Enter a list of ingredients that you'd like to make a recepie out of!
        For example, try "rice, chili oil, tomato"
        <form method="post">
            <textarea name="prompt"></textarea>
            <p><input type=submit value="get response">
        </form>
        '''


@app.route('/about', methods=['GET', 'POST'])
def about():
    return 'ChefGPT is an AI tool to help you in the kitchen, such as coming up with a recipe within certain limitations!'
    

@app.route('/team', methods=['GET', 'POST'])
def team():
    return '''Team Members:\nSam Herman: Freshman and Brandeis University studying computer science, mathematics, applied math, and Japanese language.
    Created personal Prompt engineering page, about page, and team page.\n
    Connor Zawacki\nCole Simmons\nMargaret Potagal\nDaniel Olevsky'''

if __name__=='__main__':
    # run the code on port 5001, MacOS uses port 5000 for its own service :(
    app.run(debug=True,port=5001)
    