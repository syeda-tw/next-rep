from flask import Flask, render_template
from scraper import run_scraper
import json
from data_formatter import format_jobs_by_wilaya

app = Flask(__name__)

@app.route('/')
def home():
    format_jobs_by_wilaya()

    try:
        with open('formatted_scraped_data.json', 'r') as file:
            scraped_data = json.load(file)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        scraped_data = {}

    return render_template('index.html', scraped_data=scraped_data)
  
@app.route('/scrape')
def scrape():
    run_scraper()
    return 'Scraping completed successfully!'

@app.route('/wilaya/<wilaya_name>')
def show_wilaya_jobs(wilaya_name):
    try:
        with open('formatted_scraped_data.json', 'r') as file:
            scraped_data = json.load(file)
            wilaya_jobs = scraped_data.get(wilaya_name, [])
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        wilaya_jobs = []

    return render_template('wilaya.html', wilaya_name=wilaya_name, jobs=wilaya_jobs)

if __name__ == '__main__':
    app.run(debug=True)
