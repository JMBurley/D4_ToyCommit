from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
      return """
<!DOCTYPE html>
<head>
   <title>Heroku basic</title>
</head>
<body style="width: 880px; margin: auto;">  
    <h1>Project Basics</h1>
    <p> This is a toy commit of a flask app for Heroku. </p>
</body>
    """
@app.route('/about')
def about():
  return render_template('about.html')

if __name__ == '__main__':
  app.run(port=33507)
