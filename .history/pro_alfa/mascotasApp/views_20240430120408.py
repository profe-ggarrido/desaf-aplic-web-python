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
                         <img src="https://www.bing.com/images/search?view=detailV2&ccid=oZ5mXrHS&id=7554928F1D6704616D6935922EA94D76EC1A4300&thid=OIP.oZ5mXrHSnaMS4R5C1y-N-AHaHv&mediaurl=https%3a%2f%2ffarm2.staticflickr.com%2f1920%2f44899852684_79fdfeb1d7_o.jpg&cdnurl=https%3a%2f%2fth.bing.com%2fth%2fid%2fR.a19e665eb1d29da312e11e42d72f8df8%3frik%3dAEMa7HZNqS6SNQ%26pid%3dImgRaw%26r%3d0&exph=1920&expw=1837&q=imagen+de+gato&simid=608029613070359298&FORM=IRPRST&ck=687BEE60CBF0B8F6285D10DA916C48D6&selectedIndex=0&itb=0&idpp=overlayview&ajaxhist=0&ajaxserp=0" alt="Imagen"
                        
                        """
                        )

