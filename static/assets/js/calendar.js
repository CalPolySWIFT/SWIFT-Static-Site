function get_calender() {
	var today = new Date();
	let baseurl = "https://www.googleapis.com/calendar/v3/calendars/calpolyswift.org_20ccnpmk81dvsn70peppejgf48%40group.calendar.google.com/events?maxResults=5&timeMin="+today.getFullYear()+"-"+(today.getMonth()+1)+"-"+today.getDate()+"T07%3A23%3A12.000Z&ctz=America/Los_Angeles&singleEvents=true&orderBy=startTime&key=AIzaSyBNlYH01_9Hc5S1J9vuFmu2nUqBZJNAXxs";

	console.log('Fetching calendar from: ', baseurl);

	fetch(baseurl)
	.then(res => res.json())
	.then((out) => {
		console.log('Checkout this JSON! ', out);
		var el = document.getElementById("event-list");
		for (item in out['items']) {
			console.log(item);
			var _time = "TBD";
			var _startDate = out['items'][item]['start']['dateTime'] || "YYYY-MM-DDTHH:MM:SS-OH:OM"
			_startDate = _startDate.split('T')
			_time = _startDate[1].split('-')[0]
			_startDate = _startDate[0].split('-')
			var _year = _startDate[0]
			var _month = _startDate[1]
			var _day = _startDate[2]
			var _summary = out['items'][item]['summary'] || "TBD"
			var _description = out['items'][item]['description']
			var _location = out['items'][item]['location']
			console.log(_time, _year, _month, _day, _summary, _description, _location);

			var e = document.createElement("div");
			e.setAttribute("class", "event-item");
			el.appendChild(e);
			
			var dl = document.createElement("p");
			dl.setAttribute("class", "date-label");
			e.appendChild(dl);
			
			var m = document.createElement("span");
			m.setAttribute("class", "month");
			m.appendChild(document.createTextNode(_month));
			dl.appendChild(m);
			var dn = document.createElement("span");
			dn.setAttribute("class", "date-number");
			dn.appendChild(document.createTextNode(_day));
			dl.appendChild(dn);

			var dt = document.createElement("div");
			dt.setAttribute("class", "details");
			e.appendChild(dt);
			var title = document.createElement("h2");
			title.setAttribute("class", "title");
			title.appendChild(document.createTextNode(_summary));
			dt.appendChild(title);
			if (_description) {
				var des = document.createElement("p");
				des.setAttribute("class", "description");
				des.appendChild(document.createTextNode(_description));
				dt.appendChild(des);
			}
			var timep = document.createElement("p");
			timep.setAttribute("class", "time");
			timep.innerHTML = "<i class=\"fa fa-clock-o\"></i>" + _time;
			dt.appendChild(timep);
			if (_location) {
				var loc = document.createElement("p");
				loc.setAttribute("class", "location");
				loc.innerHTML = "<i class=\"fa fa-map-marker\"></i>" + _location
				dt.appendChild(loc);
			}	
		}
		var rm = document.createElement("a");
		rm.innerHTML = "All events<i class=\"fa fa-chevron-right\"></i>"
		rm.setAttribute("class", "read-more");
		rm.setAttribute("href", "calendar.html");
		el.appendChild(rm);
	})
	.catch(err => { throw err });
}

get_calender();
