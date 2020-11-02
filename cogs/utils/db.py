from faunadb import query as q
from faunadb.objects import Ref
from faunadb.client import FaunaClient
import os

fclient = FaunaClient(secret=os.getenv("FAUNA"))

def getUser(user):
  return fclient.query(q.get(
    q.match(
      q.index("users_by_name"),str(user)
      )
    )
  )

def createUser(data):
   fclient.query(q.create(
     q.collection('users'), data
     )
   )

def updateUser(reference,data):
   fclient.query(
     q.update(
       q.ref(reference), data
     )
   )