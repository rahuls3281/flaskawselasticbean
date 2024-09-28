from flask import Flask

app=Flask(__name__)

@app.route("/")
def get_home():
    return {"message":"This is home"}

if __name__=="__main__":
    app.run()