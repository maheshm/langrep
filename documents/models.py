from pymongo import MongoClient
from bson.objectid import ObjectId
import datetime

# Create your models here.
class Document():
  def __init__(self):
    client = MongoClient()
    db = client.langrep
    self.collection = db.documents

  def to_dict(self, params, user_id):
    return {"title":params['title'],"sub_title":params["subtitle"],"text":params["content"],"tag":params["tag"],"pub_date":datetime.datetime.now(), "user":user_id}

  def find_by_id(self, id):
    oid = ObjectId(id)
    return self.collection.find_one({"_id": oid})

class Tag():
  def __init__(self):
    client = MongoClient()
    db = client.langrep
    self.collection = db.tags

  def to_dict(seld, params):
    return ("name": params['name'], "parent": ObjectId(params['parent']))

  def find_by_tag_name(self, name):
    return self.collection.find_one({"name": name})
