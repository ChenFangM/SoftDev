<<<<<<< HEAD
# New Deal: Fang Min Chen, Ryan Lau, Anson Wong
# SoftDev
# K08: Serve
# Oct 2022
# time spent: .2 hrs
=======
# Clyde 'Thluffy' Sinclair
# SoftDev
# Oct 2022
>>>>>>> 3a067dcd7ead1dca8da0cf3b25e451cdecffe358

from flask import Flask
app = Flask(__name__) #create instance of class Flask

@app.route("/")       #assign fxn to route
def hello_world():
    print("about to print __name__...")
<<<<<<< HEAD
    print(__name__)   #where will this go? in the terminal
=======
    print(__name__)   #where will this go?
>>>>>>> 3a067dcd7ead1dca8da0cf3b25e451cdecffe358
    return "No hablo queso!"

app.run()

<<<<<<< HEAD
# We predict this will do the same thing as v0
# except "about to print __name__..." will also 
# be printed in the terminal
=======
>>>>>>> 3a067dcd7ead1dca8da0cf3b25e451cdecffe358
