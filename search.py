from elasticsearch import Elasticsearch

def search_reviews(keyword):
    es = Elasticsearch(
        [
            {
                'host': 'localhost', 
                'port': 9200, 
                'scheme': 'https',
                'use_ssl': True
            }
        ],
        verify_certs=False,
        http_auth=('elastic', 'insert_elastic_password')
    )
    
    index_name = "imdb_reviews"

    # construct the search request
    search_body = {
        "query": {
            "match": {
                "review": keyword
            }
        }
    }

    # execute the search request
    response = es.search(index=index_name, body=search_body)

    # process the search hits and print results
    for hit in response['hits']['hits']:
        print("Score:", hit['_score'], "Review:", hit['_source']['review'])

if __name__ == "__main__":
    keyword = "monkey"  # DEFINE KEY WORD HERE
    search_reviews(keyword)
