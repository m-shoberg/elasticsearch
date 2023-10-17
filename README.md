## ElasticSearch Instance
A Searchable PostgreSQL database Via ElasticSearch

`https://www.elastic.co/downloads/elasticsearch`

Download & Unzip: `elasticsearch-8.10.3-darwin-x86_64.tar.gz`

run `bin/elasticsearch` in `elasticsearch-8.10.4` directory

take note of username (default:elastic) and password:

after logging in you should see something like:

{
  "name" : "theendlesssummer.lan",</br>
  "cluster_name" : "elasticsearch",</br>
  "cluster_uuid" : "JnQGQYpNTkmmh0L9JF6Uwg",</br>
  "version" : {</br>
    "number" : "8.10.4",</br>
    "build_flavor" : "default",</br>
    "build_type" : "tar",</br>
    "build_hash" : "b4a62ac808e886ff032700c391f45f1408b2538c",</br>
    "build_date" : "2023-10-11T22:04:35.506990650Z",</br>
    "build_snapshot" : false,</br>
    "lucene_version" : "9.7.0",</br>
    "minimum_wire_compatibility_version" : "7.17.0",</br>
    "minimum_index_compatibility_version" : "7.0.0"</br>
  },</br>
  "tagline" : "You Know, for Search"</br>
}

## PostgreSQL Instance - Database:

Initialize PostgreSQL session as default user:
`psql -U postgres`
(may require password)
