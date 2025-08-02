from flask import Flask 
app=Flask(__name__)

@app.route('/<int:n>')
def even(n):
    primes=""
    for i in range(2,n+1):
        for n in range(2,i):
            if(i%n==0):
                break
        else:
                primes = primes + str(i)+","
    return primes

if __name__=="__main__":
  app.run()