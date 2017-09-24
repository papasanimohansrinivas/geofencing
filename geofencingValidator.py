import csv

from geopy.geocoders import GoogleV3


from geopy.distance import vincenty

import geopy

from geopy.distance import great_circle

geolocator = GoogleV3()



corret_ones = {}

outside_city = {}

outside_state = {}


def fun(f):
	name,lat,long_ = f
	try:
		lat,long_=float(lat),float(long_)
		original = (lat,long_)
		try:
			l=geolocator.geocode(name)
			result = (l.latitude,l.longitude)
			distance = vincenty(original,result).meters
			return distance
		except geopy.exc.GeocoderQuotaExceeded:
			return fun(f)
		except geopy.exc.GeocoderTimedOut:
			return fun(f)
	except ValueError:
		pass



import sys 

inputfile = sys.argv[-2]
outputfile = sys.argv[-1]

w=open(outputfile,"w")

with open(inputfile,"r") as geolocat:
	adr=csv.reader(geolocat)
	rda = csv.writer(w)
	for b in adr:
		if len(b)==3:
			dist=fun(b)
			x1,x2,x3 = b
			if dist<10:
				rda.writerow([x1,x2,x3,"correct"])
			else:
				rda.writerow([x1,x2,x3,"wrong"])
	w.close()