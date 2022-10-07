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
    return "No hablo queso!"

app.run()

<<<<<<< HEAD
# We predict this will do the same thing as v0 except __main__ won't be printed in the terminal
=======
>>>>>>> 3a067dcd7ead1dca8da0cf3b25e451cdecffe358
