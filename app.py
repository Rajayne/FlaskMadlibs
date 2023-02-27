from flask import Flask, request, render_template
from stories import story
# from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__,template_folder='templates')
app.debug = True

app.config['SECRET_KEY'] = 'key'
# debug = DebugToolbarExtension(app)

@app.route('/')
def questions():
    """
    Page form with word prompts
    """
    prompts = story.prompts
    return render_template("questions.html", prompts=prompts)

@app.route('/story')
def show_story():
    """
    Show story results
    """
    text = story.generate(request.args)
    return render_template("story.html", text=text)