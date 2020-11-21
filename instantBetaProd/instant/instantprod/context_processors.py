from .models import *


class MudaContext:
   
    def Trocar(self, request):
        lcode = [ 
            'zh-cn',
            'en-us',
            'es-es',
            'de-de',
            'it-it',
            'nl-nl',
            'fr-fr',
            'pt-br',
            'hi-in',
            'ja-jp',
            'ar-ae',
            'gn',
            'ko-kr',
            'ru-ru',
            'yo-ng',
            'he-il',
            'uk-ua',
            'la-va',
        ]

        
        url = request.path.split('/')
        # print('/'.join(url[2:]))
        bandeira = []
        for lc in lcode:
            dado = {}
        
            LCid = LanguageCode.objects.filter( Nome__icontains = lc).values()[:1][0]

            # print('Codigo Lcode')
            # print(LCid['id'])
            
            Paisid = LinguaPais.objects.filter(id = int(LCid['id'])).values()[:1][0]
            # print(Paisid)
             
            QueryPais = Pais.objects.filter(id = Paisid['Pais_id'])
            QueryLingua = Lingua.objects.filter(id = Paisid['Lingua_id']).values()[:1][0]

            QueryBancoImagem = QueryPais.values("BancoImagem__Arquivo")
            if QueryBancoImagem[0]['BancoImagem__Arquivo'] != None:
                # print('valores')
                # print(QueryLingua)
                # print(QueryBancoImagem)
                dado['Nome'] = lc
                dado['id'] = Paisid['Pais_id']
                dado['Arquivo'] = QueryBancoImagem[0]['BancoImagem__Arquivo']
                dado['url'] = '/'.join(url[2:])
                dado['NomeOriginal'] = QueryLingua['Nome']
                bandeira.append(dado)


        return bandeira

    def PaisesBandeiras(self):

        lc = "pt-br"
        LCid = LanguageCode.objects.filter(Nome__icontains=lc).values()[:1][0]

        print('Codigo Lcode')
        print(LCid['id'])

        QueryPais = Pais.objects.filter(LanguageCode=LCid['id'])
        # QueryBancoImagem = QueryPais.values("BancoImagem__Arquivo")

        for pais in QueryPais:
            QueryBancoImagem = pais.BancoImagem
            print(pais)
            print(QueryBancoImagem)
            # print(QueryBancoImagem[0]['BancoImagem__Arquivo'])

        return 'bandeira'
