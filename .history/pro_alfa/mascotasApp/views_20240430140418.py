from django.shortcuts import render

#Se debe importar la libreria HttpResponse
from django.http import HttpResponse


def home(request):
    return HttpResponse(
        """
        <h1>ESTE ES MI HOME</h1>
        <h3>Django es un marco dedesarrollo web de código abierto, escrito en Python, que permite la creación de aplicaciones web rápidas y seguras. Ofrece una interfaz sencilla y robusta para diseñar aplicaciones web con un enfoque en la reutilización y el desarrollo ágil1. A continuación, te proporciono más detalles sobre Django:</h3><br>

<strong><u><h3>¿Qué es Django?</h3></u></strong>
Django es un framework web de alto nivel que permite el desarrollo rápido de sitios web seguros y mantenibles.
Desarrollado por programadores experimentados, Django se encarga de gran parte de las complicaciones del desarrollo web, lo que te permite concentrarte en escribir tu aplicación sin necesidad de reinventar la rueda.
Es gratuito y de código abierto, tiene una comunidad próspera y activa, una gran documentación y muchas opciones de soporte gratuito y de pago2.<br><br>
<u><strong>Características principales de Django:</strong></u><br><br>
<u>Completo:</u> <br>Sigue la filosofía “Baterías incluidas” y provee casi todo lo que los desarrolladores quisieran que tenga “de fábrica”. Todo lo que necesitas es parte de un único “producto”, lo que facilita el desarrollo y mantiene la consistencia.<br>
<u>Versátil:</u> <br>Puede ser usado para construir casi cualquier tipo de sitio web, desde sistemas manejadores de contenidos y wikis hasta redes sociales y sitios de noticias. Además, puede funcionar con cualquier framework en el lado del cliente y devolver contenido en diversos formatos (HTML, RSS feeds, JSON, XML, etc.).<br>
<u>Seguro:</u> <br>Ayuda a los desarrolladores a evitar errores comunes de seguridad al proporcionar un framework diseñado para proteger automáticamente el sitio web. Por ejemplo, maneja de forma segura las cuentas de usuario y contraseñas.<br><br>
<u>Cómo empezar con Django:</u><br>
Si es la primera vez que utilizas Django, debes hacer algunas configuraciones iniciales, como autogenerar un código que establezca un proyecto Django (un conjunto de ajustes para una instancia de Django, incluida la configuración de la base de datos y opciones específicas).
        
    """
    )

def about(request):
    return HttpResponse("""
            <h2>PAGINA ABOUT</H2><BR><br>
            <p>Lorem ipsum dolor sit amet consectetur, adipisicing elit. Cum laboriosam numquam consequatur, 
            placeat natus voluptas dolorum, fugit excepturi rerum aliquid possimus at facilis laborum s
            ed? Vitae temporibus officia quos fuga.</p>            
                        
            """)


def contacto(request):
    return HttpResponse("""
        <!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Formulario de Contacto</title>
</head>
<body>
    <h2>Formulario de Contacto</h2>
    <form action="#" method="POST">
        <div>
            <label for="nombre"><strong>Nombre:</strong></label>
            <input type="text" id="nombre" name="nombre" required>
        </div>
        <div>
            <label for="email">Correo Electrónico:</label>
            <input type="email" id="email" name="email" required>
        </div>
        <div>
            <label for="comentario">Comentario:</label>
            <textarea id="comentario" name="comentario" rows="4" required></textarea>
        </div>
        <div>
            <button type="submit">Enviar</button>
        </div>
    </form>
</body>
</html>

        """
                        )

