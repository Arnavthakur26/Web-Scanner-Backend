from flask import *
from main import single
import json, time

app = Flask(__name__)

def convert_sets_to_lists(obj):
    if isinstance(obj, set):
        return list(obj)
    elif isinstance(obj, dict):
        return {key: convert_sets_to_lists(value) for key, value in obj.items()}
    elif isinstance(obj, list):
        return [convert_sets_to_lists(item) for item in obj]
    else:
        return obj

@app.route("/", methods=['GET'])
def hello():
    return "Hello World!"

@app.route("/scan", methods=['GET'])
def scan():
    target_url = str(request.args.get("url"))
    results = single(target_url)

    print("\n\n RESULTS: ")
    print(results)

    # Convert sets to lists within the dictionary
    results_json = json.dumps(convert_sets_to_lists(results))  

    return results_json

if __name__ == '__main__':
    app.run(port=7777)
