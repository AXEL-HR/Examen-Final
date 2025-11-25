from flask import Flask, render_template, request
app = Flask(__name__)
USUARIOS = {
    "juan": {"password": "admin", "tipo": "administrador"},
    "pepe": {"password": "user", "tipo": "usuario"}
}
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ejercicio1')
def ejercicio1():
    return render_template('ejercicio1.html',
                         nombre="",
                         total_sin_descuento=0,
                         total_con_descuento=0,
                         descuento=0)
@app.route('/calcular_pinturas', methods=['POST'])
def calcular_pinturas():
    nombre = request.form['nombre']
    edad = int(request.form['edad'])
    cantidad_tarros = int(request.form['cantidad'])
    valor_tarro = 9000
    total_sin_descuento = cantidad_tarros * valor_tarro
    if edad >= 18 and edad <= 30:
        descuento = 0.15
    elif edad > 30:
        descuento = 0.25
    else:
        descuento = 0
    total_con_descuento = total_sin_descuento * (1 - descuento)
    return render_template('ejercicio1.html',
                           resultado=True,
                           nombre=nombre,
                           total_sin_descuento=total_sin_descuento,
                           total_con_descuento=total_con_descuento,
                           descuento=total_sin_descuento - total_con_descuento)
@app.route('/ejercicio2')
def ejercicio2():
    return render_template('ejercicio2.html')
@app.route('/procesar_login', methods=['POST'])
def procesar_login():
    usuario = request.form['usuario']
    password = request.form['password']
    if usuario in USUARIOS and USUARIOS[usuario]['password'] == password:
        tipo_usuario = USUARIOS[usuario]['tipo']
        mensaje = f"Bienvenido {'Administrador' if tipo_usuario == 'administrador' else 'Usuario'} {usuario}"
        return render_template('ejercicio2.html',
                               mensaje=mensaje,
                               mostrar_resultado=True)
    else:
        return render_template('ejercicio2.html',
                               error="Usuario o contraseña incorrecto.")
if __name__ == '__main__':
    app.run(debug=True)