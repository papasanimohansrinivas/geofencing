# (C) Copyright ${year} Nuxeo (http://nuxeo.com/) and others.
# 	
# 	Licensed under the Apache License, Version 2.0 (the "License");
# 	you may not use this file except in compliance with the License.
# 	You may obtain a copy of the License at
# 	
# 	    http://www.apache.org/licenses/LICENSE-2.0
# 	
# 	Unless required by applicable law or agreed to in writing, software
# 	distributed under the License is distributed on an "AS IS" BASIS,
# 	WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# 	See the License for the specific language governing permissions and
# 	limitations under the License.
# 	
# 	Contributors:


import csv

from geopy.geocoders import GoogleV3


from geopy.distance import vincenty


import geopy

from geopy.distance import great_circle

geolocator = GoogleV3()

results = []

app = results.append 


corret_ones = {}

outside_city = {}

outside_state = {}


def fun(f,app):
	name,lat,long_ = f
	try:
		lat,long_=float(lat),float(long_)
		original = (lat,long_)
		try:
			l=geolocator.geocode(name)
			result = (l.latitude,l.longitude)
			distance = vincenty(original,result).meters
			print distance
			app([f,distance])
		except geopy.exc.GeocoderQuotaExceeded:
			pass
		except geopy.exc.GeocoderTimedOut:
			pass
	except ValueError:
		pass


c=0

corret_ones["correct"]=[]

outside_city["outsidecity"]=[]

outside_state["outsidestate"]=[]

with open("location-for-dev.csv","r") as d:
	file=csv.reader(d)
	for f in file:
		c+=1
		if 5<=c<=31:
			if len(f)!=0:
				corret_ones["correct"].append(f)
		if 35<c<=43:
			if len(f)!=0:
				outside_city["outsidecity"].append(f)
		if 46<=c<=53:
			if len(f)!=0:
				outside_state["outsidestate"].append(f)

from geopy.geocoders import Nominatim

def location(details):
	geo=Nominatim()
	try:
		leo=geo.geocode(cities[0],addressdetails=True)
		if leo!=None:
			return leo.raw['address']
	except geopy.exc.GeocoderTimedOut:
		return location(details)


def r_():
	for cities in corret_ones["correct"]:
		if location(cities[0])==None:
			print cities[0]
		else:
			print location(cities[0])
	
# for c in outside_city["outsidecity"]:
	# fun(c,app)

# for t in outside_state["outsidestate"]:
	# fun(t,app)