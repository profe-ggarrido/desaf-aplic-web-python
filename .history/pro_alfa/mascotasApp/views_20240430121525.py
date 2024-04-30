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
        <h1>Titulo 1</h1>
        <h2>Titulo 2</h2>
        <h3>Titulo 3</h3>
        <h4>Titulo 4</h4>
        <h5>Titulo 5</h5>
        <h6>Titulo 6</h6>
    """
    )

def parrafo(request):
    return HttpResponse("""
            <p>Lorem ipsum dolor sit amet consectetur, adipisicing elit. Cum laboriosam numquam consequatur, 
            placeat natus voluptas dolorum, fugit excepturi rerum aliquid possimus at facilis laborum s
            ed? Vitae temporibus officia quos fuga.</p>            
                        
            """)


def imagen(request):
    return HttpResponse("""
        <div class="tenor-gif-embed" data-postid="11192465650684032649" data-share-method="host" data-aspect-ratio="1.33333" data-width="100%"><a href="https://tenor.com/view/pedro-gif-11192465650684032649">Pedro GIF</a>from <a href="https://tenor.com/search/pedro-gifs">Pedro GIFs</a></div> <script type="text/javascript" async src="https://tenor.com/embed.js"></script>
        """
                        )

