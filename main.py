from flask import Flask, render_template, request, url_for, redirect, make_response, jsonify
from bson import ObjectId
from datetime import datetime
from config import DevConfig
from db import get_db

app = Flask(__name__, template_folder='templates')
app.config.from_object(DevConfig)


db = get_db()


@app.route('/user', methods=['GET'])
def about():
    return render_template('about.html')


client_posts = db['posts']


@app.route('/posts', methods=['GET'])
def index():
    posts = client_posts.find()
    return render_template('index.html', posts=posts)


@app.route('/posts/create', methods=['GET', 'POST'])
def createPost():
    if request.method == 'POST':
        obj = request.json
        print(obj)
        dateNow = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        obj['date_created'] = dateNow
        client_posts.insert_one(obj)
        return make_response(jsonify({'message': 'Post Created', 'time': dateNow}),
                             201)
    return render_template('create.html')


@app.route('/posts/<string:id>/', methods=['GET', 'DELETE', 'PUT'])
def getPost(id):
    if request.method == 'GET':
        try:
            objectID = ObjectId(id)
            post = client_posts.find_one({"_id": objectID})
            if post is None:
                return make_response(jsonify({'message': 'Post not found'}), 404)
            return render_template('post.html', post=post)

        except:
            return make_response(jsonify({'message': 'Invalid parameter value'}), 400)
    elif request.method == 'DELETE':
        try:
            objectID = ObjectId(id)
            deleteResult = client_posts.delete_one({"_id": objectID})
            if deleteResult.deleted_count == 0:
                return make_response(jsonify({'message': 'Post not found'}), 404)
            return make_response(jsonify({'message': 'Post deleted'}), 200)

        except:
            return make_response(jsonify({'message': 'Invalid parameter value'}), 400)
    elif request.method == 'PUT':
        try:
            objectID = ObjectId(id)
            obj = request.json
            updateResult = client_posts.update_one({"_id": objectID}, {"$set": obj})
            if updateResult.modified_count == 0:
                return make_response(jsonify({'message': 'Post not found'}), 404)
            return make_response(jsonify({'message': 'Post was updated'}), 200)

        except:
            return make_response(jsonify({'message': 'Invalid parameter value'}), 400)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
