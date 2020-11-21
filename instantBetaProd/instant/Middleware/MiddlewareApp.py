from instantprod import models


class LinguaMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):

        # queryset = models.BancoImagem.objects.all()[:18]
        # link = request.path.split('/')
        # linkcont = '/'.join(link[2:])
        # request.GET = dict(
        #     {'Bandeiras': queryset, 'url': linkcont},
        #     **dict(request.GET.values())
        # )
        # request.session.__setitem__('Bandeiras', dict(queryset))
        # request.session.__setitem__('url', linkcont)
        # request.session.__setitem__('CPF', texto)
        
        response = self.get_response(request)
        
        # print(' Middleware')
        # link = request.path.split('/')

        return response
