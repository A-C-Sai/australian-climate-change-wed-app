from flask import Flask, url_for, render_template, redirect

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/in_production')
def in_production():
    return '<h1 style="color:red;">THIS PAGE YET TO BE IMPLEMENTD.</h1>'

if __name__ == '__main__':
    app.run(debug=True)
