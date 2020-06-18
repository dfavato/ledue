from django.shortcuts import render

# Create your views here.
def homepage(request):
    secoes_anchors = ['sobre_nos', 'Contato']
    secoes_headers = ['Sobre nós', 'Contato']
    context = {
        'title': 'le due',
        'secoes_anchors': secoes_anchors,
        'secoes_headers': secoes_headers,
        'secoes': {x: y for x, y in zip(secoes_anchors, secoes_headers)},
        'contacts': {
            'telephone_number': '31995540401',
            'telephone_text': '(31) 9 9554 0401',
            'whatsapp_number': '553195540401',
            'email': 'ledueceramicas@gmail.com',
            'instagram': 'https://www.instagram.com/ledueceramicas/'
        }
    }
    return render(request, 'homepage/homepage.html', context=context)
