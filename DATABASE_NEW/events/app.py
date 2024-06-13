from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
base_dir = os.path.abspath(os.path.dirname(__file__))

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(base_dir, 'events.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    location = db.Column(db.String(150))
    date = db.Column(db.String(50))
    description = db.Column(db.String(500))

    def __repr__(self):
        return f"<Event {self.name}>"


# push context manually to app
with app.app_context():
    db.create_all()


@app.route('/events', methods=['POST'])
def create_event():
    data = request.get_json()
    new_event = Event(name=data['name'], location=data['location'], date=data['date'], description=data['description'])
    db.session.add(new_event)
    db.session.commit()
    return jsonify({"message": "Event created successfully."}), 201

@app.route('/events', methods=['GET'])
def get_events():
    events = Event.query.all()
    return jsonify([{"id": event.id, "name": event.name, "location": event.location, "date": event.date, "description": event.description} for event in events])

@app.route('/events/<int:id>', methods=['PUT'])
def update_event(id):
    event = Event.query.get_or_404(id)
    data = request.get_json()
    event.name = data.get('name', event.name)
    event.location = data.get('location', event.location)
    event.date = data.get('date', event.date)
    event.description = data.get('description', event.description)
    db.session.commit()
    return jsonify({"message": "Event updated successfully."})

@app.route('/events/<int:id>', methods=['DELETE'])
def delete_event(id):
    event = Event.query.get_or_404(id)
    db.session.delete(event)
    db.session.commit()
    return jsonify({"message": "Event deleted successfully."})


if __name__ == '__main__':
    app.run(debug=True)
