from flask import Flask, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
import json

# sudo apt-get install libapache2-mod-wsgi-py3
# sudo apt-get install python3-flask python3-sqlalchemy python3-psycopg2

app = Flask(__name__)

# Set up database
engine = create_engine('postgres://consulta:selectconsulta@localhost:5432/museu')
db = scoped_session(sessionmaker(bind=engine))

@app.route("/objeto/<string:id>")
def objeto(id):
    objeto = db.execute("SELECT * from objetos where id_objeto = :id ;", {"id": id}).fetchone()
    imagens = db.execute("SELECT caminho from imagens where ref_objeto = :id ",{"id":id}).fetchall()
    imagens_lista = []
    for linha in imagens:
    	imagens_lista.append(linha[0])
    return json.dumps({'nome_objeto':objeto.nome_objeto,'audiodescricao': objeto.audiodescricao ,'descricao_intrinsica': objeto.descricao_intrisica,'descricao_extrinsica': objeto.descricao_extrinsica, 'imagens': imagens_lista })


if __name__ == "__main__":
    app.run()
