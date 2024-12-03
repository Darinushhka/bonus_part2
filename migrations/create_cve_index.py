import os
from elasticsearch import Elasticsearch

def create_cve_index():
    es_url = os.environ.get('ES_URL')
    es_token = os.environ.get('ES_TOKEN')

    if not (es_url and es_token ):
        print('No provide Elasticsearch URL and Token!')
        

    client = Elasticsearch(es_url, api_key=es_token)  
    response = client.indices.create(index="cve")

    if response.meta.status == 200:
        print("Success!")
    else:
        print("Creation failed!")


if __name__ == "__main__":
    create_cve_index()