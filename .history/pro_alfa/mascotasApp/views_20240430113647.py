from django.shortcuts import render
#Se debe importar la libreria HttpResponse
from django.http import HttpResponse

# Create your views here.
# def hola(request):
#     return HttpResponse(
#         """
#         <h1><center>saludos desde mi proyecto Django</center></h1>
#         <p> 1. Eficiencia en el desarrollo Utilizar Django permite agilizar el proceso de desarrollo gracias a su enfoque basado en la reutilización de código y la provisión de herramientas convenientes. ... <br>
# 2. Seguridad La seguridad es una preocupación fundamental en cualquier proyecto web. ...<br>
# 3. Escalabilidad ...<br>
# 4. Ejemplo de código en Django ...<br>
# 5. Recursos adicionales para aprender Django
#     """
#     )

def titulo(request):
    return HttpResponse(
        """
        <h1>Titulo</h1>
        <h2>Titulo</h2>
        <h3>Titulo</h3>
        <h4>Titulo</h4>
        <h5>Titulo</h5>
        <h6>Titulo</h6>
    """
    )

def parrafo(request):
    return HttpResponse("""
            <p>Lorem ipsum dolor sit amet consectetur, adipisicing elit. Cum laboriosam numquam consequatur, 
            placeat natus voluptas dolorum, fugit excepturi rerum aliquid possimus at facilis laborum s
            ed? Vitae temporibus officia quos fuga.</p>            
                        
            """)

