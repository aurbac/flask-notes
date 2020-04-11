from flask import Flask, escape, request, make_response, jsonify
import json

app = Flask(__name__)

notes = []
notes.append({"id": 1, "title": "Note number 1","description": "This a description for the note number 1","image": "https://aws.amazon.com/","attribute1": "Example attribute 1","attribute2": "Example attribute 2","attribute3": "Example attribute 3","attribute4": "Example attribute 4"})
notes.append({"id": 2, "title": "Note number 2","description": "This a description for the note number 2","image": "https://aws.amazon.com/","attribute1": "Example attribute 1","attribute2": "Example attribute 2","attribute3": "Example attribute 3","attribute4": "Example attribute 4"})
notes.append({"id": 3, "title": "Note number 3","description": "This a description for the note number 3","image": "https://aws.amazon.com/","attribute1": "Example attribute 1","attribute2": "Example attribute 2","attribute3": "Example attribute 3","attribute4": "Example attribute 4"})
notes.append({"id": 4, "title": "Note number 4","description": "This a description for the note number 4","image": "https://aws.amazon.com/","attribute1": "Example attribute 1","attribute2": "Example attribute 2","attribute3": "Example attribute 3","attribute4": "Example attribute 4"})
notes.append({"id": 5, "title": "Note number 5","description": "This a description for the note number 5","image": "https://aws.amazon.com/","attribute1": "Example attribute 1","attribute2": "Example attribute 2","attribute3": "Example attribute 3","attribute4": "Example attribute 4"})
notes.append({"id": 6, "title": "Note number 6","description": "This a description for the note number 6","image": "https://aws.amazon.com/","attribute1": "Example attribute 1","attribute2": "Example attribute 2","attribute3": "Example attribute 3","attribute4": "Example attribute 4"})
notes.append({"id": 7, "title": "Note number 7","description": "This a description for the note number 7","image": "https://aws.amazon.com/","attribute1": "Example attribute 1","attribute2": "Example attribute 2","attribute3": "Example attribute 3","attribute4": "Example attribute 4"})
notes.append({"id": 8, "title": "Note number 8","description": "This a description for the note number 8","image": "https://aws.amazon.com/","attribute1": "Example attribute 1","attribute2": "Example attribute 2","attribute3": "Example attribute 3","attribute4": "Example attribute 4"})
notes.append({"id": 9, "title": "Note number 9","description": "This a description for the note number 9","image": "https://aws.amazon.com/","attribute1": "Example attribute 1","attribute2": "Example attribute 2","attribute3": "Example attribute 3","attribute4": "Example attribute 4"})
notes.append({"id": 10, "title": "Note number 10","description": "This a description for the note number 10","image": "https://aws.amazon.com/","attribute1": "Example attribute 1","attribute2": "Example attribute 2","attribute3": "Example attribute 3","attribute4": "Example attribute 4"})

def findNote(id,items):
    for item in items:
        if item['id']==id:
            return item
    return False

@app.route('/notes')
def getNotes():
    return json.dumps(notes)

@app.route('/notes/id/<int:note_id>')
def getNote(note_id):
    note = findNote(note_id,notes)
    if note:
        return jsonify(note)
    else:
        return make_response(jsonify({'error': 'Note not found'}), 500)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)