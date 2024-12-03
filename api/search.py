import os
from fastapi import APIRouter, Query
from elasticsearch import Elasticsearch

router = APIRouter(tags=['Search CVEs'])

@router.get("/search")
def search_vulnerabilities(query: str = Query(..., description="Search keyword for CVE entries")):
    index_name = 'cve'
    es_url = os.environ.get("ES_URL")
    es_token = os.environ.get("ES_TOKEN")

    if not (es_token and es_url):
        print('Elasticsearch URL and/or Token not provided!')

    client = Elasticsearch(es_url, api_key = es_token)

    response = client.search(index=index_name, body={
        "query": {
            "query_string": {
                "query": query,
                "fields": ["*"]
                }
            },
        "size": 1223     
        } 
    )
        
    return [doc['_source'] for doc in response.get('hits', {}).get('hits', [])]
