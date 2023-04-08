import logging
from flask import Flask,request,render_template
from flask_cors import CORS,cross_origin
import pywhatkit as wapp

logging.basicConfig(filename="app.log",
                    format='%(asctime)s %(message)s', filemode='w', level=logging.DEBUG)

logging.info("Application has been initiat")
app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
@cross_origin()
def homepage():
    return render_template("index.html")

@app.route("/send",methods=["GET","POST"])
@cross_origin()
def Sender():
    if request.method == 'POST':
        number = request.form("Mobile Number")
        message = request.form("Message")
        hours = request.form("Hours")
        minutes = request.form('Minutes')

        try:
            wapp(number,message,hours,minutes)
            results = "Message will be sent on schedule time please keep whatappweb login at the schedule time"
            
            return render_template("index.html",results= results)
        
        except Exception as e:
            results = "Something Went worng"
            return render_template("index.html",results=results)
        
    
    else:
        results = "Something Went Wrong"
        return render_template("index.html",results=results)
    

logging.info("Application proceed to start")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000) 

logging.info("Application Started")


        
        



