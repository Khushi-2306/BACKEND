from flask import Flask 
app = Flask(__name__)

@app.route("/<int:number>")
def fibonacci(number):
    fibs = f"First {number} Fibonacci numbers :"
    fib1 = 0
    fib2 = 1
    for i in range(2,number+1):
            fibs = fibs + str(fib1) + ","
            fib1, fib2 = fib2,fib1+fib2
    return fibs

if __name__ == "_main__":
    app.run(debug=True)