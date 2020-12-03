from flask import Flask, render_template, request


app = Flask(__name__)


@app.route('/hello/<name>')
def hello_get1(name=None):
    #return name
    return render_template('hello.html', title='flask test', name=name) 


@app.route('/hello')
def hello_get2():
    name = request.args.get('name')
    return render_template('hello.html', title='flask test', name=name) 


@app.route('/hello', methods=['POST']) #Methodを明示する必要あり
def hello():
    if request.method == 'POST':
        name = request.form['name']
    else:
        name = "no name."
    return render_template('hello.html', title='flask test', name=name) 


## おまじない
if __name__ == "__main__":
    app.run(debug=True)