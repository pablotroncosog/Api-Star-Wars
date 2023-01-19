from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, ForeignKey

db = SQLAlchemy()  

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    email = db.Column(db.String(100))

    def serialize(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email
        }

class Favorites(db.Model):
    tablename = "favorites"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    character_id = db.Column(db.Integer, db.ForeignKey('characters.id'))
    planet_id = db.Column(db.Integer, db.ForeignKey('planets.id'))
    user = db.relationship("User", back_populates="favorites")
    character = db.relationship("Characters", back_populates="favorites")
    planet = db.relationship("Planets", back_populates="favorites")

    def serialize(self):
        return {
            "id": self.id,
            "characters_id": self. characters_id,
            "planets_id": self. planets_id,
        }

class Characters(db.Model):
    tablename = "characters"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    height = db.Column(db.Integer) 
    favorites = db.relationship("Favorite", back_populates="character")

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "height": self.height,
        }
    

class Planets(db.Model):
    tablename = "planets"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    climate = db.Column(db.String(100))
    population = db.Column(db.Integer) 
    favorites = db.relationship("Favorite", back_populates="planet")

    def serialize(self):
        return {
            "id": self.id,
            "name": self.title,
            "climate":self.body,
            "population": self.done,
        }
