import requests
from flask import Flask, render_template, request

app = Flask(__name__)

# Replace YOUR_API_KEY with your actual Google API key
API_KEY = "AIzaSyBKBoDDpBC0sWmDqtAdV__gghUPZuywTHc"

@app.route("/")
def index():
    return render_template("index.html", api_key=API_KEY)

@app.route("/route")
def route():
    start = request.args.get("start")
    end = request.args.get("end")
    if not start or not end:
        return "Please provide start and end addresses in the URL parameters", 400
    params = {
        "origin": start,
        "destination": end,
        "key": API_KEY,
    }
    response = requests.get("https://maps.googleapis.com/maps/api/directions/json", params=params)
    data = response.json()
    if data["status"] != "OK":
        return f"Error: {data['status']}", 400
    polyline = data["routes"][0]["overview_polyline"]["points"]
    return polyline

if __name__ == "__main__":
    app.run(debug=True)
