import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import os
import redflagdealsScraper
import datetime

def login():
	project_id = "cdndiscountrfdservice"
	credential_path = r".\auth\cdndiscountservice-df4dc7a85942.json"
	os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credential_path
	cred = credentials.ApplicationDefault()
	firebase_admin.initialize_app(cred, {
	  'projectId': project_id,
	})

	db = firestore.client()	
	return db

def getRFDdata(db): 
	print ("Getting data...")
	rfd_threads = db.collection(u"rfd_threads")
	threads = rfd_threads.get()
	for thread in threads:
		print (thread.to_dict()['title'].encode("utf-8"))

def pushRFDdata(db, content):
	print ("Setting data...")
	rfd_threads = db.collection(u"rfd_threads")
	for topic in content:
		doc_rfd_threads = rfd_threads.document(topic['title'])
		doc_rfd_threads.set({
			u'topic' : topic['topic'],
			u'hashtags' : topic['hashtags'],
			u'link' : topic['link'],
			u'title': topic['title'],
			u'points': topic['points'],
			u'upvotes': 0,
			u'origin' : 'RFD',
			u'date' : datetime.datetime.now()
			})

if __name__ == '__main__':
	db = login()
	pushRFDdata(db, redflagdealsScraper.getRFDThreads())
	getRFDdata(db)
