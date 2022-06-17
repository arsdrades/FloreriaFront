# 0. ejecutamos pip install flask flask-sqlalchemy flask-migrate flask-cors
# 1. Crear modelos
# 2. importamos las librerias de flask

from flask import Flask, request, jsonify
from flask_migrate import Migrate
from models import db, Usuario, Cliente, Vendedor
from flask_cors import CORS, cross_origin

# 3. instanciamos la app
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Conten-Type'
app.url_map.strict_slashes = False
app.config['DEBUG'] = False
app.config['ENV'] = 'development'
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

db.init_app(app)

Migrate(app, db)

# 5. Creamos la ruta por defecto para saber si mi app esta funcionado
# 6. ejecutamos el comando en la consola: python app.py o python3 app.py y revisamos nuestro navegador
@app.route('/')
def index():
    return 'Hola desde gitpod'

# 7. Ruta para consultar todos los Usuarios
@app.route('/usuarios', methods=['GET'])
def getUsuarios():
    user = Usuario.query.all()
    user = list(map(lambda x: x.serialize(), user))
    return jsonify(user),200

# 12. Ruta para agregar usuario
@app.route('/usuarios', methods=['POST'])
def addUsuario():
    user = Usuario()
    # asignar a variables lo que recibo mediante post
    user.primer_nombre = request.json.get('primer_nombre')
    user.segundo_nombre = request.json.get('segundo_nombre')
    user.apellido_paterno = request.json.get('apellido_paterno')
    user.apellido_materno = request.json.get('apellido_materno')
    user.direccion = request.json.get('direccion')

    Usuario.save(user)

    return jsonify(user.serialize()),200

# 13. Creamos metodo para consultar un usuario en especifico
@app.route('/usuarios/<id>', methods=['GET'])
def getUsuario(id):
    user = Usuario.query.get(id)
    return jsonify(user.serialize()),200

# 14. Borrar usuario
@app.route('/usuarios/<id>', methods=['DELETE'])
def deleteUsuario(id):
    user = Usuario.query.get(id)
    Usuario.delete(user)
    return jsonify(user.serialize()),200

# 15. Modificar Usuario
@app.route('/usuarios/<id>', methods=['PUT'])
def updateUsuario(id):
    user = Usuario.query.get(id)

    user.primer_nombre = request.json.get('primer_nombre')
    user.segundo_nombre = request.json.get('segundo_nombre')
    user.apellido_paterno = request.json.get('apellido_paterno')
    user.apellido_materno = request.json.get('apellido_materno')
    user.direccion = request.json.get('direccion')

    Usuario.save(user)

    return jsonify(user.serialize()),200




# 8. comando para iniciar mi app flask: flask db init
# 9. comando para migrar mis modelos:   flask db migrate
# 10. comando para crear nuestros modelos como tablas : flask db upgrade
# 11. comando para iniciar la app flask: flask run

# 4. Configurar los puertos nuestra app 
if __name__ == '__main__':
    app.run(port=5000, debug=True)


@app.route('/cliente', methods=['POST'])
def addCliente():
    client = Cliente()
    # asignar a variables lo que recibo mediante post
    client.id = request.json.get('id')
    client.rut = request.json.get('rut')
    client.dv = request.json.get('dv')
    client.primer_nombre = request.json.get('primer_nombre')
    client.segundo_nombre = request.json.get('segundo_nombre')
    client.apellido_paterno = request.json.get('apellido_paterno')
    client.apellido_materno = request.json.get('apellido_materno')
    client.direccion = request.json.get('direccion')
    client.fono = request.json.get('fono')
    client.correo = request.json.get('correo')
    client.estado = request.json.get('estado')


    Cliente.save(client)

    return jsonify(client.serialize()),200

# 13. Creamos metodo para consultar un usuario en especifico
@app.route('/clientes/<id>', methods=['GET'])
def getCliente(id):
    client = Cliente.query.get(id)
    return jsonify(client.serialize()),200

# 14. Borrar usuario
@app.route('/clientes/<id>', methods=['DELETE'])
def deleteCliente(id):
    client = Cliente.query.get(id)
    client.delete(client)
    return jsonify(client.serialize()),200

# 15. Modificar Usuario
@app.route('/clientes/<id>', methods=['PUT'])
def updateCliente(id):
    client = Cliente.query.get(id)


    client.id = request.json.get('id')
    client.rut = request.json.get('rut')
    client.dv = request.json.get('dv')
    client.primer_nombre = request.json.get('primer_nombre')
    client.segundo_nombre = request.json.get('segundo_nombre')
    client.apellido_paterno = request.json.get('apellido_paterno')
    client.apellido_materno = request.json.get('apellido_materno')
    client.direccion = request.json.get('direccion')
    client.fono = request.json.get('fono')
    client.correo = request.json.get('correo')
    client.estado = request.json.get('estado')

    Cliente.save(client)

    return jsonify(client.serialize()),200

#---------------------------------------------------------------------------------------------------------------------------------------------

# 4. Configurar los puertos nuestra app 
if __name__ == '__main__':
    app.run(port=5000, debug=True)


@app.route('/vendedor', methods=['POST'])
def addCliente():
    vend = Vendedor()
    # asignar a variables lo que recibo mediante post
    vend.id_vendedor = request.json.get('id_venta')
    vend.rut = request.json.get('rut')
    vend.dv = request.json.get('dv')
    vend.primer_nombre = request.json.get('primer_nombre')
    vend.segundo_nombre = request.json.get('segundo_nombre')
    vend.apellido_paterno = request.json.get('apellido_paterno')
    vend.apellido_materno = request.json.get('apellido_materno')
    vend.direccion = request.json.get('direccion')
    vend.fono = request.json.get('fono')
    vend.correo = request.json.get('correo')
    vend.estado = request.json.get('estado')
    vend.comuna_id = request.json.get('comuna_id')


    Vendedor.save(vend)

    return jsonify(vend.serialize()),200

# 13. Creamos metodo para consultar un usuario en especifico
@app.route('/vendedor/<id>', methods=['GET'])
def getVendedor(id):
    vend = Vendedor.query.get(id)
    return jsonify(vend.serialize()),200

# 14. Borrar usuario
@app.route('/vendedor<id>', methods=['DELETE'])
def deleteVendedor(id):
    vend = Vendedor.query.get(id)
    vend.delete(vend)
    return jsonify(vend.serialize()),200

# 15. Modificar Usuario
@app.route('/Vendedors/<id>', methods=['PUT'])
def updateVendedor(id):
    vend = Vendedor.query.get(id)


    vend.id_vendedor = request.json.get('id')
    vend.rut = request.json.get('rut')
    vend.dv = request.json.get('dv')
    vend.primer_nombre = request.json.get('primer_nombre')
    vend.segundo_nombre = request.json.get('segundo_nombre')
    vend.apellido_paterno = request.json.get('apellido_paterno')
    vend.apellido_materno = request.json.get('apellido_materno')
    vend.direccion = request.json.get('direccion')
    vend.fono = request.json.get('fono')
    vend.correo = request.json.get('correo')
    vend.estado = request.json.get('estado')
    vend.comuna_id = request.json.get('comuna_id')

    Vendedor.save(vend)

    return jsonify(vend.serialize()),200
