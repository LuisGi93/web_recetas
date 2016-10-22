import pdb # pdb.set_trace()
import unittest
import random

from app import app, db
from app.mod_auth.models import User, Receta

class TestParticipant(unittest.TestCase):
    def setUp(self):
        app.config.from_object('config')
        db.session.close()
        db.drop_all()
        db.create_all()

    def test_receta(self):
        print "Receta:"
        size= Receta.query.all()
        receta = Receta('Lasana bolonesa', 'c4@c4.com','Canelones, cerne, bechamel')
        db.session.add(receta)
        db.session.commit()
        recetas = Receta.query.all()
        assert receta in recetas
	    print "  Inserccion: ok"
        assert len(recetas)==len(size)+1
        print "  Numero entradas: ok"


    def test_usuario(self):
	    print "Usuario:"
	    size= User.query.all()
        usuario = User("pepe","pepe@pepe.com","123423", 'user', '0')
        db.session.add(usuario)
        db.session.commit()
        usuarios = User.query.all()
        assert usuario in usuarios
	    print "  Inserccion: ok"
        assert len(usuarios)==len(size)+1
        print "  Numero entradas: ok"



if __name__ == '__main__':
    unittest.main()
