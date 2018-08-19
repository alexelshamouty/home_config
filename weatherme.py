#!/usr/bin/python
#export apikey=50a0d4e894d9cadeaa04ad64572d4af5 ; curl -s "http://api.openweathermap.org/data/2.5/weather?q=Amsterdam&appid=$apikey&units=metric" | python -c 'import json ; import sys ; x = sys.stdin.read() ; unpacked=json.loads(str(x)) ; weather=unpacked["main"] ; print ("Min %dc Max %dc" % (weather["temp_min"], weather["temp_max"]))'
import json
import urllib.request
from i3pystatus import IntervalModule

class Weatherme(IntervalModule):
    settings = (
        ("format", "format string used for output."),
        ("color", "standard color"),
    )
    format = "Current Temp {temp}c Min {temp_min}c Max {temp_max}c Rain:{drizzel}"
    color="#00FF00"
    interval=120
    
    def run(self):
        apikey="50a0d4e894d9cadeaa04ad64572d4af5"
        location="Amsterdam"
        units="metric"
        output=urllib.request.urlopen("http://api.openweathermap.org/data/2.5/weather?q=%s&units=%s&appid=%s" %
                (location,units,apikey))
        json_data=output.read().decode('ascii')
        unpacked_json=json.loads(json_data)
        weather=unpacked_json['main']
        drizzel=unpacked_json['weather'][0]
        cdict = {
                "temp": weather["temp"],
                "temp_min": weather["temp_min"],
                "temp_max": weather["temp_max"],
                'drizzel' : drizzel['description']
                }
        self.output = {
                'full_text': self.format.format(**cdict),
                "color" : self.color
                }

