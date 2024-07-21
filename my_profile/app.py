from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
from bson.objectid import ObjectId

app = Flask(__name__)

client = MongoClient('mongodb://localhost:27017/')
db = client.profileDB
profiles_collection = db.profiles

@app.route('/')
def index():
    profiles = profiles_collection.find()
    return render_template('index.html', profiles=profiles)

@app.route('/add', methods=['GET', 'POST'])
def add_profile():
    if request.method == 'POST':
        profile = {
            'name': request.form['name'],
            'objective': request.form['objective'],
            'skills': request.form['skills'],
            'experience': request.form['experience'],
            'education': request.form['education'],
            'projects': request.form['projects'],
            'certifications': request.form['certifications'],
            'languages': request.form['languages']
        }
        profiles_collection.insert_one(profile)
        return redirect(url_for('index'))
    return render_template('add.html')

@app.route('/delete/<id>')
def delete_profile(id):
    profiles_collection.delete_one({'_id': ObjectId(id)})
    return redirect(url_for('index'))

@app.route('/update/<id>', methods=['GET', 'POST'])
def update_profile(id):
    profile = profiles_collection.find_one({'_id': ObjectId(id)})
    if request.method == 'POST':
        updated_profile = {
            'name': request.form['name'],
            'objective': request.form['objective'],
            'skills': request.form['skills'],
            'experience': request.form['experience'],
            'education': request.form['education'],
            'projects': request.form['projects'],
            'certifications': request.form['certifications'],
            'languages': request.form['languages']
        }
        profiles_collection.update_one({'_id': ObjectId(id)}, {'$set': updated_profile})
        return redirect(url_for('index'))
    return render_template('update.html', profile=profile)

if __name__ == '__main__':
    app.run(debug=True)
