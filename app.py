#import cs50
import csv

from flask import Flask, jsonify, redirect, render_template, request

# Configure application
app = Flask(__name__)

# Reload templates when they are changed
app.config["TEMPLATES_AUTO_RELOAD"] = True


@app.after_request
def after_request(response):
    """Disable caching"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/", methods=["GET"])
def get_index():
    return redirect("/form")


@app.route("/form", methods=["GET"])
def get_form():
    return render_template("form.html")


@app.route("/form", methods=["POST"])
def post_form():

    name = request.form.get("name-input")
    age = request.form.get("age-input")
    gender = request.form.get("gender-input")
    income = request.form.get("income-input")
    satisfaction = request.form.get("job-satisfaction")

    if name == "" or age == None or gender == None or satisfaction == None:

        return render_template("error.html", message="You need to input your: Name, Age, Gender, Incom and Satisfaction.")

    csvF = open("survey.csv", "a")
    writer = csv.writer(csvF)
    writer.writerow([name, age, gender, income, satisfaction])
    csvF.close()

    return tableAppend("success")

@app.route("/sheet", methods=["GET"])
def get_sheet():
    return tableAppend("")

def tableAppend(success):
    surveys = []
    file = open("survey.csv")
    for line in file:
        if line == "\n" or line == "":
            continue

        surveys.append(line.split(","))

    file.close()

    return render_template("sheet.html", surveys=surveys,message=success)



