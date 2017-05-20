import web
import RPi.GPIO as GPIO 
from web import form

GPIO.setmode(GPIO.BCM)
GPIO.setup(7, GPIO.OUT)

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
 form.Button("btn", id="btnR", value=True, html="on", class_="on"),
 form.Button("btn", id="btnG", value=False, html="off", class_="off")
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
        userData = web.input()
		GPIO.output(7, userData.btn)
		
		print ""
		
        #if userData.btn == "on":
         #   GPIO.output(7,True) #Turn on the LED
          #  print "LED is ON"   #prints the status in Pi's Terminal
        #elif userData.btn == "off":
         #   GPIO.output(7,False) #Turn of the LED
          #  print "LED is OFF" #prints the status in Pi's Terminal
			
        raise web.seeother('/')
# run
if __name__ == '__main__':
    app.run()
