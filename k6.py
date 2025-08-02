from flask import Flask 
app=Flask(__name__)

@app.route('/<int:n>')
def prime(n):
    primes=""
    for i in range(1,n+1):
       primes= primes + str(i)+","
    return primes
if __name__=="__main__":
  app.run()
        