# app.py
from flask import Flask, render_template, request
from datetime import datetime, timedelta

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            holiday_date_str = request.form['holiday_date']
            holiday_date = datetime.strptime(holiday_date_str, '%Y-%m-%d')
            expiry_date = holiday_date + timedelta(days=45)
            formatted_expiry_date = expiry_date.strftime("%d %B %Y")  # Format the expiry date
            return render_template('index.html', expiry_date=formatted_expiry_date)
        except Exception as e:
            return f'Error: {str(e)}'
    return render_template('index.html', expiry_date=None)

if __name__ == '__main__':
    app.run(debug=True)
