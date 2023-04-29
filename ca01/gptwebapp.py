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
        <a href="{url_for('connor')}">Connor's GPT prompt: Make a recipe to fit your needs</a><br>
        <a href="{url_for('sam')}">Sam's GPT prompt: Get a recipe that uses the ingredients you have</a><br>
        <a href="{url_for('cole')}">Cole's GPT prompt: Create a recipe for a dish based off of your favorite foods</a>
        <a href="{url_for('disclaimer')}">Disclaimer</a><br>
    '''

@app.route('/cole', methods = ['Get', 'POST'])
def cole():
    ''' Cole prompt engineering page
    '''
    if request.method == 'POST':
        prompt = request.form['prompt']
        passalong = "Give me a recipe for a meal that is inspired by these foods : " + prompt
        answer = gptAPI.coleResponse(passalong)
        return f'''
        <h1>Cole's GPT Demo</h1>
        <pre style="bgcolor:yellow">{"Your favorite foods are " + prompt}</pre>
        <hr>
        Here is a recipe you should try:
        <div style="border:thin solid black">{answer}</div>
        Here is the answer in "pre" mode:
        <pre style="border:thin solid black">{answer}</pre>
        <a href={url_for('connor')}> Make another recipe?</a>
        <p> </p>
        <a href={url_for('index')}> Go back home</a>
        '''
    else:
        return '''
        <h1>Cole's GPT Demo App</h1>
        Enter a list of your favorite foods which you'd like a recipe inspired by! For
        example, try "Ice cream, chicken tiki masala, and onion rings"
        <form method="post">
            <textarea name="prompt"></textarea>
            <p><input type=submit value="get response">
        </form>
        '''


@app.route('/connor', methods=['Get', 'POST'])
def connor():
    ''' Connor's prompt engineering page, work in progress
    '''
    if request.method == 'POST':
        prompt = request.form['prompt']
        passalong = "Give me a recipe that meets the following parameters: " + prompt
        answer = gptAPI.connorResponse(passalong)
        return f'''
        <h1>Connor's GPT Demo</h1>
        <pre style="bgcolor:yellow">{"Your keywords were: " + prompt}</pre>
        <hr>
        Here is the answer in text mode:
        <div style="border:thin solid black">{answer}</div>
        Here is the answer in "pre" mode:
        <pre style="border:thin solid black">{answer}</pre>
        <a href={url_for('connor')}> Make another recipe?</a>
        <p> </p>
        <a href={url_for('index')}> Go back home</a>
        '''
    else:
        return '''
        <h1>Connor's GPT Demo App</h1>
        Enter a list of keywords (up to 10, seperated by commas) that you'd like to 
        make a recipe out of! For example, try "fast, cheap, vegetarian, dinner"
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
        passalong = "Give me a recipe that includes the following ingredients: " + prompt
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
        Enter a list of ingredients that you'd like to make a recipe out of!
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
    return '''Team Members:\n<p>Sam Herman: Freshman at Brandeis University studying computer science, mathematics, applied math, and Japanese language.
    Created personal Prompt engineering page, about page, and team page.</p>\n
    <p>Connor Zawacki: Junior at Brandeis University studying computer science and neuroscience. Created personal prompt engineering page, index page and disclaimer, modified about and team pages</p>\n
    <p>Cole Simmons: Freshman at Brandeis University studying computer science and anthropology. Created personal promt engineering page, corrected text, and modified index and team page\nDaniel Olevsky'''

@app.route('/disclaimer', methods=['GET'])
def disclaimer():
    return '''
    <p>chefGPT uses openAI's chatgpt language processing AI in order to create potential cooking solutions. Given that this is not chatGPT's origninal purpose,</p>
    <p>all recipes and advice given by chefGPT should be checked and/or modified by the USER in order to meet FDA guidelines. Neither the creator's of this webapp</p>
    <p>nor openAI are responsible for any consequences misuse of chefGPT nor any potential alergic reactions or sickness sustained as a result of not exercising due caution
    <p> </p>
    <p> for more information on safely preparing food, visit </p>
    <a> https://www.fda.gov/food/people-risk-foodborne-illness/meat-poultry-seafood-food-safety-moms-be#:~:text=Cook%20beef%2C%20pork%2C%20veal%2C,a%203%20minute%20rest%20time.&text=Cook%20ground%20beef%2C%20veal%2C%20lamb,F%20(74%C2%B0%20C).&text=Cook%20all%20poultry%20to%20minimal,F%20(74%C2%B0%20C). </a>'''
if __name__=='__main__':
    # run the code on port 5001, MacOS uses port 5000 for its own service :(
    app.run(debug=True,port=5001)
    