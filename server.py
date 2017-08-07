from flask import Flask, render_template, redirect, request

app = Flask(__name__)

@app.route("/")
def root():
    return render_template("landingPage.html")


@app.route("/process", methods=["POST"])
def processForm():
    name = request.form["queryName"]
    print name
    return redirect("/")

app.run(debug=True)
