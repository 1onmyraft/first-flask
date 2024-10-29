from flask import Flask, render_template
from flask_bootstrap import Bootstrap5


# create an instance of Flask
app = Flask(__name__)
bootstrap = Bootstrap5(app)

# route decorator binds a function to a URL
@app.route('/')
def acronym():
  return '''<p>Cody S. : lol Me: idgaf</p>'''

@app.route('/tyler')
def t_test():
    return render_template('template.html')
