import flask
import firestoreHandler
from firebase_admin import firestore
from flask_cors import CORS


print("Starting server...")
app = flask.Flask(__name__)
CORS(app)
THREADS = firestoreHandler.login().collection(u"rfd_threads")




@app.route('/threads/featured', methods=['GET'])
def get_featured():
	response_object = {'status' : 'success'}
	threads = THREADS.document()
	query = THREADS.order_by(u'date', direction=firestore.Query.DESCENDING).limit(10)
	results = query.get()
	results_dict = {result.to_dict()['title'] : result.to_dict() for result in results}
	response_object['threads'] = results_dict	
	return (flask.jsonify(response_object))

def _ensure_thread(id):
    try:
        return threads.document(id).get()
    except:
        flask.abort(404)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)

