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

from flask import abort, Flask, g, jsonify, redirect, render_template, request

presentation = Flask(__name__)

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
