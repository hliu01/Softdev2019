from flask import Flask
app = Flask(__name__)#create instance of class Flask

@app.route("/")#assign following fxn to run when route requested
def hello_world():
    print(__name__)#where will this go
    return "No!"


@app.route("/sister")#assign following fxn to run when route requested
def hi_world():
    print(__name__)#where will this go
    return "Hey"



@app.route("/brother")#assign following fxn to run when route requested
def hey_world():
    print(__name__)#where will this go
    return "yes"

if __name__ == "__main__":
    app.debug = True
    app.run()
