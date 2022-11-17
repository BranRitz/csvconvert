import json
from bottle import run, post, get, request
import sys
import json
import httplib2
import pandas as pd

@post('/convert')
def convert():
    try:
        username = sys.argv[1]
        (resp_headers, content) = c.request(f"http://localhost:8000/v1/professor/data/{username}/", "GET")
        # data = content.json()
        data = json.loads(content)
        # data = json.loads(json.dumps(content))
        print(type(data))
        df = pd.DataFrame.from_dict(data)
        file_name = f"surveys_{username}.csv"
        df.to_csv(file_name, index=False, header=False)
        # df = pd.read_json(data)
        # df.to_csv('data.csv', encoding='utf-8', index=False)
    except Exception:
        pass


if __name__ == "__main__":
    c = httplib2.Http()
    convert()









