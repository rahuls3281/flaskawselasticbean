from flask import Flask

application=Flask(__name__)

@application.route("/")
def get_home():
    return {"message":"This is home"}

if __name__=="__main__":
    application.run()