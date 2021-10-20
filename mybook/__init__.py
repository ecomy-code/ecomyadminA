from flask import Flask,render_template, url_for, request, redirect

app = Flask (__name__)




@app.route("/")
def home():
    return render_template(
        "menu/home.html"
        )



@app.route("/login")
def login():
    return render_template(
        "log/login.html"
    )




@app.route("/agregar")
def agregar():
    return render_template(
        "productos/agregar.html"
    )




@app.route("/ver")
def ver():
    productos_array = [["1", "ecomy", "appadmin", "mi apps", "283.994.883.928", "productosImages/ecomyProductsA1.png", "productosImages/ecomyProductsA2.png", "octubre" ],["2", "ecomy", "appadmin", "mi apps", "283.994.883.928",  "productosImages/ecomyProductsA1.png", "productosImages/ecomyProductsA2.png", "octubre" ]]
    return render_template(
        "productos/ver.html",productos_array=productos_array
    )





@app.route("/realizadas")
def realizadas():
    
    productos_array = [["1", "ecomy", "appadmin", "mi apps" ],["2", "ecomy", "appadmin", "mi apps" ]]
    return render_template(
        "compras/realizadas.html", productos_array=productos_array
    )





@app.route("/facturas")
def facturas():
    
    productos_array = [["1", "ecomy", "appadmin", "mi apps" ],["2", "ecomy", "appadmin", "mi apps" ]]
    return render_template(
        "compras/facturas.html" , productos_array=productos_array
    )






@app.route("/enespera")
def enespera():
    
    productos_array = [["1", "ecomy", "appadmin", "mi apps" ],["2", "ecomy", "appadmin", "mi apps" ]]
    return render_template(
        "pedidos/enespera.html",productos_array=productos_array
    )






@app.route("/enproceso")
def enproceso():
    
    productos_array = [["1", "ecomy", "appadmin", "mi apps" ],["2", "ecomy", "appadmin", "mi apps" ]]
    return render_template(
        "pedidos/enproceso.html", productos_array=productos_array
    )





@app.route("/entregados")
def entregados():
    
    productos_array = [["1", "ecomy", "appadmin", "mi apps" ],["2", "ecomy", "appadmin", "mi apps" ]]
    return render_template(
        "pedidos/entregados.html", productos_array=productos_array
    )



@app.route("/quejas")
def quejas():
    
    productos_array = [["1", "ecomy", "appadmin", "mi apps" ],["2", "ecomy", "appadmin", "mi apps" ]]
    return render_template(
        "usuarios/quejas.html",productos_array=productos_array
    )




@app.route("/cargar_producto" , methods=['POST', 'GET'])
def cargar_producto():
    
    fotoa = request.files['pic']
    fotob = request.files['pic2']
    name = request.form['namep']
    detalle = request.form['detallep']
    precio = request.form['preciop']
    cantidad = request.form['cantidadp']
    id_empresa = "id empresa ecomycr"
    
    
    return redirect(url_for(".home"))
