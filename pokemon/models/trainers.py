from pokemon.ext.database import db


class TrainerModel(db.Model):
    __tablename__ = 'trainer'

    id_trainer = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(10))
    first_name = db.Column(db.String(15))
    last_name = db.Column(db.String(15))
    email = db.Column(db.String(50))
    password = db.Column(db.String(128))
    team = db.Column(db.Enum('Team Valor', 'Team Instinct', 'Team Mystic', name='team'))
    pokemonOwned = db.relationship('PokemonOwdModel')


    def __init__(self, id_trainer, nickname, first_name, last_name, email, password, team):
        self.id_trainer = id_trainer
        self.nickname = nickname
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.team = team
        

    def json(self):
        res = ''
        if self.pokemonOwned:
            poke = [pokemon.json() for pokemon in self.pokemonOwned]
            res = poke[0]['id']
        return {
            'id': self.id_trainer,
            'nickname': self.nickname,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email,
            'password': self.password,
            'team': self.team,
            'pokemonOwned': res
        }

    @classmethod
    def find(cls, id_trainer):
        trainer = cls.query.filter_by(id_trainer=id_trainer).first()
        if trainer:
            return trainer
        return None

    @classmethod
    def find_by_email(cls, email):
        trainer = cls.query.filter_by(email=email).first()
        if trainer:
            return trainer
        return None
        
    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self, nickname, first_name, last_name, email, password, team):
        self.nickname = nickname
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.team = team

    def delete(self):
        db.session.delete(self)
        db.session.commit()