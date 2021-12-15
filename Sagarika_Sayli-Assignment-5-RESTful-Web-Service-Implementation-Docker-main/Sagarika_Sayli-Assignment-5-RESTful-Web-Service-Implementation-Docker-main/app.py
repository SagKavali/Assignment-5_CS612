from flask import Flask,jsonify, render_template, request, redirect,url_for,escape
import json


app = Flask(__name__)
jData = json.loads(open('./Students.json').read())
data=jData["Students"]

@app.route('/')
def car_main():
    return render_template("index.html")

@app.route('/Students/')
def getAllStudents():
    myList=[]
    for element in data:
        myList.append(element)
    result = jsonify(myList)
    return render_template("index.html",items=myList)

@app.route('/Students/<string:Year>/')
def getyear(Year=''):
    myList=[]
    for element in data:
        if element["Year"] == Year:
            myList.append(element)
    result = jsonify(myList)
    return render_template("index.html",items=myList)


@app.route('/Students/<string:Year>/<string:Class>')
def getClass(Year, Class):
    myList=[]
    for element in data:
        if element["Year"]== Year:
            if element ["Class"] == Class:
                myList.append(element)
    result = jsonify(myList)
    return render_template("index.html",items=myList)

@app.route('/Students/<string:Year>/<string:Class>/<string:Subject>')
def getSubject(Year,Subject,Class):
    myList=[]
    for element in data:
        if element["Year"]== Year:
            if element ["Class"] == Class:
                if element ['Subject'] == Subject:
                    myList.append(element)
    result = jsonify(myList)
    return render_template("index.html",items=myList)

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')