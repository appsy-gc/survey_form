from flask import Flask, render_template
from datetime import datetime
import pytz

app = Flask(__name__)

@app.route('/')
def index():
    # Define timezones for team members
    people_timezones = {
        "Danielle": "America/Phoenix",
        "Alan": "America/Phoenix",
        "Tyler": "America/Chicago",
        "Appsy": "Australia/Brisbane",
        "Gav/HO": "Australia/Sydney"
    }

    people_times = []

    for person, tz_name in people_timezones.items():
        tz = pytz.timezone(tz_name)
        current_time = datetime.now(tz).strftime("%H:%M:%S - %d/%m/%Y")
        people_times.append({"name": person, "current_time": current_time})

    # QnA times (in EST)
    qna_times = {
        "Nutrition L1": {"Mon": "13:00", "Wed": "13:00", "Thur": "18:00"},
        "Nutrition L2": {"Mon": "19:00", "Wed": "09:00", "Thur": "19:00"},
        "Business Mastery": {"Mon": "12:00", "Wed": "12:00", "Thur": "19:00"}
    }

    return render_template("index.html", people_times=people_times, qna_times=qna_times)

if __name__ == "__main__":
    app.run(debug=True)
