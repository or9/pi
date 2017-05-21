import web
import RPi.GPIO as GPIO 
from web import form

pin = 21

GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.OUT)

#Defining the index page
urls = ('/', 'index')
render = web.template.render('templates') #index.html is stored in '/templates' folder
app = web.application(urls, globals())

my_form = form.Form(
	form.Checkbox("toggleCtrl", id="toggleCtrl", value="YES", class_="on", checked="checked")
)

# Above, we actually need a toggle (or checkbox), not a button
# This would read its value from a file, and write to the same file

# define the task of index page
class index:
    # rendering the HTML page
    def GET(self):
	if GPIO.input(pin) == 0:
		element = form.Checkbox("toggleCtrl", id="toggleCtrl", value="YES", class_="on", checked="checked")
	else:
		element = form.Checkbox("toggleCtrl", id="toggleCtrl", value="YES", class_="on")

	my_form = form.Form(element)
	title = "Python Pi Garage Door"

        return render.index(my_form, title)

    # posting the data from the webpage to Pi
    def POST(self):
        # get the data submitted from the web form
        form_data = web.input()
	
	if form_data.has_key("toggleCtrl"):
		GPIO.output(pin, False)
		print "Open"

	elif not form_data.has_key("toggleCtrl"):
		GPIO.output(pin, True)
		print "Close"
		
        #raise web.seeother('/')
# run
if __name__ == '__main__':
    app.run()
