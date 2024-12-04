import json

def format_jobs_by_wilaya():
    def _load_data(file):
        try:
            with open(file, "r", encoding='utf-8') as json_file:
                return json.load(json_file)
        except FileNotFoundError:
            print(f"File '{file}' not found.")
            return []
        except json.JSONDecodeError:
            print(f"Unable to decode JSON from file '{file}'.")
            return []

    def _save_data(data, file):
        try:
            with open(file, "w", encoding='utf-8') as json_file:
                json.dump(data, json_file, indent=4, ensure_ascii=False)
            print(f"Formatted data saved to {file}")
        except IOError:
            print(f"Unable to write to file '{file}'.")

    input_file = "scraped_data.json"
    output_file = "formatted_scraped_data.json"

    data = _load_data(input_file)
    if not data:
        print("No data found or unable to load data.")
        return

    formatted_data = {}
    for job in data:
        wilaya = job.get("Wilaya", "Unknown")
        if wilaya not in formatted_data:
            formatted_data[wilaya] = []
        formatted_data[wilaya].append(job)
    
    _save_data(formatted_data, output_file)