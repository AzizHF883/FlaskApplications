#FlaskWebAppplicationDevelopment
from flask import Flask , render_template

app =Flask(__name__)

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)

@app.route('/cal/<int:num1>/<op>/<int:num2>')
def cal(num1, op, num2):
    
    if op=="+":
        result= num1+num2
    elif op== "-":
        result= num1-num2
    elif op == '/':
        result = num1 / num2
    elif op == '*':    
        result= num1*num2
    elif op == "%":
        result= num1%num2
    else:
         print("Invalid Operator!")
    return render_template('calculator.html', num1=num1, op=op, num2=num2, result=result)
    #return f'<h1>Result of {num1} {op} {num2} is {result}!</h1>'

if __name__== '__main__':
    app.run(debug=True)