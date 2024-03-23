# app.py
from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime, timedelta

app = Flask(__name__)

class Record:
    def __init__(self, input_date, output_date):
        self.input_date = input_date
        self.output_date = output_date

records = []  # Initialize an empty list to store records

@app.route('/', methods=['GET', 'POST'])
def index():
    expiry_date = None
    if request.method == 'POST':
        try:
            holiday_date_str = request.form['holiday_date']
            holiday_date = datetime.strptime(holiday_date_str, '%Y-%m-%d')
            expiry_date = holiday_date + timedelta(days=45)
            formatted_expiry_date = expiry_date.strftime("%d %B %Y")  # Format the expiry date
            records.append(Record(holiday_date_str, formatted_expiry_date))  # Add record to the list
        except Exception as e:
            return f'Error: {str(e)}'
    return render_template('index.html', expiry_date=expiry_date, records=records)

@app.route('/delete', methods=['POST'])
def delete_record():
    record_index = int(request.form['record_index'])
    del records[record_index]  # Delete the record
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
    