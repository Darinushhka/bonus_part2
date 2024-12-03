import os
from fastapi import APIRouter
from elasticsearch import Elasticsearch


router=APIRouter(tags=['Known Ransomware СVEs'])

@router.get("/get/known")
def get_known():
    index_name = 'cve'
    es_url = os.environ.get('ES_URL')
    es_token = os.environ.get('ES_TOKEN')
    
    if not (es_token and es_url):
        print('Elasticsearch URL and/or Token not provided')
    
    client = Elasticsearch(es_url, api_key = es_token)

    response = client.search(index=index_name, body={
            "size": 10,
            "query": {
                "match": {"knownRansomwareCampaignUse": "Known"}},
        })
    
    return [doc['_source'] for doc in response.get('hits', {}).get('hits', [])]

