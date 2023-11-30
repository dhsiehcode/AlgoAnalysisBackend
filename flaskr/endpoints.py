import sqlite3
from flask import current_app, g, Blueprint, request
import requests
from flaskr import vocareum
from flaskr import db
from flask import Flask

'''
author: Dennis

should have most endpoints here

TODO:
1. endpoints to download submissions 
    1-1 error handling to make sure we don't re-download code that hasn't bee changed
    1-2 download according to specification such as course, assignment, part

2. endpoints to run submission
    2-1 future handling to bundle with downloading so code not changed doesn't get run twice
    2-2 run multiple tests on submission as desired by user
    2-3 return information desired by user (maybe can be handled on front-end)


 
'''

## sets up a blueprint so it can be called
bp = Blueprint('services', __name__, url_prefix='/services')