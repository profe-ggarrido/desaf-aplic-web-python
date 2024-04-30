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
        <div class="tenor-gif-embed" data-postid="11192465650684032649" data-share-method="host" data-aspect-ratio="1.33333" data-width="100%"><a href="https://tenor.com/view/pedro-gif-11192465650684032649">Pedro GIF</a>from <a href="https://tenor.com/search/pedro-gifs">Pedro GIFs</a></div> <script type="text/javascript" async src="https://tenor.com/embed.js"></script>
        """
                        )

