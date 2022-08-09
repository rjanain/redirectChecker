from typing import Optional
from fastapi import FastAPI
import json
import requests

app = FastAPI()

@app.get("/")
def home():
    return {"source_url": "source url not found"}

@app.get("/qa-redirect-checker")
def get_redirection(source_url: Optional[str]=None):
    if(source_url== None):
        return {"Error": "Source url is missing"}
    results= {}
    r = requests.get(source_url, allow_redirects=False)
    actual_redirect = '' if not 'location' in r.headers else r.headers['location']
    status_code = r.status_code
    result = status_code in [301, 302] and actual_redirect == source_url
    results ={
        'source' : source_url,
        'actual_redirect': actual_redirect,
        'status_code' : status_code,
        'result' : result
    }
    json_dump = json.dumps(results) 
    return results