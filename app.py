from flask import Flask, jsonify, request
import cv2

# initializing the app
app = Flask(__name__)

# creating a home directory
@app.route("/")
def home():
    return "Hello"


# creating anothero route for the open cv computation
@app.route("/opencv")
def cv():

    # you can then write the function for opencv here

    # let's see how you get input into your api, let's say I wanna get a name  as an input
    name = request.json["name"] # this how you input into your api

    # you can write the opencv processing here

    # let's see how to output from this api
    return jsonify({"name":name})





# this part is responsible for starting the flask wsgi server.
if __name__ == "__main__":
    app.run(debug=True)