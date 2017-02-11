from flask import Flask, render_template, abort
import urllib
import json
import datetime
import os

app = Flask(__name__)
app.debug = True


@app.route('/')
def index():
    return page("index")


@app.route('/<page>.html')
def page(page):
    if os.path.exists("templates/" + page + ".html"):
        return render_template(page + ".html")
    else:
        abort(404)


@app.route('/membership')
def membership():
    return render_template("membership.html")

@app.route('/calendar')
def calendar():
    return render_template("calendar.html")

def get_calendar():
    try:
        today = datetime.date.today()
        response = urllib.urlopen(
            "https://www.googleapis.com/calendar/v3/calendars/calpolyswift.org_20ccnpmk81dvsn70peppejgf48%40group.calendar.google.com/events?maxResults=5&timeMin="+str(today.year)+"-"+str(today.month)+"-"+str(today.day)+"T07%3A23%3A12.000Z&ctz=America/Los_Angeles&singleEvents=true&orderBy=startTime&key=AIzaSyBNlYH01_9Hc5S1J9vuFmu2nUqBZJNAXxs").read().decode(
            'utf-8')
        jdata = json.loads(response)
        hdata = ""
        for item in jdata['items'][:3]:
            try:
                # 'dateTime' 2015-09-29T12:00:00-07:00
                # 'date' 2015-09-29
                time = "TBD"
                startDate = item['start'].get('dateTime', None)
                if startDate is None:
                    startDate = item['start'].get('date', "TBD-TBD-TBD")
                    time = item['start'].get('date', "TBD-TBD-TBD") + ' to ' + item['end'].get('date', "TBD-TBD-TBD")
                else:
                    startDate = startDate.split("T", 1)
                    time = startDate[1].split("-", 1)[0]
                    startDate = startDate[0]
                # Date processing
                startDate = startDate.split("-")
                month = startDate[1]
                day = startDate[2]
                year = startDate[0]
                summary = item.get('summary', "TBD")
                description = item.get('description', None)
                location = item.get('location', None)
                tdata = "<div class=\"event-item\">"
                tdata += "<p class=\"date-label\">"
                tdata += "<span class=\"month\">" + month + "</span>"
                tdata += "<span class=\"date-number\">" + day + "</span>"
                tdata += "</p>"
                tdata += "<div class=\"details\">"
                tdata += "<h2 class=\"title\">" + summary + "</h2>"
                if description:
                    tdata += "<p class=\"description\">" + description + "</p>"
                tdata += "<p class=\"time\"><i class=\"fa fa-clock-o\"></i>" + time + "</p>"
                if location:
                    tdata += "<p class=\"location\"><i class=\"fa fa-map-marker\"></i>" + location + "</p>"
                tdata += "</div>"
                tdata += "</div>"
                hdata += tdata
            except:
                continue
    except:
        return ""
    return hdata


app.jinja_env.globals.update(get_calendar=get_calendar)


@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html")


@app.errorhandler(500)
def error_500(error):
    return render_template("500.html")


if __name__ == '__main__':
    app.run(host='0.0.0.0')
