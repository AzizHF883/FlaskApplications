#FlaskWebAppplicationDevelopment
from flask import Flask , request

app =Flask(__name__)

@app.route('/user/<name>')
def user(name):
	return '<h1>Hello, %s!</h1>' % name

@app.route('/cal/<num1>/<op>/<num2>')
def cal(num1, op, num2):
    n1= int(num1)
    n2= int(num2)
    if op=="+":
        result= n1+n2
    elif op== "-":
        result= n1-n2
    elif op == '/':
        result = n1 / n2
    elif op == '*':    
        result= n1*n2
    elif op == "%":
        result= n1%n2
    else:
         print("Invalid Operator!")
    return f'<h1>Result: {result}!</h1>'

if __name__== '__main__':
    app.run(debug=True)