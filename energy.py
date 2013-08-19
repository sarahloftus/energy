import webapp2
from google.appengine.ext.webapp import template
import datetime
import models
import time

class MainPage(webapp2.RequestHandler):
	
	def get(self):

		template_values = {'title': 'Home', 'today': datetime.date.today().isoformat(), 'entries': models.Entry.query()}

		self.response.out.write(
			template.render('form.html', template_values)
			)
	
	def post(self):

		post_values = self.request.POST

		posted_date = datetime.datetime.strptime(post_values["date"], "%Y-%m-%d")
		posted_units = float(post_values["units"])
		entry = models.Entry(date=posted_date, units=posted_units)
		entry.put()
		# delay to hack eventual consistency of ndb
		time.sleep(1)

		self.redirect('/')

application = webapp2.WSGIApplication([
	('/', MainPage),
], debug=True)
