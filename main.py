from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
        return render_template ('index.html')
#	return "do you have time for a joke?; this is the main.py page"

@app.route('/joke')
def joke():
        return render_template ('joke.html')
#	return 'joke page'

@app.route('/answer')
def answer():
        return render_template ('answer.html')
#	return 'answer page'
