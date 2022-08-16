from flask import Flask, render_template, request, Response, jsonify, redirect, url_for
from flask import Flask, redirect, render_template, request, url_for, flash
import pymongo
import database as dbase  
from product import Product
from productn import Productn

db = dbase.dbConnection()

app = Flask(__name__)


#Controlador de la ruta inicial
@app.route('/')
def principal():
    return render_template('index.html')

#Rutas de la aplicación
@app.route('/index1')
def index1():
    products = db['products']
    productsReceived = products.find()
    return render_template('index1.html', products = productsReceived)

@app.route('/index2')
def index2():
    productsn = db['productsn']
    productsnReceived = productsn.find()
    return render_template('index2.html', productsn = productsnReceived)

# contenedor para registrar un los puntajes
@app.route('/gametimer')
def gametimer():
    return render_template('gametimer.html')

@app.route('/gametrain')
def gametrain():
    return render_template('gametrain.html')

@app.route('/logind')
def logind():
    return render_template('logind.html')

@app.route('/loginn')
def loginn():
    return render_template('loginn.html')

@app.route('/users')
def users():
    return render_template('users.html')

@app.route('/menugame')
def menugame():
    return render_template('menugame.html')

@app.route('/menuadmin')
def menuadmin():
    return render_template('menuadmin.html')

@app.route('/interfaceadmin')
def interfaceadmin():
    return render_template('interfaceadmin.html')

@app.route('/ensatis')
def ensatis():
    return render_template('ensatis.html')

@app.route('/tabled')
def tabled():
    return render_template('tabled.html')

#Method Post
@app.route('/products', methods=['POST'])
def addProduct():
    products = db['products']
    name = request.form['name']
    rol = request.form['rol']
    mail = request.form['mail']
    pwd = request.form['pwd']

    if name and rol and mail and pwd:
        product = Product(name, rol, mail, pwd)
        products.insert_one(product.toDBCollection())
        response = jsonify({
            'name' : name,
            'rol' : rol,
            'mail' : mail,
            'pwd' : pwd
        })
        return redirect(url_for('interfaceadmin'))
    else:
        return notFound()

#Method delete
@app.route('/delete/<string:product_name>')
def delete(product_name):
    products = db['products']
    products.delete_one({'name' : product_name})
    return redirect(url_for('interfaceadmin'))

#Method Put
@app.route('/edit/<string:product_name>', methods=['POST'])
def edit(product_name):
    products = db['products']
    name = request.form['name']
    rol = request.form['rol']
    mail = request.form['mail']
    pwd = request.form['pwd']

    if name and rol and mail and pwd:
        products.update_one({'name' : product_name}, {'$set' : {'name' : name, 'rol' : rol, 'mail' : mail, 'pwd' : pwd}})
        response = jsonify({'message' : 'Docente ' + product_name + ' actualizado correctamente'})
        return redirect(url_for('interfaceadmin'))
    else:
        return notFound()

#------------------------------------------------------------------------------------------------------
#Method Post
@app.route('/productsn', methods=['POST'])
def addProductn():
    productsn = db['productsn']
    name = request.form['name']
    rol = request.form['rol']
    nota = request.form['nota']
    star = request.form['star']

    if name and rol and nota and star:
        productn = Productn(name, rol, nota, star)
        productsn.insert_one(productn.toDBCollection())
        response = jsonify({
            'name' : name,
            'rol' : rol,
            'nota' : nota,
            'star' : star
        })
        return redirect(url_for('interfaceadmin'))
    else:
        return notFound()

#Method delete
@app.route('/delete/<string:productn_name>')
def deleten(productn_name):
    productsn = db['productsn']
    productsn.delete_one({'name' : productn_name})
    return redirect(url_for('interfaceadmin'))

#Method Put
@app.route('/edit/<string:productn_name>', methods=['POST'])
def editn(productn_name):
    productsn = db['productsn']
    name = request.form['name']
    rol = request.form['rol']
    nota = request.form['nota']
    star = request.form['star']

    if name and rol and nota and star:
        productsn.update_one({'name' : productn_name}, {'$set' : {'name' : name, 'rol' : rol, 'nota' : nota, 'star' : star}})
        response = jsonify({'message' : 'Estudiante ' + productn_name + ' actualizado correctamente'})
        return redirect(url_for('interfaceadmin'))
    else:
        return notFound()
#---------------------------------------------------------------------------------------------------------

@app.errorhandler(404)
def notFound(error=None):
    message ={
        'message': 'No encontrado ' + request.url,
        'status': '404 Not Found'
    }
    response = jsonify(message)
    response.status_code = 404
    return response



if __name__ == '__main__':
    app.run(debug=True, port=4000)