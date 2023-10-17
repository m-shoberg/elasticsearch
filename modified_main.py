#%%
import psycopg2

def get_data_from_postgres():
    connection = None
    try:
        connection = psycopg2.connect(
            user="postgres",
            password="insert_postgres_password",
            host="localhost",
            port="5432",
            database="imdb_reviews"
        )
        cursor = connection.cursor()

        select_query = "SELECT review, sentiment FROM reviews;"
        cursor.execute(select_query)
        records = cursor.fetchall()
        return records

    except (Exception, psycopg2.Error) as error:
        print("Error while fetching data from PostgreSQL", error)
    finally:
        if connection:
            cursor.close()
            connection.close()

#%%

from elasticsearch import Elasticsearch, helpers

def index_data_in_elasticsearch(data):
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

    # Define Elasticsearch mappings
    mappings = {
        "mappings": {
            "properties": {
                "review": {"type": "text"},
                "sentiment": {"type": "text"},
            }
        }
    }
    if not es.indices.exists(index=index_name):
        es.indices.create(index=index_name, body=mappings)


    # Prepare data for indexing
    es_data = [
        {
            "_index": index_name,
            "_source": {
                "review": record[0],
                "sentiment": record[1]
            }
        }
        for record in data
    ]

    helpers.bulk(es, es_data)

if __name__ == "__main__":
    data_from_postgres = get_data_from_postgres()
    index_data_in_elasticsearch(data_from_postgres)
# %%
