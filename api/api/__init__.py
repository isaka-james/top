""" api module """

from flask import Flask

app = Flask(__name__)

from api.views import *
