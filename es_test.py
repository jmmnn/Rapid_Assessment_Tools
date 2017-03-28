from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search, Q , Index, DocType
from elasticsearch_dsl.connections import connections
import targets_dev as ts
import text_extract as ex
import pandas as pd

#Default connection and port 9200
connections.create_connection(hosts=['localhost'], timeout=20)

#Index methods:
#i = Index('my-index') # create the elasticsearch index
#i.create()   #use this line only the first time
# print (i.exists()) # Check if index exists
# i.delete()  # delete the index

#Define the index you are working with:
i = Index('my-index')

# s = Search(using=client, index="my-index") \
#     .filter("term", category="search") \
#     .query("match", title="python")   \
#     .query(~Q("match", description="beta"))
#
# s.aggs.bucket('per_tag', 'terms', field='tags') \
#     .metric('max_lines', 'max', field='lines')
#
# response = s.execute()
#
# for hit in response:
#     print(hit.meta.score, hit.title)
#
# for tag in response.aggregations.per_tag.buckets:
#     print(tag.key, tag.max_lines.value)
