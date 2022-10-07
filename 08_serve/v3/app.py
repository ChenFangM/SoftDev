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
    print(__name__)   #where will this go?
    return "No hablo queso!"

<<<<<<< HEAD
app.debug = True # Terminal prints "Debugger is active!"
app.run()

# We predict that the debug mode will be on.
# We DISCOed that everytime the file changes, the terminal reloads
=======
app.debug = True
app.run()
>>>>>>> 3a067dcd7ead1dca8da0cf3b25e451cdecffe358
