from kivy.app import App
from kivy.uix.textinput import TextInput
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
echo "# Tipificador" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/Davidldd/Tipificador.git
git push -u origin main




def build():

    layout = FloatLayout()
     
    nombre = TextInput(text="Nombre de Usuario: ")
    nombre.size_hint = None, None
    nombre.height = 30
    nombre.width = 400
    nombre.y= 550
    nombre.x = 20

    layout.add_widget(nombre)

    
    doc = TextInput(text= "Cedula: ")
    doc.size_hint = None, None
    doc.height = 30
    doc.width = 400
    doc.y= 510
    doc.x = 20

    layout.add_widget(doc)

    tel = TextInput(text="Telefono: ")
    tel.size_hint = None, None
    tel.height = 30
    tel.width = 400
    tel.y= 470
    tel.x = 20

    layout.add_widget(tel)

    correo = TextInput(text="E-mail: ")
    correo.size_hint = None, None
    correo.height = 30
    correo.width = 400
    correo.y= 430
    correo.x = 20

    layout.add_widget(correo)

    comercio = TextInput(text="CRC/CEA: ")
    comercio.size_hint = None, None
    comercio.height = 30
    comercio.width = 400
    comercio.y= 390
    comercio.x = 20

    layout.add_widget(comercio)

    asunto = TextInput(text="Asunto: ")
    asunto.size_hint = None, None
    asunto.height = 30
    asunto.width = 400
    asunto.y= 350
    asunto.x = 20

    layout.add_widget(asunto)

    spt = TextInput(text="Usuario/a se comunica indicando ")
    spt.size_hint = None, None
    spt.height = 115
    spt.width = 400
    spt.y= 230
    spt.x = 20

    layout.add_widget(spt)

    sol = TextInput(text="Solucion: ")
    
    sol.size_hint = None, None
    sol.height = 115
    sol.width = 400
    sol.y= 110
    sol.x = 20

    layout.add_widget(sol)

        
    clean = Button(text="Limpiar")
    clean.size_hint = None, None
    clean.font_size = 18
    clean.height = 40
    clean.width = 70
    clean.y= 50
    clean.x = 20

    layout.add_widget(clean)

    save = Button(text="Guardar")
    save.size_hint = None, None
    save.font_size = 18
    save.height = 40
    save.width = 80
    save.y= 50
    save.x = 100

    layout.add_widget(save)

    open = Button(text="Ver Archivo")
    open.size_hint = None, None
    open.font_size = 18
    open.height = 40
    open.width = 120
    open.y= 50
    open.x = 190

    layout.add_widget(open)

    return layout



ventana = App()
ventana.build = build
ventana.run()


