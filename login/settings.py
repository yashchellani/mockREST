from pymongo import MongoClient
import urllib.parse
import os
password = urllib.parse.quote_plus('YASH@atlas')
MONGO_URI = 'mongodb+srv://yashc:%s@cluster0.xurqe.mongodb.net/mockREST1' %(password)
