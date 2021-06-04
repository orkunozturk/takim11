from elasticsearch import Elasticsearch
from pprint import pprint

es = Elasticsearch()
'''
data = [dict(name="hello.pdf",
             content='merhaba dünya',
             path='/home/ibrahim/hello.pdf',
             keywords='')]

for a_data in data:
    res = es.index(index='my-index', body=a_data)
    pprint(res)

'''
# body = {'query': {'bool': {'must': [{'match': {'gender': 'male'}}, {'range': {'age': {'gte': 50}}}]}}}

body = {
  "query": {
    "query_string": {
      "query": "(python)",
      "default_field": "content"
    }
  }
}

res = es.search(index='my-index', body=body)
#pprint(res)

print(len(res["hits"]["hits"]))

print('finish')
