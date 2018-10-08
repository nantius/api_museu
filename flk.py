from flask import Flask, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

# sudo apt-get install libapache2-mod-wsgi-py3
# sudo apt-get install python3-flask python3-sqlalchemy python3-psycopg2

app = Flask(__name__)

# Set up database
engine = create_engine('postgres://consulta:selectconsulta@localhost:5432/museu')
db = scoped_session(sessionmaker(bind=engine))

@app.route("/<string:id>")
def objeto(id):
    objeto = db.execute("SELECT * from client where id = :id ;", {"id": id}).fetchone()
    return jsonify(descricao_intrinsica=objeto.login,
                   descricao_extrinsica=objeto.password)


if __name__ == "__main__":
    app.run()