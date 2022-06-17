from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Usuario(db.Model):
    __tablename__ = 'Usuario'
    id = db.Column(db.Integer, primary_key=True)
    primer_nombre = db.Column(db.String(250), nullable= False)
    segundo_nombre = db.Column(db.String(250), nullable= True)
    apellido_paterno = db.Column(db.String(250), nullable= False)
    apellido_materno = db.Column(db.String(250), nullable= True)
    direccion = db.Column(db.String(250), nullable= False)

    def serialize(self):
        return{
            "id": self.id,
            "primer_nombre": self.primer_nombre,
            "segundo_nombre": self.segundo_nombre,
            "apellido_paterno": self.apellido_paterno,
            "apellido_materno": self.apellido_materno,
            "direccion": self.direccion
        }
    
    def save(self):
        db.session.add(self)
        db.session.commit()
    
    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

#------------------------------------------------------------------------------------------------------------------------------------------

class Cliente(db.Model):
    __tablename__ = 'Cliente'
    id = db.Column(db.Integer, primary_key=True)
    rut = db.Column(db.String(11), nullable= False)
    dv = db.Column(db.String(1), nullable= False)    
    primer_nombre = db.Column(db.String(250), nullable= False)
    segundo_nombre = db.Column(db.String(250), nullable= True)
    apellido_paterno = db.Column(db.String(250), nullable= False)
    apellido_materno = db.Column(db.String(250), nullable= True)
    direccion = db.Column(db.String(250), nullable= False)
    fono = db.Column(db.String(11), nullable= False)
    correo = db.Column(db.String(100), nullable= False)
    estado = db.Column(db.String(1),nullable= True)

    def serialize(self):
        return{
            "id": self.id,
            "rut": self.rut,
            "dv": self.id,
            "primer_nombre": self.primer_nombre,
            "segundo_nombre": self.segundo_nombre,
            "apellido_paterno": self.apellido_paterno,
            "apellido_materno": self.apellido_materno,
            "direccion": self.direccion,
            "fono": self.fono,
            "correo": self.correo,
            "estado": self.estado
        }

   
    def save(self):
        db.session.add(self)
        db.session.commit()
    
    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()   

#---------------------------------------------------------------------------------------------------------------------------------------------}

class Venta(db.Model):
    __tablename__ = 'Venta'
    id = db.Column(db.Integer, primary_key=True)
    rut = db.Column(db.String(11), nullable= False)
    dv = db.Column(db.String(1), nullable= False)    
    primer_nombre = db.Column(db.String(250), nullable= False)
    segundo_nombre = db.Column(db.String(250), nullable= True)
    apellido_paterno = db.Column(db.String(250), nullable= False)
    apellido_materno = db.Column(db.String(250), nullable= True)
    direccion = db.Column(db.String(250), nullable= False)
    fono = db.Column(db.String(11), nullable= False)
    correo = db.Column(db.String(100), nullable= False)
    estado = db.Column(db.String(1),nullable= True)

    def serialize(self):
        return{
            "id": self.id,
            "rut": self.rut,
            "dv": self.id,
            "primer_nombre": self.primer_nombre,
            "segundo_nombre": self.segundo_nombre,
            "apellido_paterno": self.apellido_paterno,
            "apellido_materno": self.apellido_materno,
            "direccion": self.direccion,
            "fono": self.fono,
            "correo": self.correo,
            "estado": self.estado
        }

   
    def save(self):
        db.session.add(self)
        db.session.commit()
    
    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()   

#--------------------------------------------------------------------------------------------------------------------------------------------

class Vendedor(db.Model):
    __tablename__ = 'Vendedor'
    id_vendedor = db.Column(db.Integer, primary_key=True)
    rut = db.Column(db.String(11), nullable= False)
    dv = db.Column(db.String(1), nullable= False)    
    primer_nombre = db.Column(db.String(250), nullable= False)
    segundo_nombre = db.Column(db.String(250), nullable= True)
    apellido_paterno = db.Column(db.String(250), nullable= False)
    apellido_materno = db.Column(db.String(250), nullable= True)
    direccion = db.Column(db.String(250), nullable= False)
    fono = db.Column(db.String(11), nullable= False)
    correo = db.Column(db.String(100), nullable= False)
    estado = db.Column(db.String(1),nullable= False)
    comuna_id = db.Column(db.Integer, db.ForeignKey('Comuna.id_comuna'), nullable=False)

    def serialize(self):
        return{
            "id_vendedor": self.id_venta,
            "rut": self.rut,
            "dv": self.id,
            "primer_nombre": self.primer_nombre,
            "segundo_nombre": self.segundo_nombre,
            "apellido_paterno": self.apellido_paterno,
            "apellido_materno": self.apellido_materno,
            "direccion": self.direccion,
            "fono": self.fono,
            "correo": self.correo,
            "estado": self.estado,
            "comuna_id": self.comuna_id   
        }

   
    def save(self):
        db.session.add(self)
        db.session.commit()
    
    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()   
