from google.appengine.ext import ndb

class Entry(ndb.Model):
	date = ndb.DateProperty(required=True)
	units = ndb.FloatProperty(required=True)
