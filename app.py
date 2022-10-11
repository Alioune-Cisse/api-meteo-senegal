from flask import Flask, render_template, request, jsonify, Response
from meteo import weather
from flask_cors import CORS
from datetime import datetime, timedelta
from meteostat import Point, Daily, Stations, Hourly, Monthly
import json
import ast

#donnees = getdata()

app = Flask(__name__)
app.config["DEBUG"] = True
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
app.config['JSON_AS_ASCII'] = False



@app.route('/')
def index():
    return render_template("index.html")



@app.route('/api/v1')
def my_route():
    
  date1 = (datetime.now() - timedelta(days=7)).strftime('%d/%m/%Y %H:%M:%S')
  date2 = (datetime.now() + timedelta(hours=12)).strftime('%d/%m/%Y %H:%M:%S')

  momentum = request.args.get('moment', default="hour", type=str)
  start_date = request.args.get('start', default=date1, type=str)
  end_date = request.args.get('end', default=date2, type=str)

  start = datetime.strptime(start_date, '%d/%m/%Y %H:%M:%S')
  end = datetime.strptime(end_date, '%d/%m/%Y %H:%M:%S')

  moment = (momentum == "hour" and Hourly) or (momentum == "day" and Daily) or (momentum == "month" and Monthly)
  print(moment)
  repartitions = weather(moment=moment, start=start, end=end)
  response = jsonify(repartitions)
  response.headers.add('Access-Control-Allow-Methods', 'GET,POST,PUT,DELETE,OPTIONS')
  return response


if __name__ == "__main__":
    app.run(debug=True, port=3000)















