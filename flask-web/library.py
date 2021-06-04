# library.py
from flask import Flask, render_template, request, redirect, send_from_directory
from elasticsearch import Elasticsearch
from pprint import pprint
import json
import os

es = Elasticsearch()

app = Flask(__name__)

@app.route("/")
def main():
    return "Hello world from Flask!"


cat_dict = {"contracts": "Sözleşme",
            "inside": "Kurum İçi",
            "invoices": "Fatura",
            "others": "Diğer",
            "security": "Güvenlik"}

cat_tr_dict = {"Sözleşme": "contracts",
               "Kurum İçi": "inside",
               "Fatura": "invoices",
               "Diğer": "others",
               "Güvenlik": "security"}


def path2cat(path):
    cat_name = path.split('/')[-2]
    return cat_dict[cat_name]


css_dict = {"contracts": "warning",
            "inside": "success",
            "invoices": "info",
            "others": "base",
            "security": "danger"}


def cat2css(path):
    cat_name = path.split('/')[-2]
    return css_dict[cat_name]


def tuple2list(t_data):
    res = []
    for t in t_data:
        res.append(t[0])
    return ', '.join(res)


#endpoint for search
@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == "POST":
        query_text = request.form['search']
        doc_type = request.form['doc_type']
        print(doc_type)
        body = {
            'size': 1000,
            "query": {
                "bool": {
                    "must":  [
                        {
                            "query_string": {
                                "query": "({})".format(query_text),
                                "default_field": "content"
                            },
                        },
                        # {
                        #     "match": {
                        #         "category": "{}".format(doc_type)
                        #     }
                        # }

                    ],
                }
             }
        }

        if doc_type != 'Tümü':
            category_query = {
                "match": {
                    "category": "{}".format(cat_tr_dict[doc_type])
                }
            }
            body['query']["bool"]['must'].append(category_query)

        # if doc_type
        pprint(body)
        data = []
        num_results = 0
        try:
            res = es.search(index='my-index', body=body)
            for doc_dict in res["hits"]["hits"]:
                doc_name = doc_dict["_source"]["name"]
                doc_content = doc_dict["_source"]["content"]
                num_count = doc_content.lower().count(query_text.lower())
                keywords = doc_dict["_source"]["keywords"].split(", ")
                base_name = os.path.basename(doc_name)

                doc_path = "tos?filename=" + doc_name
                # cat_name = path2cat(doc_name)
                cat_name = doc_dict["_source"]["category"]
                cat_name_tr = cat_dict[cat_name]
                creation_date = doc_dict["_source"]["creation_date"]
                css_name = cat2css(doc_name)

                data.append((
                            "https://upload.wikimedia.org/wikipedia/commons/thumb/8/87/PDF_file_icon.svg/833px-PDF_file_icon.svg.png",
                            doc_path, base_name, cat_name_tr, css_name, keywords, num_count, creation_date))
            num_results = len(res["hits"]["hits"])
        except Exception as e:
            print(e)

            # break
            # data = [("https://upload.wikimedia.org/wikipedia/commons/thumb/8/87/PDF_file_icon.svg/833px-PDF_file_icon.svg.png", doc_path, base_name),
            #         ("https://upload.wikimedia.org/wikipedia/commons/thumb/6/6b/Picture_icon_BLACK.svg/1200px-Picture_icon_BLACK.svg.png", "doküman2.png", "doküman2.png")]
        return render_template('search.html', data=data, records="{} sonuç listelendi".format(num_results), hidden="")
    return render_template('search.html', hidden="hidden")


@app.route("/tos", methods=['GET', 'POST'])
def tos():
    workingdir = os.path.abspath(os.getcwd())
    filepath = workingdir
    return send_from_directory(filepath, request.args.get('filename'))


@app.route('/process')
def process():
    return "Hello"
    
if __name__ == "__main__":
    app.run()
