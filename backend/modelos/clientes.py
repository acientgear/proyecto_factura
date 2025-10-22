import database
class Cliente(database.db.Model):
    __tablename__ = 'clientes'
    id = database.db.Column(database.db.Integer, primary_key=True)
    nombre = database.db.Column(database.db.String(100), nullable=False)
    email = database.db.Column(database.db.String(100), unique=True, nullable=False)

