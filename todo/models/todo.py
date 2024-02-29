import datetime
from . import db
# This imports the db object from the __init__.py file in the same package.

class Todo(db.Model):
    __tablename__ = 'todos'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    completed = db.Column(db.Boolean, nullable =False,default=False)
    deadline = db.Column(db.DateTime, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    description = db.Column(db.String(200), nullable=True)
    updated_at = db.Column(db.DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)
    # This is the Todo model that we will use to interact with the todos table in the database.

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "completed": self.completed,
            "deadline": self.deadline,
            "created_at": self.created_at,
            "description": self.description,
            "updated_at": self.updated_at
        }  
# This method returns a dictionary representation of the Todo model.
# This will allow us to easily convert the Todo model to JSON.
    
    def __repr__(self):
        return f"<Todo {self.id} {self.title}>"