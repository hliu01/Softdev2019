from flask import Flask, render_template
app = Flask(__name__)#create instance of class Flask


@app.route("/")#assign following fxn to run when route requested
def hi_world():
    return "No so!"

coll = {0,1,1,2,3,5,8}

@app.route("/my_foist_template")#assign following fxn to run when route requested
def test_templt():
    return render_template(
    'model_tmplt.html',
    foo = "foooo",
    collection = coll
    )


if __name__ == "__main__":
    app.debug = True
    app.run()
