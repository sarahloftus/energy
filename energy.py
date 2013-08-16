import webapp2
from google.appengine.ext.webapp import template
import datetime
import models

class MainPage(webapp2.RequestHandler):
	
	def get(self):

		template_values = {'fish': 5}

		template_values['dog'] = 3
		template_values['title'] = 'Home'
		template_values['today'] = datetime.date.today().isoformat()

		self.response.out.write(
			template.render('/home/sarah/energy/form.html', template_values)
			)

class OutputPage(webapp2.RequestHandler):
	
	def post(self):

		post_values = self.request.POST
		post_values["title"] = "Output"
		posted_date = datetime.datetime.strptime(post_values["date"], "%Y-%m-%d")
		posted_units = float(post_values["units"])
		entry = models.Entry(date=posted_date, units=posted_units)
		entry.put()

		self.response.out.write(
			template.render('/home/sarah/energy/output.html', post_values)
			)

application = webapp2.WSGIApplication([
	('/', MainPage),
	('/output', OutputPage),
], debug=True)