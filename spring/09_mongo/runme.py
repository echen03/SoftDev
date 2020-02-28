from pymongo import MongoClient
from bson.json_util import loads
from random import choice

# test client so this runs fast
client = MongoClient()
db = client.test
doc = db.restaurants

# load data into the database if there isn't any
if doc.estimated_document_count() == 0:
    f = open('dataset.json', 'r')
    to_insert = []
    for line in f.readlines():
        to_insert.append(loads(line))
    doc.insert_many(to_insert)


def query(verbose, q):
    print('Getting %s' % verbose)
    res = [i for i in doc.find(q)]
    print(' Found %d total' % len(res))
    if len(res) > 0:
        print(' Random: [%s]' % choice(res)['name'])
    print()


query('all restaurants in Manhattan', {'borough': 'Manhattan'})
query('all restaurants in zipcode 11214', {'address.zipcode': '11214'})
query('all restaurants in zipcode 11214 with grade C', {'address.zipcode': '11214', 'grades.grade': 'C'})
query('all restaurants in zipcode 11214 with score below 2', {'address.zipcode': '11214', 'grades.score': {'$lt': 2}})
print(
    'We can\'t think of anything more clever, so I guess the real '
    'clever are\033[0;31m the friends we made along the way\033[0m')
