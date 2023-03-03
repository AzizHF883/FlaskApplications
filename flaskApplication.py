#FlaskWebAppplicationDevelopment
from flask import Flask , request

app =Flask(__name__)

@app.route('/cal/<int:num1>/<op>/<int:num2>')
def cal(num1, op, num2):
    #n1= int(num1)
    #n2= int(num2)
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
    return f'<h1>Result of {num1} {op} {num2} is {result}!</h1>'

if __name__== '__main__':
    app.run(debug=True)