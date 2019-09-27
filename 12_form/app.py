#Henry Liu and Jude Rizzo
#SoftDev1 pd9
#K12 -- Using Python, Flask, Jinja2, and HTML to create a form and custom response.
#2019-09-26

from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route("/")
def functions():
    return render_template(
    'form.html'
    )

@app.route("/auth")
def authenticate():
    print("\n\n")
    print("*** DIAG: this Flask obj***")
    print(app)
    print("*** DIAG: request obj ****")
    print(request)
    print("*** DIAG: request.method ****")
    print(request.method)
    print("*** DIAG: request.headers ****")
    print(request.headers)
    print("*** DIAG: request.form ****")
    print(request.form)
    print("*** DIAG: request.args ****")
    print(request.args)
    print("\n\n")

    return render_template('submited.html')



if __name__ == "__main__":
  app.debug = True
  #run the main code
  app.run()
