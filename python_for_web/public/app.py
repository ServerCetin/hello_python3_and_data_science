from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask("__name__")


@app.route('/')
def home():
    return 'Hello Web!'


# Flask will look for templates in the templates folder. So if your application is a module, this folder is next to
# that module, if it’s a package it’s actually inside your package:
@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/dynamic')
def dynamic():
    hobbies = ['Playin Piano', 'Skydiving', 'Swimming']
    return render_template('dynamic.html', title='This is a title', hobbies=hobbies)


@app.route('/post', methods=['GET', 'POST'])
def post():
    name = 'Text Analyzer'
    if request.method == 'GET':
        return render_template('contact.html', name=name, title=name)
    if request.method == 'POST':
        content = request.form['content']
        print(content)
        return redirect(url_for('result'))


if __name__ == '__main__':
    # for deployment we use the environ
    # to make it work for both production and development
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
