import web
import RPi.GPIO as GPIO 
from web import form

GPIO.setmode(GPIO.BCM)
GPIO.setup(29, GPIO.OUT)

#Defining the index page
urls = ('/', 'index')
render = web.template.render('templates') #index.html is stored in '/templates' folder
app = web.application(urls, globals())

""" Defining the buttons. 
	id: 	id of element 
	value: 	button value as interpreted by Python
	html: 	text displayed in HTML page. 
	class_: is HTML class
	"""
my_form = form.Form(
 form.Checkbox("toggleCtrl", id="toggleCtrl", value="YES", class_="on"),
)
# Above, we actually need a toggle (or checkbox), not a button
# This would read its value from a file, and write to the same file

# define the task of index page
class index:
    # rendering the HTML page
    def GET(self):
        form = my_form()
	title = "Python Pi Garage Door"

        return render.index(form, title)

    # posting the data from the webpage to Pi
    def POST(self):
        # get the data submitted from the web form
        form_data = web.input()
	
	if form_data.has_key("toggleCtrl"):
		GPIO.output(29, False)
		print "Open"

	elif !form_data.has_key("toggleCtrl"):
		GPIO.output(29, True)
		print "Close"
		
        raise web.seeother('/')
# run
if __name__ == '__main__':
    app.run()
