#-------------------------------------------------------------------------------
# Name:        presentation
# Purpose:     Islandora Camp 2014 Presentation
#
# Author:      Jeremy Nelson
#
# Created:     2014/03/09
# Copyright:   (c) Jeremy Nelson, Colorado College 2014
# Licence:     GPLv2
#-------------------------------------------------------------------------------
import json
import urllib.request
from flask import abort, Flask, g, jsonify, redirect, render_template, request
from flask import url_for
presentation = Flask(__name__)
REFS = []

for row in [
    ('/home/jpnelson/intro2libsys/thing/Article/bibliographic-framework-as-a-web-of-data.json','bibframe-newlogo.png'),
    ('/home/jpnelson/intro2libsys/thing/WebPage/bibframe.json', 'bibframe-newlogo.png'),
    ('/home/jpnelson/intro2libsys/thing/Article/bibframe-av-modeling-study-defining-a-flexible-model-for-description-of-audiovisual-resources.json',
     'bibframe-newlogo.png'),
    ('/home/jpnelson/intro2libsys/thing/WebPage/getting-started-schema-org.json', 'schema-org.png'),
    ('/home/jpnelson/intro2libsys/thing/WebPage/fedora.json', 'fedora-commons-4-beta.png'),
    ('/home/jpnelson/intro2libsys/thing/WebPage/linked-open-vocabularies-lov.json', 'rdf-w3c.gif'),
    ('/home/jpnelson/intro2libsys/thing/WebPage/the-marc21-vocabularies-from-metadata-management-associates.json', 'marc21h2.gif'),
    ('/home/jpnelson/intro2libsys/thing/WebPage/schema-org.json', 'schema-org.png'),
    ('/home/jpnelson/intro2libsys/thing/BlogPosting/visualising-schemaorg.json', 'schema-org.png')]:
    uri_json = json.load(open(row[0]))
    reference = {'id': uri_json.get('@id'), 'author': [], 'thumbnail': "http://intro2libsys.info/islandora-camp-2014/static/img/{}".format(row[1])}
    for row in uri_json.get('author',[]):
        author_id = row.get('@id').split("/")[-1]
        author_json = json.load(open('/home/jpnelson/intro2libsys/thing/Person/{}.json'.format(author_id)))
        reference['author'].append({"name": author_json.get('name')[0]['@value']})
    if 'copyrightYear' in uri_json:
        reference['copyright'] = uri_json['copyrightYear'][0].get('@value')
    else:
        reference['copyright'] = 2014
    if 'headline' in uri_json:
        reference['title'] = uri_json['headline'][0]['@value']
    else:   
        reference['title'] = uri_json['name'][0]['@value']
    if 'url' in uri_json:
        reference['url'] = uri_json['url'][0]['@value']
    REFS.append(reference)

@presentation.route("/references")
@presentation.route("/references.html")
def reference_view():
    return render_template("references.html", references=REFS)

@presentation.route("/<name>")
@presentation.route("/<name>.html")
def slide(name):
    return render_template("{}.html".format(name))


@presentation.route("/")
def index():
    return render_template("index.html")

def main():
    host = '0.0.0.0'
    port = 7100
    presentation.run(
        host=host,
        port=port,
        debug=True)

if __name__ == '__main__':
    main()
