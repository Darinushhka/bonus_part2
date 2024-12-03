import os
from fastapi import APIRouter
from elasticsearch import Elasticsearch
from datetime import datetime, timedelta

router = APIRouter(tags=['Last N Days CVEs'])

@router.get("/get/all")
def get_vulnerabilities_from_last_month(limit: int = 40, days: int = 10):
    index_name = 'cve'
    es_url = os.environ.get("ES_URL")
    es_token = os.environ.get("ES_TOKEN")

    if not (es_token and es_url):
        print('Elasticsearch URL and/or Token not provided')

    client = Elasticsearch(es_url, api_key=es_token)

    today = datetime.now()
    last_month_date = (today - timedelta(days=days)).strftime('%Y-%m-%d')

    response = client.search(index=index_name, body={
            "size": limit,  
            "query": {
                "range": {
                    "dateAdded": {
                        "gte": last_month_date,  
                        "lte": today.strftime('%Y-%m-%d'),
                        "format": "yyyy-MM-dd"
                    }
                }
            },
            "sort": [{"dateAdded": {"order": "desc"}}]
        })

    return [doc['_source'] for doc in response.get('hits', {}).get('hits', [])]

