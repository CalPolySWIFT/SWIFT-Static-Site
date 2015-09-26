from flask import Flask, render_template
import urllib
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/<page>')
def page(page):
    return render_template(page)

@app.route("/getcalendar")
def get_calendar():
    response = urllib.request.urlopen("https://www.googleapis.com/calendar/v3/calendars/calpolyswift.org_20ccnpmk81dvsn70peppejgf48%40group.calendar.google.com/events?maxResults=5&timeMin=2015-09-05T07%3A23%3A12.000Z&ctz=America/Los_Angeles&singleEvents=true&orderBy=startTime&key=AIzaSyBNlYH01_9Hc5S1J9vuFmu2nUqBZJNAXxs").read().decode('utf-8')
    jdata = json.loads(response)
    hdata = ""
    for item in jdata['items']:
        hdata += "<div class=\"event-item\">"
        hdata += "<p class=\"date-label\">"
        date = item['start']['dateTime'].split("T", 1)
        time = date[1].split("-", 1)
        timeEnd = time[1]
        time = time[0]
        date = date[0].split("-")
        month = date[1]
        day = date[2]
        year = date[0]
        # 2015-09-29T12:00:00-07:00
        hdata += "<span class=\"month\">"+month+"</span>"
        hdata += "<span class=\"date-number\">"+day+"</span>"
        hdata += "</p>"
        hdata += "<div class=\"details\">"
        hdata += "<h2 class=\"title\">"+item['summary']+"</h2>"
        hdata += "<p class=\"time\"><i class=\"fa fa-clock-o\"></i>"+time+"</p>"
        #hdata += "<p class=\"location\"><i class=\"fa fa-map-marker\"></i>"+item['location']+"</p>"
        hdata += "</div>"
        hdata += "</div>"
    return hdata

app.jinja_env.globals.update(get_calendar=get_calendar)

@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html")

@app.errorhandler(500)
def error_500(error):
    return render_template("404.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False)