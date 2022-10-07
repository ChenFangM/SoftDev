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
    print("the __name__ of this module is... ")
    print(__name__)
    return "No hablo queso!"

if __name__ == "__main__":  # true if this file NOT imported
    app.debug = True        # enable auto-reload upon code change
    app.run()
<<<<<<< HEAD

# We predict that if __name__ is not __main__, then nothing will happen
# QCC: When is __name__ not __main__?
=======
>>>>>>> 3a067dcd7ead1dca8da0cf3b25e451cdecffe358
