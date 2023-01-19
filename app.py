from flask import Flask, jsonify, request 
from flask_cors import CORS 
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from models import db, User, Favorites, Characters, Planets

app = Flask(__name__) 
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
db.init_app(app)
CORS(app)
Migrate(app, db)

@app.route("/characters", methods=["GET"])
def characters():
    characters = Characters.query.all()
    characters_serializados = list(map(lambda characters: characters.serialize(), characters))
    return jsonify(characters_serializados)

@app.route("/characters/<int:character_id>", methods=["GET"])
def get_character(character_id):
    char = Character.query.get(character_id)
    if char:
        return jsonify(char.to_json())
    else:
        return jsonify({"error": "Character not found"}), 404


@app.route("/planets", methods=["GET"])
def planets():
    planets = Planets.query.all()
    planets_serializados = list(map(lambda planets: planets.serialize(), planets))
    return jsonify(planets_serializados)

@app.route("/planets/<int:planet_id>", methods=["GET"])
def get_planet(planet_id):
    planet = Planet.query.get(planet_id)
    if planet:
        return jsonify(planet.to_json())
    else:
        return jsonify({"error": "Planet not found"}), 404


@app.route("/users", methods=["GET"])
def list_users():
    users = User.query.all()
    return jsonify([user.to_json() for user in users])



@app.route("/users/favorites", methods=["GET"])
def list_favorites():
    user = User.query.get(current_user_id)
    favorites = user.favorites
    return jsonify([fav.to_json() for fav in favorites])

@app.route("/favorite/planet/<int:planet_id>", methods=["POST"])
def add_favorite_planet(planet_id):
    
    user = User.query.get(current_user_id)
    planet = Planet.query.get(planet_id)
    fav = Favorite(user=user, planet=planet)
    db.session.add(fav)
    db.session.commit()

    return jsonify({"message": "Planet added to favorites"})

@app.route("/favorite/character/<int:character_id>", methods=["POST"])
def add_favorite_character(character_id):

    user = User.query.get(current_user_id)
    character = Character.query.get(character_id)
    fav = Favorite(user=user, character=character)

    db.session.add(fav)
    db.session.commit()

    return jsonify({"message": "Character added to favorites"})


@app.route("/favorite/planet/<int:planet_id>", methods=["DELETE"])
def delete_favorite_planet(planet_id):

    user = User.query.get(current_user_id)
    planet = Planet.query.get(planet_id)
    fav = Favorite.query.filter_by(user=user, planet=planet).first()

    db.session.delete(fav)
    db.session.commit()

    return jsonify({"message": "Planet removed from favorites"})

@app.route("/favorite/character/<int:character_id>", methods=["DELETE"])
def delete_favorite_character(character_id):
    
    user = User.query.get(current_user_id)
    character = Character.query.get(character_id)
    fav = Favorite.query.filter_by(user=user, character=character).first()

    db.session.delete(fav)
    db.session.commit()

    return jsonify({"message": "Character removed from favorites"})

app.run(host="localhost", port=8080)