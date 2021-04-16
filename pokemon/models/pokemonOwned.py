from pokemon.ext.database import db 
import requests


class PokemonOwdModel(db.Model):
    __tablename__ = 'pokemonOwned'

    id_poke_owd = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(15))
    level = db.Column(db.Integer)
    pokemon_id = db.Column(db.Integer)
    trainer = db.Column(db.Integer, db.ForeignKey('trainer.id_trainer'))

    def __init__(self, id_poke_owd, name, level, pokemon_id, trainer):
        self.id_poke_owd = id_poke_owd
        self.name = name
        self.level = level
        self.pokemon_id = pokemon_id
        self.trainer = trainer
        
        

    def json(self):
        url = 'https://pokeapi.co/api/v2/pokemon/' + str(self.pokemon_id)
        req = requests.get(url)
        return {
            'id': self.id_poke_owd,
            'name': self.name,
            'level': self.level,
            'pokemon_id': self.pokemon_id,
            'trainer': self.trainer,
            'pokemon_data': req.json()
        }
    
    @classmethod
    def find(cls, id_poke_owd):
        pokemon = cls.query.filter_by(id_poke_owd=id_poke_owd).first()
        if pokemon:
            return pokemon
        return None

    @classmethod
    def find_by_trainer(cls, trainer):
        pokemon = cls.query.filter_by(trainer=trainer).first()
        if pokemon:
            return pokemon
        return None

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self, name, level, pokemon_id):
        self.name = name
        self.level = level
        self.pokemon_id = pokemon_id

    def delete(self):
        db.session.delete(self)
        db.session.commit()