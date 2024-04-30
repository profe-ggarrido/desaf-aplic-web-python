from django.shortcuts import render

#Se debe importar la libreria HttpResponse
from django.http import HttpResponse


def home(request):
    return HttpResponse(
        """
        <h1>ESTE ES MI HOME</h1>
        
    """
    )

def about(request):
    return HttpResponse("""
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
            <label for="nombre">Nombre:</label>
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

