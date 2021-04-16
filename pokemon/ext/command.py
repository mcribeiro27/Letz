from .database import db
from pokemon.models.trainers import TrainerModel


def create_db():
    """Creates database"""
    db.create_all()

def drop_db():
    """Cleans database"""
    db.drop_all()

def populate_db():
    """Populate db with sample data"""
    data = [
        TrainerModel(
            id_trainer=1, 
            nickname="ash", 
            first_name="Ash", 
            last_name="Kutchum", 
            email = "ash@pokemon.com",
            password= "coxinha123",
            team= "Team Valor"
        ),
    ]
    db.session.bulk_save_objects(data)
    db.session.commit()
    return TrainerModel.query.all()

def init_app(app):
    # add multiple commands in a bulk
    for command in [create_db, drop_db, populate_db]:
        app.cli.add_command(app.cli.command()(command))
