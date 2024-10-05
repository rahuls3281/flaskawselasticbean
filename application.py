from flask import Flask

application=Flask(__name__)

@application.route("/")
def get_home():
    return {"message":"This is home"}

@application.route("/hello")
def hello():
    return {"message":"Hello Bro"}

if __name__=="__main__":
    application.run()