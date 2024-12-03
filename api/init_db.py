import os
import json
from uuid import uuid4
from fastapi import APIRouter
from elasticsearch import Elasticsearch

router = APIRouter(tags=['Init db'])

def load_vulnerabilities(file_path='data/known_exploited_vulnerabilities.json'):
    with open(file_path, 'r') as file:
        data = json.load(file)
        vulnerabilities = data["vulnerabilities"]
    return vulnerabilities

@router.get('/init-db')
def text_init_db_content():
   
    index_name = 'cve'
    es_url = os.environ.get("ES_URL")
    es_token = os.environ.get("ES_TOKEN")

    if not (es_token and es_url):
        print('Elasticsearch URL and/or Token not provided')

    client = Elasticsearch(es_url, api_key = es_token)

    data = load_vulnerabilities()
    for vuln in data:
       doc = {
           "cveID": vuln.get("cveID"),
            "vendorProject": vuln.get("vendorProject"),
            "product": vuln.get("product"),
            "vulnerabilityName": vuln.get("vulnerabilityName"),
            "dateAdded": vuln.get("dateAdded"),
            "shortDescription": vuln.get("shortDescription"),
            "requiredAction": vuln.get("requiredAction"),
            "dueDate": vuln.get("dueDate"),
            "knownRansomwareCampaignUse": vuln.get("knownRansomwareCampaignUse"),
            "notes": vuln.get("notes"),
            "cwes": vuln.get("cwes"),
       }

       client.create(index=index_name, id=str(uuid4()), body=doc)
    return 'Succes!!!'