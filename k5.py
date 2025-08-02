from flask import Flask
app=Flask(__name__)

@app.route("/<name>")
def hello_name(name):
    msg ='<i>hello %s! </p>' % name
    msg+= '<p> enjoy ur journey </p>'
    msg+='<p>have a great day</p>'
    msg+='<p> welcome to my page  and here here is the vs code </p>'
    return msg
if __name__=='__main__':
    app.run()
