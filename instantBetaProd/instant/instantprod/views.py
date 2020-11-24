from django.shortcuts import render, redirect
from django.http import HttpResponse, FileResponse
from django.template import (
	loader,
	Context,
	Template,
	engines,
	RequestContext
)
from . import models
from . import forms
from django.template import (
	loader,
	Context,
	Template,
	RequestContext
)
import io
from random import randrange
from datetime import datetime
from django.db.models import Q
from django.conf import settings
from django.core.mail import (
	EmailMessage,
	send_mail,
	EmailMultiAlternatives
)
from django.forms import widgets
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.utils import timezone
from django.views import View
from django.views.generic.base import TemplateView
from xhtml2pdf import pisa
import os
from django.conf import settings
import string
from django.views.generic import (
	DetailView,
	ListView,
	CreateView,
)
from django.views.generic.detail import SingleObjectMixin
from django.views.generic.edit import FormView
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from django.contrib.auth import password_validation as p_v
import re
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.renderers import *
from rest_framework.views import *
from django.shortcuts import get_object_or_404
from .api.serializers import *
from rest_framework.viewsets import *
from django.utils import timezone, translation
from .context_processors import *
# import requests
from decimal import Decimal


class Pagamento(TemplateView):
	
	template_name = "instantprod/pagseguro.html"
	email_pagseguro = "admsociedade@simoes.trd.br" 
	token_sandbox = "873C82585ECE4B678D1CDB6315C6FF5A"
	token_pagseguro = ""
	site_session = "https://ws.sandbox.pagseguro.uol.com.br/v2/transactions?email={email_pagseguro}&token={token}"

	def get_context_data(self, request):
	
		muda = MudaContext()
	
		context = {
			'Bandeiras': muda.Trocar(request),
		}
		# print(context)
		
		return context

	
	def post(self, request, *args, **kwargs):

		print('args')
		print(args)

		print('kwargs')
		print(kwargs)

		print('request')
		print(request.POST)

		dado = request.POST
		Parcelas = dado['Parcelas'].split(' x ')

		site = self.site_session.format(
			email_pagseguro = self.email_pagseguro, 
			token = self.token_sandbox
		)
		
		teste = {
			'paymentMode' : 'default',
			'paymentMethod' : 'creditCard',
			'receiverEmail' :  self.email_pagseguro,
			'currency' : 'BRL',
			'extraAmount' : '0.00',
			'itemId1' : '0001',
			'itemDescription1' : 'Notebook Prata',
			'itemAmount1' : dado['Valor'],
			'itemQuantity1' : '1',
			'notificationURL' : 'https://sualoja.com.br/notifica.html',
			'reference' : 'REF1234',
			'senderName' : 'Jose Comprador',
			'senderCPF' : '22111944785',
			'senderAreaCode' : '11',
			'senderPhone' : '56273440',
			'senderEmail' : 'c80773836376172153653@sandbox.pagseguro.com.br',
			'senderHash' : dado['HashCard'],
			'shippingAddressRequired' : 'true',
			'shippingAddressStreet' : 'Av. Brig. Faria Lima',
			'shippingAddressNumber' : '1384',
			'shippingAddressComplement' : '5o andar',
			'shippingAddressDistrict' : 'Jardim Paulistano',
			'shippingAddressPostalCode' : '01452002',
			'shippingAddressCity' : 'Sao Paulo',
			'shippingAddressState' : 'SP',
			'shippingAddressCountry' : 'BRA',
			'shippingType' : '1',
			'shippingCost' : '0.00',
			'creditCardToken' : dado['TokenCard'],
			'installmentQuantity' : int(Parcelas[0]),
			'installmentValue' : round(Decimal(float(Parcelas[1])*1.0000000000000001), 2),
			'noInterestInstallmentQuantity' : 2,
			'creditCardHolderName' : 'Jose Comprador',
			'creditCardHolderCPF' : '22111944785',
			'creditCardHolderBirthDate' : '27/10/1987',
			'creditCardHolderAreaCode' : '11',
			'creditCardHolderPhone' : '56273440',
			'billingAddressStreet' : 'Av. Brig. Faria Lima',
			'billingAddressNumber' : '1384',
			'billingAddressComplement' : '5o andar',
			'billingAddressDistrict' : 'Jardim Paulistano',
			'billingAddressPostalCode' : '01452002',
			'billingAddressCity' : 'Sao Paulo',
			'billingAddressState' : 'SP',
			'billingAddressCountry' : 'BRA',
		}
		curl = requests.post(site, data = teste)

		

		return HttpResponse(curl)

	def get(self, request, *args, **kwargs):
		return render(request, self.template_name, self.get_context_data(request))


class DeleteUserView(TemplateView):
	template_name = 'instantprod/deleteuser.html'
	

	def get_context_data(self, request):

		muda = MudaContext()
		
		context = {
			'users': User.objects.all(),
			'Bandeiras': muda.Trocar(request),
		}
		# print(context)
		
		return context

	def get(self, request, *args, **kwargs):

		return render(request, self.template_name, self.get_context_data(request))

	
class CadastroView(APIView):
	template_name = 'instantprod/cadastro.html'
	queryset = User.objects.all()
	serializer_class = UserSerializer
	renderer_classes = [TemplateHTMLRenderer]
	style = {'template_pack': 'rest_framework/vertical/'}

	def get_context_data(self, request):

		LCid = LanguageCode.objects.filter( Nome__icontains = translation.get_language())[0]
		serializer = UserSerializer()
		parteserializer = ParteSerializer()
		contato = ContatoSerializer()
		seguranca = SegurancaSerializer()
		identificacao = IdentificacaoSerializer()
		QueryPais = Pais.objects.filter(LanguageCode = LCid).order_by('Ordem')
		QueryTipoPron = TipoPronomeTratamento.objects.filter(LanguageCode = LCid).order_by('Ordem')
		QueryTipoSexo = TipoSexo.objects.filter(LanguageCode = LCid).order_by('Ordem')
		QueryTipoOp = TipoOpTelefonia.objects.filter(LanguageCode = LCid).order_by('Ordem')
		QueryTipoContato = TipoContato.objects.filter(LanguageCode = LCid, TipoContatoTecn_id = 1).order_by('Ordem')
		QueryBancoImagem = QueryPais.values("BancoImagem__Arquivo","BancoImagem__id")
		QueryTipoId = TipoIdentificacao.objects.filter(CodigoIDezoitoN = 700, LanguageCode = LCid).order_by('Ordem')
		muda = MudaContext()
		muda.PaisesBandeiras()
		context = {
			'users': serializer,
			'identificacao': identificacao,
			'parte': parteserializer,
			'tipopron': QueryTipoPron.values(),
			'tiposexo': QueryTipoSexo.values(),
			'tipoop': QueryTipoOp.values(),
			'tipoid': QueryTipoId.values(),
			'tipocontato': QueryTipoContato.values(),
			'contato': contato,
			'seguranca': seguranca,
			'pais': QueryPais.values(),
			'paisimagens': QueryBancoImagem,
			#'Bandeiras': muda.Trocar(request),
			'style': self.style
		}
		return context

	def get(self, request, *args, **kwargs):

		return render(request, self.template_name, self.get_context_data(request))

	def post(self, request, format=None):

		print('request.POST')
		print(request.POST)
		print('user')
		serializer = UserSerializer(data=request.POST)
		print('Parte')
		parteserializer = ParteSerializer(data=request.POST)
		print('Contato')
		contato = ContatoSerializer(data=request.POST)
		print('segurança')
		seguranca = SegurancaSerializer(data=request.POST)

		try:
			print(serializer.is_valid())
		except:
			print('user')

		try:
			print(parteserializer.is_valid())
		except:
			print('Parte')

		try:
			print(contato.is_valid())
		except:
			print('Contato')

		try:
			seguranca.is_valid()
		except:
			print('segurança')

		if serializer.is_valid() and parteserializer.is_valid() and contato.is_valid() and seguranca.is_valid():
			serializer.save()
			parteserializer.save()
			contato.save()
			seguranca.save()

			print('funcionou')
			return Response('Funcionou', status=status.HTTP_201_CREATED)
		else:
			print('não funcionou')

			return Response('nãofuncionou', status=status.HTTP_400_BAD_REQUEST)


class CadastroLinguasView(TemplateView):
	template_name = 'instantprod/cadastro_languages.html'


# View para acesso das tabelas pelo instant
class LanguageCodeAPIView(APIView):
	queryset = LanguageCode.objects.all()
	serializer_class = LanguageCodeSerializer
	template_name = 'instantprod/apilanguagecode.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = LanguageCodeSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = LanguageCodeSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class PalavraChaveAPIView(APIView):
	queryset = PalavraChave.objects.all()
	serializer_class = PalavraChaveSerializer
	template_name = 'instantprod/apipalavrachave.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = PalavraChaveSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = PalavraChaveSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class TipoBancoImagemAPIView(APIView):
	queryset = TipoBancoImagem.objects.all()
	serializer_class = TipoBancoImagemSerializer
	template_name = 'instantprod/apitipobancoimagem.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = TipoBancoImagemSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = TipoBancoImagemSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class BancoImagemAPIView(APIView):
	queryset = BancoImagem.objects.all()
	serializer_class = BancoImagemSerializer
	template_name = 'instantprod/apibancoimagem.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = BancoImagemSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = BancoImagemSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class ContinenteAPIView(APIView):
	queryset = Continente.objects.all()
	serializer_class = ContinenteSerializer
	template_name = 'instantprod/apicontinente.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = ContinenteSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = ContinenteSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class TipoHemisferioAPIView(APIView):
	queryset = TipoHemisferio.objects.all()
	serializer_class = TipoHemisferioSerializer
	template_name = 'instantprod/apitipohemisferio.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = TipoHemisferioSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = TipoHemisferioSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class AreaGeograficaAPIView(APIView):
	queryset = AreaGeografica.objects.all()
	serializer_class = AreaGeograficaSerializer
	template_name = 'instantprod/apiareageografica.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = AreaGeograficaSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = AreaGeograficaSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class PaisAPIView(APIView):
	queryset = Pais.objects.all()
	serializer_class = PaisSerializer
	template_name = 'instantprod/apipais.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = PaisSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = PaisSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class RegiaoAPIView(APIView):
	queryset = Regiao.objects.all()
	serializer_class = RegiaoSerializer
	template_name = 'instantprod/apiregiao.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = RegiaoSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = RegiaoSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class TipoOrgaoEmissAPIView(APIView):
	queryset = TipoOrgaoEmiss.objects.all()
	serializer_class = TipoOrgaoEmissSerializer
	template_name = 'instantprod/apitipoorgaoemiss.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = TipoOrgaoEmissSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = TipoOrgaoEmissSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class EstadoAPIView(APIView):
	queryset = Estado.objects.all()
	serializer_class = EstadoSerializer
	template_name = 'instantprod/apiestado.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = EstadoSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = EstadoSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class CidadeAPIView(APIView):
	queryset = Cidade.objects.all()
	serializer_class = CidadeSerializer
	template_name = 'instantprod/apicidade.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = CidadeSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = CidadeSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class TipoLogradouroAPIView(APIView):
	queryset = TipoLogradouro.objects.all()
	serializer_class = TipoLogradouroSerializer
	template_name = 'instantprod/apitipologradouro.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = TipoLogradouroSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = TipoLogradouroSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class CodigoEndPostalAPIView(APIView):
	queryset = CodigoEndPostal.objects.all()
	serializer_class = CodigoEndPostalSerializer
	template_name = 'instantprod/apicodigoendpostal.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = CodigoEndPostalSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = CodigoEndPostalSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class TipoComplementoAPIView(APIView):
	queryset = TipoComplemento.objects.all()
	serializer_class = TipoComplementoSerializer
	template_name = 'instantprod/apitipocomplemento.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = TipoComplementoSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = TipoComplementoSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class TipoEnderecoAPIView(APIView):
	queryset = TipoEndereco.objects.all()
	serializer_class = TipoEnderecoSerializer
	template_name = 'instantprod/apitipoendereco.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = TipoEnderecoSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = TipoEnderecoSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class EnderecoAPIView(APIView):
	queryset = Endereco.objects.all()
	serializer_class = EnderecoSerializer
	template_name = 'instantprod/apiendereco.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = EnderecoSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = EnderecoSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class TipoContatoTecnAPIView(APIView):
	queryset = TipoContatoTecn.objects.all()
	serializer_class = TipoContatoTecnSerializer
	template_name = 'instantprod/apitipocontatotecn.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = TipoContatoTecnSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = TipoContatoTecnSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class TipoContatoAPIView(APIView):
	queryset = TipoContato.objects.all()
	serializer_class = TipoContatoSerializer
	template_name = 'instantprod/apitipocontato.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = TipoContatoSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = TipoContatoSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class TipoOpTelefoniaAPIView(APIView):
	queryset = TipoOpTelefonia.objects.all()
	serializer_class = TipoOpTelefoniaSerializer
	template_name = 'instantprod/apitipooptelefonia.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = TipoOpTelefoniaSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = TipoOpTelefoniaSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class ContatoAPIView(APIView):
	queryset = Contato.objects.all()
	serializer_class = ContatoSerializer
	template_name = 'instantprod/apicontato.html'
	renderer_classes = [TemplateHTMLRenderer]
	style = {'template_pack': 'rest_framework/vertical/'}

	def get_context_data(self, request):

		LCid = LanguageCode.objects.filter(Nome__icontains=translation.get_language())[0]
		serializer = ContatoSerializer()
		tipocontato = TipoContatoSerializer()
		cidade = CidadeSerializer()
		tipooptelefonia = TipoOpTelefoniaSerializer()
		QueryPais = Pais.objects.filter(LanguageCode=LCid).order_by('Ordem')

		context = {
			'contato': serializer,
			'tipocontato': tipocontato,
			'cidade': cidade,
			'tipooptelefonia': tipooptelefonia,
			'pais': QueryPais.values(),
			'style': self.style
		}
		return context

	def get(self, request, *args, **kwargs):

		return render(request, self.template_name, self.get_context_data(request))

	def post(self, request, format=None):
		
		serializer = ContatoSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class TipoPcDCategAPIView(APIView):
	queryset = TipoPcDCateg.objects.all()
	serializer_class = TipoPcDCategSerializer
	template_name = 'instantprod/apitipopcdcateg.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = TipoPcDCategSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = TipoPcDCategSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class TipoDiaSemanaAPIView(APIView):
	queryset = TipoDiaSemana.objects.all()
	serializer_class = TipoDiaSemanaSerializer
	template_name = 'instantprod/apitipodiasemana.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = TipoDiaSemanaSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = TipoDiaSemanaSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class TipoHorarioFuncionamentoAPIView(APIView):
	queryset = TipoHorarioFuncionamento.objects.all()
	serializer_class = TipoHorarioFuncionamentoSerializer
	template_name = 'instantprod/apitipohorariofuncionamento.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = TipoHorarioFuncionamentoSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = TipoHorarioFuncionamentoSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class HorarioFuncionamentoAPIView(APIView):
	queryset = HorarioFuncionamento.objects.all()
	serializer_class = HorarioFuncionamentoSerializer
	template_name = 'instantprod/apihorariofuncionamento.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = HorarioFuncionamentoSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = HorarioFuncionamentoSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class TipoUrlAPIView(APIView):
	queryset = TipoUrl.objects.all()
	serializer_class = TipoUrlSerializer
	template_name = 'instantprod/apitipourl.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = TipoUrlSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = TipoUrlSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class UrlAPIView(APIView):
	queryset = Url.objects.all()
	serializer_class = UrlSerializer
	template_name = 'instantprod/apiurl.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = UrlSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = UrlSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class TipoPDVAPIView(APIView):
	queryset = TipoPDV.objects.all()
	serializer_class = TipoPDVSerializer
	template_name = 'instantprod/apitipopdv.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = TipoPDVSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = TipoPDVSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class PDVAPIView(APIView):
	queryset = PDV.objects.all()
	serializer_class = PDVSerializer
	template_name = 'instantprod/apipdv.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = PDVSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = PDVSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class ItemTipoAreaAPIView(APIView):
	queryset = ItemTipoArea.objects.all()
	serializer_class = ItemTipoAreaSerializer
	template_name = 'instantprod/apiitemtipoarea.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = ItemTipoAreaSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = ItemTipoAreaSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class MicrositeAPIView(APIView):
	queryset = Microsite.objects.all()
	serializer_class = MicrositeSerializer
	template_name = 'instantprod/apimicrosite.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = MicrositeSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = MicrositeSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class UnidadeAPIView(APIView):
	queryset = Unidade.objects.all()
	serializer_class = UnidadeSerializer
	template_name = 'instantprod/apiunidade.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = UnidadeSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = UnidadeSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class TipoPromocaoAPIView(APIView):
	queryset = TipoPromocao.objects.all()
	serializer_class = TipoPromocaoSerializer
	template_name = 'instantprod/apitipopromocao.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = TipoPromocaoSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = TipoPromocaoSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class TipoProgressaoAPIView(APIView):
	queryset = TipoProgressao.objects.all()
	serializer_class = TipoProgressaoSerializer
	template_name = 'instantprod/apitipoprogressao.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = TipoProgressaoSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = TipoProgressaoSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class TipoCargoAPIView(APIView):
	queryset = TipoCargo.objects.all()
	serializer_class = TipoCargoSerializer
	template_name = 'instantprod/apitipocargo.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = TipoCargoSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = TipoCargoSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class TipoDocumentoAPIView(APIView):
	queryset = TipoDocumento.objects.all()
	serializer_class = TipoDocumentoSerializer
	template_name = 'instantprod/apitipodocumento.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = TipoDocumentoSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = TipoDocumentoSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class TipoSetorAPIView(APIView):
	queryset = TipoSetor.objects.all()
	serializer_class = TipoSetorSerializer
	template_name = 'instantprod/apitiposetor.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = TipoSetorSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = TipoSetorSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class TipoFuncioTurnoAPIView(APIView):
	queryset = TipoFuncioTurno.objects.all()
	serializer_class = TipoFuncioTurnoSerializer
	template_name = 'instantprod/apitipofuncioturno.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = TipoFuncioTurnoSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = TipoFuncioTurnoSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class TipoRelacaoAPIView(APIView):
	queryset = TipoRelacao.objects.all()
	serializer_class = TipoRelacaoSerializer
	template_name = 'instantprod/apitiporelacao.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = TipoRelacaoSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = TipoRelacaoSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class CargoAPIView(APIView):
	queryset = Cargo.objects.all()
	serializer_class = CargoSerializer
	template_name = 'instantprod/apicargo.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = CargoSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = CargoSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class TipoCargoTradAPIView(APIView):
	queryset = TipoCargoTrad.objects.all()
	serializer_class = TipoCargoTradSerializer
	template_name = 'instantprod/apitipocargotrad.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = TipoCargoTradSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = TipoCargoTradSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class TipoCtrlQualidadeAPIView(APIView):
	queryset = TipoCtrlQualidade.objects.all()
	serializer_class = TipoCtrlQualidadeSerializer
	template_name = 'instantprod/apitipoctrlqualidade.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = TipoCtrlQualidadeSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = TipoCtrlQualidadeSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class TipoProficienciaLinguaAPIView(APIView):
	queryset = TipoProficienciaLingua.objects.all()
	serializer_class = TipoProficienciaLinguaSerializer
	template_name = 'instantprod/apitipoproficiencialingua.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = TipoProficienciaLinguaSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = TipoProficienciaLinguaSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class TipoMoedaAPIView(APIView):
	queryset = TipoMoeda.objects.all()
	serializer_class = TipoMoedaSerializer
	template_name = 'instantprod/apitipomoeda.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = TipoMoedaSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = TipoMoedaSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class TipoVolumeAcumuladoVendaAPIView(APIView):
	queryset = TipoVolumeAcumuladoVenda.objects.all()
	serializer_class = TipoVolumeAcumuladoVendaSerializer
	template_name = 'instantprod/apitipovolumeacumuladovenda.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = TipoVolumeAcumuladoVendaSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = TipoVolumeAcumuladoVendaSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class TipoDomUmGdArCoAPIView(APIView):
	queryset = TipoDomUmGdArCo.objects.all()
	serializer_class = TipoDomUmGdArCoSerializer
	template_name = 'instantprod/apitipodomumgdarco.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = TipoDomUmGdArCoSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = TipoDomUmGdArCoSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class TipoDomUmSbArCoAPIView(APIView):
	queryset = TipoDomUmSbArCo.objects.all()
	serializer_class = TipoDomUmSbArCoSerializer
	template_name = 'instantprod/apitipodomumsbarco.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = TipoDomUmSbArCoSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = TipoDomUmSbArCoSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class TipoDominioUmAPIView(APIView):
	queryset = TipoDominioUm.objects.all()
	serializer_class = TipoDominioUmSerializer
	template_name = 'instantprod/apitipodominioum.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = TipoDominioUmSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = TipoDominioUmSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class TipoLinguaClasfAPIView(APIView):
	queryset = TipoLinguaClasf.objects.all()
	serializer_class = TipoLinguaClasfSerializer
	template_name = 'instantprod/apitipolinguaclasf.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = TipoLinguaClasfSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = TipoLinguaClasfSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class LinguaAPIView(APIView):
	queryset = Lingua.objects.all()
	serializer_class = LinguaSerializer
	template_name = 'instantprod/apilingua.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = LinguaSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = LinguaSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class TipoImpostoAPIView(APIView):
	queryset = TipoImposto.objects.all()
	serializer_class = TipoImpostoSerializer
	template_name = 'instantprod/apitipoimposto.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = TipoImpostoSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = TipoImpostoSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class TipoNotaComunicacaoAPIView(APIView):
	queryset = TipoNotaComunicacao.objects.all()
	serializer_class = TipoNotaComunicacaoSerializer
	template_name = 'instantprod/apitiponotacomunicacao.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = TipoNotaComunicacaoSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = TipoNotaComunicacaoSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class TipoNotaQualidadeAPIView(APIView):
	queryset = TipoNotaQualidade.objects.all()
	serializer_class = TipoNotaQualidadeSerializer
	template_name = 'instantprod/apitiponotaqualidade.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = TipoNotaQualidadeSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = TipoNotaQualidadeSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class TipoNotaGeralAPIView(APIView):
	queryset = TipoNotaGeral.objects.all()
	serializer_class = TipoNotaGeralSerializer
	template_name = 'instantprod/apitiponotageral.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = TipoNotaGeralSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = TipoNotaGeralSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class CtrlQualidadeAPIView(APIView):
	queryset = CtrlQualidade.objects.all()
	serializer_class = CtrlQualidadeSerializer
	template_name = 'instantprod/apictrlqualidade.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = CtrlQualidadeSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = CtrlQualidadeSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class TipoMargemLucroAPIView(APIView):
	queryset = TipoMargemLucro.objects.all()
	serializer_class = TipoMargemLucroSerializer
	template_name = 'instantprod/apitipomargemlucro.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = TipoMargemLucroSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = TipoMargemLucroSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class MargemLucroAPIView(APIView):
	queryset = MargemLucro.objects.all()
	serializer_class = MargemLucroSerializer
	template_name = 'instantprod/apimargemlucro.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = MargemLucroSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = MargemLucroSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class TituloAPIView(APIView):
	queryset = Titulo.objects.all()
	serializer_class = TituloSerializer
	template_name = 'instantprod/apititulo.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = TituloSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = TituloSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class SubTituloServicoAPIView(APIView):
	queryset = SubTituloServico.objects.all()
	serializer_class = SubTituloServicoSerializer
	template_name = 'instantprod/apisubtituloservico.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = SubTituloServicoSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = SubTituloServicoSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class SubTipoDocumentoAPIView(APIView):
	queryset = SubTipoDocumento.objects.all()
	serializer_class = SubTipoDocumentoSerializer
	template_name = 'instantprod/apisubtipodocumento.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = SubTipoDocumentoSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = SubTipoDocumentoSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class ItemCategoriaAPIView(APIView):
	queryset = ItemCategoria.objects.all()
	serializer_class = ItemCategoriaSerializer
	template_name = 'instantprod/apiitemcategoria.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = ItemCategoriaSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = ItemCategoriaSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class TipoDomDoisSecAPIView(APIView):
	queryset = TipoDomDoisSec.objects.all()
	serializer_class = TipoDomDoisSecSerializer
	template_name = 'instantprod/apitipodomdoissec.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = TipoDomDoisSecSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = TipoDomDoisSecSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class TipoDomDoisDivAPIView(APIView):
	queryset = TipoDomDoisDiv.objects.all()
	serializer_class = TipoDomDoisDivSerializer
	template_name = 'instantprod/apitipodomdoisdiv.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = TipoDomDoisDivSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = TipoDomDoisDivSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class TipoDomDoisGrupAPIView(APIView):
	queryset = TipoDomDoisGrup.objects.all()
	serializer_class = TipoDomDoisGrupSerializer
	template_name = 'instantprod/apitipodomdoisgrup.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = TipoDomDoisGrupSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = TipoDomDoisGrupSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class TipoDomDoisClasAPIView(APIView):
	queryset = TipoDomDoisClas.objects.all()
	serializer_class = TipoDomDoisClasSerializer
	template_name = 'instantprod/apitipodomdoisclas.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = TipoDomDoisClasSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = TipoDomDoisClasSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class TipoDominioDoisAPIView(APIView):
	queryset = TipoDominioDois.objects.all()
	serializer_class = TipoDominioDoisSerializer
	template_name = 'instantprod/apitipodominiodois.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = TipoDominioDoisSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = TipoDominioDoisSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class FuncaoAPIView(APIView):
	queryset = Funcao.objects.all()
	serializer_class = FuncaoSerializer
	template_name = 'instantprod/apifuncao.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = FuncaoSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = FuncaoSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class TipoExtCategoriaAPIView(APIView):
	queryset = TipoExtCategoria.objects.all()
	serializer_class = TipoExtCategoriaSerializer
	template_name = 'instantprod/apitipoextcategoria.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = TipoExtCategoriaSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = TipoExtCategoriaSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class TipoExtensaoAPIView(APIView):
	queryset = TipoExtensao.objects.all()
	serializer_class = TipoExtensaoSerializer
	template_name = 'instantprod/apitipoextensao.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = TipoExtensaoSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = TipoExtensaoSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class CodigoValidacaoAPIView(APIView):
	queryset = CodigoValidacao.objects.all()
	serializer_class = CodigoValidacaoSerializer
	template_name = 'instantprod/apicodigovalidacao.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = CodigoValidacaoSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = CodigoValidacaoSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class ImpostoAPIView(APIView):
	queryset = Imposto.objects.all()
	serializer_class = ImpostoSerializer
	template_name = 'instantprod/apiimposto.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = ImpostoSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = ImpostoSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class PadraoDocumentoAPIView(APIView):
	queryset = PadraoDocumento.objects.all()
	serializer_class = PadraoDocumentoSerializer
	template_name = 'instantprod/apipadraodocumento.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = PadraoDocumentoSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = PadraoDocumentoSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class BancoArquivoAPIView(APIView):
	queryset = BancoArquivo.objects.all()
	serializer_class = BancoArquivoSerializer
	template_name = 'instantprod/apibancoarquivo.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = BancoArquivoSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = BancoArquivoSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class ItemAPIView(APIView):
	queryset = Item.objects.all()
	serializer_class = ItemSerializer
	template_name = 'instantprod/apiitem.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = ItemSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = ItemSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class CapacidadeDiariaAPIView(APIView):
	queryset = CapacidadeDiaria.objects.all()
	serializer_class = CapacidadeDiariaSerializer
	template_name = 'instantprod/apicapacidadediaria.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = CapacidadeDiariaSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = CapacidadeDiariaSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class TipoMedidaServAPIView(APIView):
	queryset = TipoMedidaServ.objects.all()
	serializer_class = TipoMedidaServSerializer
	template_name = 'instantprod/apitipomedidaserv.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = TipoMedidaServSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = TipoMedidaServSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class TipoMedidaAPIView(APIView):
	queryset = TipoMedida.objects.all()
	serializer_class = TipoMedidaSerializer
	template_name = 'instantprod/apitipomedida.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = TipoMedidaSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = TipoMedidaSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class TipoCompLinguaAPIView(APIView):
	queryset = TipoCompLingua.objects.all()
	serializer_class = TipoCompLinguaSerializer
	template_name = 'instantprod/apitipocomplingua.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = TipoCompLinguaSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = TipoCompLinguaSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class TipoAnoInicioAtuacaoAPIView(APIView):
	queryset = TipoAnoInicioAtuacao.objects.all()
	serializer_class = TipoAnoInicioAtuacaoSerializer
	template_name = 'instantprod/apitipoanoinicioatuacao.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = TipoAnoInicioAtuacaoSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = TipoAnoInicioAtuacaoSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class ValorAPIView(APIView):
	queryset = Valor.objects.all()
	serializer_class = ValorSerializer
	template_name = 'instantprod/apivalor.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = ValorSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = ValorSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class TipoFuncaoTradAPIView(APIView):
	queryset = TipoFuncaoTrad.objects.all()
	serializer_class = TipoFuncaoTradSerializer
	template_name = 'instantprod/apitipofuncaotrad.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = TipoFuncaoTradSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = TipoFuncaoTradSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class PosicaoClausulaDocumentoAPIView(APIView):
	queryset = PosicaoClausulaDocumento.objects.all()
	serializer_class = PosicaoClausulaDocumentoSerializer
	template_name = 'instantprod/apiposicaoclausuladocumento.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = PosicaoClausulaDocumentoSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = PosicaoClausulaDocumentoSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class TipoClausulaAPIView(APIView):
	queryset = TipoClausula.objects.all()
	serializer_class = TipoClausulaSerializer
	template_name = 'instantprod/apitipoclausula.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = TipoClausulaSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = TipoClausulaSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class ClausulaAPIView(APIView):
	queryset = Clausula.objects.all()
	serializer_class = ClausulaSerializer
	template_name = 'instantprod/apiclausula.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = ClausulaSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = ClausulaSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class TipoIdentificacaoAPIView(APIView):
	queryset = TipoIdentificacao.objects.all()
	serializer_class = TipoIdentificacaoSerializer
	template_name = 'instantprod/apitipoidentificacao.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = TipoIdentificacaoSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = TipoIdentificacaoSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class IdentificacaoAPIView(APIView):
	queryset = Identificacao.objects.all()
	serializer_class = IdentificacaoSerializer
	template_name = 'instantprod/apiidentificacao.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = IdentificacaoSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = IdentificacaoSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class TipoSituacaoAPIView(APIView):
	queryset = TipoSituacao.objects.all()
	serializer_class = TipoSituacaoSerializer
	template_name = 'instantprod/apitiposituacao.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = TipoSituacaoSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = TipoSituacaoSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class TipoCargoProjetoAPIView(APIView):
	queryset = TipoCargoProjeto.objects.all()
	serializer_class = TipoCargoProjetoSerializer
	template_name = 'instantprod/apitipocargoprojeto.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = TipoCargoProjetoSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = TipoCargoProjetoSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class TipoVinculoAPIView(APIView):
	queryset = TipoVinculo.objects.all()
	serializer_class = TipoVinculoSerializer
	template_name = 'instantprod/apitipovinculo.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = TipoVinculoSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = TipoVinculoSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class TipoCtrlPrazoAPIView(APIView):
	queryset = TipoCtrlPrazo.objects.all()
	serializer_class = TipoCtrlPrazoSerializer
	template_name = 'instantprod/apitipoctrlprazo.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = TipoCtrlPrazoSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = TipoCtrlPrazoSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class CtrlPrazoAPIView(APIView):
	queryset = CtrlPrazo.objects.all()
	serializer_class = CtrlPrazoSerializer
	template_name = 'instantprod/apictrlprazo.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = CtrlPrazoSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = CtrlPrazoSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class ProjetoAPIView(APIView):
	queryset = Projeto.objects.all()
	serializer_class = ProjetoSerializer
	template_name = 'instantprod/apiprojeto.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = ProjetoSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = ProjetoSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class OutorgaAPIView(APIView):
	queryset = Outorga.objects.all()
	serializer_class = OutorgaSerializer
	template_name = 'instantprod/apioutorga.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = OutorgaSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = OutorgaSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class TipoEmailAPIView(APIView):
	queryset = TipoEmail.objects.all()
	serializer_class = TipoEmailSerializer
	template_name = 'instantprod/apitipoemail.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = TipoEmailSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = TipoEmailSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class EmailAPIView(APIView):
	queryset = Email.objects.all()
	serializer_class = EmailSerializer
	template_name = 'instantprod/apiemail.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = EmailSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = EmailSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class TipoDataDiaCardAPIView(APIView):
	queryset = TipoDataDiaCard.objects.all()
	serializer_class = TipoDataDiaCardSerializer
	template_name = 'instantprod/apitipodatadiacard.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = TipoDataDiaCardSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = TipoDataDiaCardSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class TipoDataAnoCardAPIView(APIView):
	queryset = TipoDataAnoCard.objects.all()
	serializer_class = TipoDataAnoCardSerializer
	template_name = 'instantprod/apitipodataanocard.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = TipoDataAnoCardSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = TipoDataAnoCardSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class TipoRedeSocialAPIView(APIView):
	queryset = TipoRedeSocial.objects.all()
	serializer_class = TipoRedeSocialSerializer
	template_name = 'instantprod/apitiporedesocial.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = TipoRedeSocialSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = TipoRedeSocialSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class RedeSocialAPIView(APIView):
	queryset = RedeSocial.objects.all()
	serializer_class = RedeSocialSerializer
	template_name = 'instantprod/apiredesocial.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = RedeSocialSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = RedeSocialSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class TipoPronomeTratamentoAPIView(APIView):
	queryset = TipoPronomeTratamento.objects.all()
	serializer_class = TipoPronomeTratamentoSerializer
	template_name = 'instantprod/apitipopronometratamento.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = TipoPronomeTratamentoSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = TipoPronomeTratamentoSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class ReferenciaAPIView(APIView):
	queryset = Referencia.objects.all()
	serializer_class = ReferenciaSerializer
	template_name = 'instantprod/apireferencia.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = ReferenciaSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = ReferenciaSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class TipoAreaGeoAtuAPIView(APIView):
	queryset = TipoAreaGeoAtu.objects.all()
	serializer_class = TipoAreaGeoAtuSerializer
	template_name = 'instantprod/apitipoareageoatu.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = TipoAreaGeoAtuSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = TipoAreaGeoAtuSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class UserAPIView(APIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer
	template_name = 'instantprod/apiuser.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = UserSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = UserSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class TipoFiliacaoAPIView(APIView):
	queryset = TipoFiliacao.objects.all()
	serializer_class = TipoFiliacaoSerializer
	template_name = 'instantprod/apitipofiliacao.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = TipoFiliacaoSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = TipoFiliacaoSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class OrdemPagamentoBrasilAPIView(APIView):
	queryset = OrdemPagamentoBrasil.objects.all()
	serializer_class = OrdemPagamentoBrasilSerializer
	template_name = 'instantprod/apiordempagamentobrasil.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = OrdemPagamentoBrasilSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = OrdemPagamentoBrasilSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class QRCodeAPIView(APIView):
	queryset = QRCode.objects.all()
	serializer_class = QRCodeSerializer
	template_name = 'instantprod/apiqrcode.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = QRCodeSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = QRCodeSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class TipoMetodoPgtoAPIView(APIView):
	queryset = TipoMetodoPgto.objects.all()
	serializer_class = TipoMetodoPgtoSerializer
	template_name = 'instantprod/apitipometodopgto.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = TipoMetodoPgtoSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = TipoMetodoPgtoSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class TipoBancoAPIView(APIView):
	queryset = TipoBanco.objects.all()
	serializer_class = TipoBancoSerializer
	template_name = 'instantprod/apitipobanco.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = TipoBancoSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = TipoBancoSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class TipoContaAPIView(APIView):
	queryset = TipoConta.objects.all()
	serializer_class = TipoContaSerializer
	template_name = 'instantprod/apitipoconta.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = TipoContaSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = TipoContaSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class DadoBancarioAPIView(APIView):
	queryset = DadoBancario.objects.all()
	serializer_class = DadoBancarioSerializer
	template_name = 'instantprod/apidadobancario.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = DadoBancarioSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = DadoBancarioSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class TipoFaturacaoAPIView(APIView):
	queryset = TipoFaturacao.objects.all()
	serializer_class = TipoFaturacaoSerializer
	template_name = 'instantprod/apitipofaturacao.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = TipoFaturacaoSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = TipoFaturacaoSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class TipoCriptomoedaAPIView(APIView):
	queryset = TipoCriptomoeda.objects.all()
	serializer_class = TipoCriptomoedaSerializer
	template_name = 'instantprod/apitipocriptomoeda.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = TipoCriptomoedaSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = TipoCriptomoedaSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class CriptomoedaAPIView(APIView):
	queryset = Criptomoeda.objects.all()
	serializer_class = CriptomoedaSerializer
	template_name = 'instantprod/apicriptomoeda.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = CriptomoedaSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = CriptomoedaSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class TipoPrimeiroDiaSemanaAPIView(APIView):
	queryset = TipoPrimeiroDiaSemana.objects.all()
	serializer_class = TipoPrimeiroDiaSemanaSerializer
	template_name = 'instantprod/apitipoprimeirodiasemana.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = TipoPrimeiroDiaSemanaSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = TipoPrimeiroDiaSemanaSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class TipoDispHoraSemanaAPIView(APIView):
	queryset = TipoDispHoraSemana.objects.all()
	serializer_class = TipoDispHoraSemanaSerializer
	template_name = 'instantprod/apitipodisphorasemana.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = TipoDispHoraSemanaSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = TipoDispHoraSemanaSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class TipoFacilidadeAPIView(APIView):
	queryset = TipoFacilidade.objects.all()
	serializer_class = TipoFacilidadeSerializer
	template_name = 'instantprod/apitipofacilidade.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = TipoFacilidadeSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = TipoFacilidadeSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class TipoSegmentoInteresseAPIView(APIView):
	queryset = TipoSegmentoInteresse.objects.all()
	serializer_class = TipoSegmentoInteresseSerializer
	template_name = 'instantprod/apitiposegmentointeresse.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = TipoSegmentoInteresseSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = TipoSegmentoInteresseSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class TipoDataMesCardAPIView(APIView):
	queryset = TipoDataMesCard.objects.all()
	serializer_class = TipoDataMesCardSerializer
	template_name = 'instantprod/apitipodatamescard.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = TipoDataMesCardSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = TipoDataMesCardSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class TipoTurnoTrabAPIView(APIView):
	queryset = TipoTurnoTrab.objects.all()
	serializer_class = TipoTurnoTrabSerializer
	template_name = 'instantprod/apitipoturnotrab.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = TipoTurnoTrabSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = TipoTurnoTrabSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class DispTurnoPreferidoAPIView(APIView):
	queryset = DispTurnoPreferido.objects.all()
	serializer_class = DispTurnoPreferidoSerializer
	template_name = 'instantprod/apidispturnopreferido.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = DispTurnoPreferidoSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = DispTurnoPreferidoSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class TipoAmenidadeAPIView(APIView):
	queryset = TipoAmenidade.objects.all()
	serializer_class = TipoAmenidadeSerializer
	template_name = 'instantprod/apitipoamenidade.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = TipoAmenidadeSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = TipoAmenidadeSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class TipoPagamentoOnlineAPIView(APIView):
	queryset = TipoPagamentoOnline.objects.all()
	serializer_class = TipoPagamentoOnlineSerializer
	template_name = 'instantprod/apitipopagamentoonline.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = TipoPagamentoOnlineSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = TipoPagamentoOnlineSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class PagamentoOnlineAPIView(APIView):
	queryset = PagamentoOnline.objects.all()
	serializer_class = PagamentoOnlineSerializer
	template_name = 'instantprod/apipagamentoonline.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = PagamentoOnlineSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = PagamentoOnlineSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class TipoMarcadorAPIView(APIView):
	queryset = TipoMarcador.objects.all()
	serializer_class = TipoMarcadorSerializer
	template_name = 'instantprod/apitipomarcador.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = TipoMarcadorSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = TipoMarcadorSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class DispDiaPreferidoAPIView(APIView):
	queryset = DispDiaPreferido.objects.all()
	serializer_class = DispDiaPreferidoSerializer
	template_name = 'instantprod/apidispdiapreferido.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = DispDiaPreferidoSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = DispDiaPreferidoSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class TipoPerfilContaAPIView(APIView):
	queryset = TipoPerfilConta.objects.all()
	serializer_class = TipoPerfilContaSerializer
	template_name = 'instantprod/apitipoperfilconta.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = TipoPerfilContaSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = TipoPerfilContaSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class TipoEmpresaAPIView(APIView):
	queryset = TipoEmpresa.objects.all()
	serializer_class = TipoEmpresaSerializer
	template_name = 'instantprod/apitipoempresa.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = TipoEmpresaSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = TipoEmpresaSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class TipoBandeiraCartaoAPIView(APIView):
	queryset = TipoBandeiraCartao.objects.all()
	serializer_class = TipoBandeiraCartaoSerializer
	template_name = 'instantprod/apitipobandeiracartao.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = TipoBandeiraCartaoSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = TipoBandeiraCartaoSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class CartaoCreditoAPIView(APIView):
	queryset = CartaoCredito.objects.all()
	serializer_class = CartaoCreditoSerializer
	template_name = 'instantprod/apicartaocredito.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = CartaoCreditoSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = CartaoCreditoSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class PersonificacaoDominioAPIView(APIView):
	queryset = PersonificacaoDominio.objects.all()
	serializer_class = PersonificacaoDominioSerializer
	template_name = 'instantprod/apipersonificacaodominio.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = PersonificacaoDominioSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = PersonificacaoDominioSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class TipoSocioAPIView(APIView):
	queryset = TipoSocio.objects.all()
	serializer_class = TipoSocioSerializer
	template_name = 'instantprod/apitiposocio.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = TipoSocioSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = TipoSocioSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class QuadroSocioAPIView(APIView):
	queryset = QuadroSocio.objects.all()
	serializer_class = QuadroSocioSerializer
	template_name = 'instantprod/apiquadrosocio.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = QuadroSocioSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = QuadroSocioSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class TipoFerramentaIntegracaoAPIView(APIView):
	queryset = TipoFerramentaIntegracao.objects.all()
	serializer_class = TipoFerramentaIntegracaoSerializer
	template_name = 'instantprod/apitipoferramentaintegracao.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = TipoFerramentaIntegracaoSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = TipoFerramentaIntegracaoSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class IntegracaoAPIView(APIView):
	queryset = Integracao.objects.all()
	serializer_class = IntegracaoSerializer
	template_name = 'instantprod/apiintegracao.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = IntegracaoSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = IntegracaoSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class TransfSWIFTAPIView(APIView):
	queryset = TransfSWIFT.objects.all()
	serializer_class = TransfSWIFTSerializer
	template_name = 'instantprod/apitransfswift.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = TransfSWIFTSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = TransfSWIFTSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class TransfItaliaAPIView(APIView):
	queryset = TransfItalia.objects.all()
	serializer_class = TransfItaliaSerializer
	template_name = 'instantprod/apitransfitalia.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = TransfItaliaSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = TransfItaliaSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class TransfUniaoEuropeiaAPIView(APIView):
	queryset = TransfUniaoEuropeia.objects.all()
	serializer_class = TransfUniaoEuropeiaSerializer
	template_name = 'instantprod/apitransfuniaoeuropeia.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = TransfUniaoEuropeiaSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = TransfUniaoEuropeiaSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class EsquemaCorAPIView(APIView):
	queryset = EsquemaCor.objects.all()
	serializer_class = EsquemaCorSerializer
	template_name = 'instantprod/apiesquemacor.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = EsquemaCorSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = EsquemaCorSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class SaldoMensagemAPIView(APIView):
	queryset = SaldoMensagem.objects.all()
	serializer_class = SaldoMensagemSerializer
	template_name = 'instantprod/apisaldomensagem.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = SaldoMensagemSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = SaldoMensagemSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class RanqueamentoGeralAPIView(APIView):
	queryset = RanqueamentoGeral.objects.all()
	serializer_class = RanqueamentoGeralSerializer
	template_name = 'instantprod/apiranqueamentogeral.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = RanqueamentoGeralSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = RanqueamentoGeralSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class NotificacaoAPIView(APIView):
	queryset = Notificacao.objects.all()
	serializer_class = NotificacaoSerializer
	template_name = 'instantprod/apinotificacao.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = NotificacaoSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = NotificacaoSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class ComissaoAPIView(APIView):
	queryset = Comissao.objects.all()
	serializer_class = ComissaoSerializer
	template_name = 'instantprod/apicomissao.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = ComissaoSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = ComissaoSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class TipoRegimTributAPIView(APIView):
	queryset = TipoRegimTribut.objects.all()
	serializer_class = TipoRegimTributSerializer
	template_name = 'instantprod/apitiporegimtribut.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = TipoRegimTributSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = TipoRegimTributSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class TipoEmpresaTamanhoAPIView(APIView):
	queryset = TipoEmpresaTamanho.objects.all()
	serializer_class = TipoEmpresaTamanhoSerializer
	template_name = 'instantprod/apitipoempresatamanho.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = TipoEmpresaTamanhoSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = TipoEmpresaTamanhoSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class TipoContribAPIView(APIView):
	queryset = TipoContrib.objects.all()
	serializer_class = TipoContribSerializer
	template_name = 'instantprod/apitipocontrib.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = TipoContribSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = TipoContribSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class EmpresaAPIView(APIView):
	queryset = Empresa.objects.all()
	serializer_class = EmpresaSerializer
	template_name = 'instantprod/apiempresa.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = EmpresaSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = EmpresaSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class SalaAulaAPIView(APIView):
	queryset = SalaAula.objects.all()
	serializer_class = SalaAulaSerializer
	template_name = 'instantprod/apisalaaula.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = SalaAulaSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = SalaAulaSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class TipoNivelAlunoAPIView(APIView):
	queryset = TipoNivelAluno.objects.all()
	serializer_class = TipoNivelAlunoSerializer
	template_name = 'instantprod/apitiponivelaluno.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = TipoNivelAlunoSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = TipoNivelAlunoSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class TurmaAPIView(APIView):
	queryset = Turma.objects.all()
	serializer_class = TurmaSerializer
	template_name = 'instantprod/apiturma.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = TurmaSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = TurmaSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class TipoExtDigEditAPIView(APIView):
	queryset = TipoExtDigEdit.objects.all()
	serializer_class = TipoExtDigEditSerializer
	template_name = 'instantprod/apitipoextdigedit.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = TipoExtDigEditSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = TipoExtDigEditSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class TipoPerifericoAPIView(APIView):
	queryset = TipoPeriferico.objects.all()
	serializer_class = TipoPerifericoSerializer
	template_name = 'instantprod/apitipoperiferico.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = TipoPerifericoSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = TipoPerifericoSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class TipoSistemaOperacionalAPIView(APIView):
	queryset = TipoSistemaOperacional.objects.all()
	serializer_class = TipoSistemaOperacionalSerializer
	template_name = 'instantprod/apitiposistemaoperacional.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = TipoSistemaOperacionalSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = TipoSistemaOperacionalSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class TipoSoftwareTraducaoAPIView(APIView):
	queryset = TipoSoftwareTraducao.objects.all()
	serializer_class = TipoSoftwareTraducaoSerializer
	template_name = 'instantprod/apitiposoftwaretraducao.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = TipoSoftwareTraducaoSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = TipoSoftwareTraducaoSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class TipoSoftwareLocalizAPIView(APIView):
	queryset = TipoSoftwareLocaliz.objects.all()
	serializer_class = TipoSoftwareLocalizSerializer
	template_name = 'instantprod/apitiposoftwarelocaliz.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = TipoSoftwareLocalizSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = TipoSoftwareLocalizSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class TipoSoftwareDTPAPIView(APIView):
	queryset = TipoSoftwareDTP.objects.all()
	serializer_class = TipoSoftwareDTPSerializer
	template_name = 'instantprod/apitiposoftwaredtp.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = TipoSoftwareDTPSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = TipoSoftwareDTPSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class TipoSoftwarePacEscAPIView(APIView):
	queryset = TipoSoftwarePacEsc.objects.all()
	serializer_class = TipoSoftwarePacEscSerializer
	template_name = 'instantprod/apitiposoftwarepacesc.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = TipoSoftwarePacEscSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = TipoSoftwarePacEscSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class TipoSoftwareModTresDAPIView(APIView):
	queryset = TipoSoftwareModTresD.objects.all()
	serializer_class = TipoSoftwareModTresDSerializer
	template_name = 'instantprod/apitiposoftwaremodtresd.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = TipoSoftwareModTresDSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = TipoSoftwareModTresDSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class TipoSoftwareTranscAPIView(APIView):
	queryset = TipoSoftwareTransc.objects.all()
	serializer_class = TipoSoftwareTranscSerializer
	template_name = 'instantprod/apitiposoftwaretransc.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = TipoSoftwareTranscSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = TipoSoftwareTranscSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class TipoSoftwareLeitorAPIView(APIView):
	queryset = TipoSoftwareLeitor.objects.all()
	serializer_class = TipoSoftwareLeitorSerializer
	template_name = 'instantprod/apitiposoftwareleitor.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = TipoSoftwareLeitorSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = TipoSoftwareLeitorSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class TipoEngineGameAPIView(APIView):
	queryset = TipoEngineGame.objects.all()
	serializer_class = TipoEngineGameSerializer
	template_name = 'instantprod/apitipoenginegame.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = TipoEngineGameSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = TipoEngineGameSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class ProtocoloAtendimentoAPIView(APIView):
	queryset = ProtocoloAtendimento.objects.all()
	serializer_class = ProtocoloAtendimentoSerializer
	template_name = 'instantprod/apiprotocoloatendimento.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = ProtocoloAtendimentoSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = ProtocoloAtendimentoSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class TipoHardwareComputadorAPIView(APIView):
	queryset = TipoHardwareComputador.objects.all()
	serializer_class = TipoHardwareComputadorSerializer
	template_name = 'instantprod/apitipohardwarecomputador.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = TipoHardwareComputadorSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = TipoHardwareComputadorSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class TipoBancoDadosAPIView(APIView):
	queryset = TipoBancoDados.objects.all()
	serializer_class = TipoBancoDadosSerializer
	template_name = 'instantprod/apitipobancodados.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = TipoBancoDadosSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = TipoBancoDadosSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class TipoExtDiagramacaoAPIView(APIView):
	queryset = TipoExtDiagramacao.objects.all()
	serializer_class = TipoExtDiagramacaoSerializer
	template_name = 'instantprod/apitipoextdiagramacao.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = TipoExtDiagramacaoSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = TipoExtDiagramacaoSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class TipoExtAudioAPIView(APIView):
	queryset = TipoExtAudio.objects.all()
	serializer_class = TipoExtAudioSerializer
	template_name = 'instantprod/apitipoextaudio.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = TipoExtAudioSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = TipoExtAudioSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class TipoExtLocalizacaoAPIView(APIView):
	queryset = TipoExtLocalizacao.objects.all()
	serializer_class = TipoExtLocalizacaoSerializer
	template_name = 'instantprod/apitipoextlocalizacao.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = TipoExtLocalizacaoSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = TipoExtLocalizacaoSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class TipoExtVideoAPIView(APIView):
	queryset = TipoExtVideo.objects.all()
	serializer_class = TipoExtVideoSerializer
	template_name = 'instantprod/apitipoextvideo.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = TipoExtVideoSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = TipoExtVideoSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class TipoIntervaloTempoAPIView(APIView):
	queryset = TipoIntervaloTempo.objects.all()
	serializer_class = TipoIntervaloTempoSerializer
	template_name = 'instantprod/apitipointervalotempo.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = TipoIntervaloTempoSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = TipoIntervaloTempoSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class TipoParteAPIView(APIView):
	queryset = TipoParte.objects.all()
	serializer_class = TipoParteSerializer
	template_name = 'instantprod/apitipoparte.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = TipoParteSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = TipoParteSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class TipoInstCertificAPIView(APIView):
	queryset = TipoInstCertific.objects.all()
	serializer_class = TipoInstCertificSerializer
	template_name = 'instantprod/apitipoinstcertific.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = TipoInstCertificSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = TipoInstCertificSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class ExameProficienciaAPIView(APIView):
	queryset = ExameProficiencia.objects.all()
	serializer_class = ExameProficienciaSerializer
	template_name = 'instantprod/apiexameproficiencia.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = ExameProficienciaSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = ExameProficienciaSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class TipoExtDigNaoEditAPIView(APIView):
	queryset = TipoExtDigNaoEdit.objects.all()
	serializer_class = TipoExtDigNaoEditSerializer
	template_name = 'instantprod/apitipoextdignaoedit.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = TipoExtDigNaoEditSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = TipoExtDigNaoEditSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class TipoReligiaoAPIView(APIView):
	queryset = TipoReligiao.objects.all()
	serializer_class = TipoReligiaoSerializer
	template_name = 'instantprod/apitiporeligiao.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = TipoReligiaoSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = TipoReligiaoSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class TipoHobbieAPIView(APIView):
	queryset = TipoHobbie.objects.all()
	serializer_class = TipoHobbieSerializer
	template_name = 'instantprod/apitipohobbie.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = TipoHobbieSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = TipoHobbieSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class TipoAcessoInternetAPIView(APIView):
	queryset = TipoAcessoInternet.objects.all()
	serializer_class = TipoAcessoInternetSerializer
	template_name = 'instantprod/apitipoacessointernet.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = TipoAcessoInternetSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = TipoAcessoInternetSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class TipoExpLocalizaAPIView(APIView):
	queryset = TipoExpLocaliza.objects.all()
	serializer_class = TipoExpLocalizaSerializer
	template_name = 'instantprod/apitipoexplocaliza.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = TipoExpLocalizaSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = TipoExpLocalizaSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class ParteTraducaoAPIView(APIView):
	queryset = ParteTraducao.objects.all()
	serializer_class = ParteTraducaoSerializer
	template_name = 'instantprod/apipartetraducao.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = ParteTraducaoSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = ParteTraducaoSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class TipoFonteAPIView(APIView):
	queryset = TipoFonte.objects.all()
	serializer_class = TipoFonteSerializer
	template_name = 'instantprod/apitipofonte.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = TipoFonteSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = TipoFonteSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class AssinaturaDigitalAPIView(APIView):
	queryset = AssinaturaDigital.objects.all()
	serializer_class = AssinaturaDigitalSerializer
	template_name = 'instantprod/apiassinaturadigital.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = AssinaturaDigitalSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = AssinaturaDigitalSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class DispHoraSemanaAPIView(APIView):
	queryset = DispHoraSemana.objects.all()
	serializer_class = DispHoraSemanaSerializer
	template_name = 'instantprod/apidisphorasemana.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = DispHoraSemanaSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = DispHoraSemanaSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class BancoCurriculoAPIView(APIView):
	queryset = BancoCurriculo.objects.all()
	serializer_class = BancoCurriculoSerializer
	template_name = 'instantprod/apibancocurriculo.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = BancoCurriculoSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = BancoCurriculoSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class TipoRelacionamentoAPIView(APIView):
	queryset = TipoRelacionamento.objects.all()
	serializer_class = TipoRelacionamentoSerializer
	template_name = 'instantprod/apitiporelacionamento.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = TipoRelacionamentoSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = TipoRelacionamentoSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class RelacionamentoAPIView(APIView):
	queryset = Relacionamento.objects.all()
	serializer_class = RelacionamentoSerializer
	template_name = 'instantprod/apirelacionamento.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = RelacionamentoSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = RelacionamentoSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class TipoUnidComprimentoAPIView(APIView):
	queryset = TipoUnidComprimento.objects.all()
	serializer_class = TipoUnidComprimentoSerializer
	template_name = 'instantprod/apitipounidcomprimento.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = TipoUnidComprimentoSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = TipoUnidComprimentoSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class TipoUnidMassaAPIView(APIView):
	queryset = TipoUnidMassa.objects.all()
	serializer_class = TipoUnidMassaSerializer
	template_name = 'instantprod/apitipounidmassa.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = TipoUnidMassaSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = TipoUnidMassaSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class ParteAPIView(APIView):
	queryset = Parte.objects.all()
	serializer_class = ParteSerializer
	template_name = 'instantprod/apiparte.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = ParteSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = ParteSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class SecaoAPIView(APIView):
	queryset = Secao.objects.all()
	serializer_class = SecaoSerializer
	template_name = 'instantprod/apisecao.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = SecaoSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = SecaoSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class TipoDescontoAPIView(APIView):
	queryset = TipoDesconto.objects.all()
	serializer_class = TipoDescontoSerializer
	template_name = 'instantprod/apitipodesconto.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = TipoDescontoSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = TipoDescontoSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class DescontoAPIView(APIView):
	queryset = Desconto.objects.all()
	serializer_class = DescontoSerializer
	template_name = 'instantprod/apidesconto.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = DescontoSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = DescontoSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class TipoComoConheceuAPIView(APIView):
	queryset = TipoComoConheceu.objects.all()
	serializer_class = TipoComoConheceuSerializer
	template_name = 'instantprod/apitipocomoconheceu.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = TipoComoConheceuSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = TipoComoConheceuSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class OrdemExeServicoAPIView(APIView):
	queryset = OrdemExeServico.objects.all()
	serializer_class = OrdemExeServicoSerializer
	template_name = 'instantprod/apiordemexeservico.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = OrdemExeServicoSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = OrdemExeServicoSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class ConvenioAPIView(APIView):
	queryset = Convenio.objects.all()
	serializer_class = ConvenioSerializer
	template_name = 'instantprod/apiconvenio.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = ConvenioSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = ConvenioSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class TipoRelDiagAPIView(APIView):
	queryset = TipoRelDiag.objects.all()
	serializer_class = TipoRelDiagSerializer
	template_name = 'instantprod/apitiporeldiag.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = TipoRelDiagSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = TipoRelDiagSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class TipoModoEntregaAPIView(APIView):
	queryset = TipoModoEntrega.objects.all()
	serializer_class = TipoModoEntregaSerializer
	template_name = 'instantprod/apitipomodoentrega.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = TipoModoEntregaSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = TipoModoEntregaSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class RelDiagAPIView(APIView):
	queryset = RelDiag.objects.all()
	serializer_class = RelDiagSerializer
	template_name = 'instantprod/apireldiag.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = RelDiagSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = RelDiagSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class ItemModeloAPIView(APIView):
	queryset = ItemModelo.objects.all()
	serializer_class = ItemModeloSerializer
	template_name = 'instantprod/apiitemmodelo.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = ItemModeloSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = ItemModeloSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class ItemModeloTraducaoAPIView(APIView):
	queryset = ItemModeloTraducao.objects.all()
	serializer_class = ItemModeloTraducaoSerializer
	template_name = 'instantprod/apiitemmodelotraducao.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = ItemModeloTraducaoSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = ItemModeloTraducaoSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class ItemTraducaoAPIView(APIView):
	queryset = ItemTraducao.objects.all()
	serializer_class = ItemTraducaoSerializer
	template_name = 'instantprod/apiitemtraducao.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = ItemTraducaoSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = ItemTraducaoSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class TipoSuporteContAPIView(APIView):
	queryset = TipoSuporteCont.objects.all()
	serializer_class = TipoSuporteContSerializer
	template_name = 'instantprod/apitiposuportecont.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = TipoSuporteContSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = TipoSuporteContSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class TipoConteudoCategoriaAPIView(APIView):
	queryset = TipoConteudoCategoria.objects.all()
	serializer_class = TipoConteudoCategoriaSerializer
	template_name = 'instantprod/apitipoconteudocategoria.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = TipoConteudoCategoriaSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = TipoConteudoCategoriaSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class TipoConteudoAPIView(APIView):
	queryset = TipoConteudo.objects.all()
	serializer_class = TipoConteudoSerializer
	template_name = 'instantprod/apitipoconteudo.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = TipoConteudoSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = TipoConteudoSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class TipoSuporteContIOAPIView(APIView):
	queryset = TipoSuporteContIO.objects.all()
	serializer_class = TipoSuporteContIOSerializer
	template_name = 'instantprod/apitiposuportecontio.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = TipoSuporteContIOSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = TipoSuporteContIOSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class TipoExtDigEdtIOAPIView(APIView):
	queryset = TipoExtDigEdtIO.objects.all()
	serializer_class = TipoExtDigEdtIOSerializer
	template_name = 'instantprod/apitipoextdigedtio.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = TipoExtDigEdtIOSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = TipoExtDigEdtIOSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class RelDiagServAdAPIView(APIView):
	queryset = RelDiagServAd.objects.all()
	serializer_class = RelDiagServAdSerializer
	template_name = 'instantprod/apireldiagservad.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = RelDiagServAdSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = RelDiagServAdSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class TipoFusoHorarioAPIView(APIView):
	queryset = TipoFusoHorario.objects.all()
	serializer_class = TipoFusoHorarioSerializer
	template_name = 'instantprod/apitipofusohorario.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = TipoFusoHorarioSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = TipoFusoHorarioSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class TipoAgendaAPIView(APIView):
	queryset = TipoAgenda.objects.all()
	serializer_class = TipoAgendaSerializer
	template_name = 'instantprod/apitipoagenda.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = TipoAgendaSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = TipoAgendaSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class AgendaAPIView(APIView):
	queryset = Agenda.objects.all()
	serializer_class = AgendaSerializer
	template_name = 'instantprod/apiagenda.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = AgendaSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = AgendaSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class AgendaDisponivelAPIView(APIView):
	queryset = AgendaDisponivel.objects.all()
	serializer_class = AgendaDisponivelSerializer
	template_name = 'instantprod/apiagendadisponivel.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = AgendaDisponivelSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = AgendaDisponivelSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class TipoStatusMensagemAPIView(APIView):
	queryset = TipoStatusMensagem.objects.all()
	serializer_class = TipoStatusMensagemSerializer
	template_name = 'instantprod/apitipostatusmensagem.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = TipoStatusMensagemSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = TipoStatusMensagemSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class TipoMensagemAPIView(APIView):
	queryset = TipoMensagem.objects.all()
	serializer_class = TipoMensagemSerializer
	template_name = 'instantprod/apitipomensagem.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = TipoMensagemSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = TipoMensagemSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class MensagemAPIView(APIView):
	queryset = Mensagem.objects.all()
	serializer_class = MensagemSerializer
	template_name = 'instantprod/apimensagem.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = MensagemSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = MensagemSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class TipoFormComplAPIView(APIView):
	queryset = TipoFormCompl.objects.all()
	serializer_class = TipoFormComplSerializer
	template_name = 'instantprod/apitipoformcompl.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = TipoFormComplSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = TipoFormComplSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class TipoCertificacaoAPIView(APIView):
	queryset = TipoCertificacao.objects.all()
	serializer_class = TipoCertificacaoSerializer
	template_name = 'instantprod/apitipocertificacao.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = TipoCertificacaoSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = TipoCertificacaoSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class TipoDataMesOrdnAPIView(APIView):
	queryset = TipoDataMesOrdn.objects.all()
	serializer_class = TipoDataMesOrdnSerializer
	template_name = 'instantprod/apitipodatamesordn.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = TipoDataMesOrdnSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = TipoDataMesOrdnSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class TipoPeriodoAnoAtualAPIView(APIView):
	queryset = TipoPeriodoAnoAtual.objects.all()
	serializer_class = TipoPeriodoAnoAtualSerializer
	template_name = 'instantprod/apitipoperiodoanoatual.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = TipoPeriodoAnoAtualSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = TipoPeriodoAnoAtualSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class TipoStatusFormAPIView(APIView):
	queryset = TipoStatusForm.objects.all()
	serializer_class = TipoStatusFormSerializer
	template_name = 'instantprod/apitipostatusform.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = TipoStatusFormSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = TipoStatusFormSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class TipoDuracaoCursoAPIView(APIView):
	queryset = TipoDuracaoCurso.objects.all()
	serializer_class = TipoDuracaoCursoSerializer
	template_name = 'instantprod/apitipoduracaocurso.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = TipoDuracaoCursoSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = TipoDuracaoCursoSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class TipoUnidTempoAPIView(APIView):
	queryset = TipoUnidTempo.objects.all()
	serializer_class = TipoUnidTempoSerializer
	template_name = 'instantprod/apitipounidtempo.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = TipoUnidTempoSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = TipoUnidTempoSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class FormComplAPIView(APIView):
	queryset = FormCompl.objects.all()
	serializer_class = FormComplSerializer
	template_name = 'instantprod/apiformcompl.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = FormComplSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = FormComplSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class TipoFormAcademAPIView(APIView):
	queryset = TipoFormAcadem.objects.all()
	serializer_class = TipoFormAcademSerializer
	template_name = 'instantprod/apitipoformacadem.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = TipoFormAcademSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = TipoFormAcademSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class FormAcademAPIView(APIView):
	queryset = FormAcadem.objects.all()
	serializer_class = FormAcademSerializer
	template_name = 'instantprod/apiformacadem.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = FormAcademSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = FormAcademSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class TipoDiaSemTradAPIView(APIView):
	queryset = TipoDiaSemTrad.objects.all()
	serializer_class = TipoDiaSemTradSerializer
	template_name = 'instantprod/apitipodiasemtrad.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = TipoDiaSemTradSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = TipoDiaSemTradSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class TipoDataDiaOrdnAPIView(APIView):
	queryset = TipoDataDiaOrdn.objects.all()
	serializer_class = TipoDataDiaOrdnSerializer
	template_name = 'instantprod/apitipodatadiaordn.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = TipoDataDiaOrdnSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = TipoDataDiaOrdnSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class TipoDataComDetlAPIView(APIView):
	queryset = TipoDataComDetl.objects.all()
	serializer_class = TipoDataComDetlSerializer
	template_name = 'instantprod/apitipodatacomdetl.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = TipoDataComDetlSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = TipoDataComDetlSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class TipoDataComAssuAPIView(APIView):
	queryset = TipoDataComAssu.objects.all()
	serializer_class = TipoDataComAssuSerializer
	template_name = 'instantprod/apitipodatacomassu.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = TipoDataComAssuSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = TipoDataComAssuSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class TipoDataComAPIView(APIView):
	queryset = TipoDataCom.objects.all()
	serializer_class = TipoDataComSerializer
	template_name = 'instantprod/apitipodatacom.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = TipoDataComSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = TipoDataComSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class TipoEstagioPropostaAPIView(APIView):
	queryset = TipoEstagioProposta.objects.all()
	serializer_class = TipoEstagioPropostaSerializer
	template_name = 'instantprod/apitipoestagioproposta.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = TipoEstagioPropostaSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = TipoEstagioPropostaSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class PropTecComercialAPIView(APIView):
	queryset = PropTecComercial.objects.all()
	serializer_class = PropTecComercialSerializer
	template_name = 'instantprod/apipropteccomercial.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = PropTecComercialSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = PropTecComercialSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class TipoPeriodicidadeAPIView(APIView):
	queryset = TipoPeriodicidade.objects.all()
	serializer_class = TipoPeriodicidadeSerializer
	template_name = 'instantprod/apitipoperiodicidade.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = TipoPeriodicidadeSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = TipoPeriodicidadeSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class LembreteAPIView(APIView):
	queryset = Lembrete.objects.all()
	serializer_class = LembreteSerializer
	template_name = 'instantprod/apilembrete.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = LembreteSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = LembreteSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class AgendaAtividadeAPIView(APIView):
	queryset = AgendaAtividade.objects.all()
	serializer_class = AgendaAtividadeSerializer
	template_name = 'instantprod/apiagendaatividade.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = AgendaAtividadeSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = AgendaAtividadeSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class ComboAPIView(APIView):
	queryset = Combo.objects.all()
	serializer_class = ComboSerializer
	template_name = 'instantprod/apicombo.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = ComboSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = ComboSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class ItemUnidadeAPIView(APIView):
	queryset = ItemUnidade.objects.all()
	serializer_class = ItemUnidadeSerializer
	template_name = 'instantprod/apiitemunidade.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = ItemUnidadeSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = ItemUnidadeSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class ProdutoAPIView(APIView):
	queryset = Produto.objects.all()
	serializer_class = ProdutoSerializer
	template_name = 'instantprod/apiproduto.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = ProdutoSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = ProdutoSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class TipoLinguaAPIView(APIView):
	queryset = TipoLingua.objects.all()
	serializer_class = TipoLinguaSerializer
	template_name = 'instantprod/apitipolingua.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = TipoLinguaSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = TipoLinguaSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class RelDiagLinguaPaisAPIView(APIView):
	queryset = RelDiagLinguaPais.objects.all()
	serializer_class = RelDiagLinguaPaisSerializer
	template_name = 'instantprod/apireldiaglinguapais.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = RelDiagLinguaPaisSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = RelDiagLinguaPaisSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class TipoDispAmbientAPIView(APIView):
	queryset = TipoDispAmbient.objects.all()
	serializer_class = TipoDispAmbientSerializer
	template_name = 'instantprod/apitipodispambient.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = TipoDispAmbientSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = TipoDispAmbientSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class TipoAutodeclaracaoAPIView(APIView):
	queryset = TipoAutodeclaracao.objects.all()
	serializer_class = TipoAutodeclaracaoSerializer
	template_name = 'instantprod/apitipoautodeclaracao.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = TipoAutodeclaracaoSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = TipoAutodeclaracaoSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class EventoInterpCargoAPIView(APIView):
	queryset = EventoInterpCargo.objects.all()
	serializer_class = EventoInterpCargoSerializer
	template_name = 'instantprod/apieventointerpcargo.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = EventoInterpCargoSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = EventoInterpCargoSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class RepeticaoInterpretacaoAPIView(APIView):
	queryset = RepeticaoInterpretacao.objects.all()
	serializer_class = RepeticaoInterpretacaoSerializer
	template_name = 'instantprod/apirepeticaointerpretacao.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = RepeticaoInterpretacaoSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = RepeticaoInterpretacaoSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class RepeticaoEventoAPIView(APIView):
	queryset = RepeticaoEvento.objects.all()
	serializer_class = RepeticaoEventoSerializer
	template_name = 'instantprod/apirepeticaoevento.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = RepeticaoEventoSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = RepeticaoEventoSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class NumeroRecepAuricularesAPIView(APIView):
	queryset = NumeroRecepAuriculares.objects.all()
	serializer_class = NumeroRecepAuricularesSerializer
	template_name = 'instantprod/apinumerorecepauriculares.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = NumeroRecepAuricularesSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = NumeroRecepAuricularesSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class EventoDetalheAPIView(APIView):
	queryset = EventoDetalhe.objects.all()
	serializer_class = EventoDetalheSerializer
	template_name = 'instantprod/apieventodetalhe.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = EventoDetalheSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = EventoDetalheSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class ResponsavelAPIView(APIView):
	queryset = Responsavel.objects.all()
	serializer_class = ResponsavelSerializer
	template_name = 'instantprod/apiresponsavel.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = ResponsavelSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = ResponsavelSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class TipoLocalPresencialAPIView(APIView):
	queryset = TipoLocalPresencial.objects.all()
	serializer_class = TipoLocalPresencialSerializer
	template_name = 'instantprod/apitipolocalpresencial.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = TipoLocalPresencialSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = TipoLocalPresencialSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class TipoPreferenciaAulaAPIView(APIView):
	queryset = TipoPreferenciaAula.objects.all()
	serializer_class = TipoPreferenciaAulaSerializer
	template_name = 'instantprod/apitipopreferenciaaula.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = TipoPreferenciaAulaSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = TipoPreferenciaAulaSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class TipoFaixaEtariaAPIView(APIView):
	queryset = TipoFaixaEtaria.objects.all()
	serializer_class = TipoFaixaEtariaSerializer
	template_name = 'instantprod/apitipofaixaetaria.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = TipoFaixaEtariaSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = TipoFaixaEtariaSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class TipoRegimeEnsinoAPIView(APIView):
	queryset = TipoRegimeEnsino.objects.all()
	serializer_class = TipoRegimeEnsinoSerializer
	template_name = 'instantprod/apitiporegimeensino.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = TipoRegimeEnsinoSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = TipoRegimeEnsinoSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class TipoModalidadeAPIView(APIView):
	queryset = TipoModalidade.objects.all()
	serializer_class = TipoModalidadeSerializer
	template_name = 'instantprod/apitipomodalidade.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = TipoModalidadeSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = TipoModalidadeSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class TipoRepeticaoCursoAPIView(APIView):
	queryset = TipoRepeticaoCurso.objects.all()
	serializer_class = TipoRepeticaoCursoSerializer
	template_name = 'instantprod/apitiporepeticaocurso.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = TipoRepeticaoCursoSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = TipoRepeticaoCursoSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class RelDiagCursoAPIView(APIView):
	queryset = RelDiagCurso.objects.all()
	serializer_class = RelDiagCursoSerializer
	template_name = 'instantprod/apireldiagcurso.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = RelDiagCursoSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = RelDiagCursoSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class TipoResidenciaContratoAPIView(APIView):
	queryset = TipoResidenciaContrato.objects.all()
	serializer_class = TipoResidenciaContratoSerializer
	template_name = 'instantprod/apitiporesidenciacontrato.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = TipoResidenciaContratoSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = TipoResidenciaContratoSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class TipoHabilitacaoAPIView(APIView):
	queryset = TipoHabilitacao.objects.all()
	serializer_class = TipoHabilitacaoSerializer
	template_name = 'instantprod/apitipohabilitacao.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = TipoHabilitacaoSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = TipoHabilitacaoSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class TipoPcDAparelhoAPIView(APIView):
	queryset = TipoPcDAparelho.objects.all()
	serializer_class = TipoPcDAparelhoSerializer
	template_name = 'instantprod/apitipopcdaparelho.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = TipoPcDAparelhoSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = TipoPcDAparelhoSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class TipoEstadoCivilAPIView(APIView):
	queryset = TipoEstadoCivil.objects.all()
	serializer_class = TipoEstadoCivilSerializer
	template_name = 'instantprod/apitipoestadocivil.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = TipoEstadoCivilSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = TipoEstadoCivilSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class TipoResidenciaAPIView(APIView):
	queryset = TipoResidencia.objects.all()
	serializer_class = TipoResidenciaSerializer
	template_name = 'instantprod/apitiporesidencia.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = TipoResidenciaSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = TipoResidenciaSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class TipoTrabalhoVoluntarioAPIView(APIView):
	queryset = TipoTrabalhoVoluntario.objects.all()
	serializer_class = TipoTrabalhoVoluntarioSerializer
	template_name = 'instantprod/apitipotrabalhovoluntario.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = TipoTrabalhoVoluntarioSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = TipoTrabalhoVoluntarioSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class TipoMoradorAPIView(APIView):
	queryset = TipoMorador.objects.all()
	serializer_class = TipoMoradorSerializer
	template_name = 'instantprod/apitipomorador.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = TipoMoradorSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = TipoMoradorSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class TipoRendaFamiliarAPIView(APIView):
	queryset = TipoRendaFamiliar.objects.all()
	serializer_class = TipoRendaFamiliarSerializer
	template_name = 'instantprod/apitiporendafamiliar.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = TipoRendaFamiliarSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = TipoRendaFamiliarSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class TipoFilhoQuantAPIView(APIView):
	queryset = TipoFilhoQuant.objects.all()
	serializer_class = TipoFilhoQuantSerializer
	template_name = 'instantprod/apitipofilhoquant.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = TipoFilhoQuantSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = TipoFilhoQuantSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class DadosPessoaisAPIView(APIView):
	queryset = DadosPessoais.objects.all()
	serializer_class = DadosPessoaisSerializer
	template_name = 'instantprod/apidadospessoais.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = DadosPessoaisSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = DadosPessoaisSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class TipoImovelAPIView(APIView):
	queryset = TipoImovel.objects.all()
	serializer_class = TipoImovelSerializer
	template_name = 'instantprod/apitipoimovel.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = TipoImovelSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = TipoImovelSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class TipoFuncionarioQuantAPIView(APIView):
	queryset = TipoFuncionarioQuant.objects.all()
	serializer_class = TipoFuncionarioQuantSerializer
	template_name = 'instantprod/apitipofuncionarioquant.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = TipoFuncionarioQuantSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = TipoFuncionarioQuantSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class TipoLicFranquiaAPIView(APIView):
	queryset = TipoLicFranquia.objects.all()
	serializer_class = TipoLicFranquiaSerializer
	template_name = 'instantprod/apitipolicfranquia.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = TipoLicFranquiaSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = TipoLicFranquiaSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class TipoInvestimentoInicialAPIView(APIView):
	queryset = TipoInvestimentoInicial.objects.all()
	serializer_class = TipoInvestimentoInicialSerializer
	template_name = 'instantprod/apitipoinvestimentoinicial.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = TipoInvestimentoInicialSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = TipoInvestimentoInicialSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class TipoCapitalGiroAPIView(APIView):
	queryset = TipoCapitalGiro.objects.all()
	serializer_class = TipoCapitalGiroSerializer
	template_name = 'instantprod/apitipocapitalgiro.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = TipoCapitalGiroSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = TipoCapitalGiroSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class TipoAreaMinimaAPIView(APIView):
	queryset = TipoAreaMinima.objects.all()
	serializer_class = TipoAreaMinimaSerializer
	template_name = 'instantprod/apitipoareaminima.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = TipoAreaMinimaSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = TipoAreaMinimaSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class TipoCompartGeoAPIView(APIView):
	queryset = TipoCompartGeo.objects.all()
	serializer_class = TipoCompartGeoSerializer
	template_name = 'instantprod/apitipocompartgeo.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = TipoCompartGeoSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = TipoCompartGeoSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class RelDiagLicFranquiaAPIView(APIView):
	queryset = RelDiagLicFranquia.objects.all()
	serializer_class = RelDiagLicFranquiaSerializer
	template_name = 'instantprod/apireldiaglicfranquia.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = RelDiagLicFranquiaSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = RelDiagLicFranquiaSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class RelDiagTradAPIView(APIView):
	queryset = RelDiagTrad.objects.all()
	serializer_class = RelDiagTradSerializer
	template_name = 'instantprod/apireldiagtrad.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = RelDiagTradSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = RelDiagTradSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class EventoEnderecoAPIView(APIView):
	queryset = EventoEndereco.objects.all()
	serializer_class = EventoEnderecoSerializer
	template_name = 'instantprod/apieventoendereco.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = EventoEnderecoSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = EventoEnderecoSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class TipoEventoAPIView(APIView):
	queryset = TipoEvento.objects.all()
	serializer_class = TipoEventoSerializer
	template_name = 'instantprod/apitipoevento.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = TipoEventoSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = TipoEventoSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class EventoAPIView(APIView):
	queryset = Evento.objects.all()
	serializer_class = EventoSerializer
	template_name = 'instantprod/apievento.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = EventoSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = EventoSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class TipoPretensaoBolsaEstagioAPIView(APIView):
	queryset = TipoPretensaoBolsaEstagio.objects.all()
	serializer_class = TipoPretensaoBolsaEstagioSerializer
	template_name = 'instantprod/apitipopretensaobolsaestagio.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = TipoPretensaoBolsaEstagioSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = TipoPretensaoBolsaEstagioSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class TipoProgrIcentEducacaoAPIView(APIView):
	queryset = TipoProgrIcentEducacao.objects.all()
	serializer_class = TipoProgrIcentEducacaoSerializer
	template_name = 'instantprod/apitipoprogricenteducacao.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = TipoProgrIcentEducacaoSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = TipoProgrIcentEducacaoSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class TipoDisponibilEstagiarAPIView(APIView):
	queryset = TipoDisponibilEstagiar.objects.all()
	serializer_class = TipoDisponibilEstagiarSerializer
	template_name = 'instantprod/apitipodisponibilestagiar.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = TipoDisponibilEstagiarSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = TipoDisponibilEstagiarSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class TipoTurnoEduAPIView(APIView):
	queryset = TipoTurnoEdu.objects.all()
	serializer_class = TipoTurnoEduSerializer
	template_name = 'instantprod/apitipoturnoedu.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = TipoTurnoEduSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = TipoTurnoEduSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class ItemBolsaEstagioAPIView(APIView):
	queryset = ItemBolsaEstagio.objects.all()
	serializer_class = ItemBolsaEstagioSerializer
	template_name = 'instantprod/apiitembolsaestagio.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = ItemBolsaEstagioSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = ItemBolsaEstagioSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class LivroAPIView(APIView):
	queryset = Livro.objects.all()
	serializer_class = LivroSerializer
	template_name = 'instantprod/apilivro.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = LivroSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = LivroSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class RelDiagLivrariaAPIView(APIView):
	queryset = RelDiagLivraria.objects.all()
	serializer_class = RelDiagLivrariaSerializer
	template_name = 'instantprod/apireldiaglivraria.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = RelDiagLivrariaSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = RelDiagLivrariaSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class CabecalhoTopoAPIView(APIView):
	queryset = CabecalhoTopo.objects.all()
	serializer_class = CabecalhoTopoSerializer
	template_name = 'instantprod/apicabecalhotopo.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = CabecalhoTopoSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = CabecalhoTopoSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class RodapeAPIView(APIView):
	queryset = Rodape.objects.all()
	serializer_class = RodapeSerializer
	template_name = 'instantprod/apirodape.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = RodapeSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = RodapeSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class RodapeMenuAPIView(APIView):
	queryset = RodapeMenu.objects.all()
	serializer_class = RodapeMenuSerializer
	template_name = 'instantprod/apirodapemenu.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = RodapeMenuSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = RodapeMenuSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class RodapeBaseAPIView(APIView):
	queryset = RodapeBase.objects.all()
	serializer_class = RodapeBaseSerializer
	template_name = 'instantprod/apirodapebase.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = RodapeBaseSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = RodapeBaseSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class CabecalhoAPIView(APIView):
	queryset = Cabecalho.objects.all()
	serializer_class = CabecalhoSerializer
	template_name = 'instantprod/apicabecalho.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = CabecalhoSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = CabecalhoSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class CabecalhoMenuAPIView(APIView):
	queryset = CabecalhoMenu.objects.all()
	serializer_class = CabecalhoMenuSerializer
	template_name = 'instantprod/apicabecalhomenu.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = CabecalhoMenuSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = CabecalhoMenuSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class PrincipalAPIView(APIView):
	queryset = Principal.objects.all()
	serializer_class = PrincipalSerializer
	template_name = 'instantprod/apiprincipal.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = PrincipalSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = PrincipalSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class SiteAPIView(APIView):
	queryset = Site.objects.all()
	serializer_class = SiteSerializer
	template_name = 'instantprod/apisite.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = SiteSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = SiteSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class TipoPainelAtendimentoAPIView(APIView):
	queryset = TipoPainelAtendimento.objects.all()
	serializer_class = TipoPainelAtendimentoSerializer
	template_name = 'instantprod/apitipopainelatendimento.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = TipoPainelAtendimentoSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = TipoPainelAtendimentoSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class TipoPosicaoAtendimentoAPIView(APIView):
	queryset = TipoPosicaoAtendimento.objects.all()
	serializer_class = TipoPosicaoAtendimentoSerializer
	template_name = 'instantprod/apitipoposicaoatendimento.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = TipoPosicaoAtendimentoSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = TipoPosicaoAtendimentoSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class TipoOrientacaoAPIView(APIView):
	queryset = TipoOrientacao.objects.all()
	serializer_class = TipoOrientacaoSerializer
	template_name = 'instantprod/apitipoorientacao.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = TipoOrientacaoSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = TipoOrientacaoSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class PainelAtendimentoAPIView(APIView):
	queryset = PainelAtendimento.objects.all()
	serializer_class = PainelAtendimentoSerializer
	template_name = 'instantprod/apipainelatendimento.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = PainelAtendimentoSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = PainelAtendimentoSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class TipoClienteAtendeAPIView(APIView):
	queryset = TipoClienteAtende.objects.all()
	serializer_class = TipoClienteAtendeSerializer
	template_name = 'instantprod/apitipoclienteatende.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = TipoClienteAtendeSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = TipoClienteAtendeSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class FormatoHoraAPIView(APIView):
	queryset = FormatoHora.objects.all()
	serializer_class = FormatoHoraSerializer
	template_name = 'instantprod/apiformatohora.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = FormatoHoraSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = FormatoHoraSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class TipoSituacOcupAPIView(APIView):
	queryset = TipoSituacOcup.objects.all()
	serializer_class = TipoSituacOcupSerializer
	template_name = 'instantprod/apitiposituacocup.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = TipoSituacOcupSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = TipoSituacOcupSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class TipoFormatoDataAPIView(APIView):
	queryset = TipoFormatoData.objects.all()
	serializer_class = TipoFormatoDataSerializer
	template_name = 'instantprod/apitipoformatodata.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = TipoFormatoDataSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = TipoFormatoDataSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class PreferenciaAdicionalAPIView(APIView):
	queryset = PreferenciaAdicional.objects.all()
	serializer_class = PreferenciaAdicionalSerializer
	template_name = 'instantprod/apipreferenciaadicional.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = PreferenciaAdicionalSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = PreferenciaAdicionalSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class SoftwareAPIView(APIView):
	queryset = Software.objects.all()
	serializer_class = SoftwareSerializer
	template_name = 'instantprod/apisoftware.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = SoftwareSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = SoftwareSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class InstituicaoEnsinoAPIView(APIView):
	queryset = InstituicaoEnsino.objects.all()
	serializer_class = InstituicaoEnsinoSerializer
	template_name = 'instantprod/apiinstituicaoensino.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = InstituicaoEnsinoSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = InstituicaoEnsinoSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class TipoServTerceiroAPIView(APIView):
	queryset = TipoServTerceiro.objects.all()
	serializer_class = TipoServTerceiroSerializer
	template_name = 'instantprod/apitiposervterceiro.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = TipoServTerceiroSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = TipoServTerceiroSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class RelDiagServTerceiroAPIView(APIView):
	queryset = RelDiagServTerceiro.objects.all()
	serializer_class = RelDiagServTerceiroSerializer
	template_name = 'instantprod/apireldiagservterceiro.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = RelDiagServTerceiroSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = RelDiagServTerceiroSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class ParteLinguaPaisAPIView(APIView):
	queryset = ParteLinguaPais.objects.all()
	serializer_class = ParteLinguaPaisSerializer
	template_name = 'instantprod/apipartelinguapais.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = ParteLinguaPaisSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = ParteLinguaPaisSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class TipoNotaAPIView(APIView):
	queryset = TipoNota.objects.all()
	serializer_class = TipoNotaSerializer
	template_name = 'instantprod/apitiponota.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = TipoNotaSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = TipoNotaSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class NotaAPIView(APIView):
	queryset = Nota.objects.all()
	serializer_class = NotaSerializer
	template_name = 'instantprod/apinota.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = NotaSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = NotaSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class ListaCampanhaAPIView(APIView):
	queryset = ListaCampanha.objects.all()
	serializer_class = ListaCampanhaSerializer
	template_name = 'instantprod/apilistacampanha.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = ListaCampanhaSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = ListaCampanhaSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class EmpresaLinguaPaisAPIView(APIView):
	queryset = EmpresaLinguaPais.objects.all()
	serializer_class = EmpresaLinguaPaisSerializer
	template_name = 'instantprod/apiempresalinguapais.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = EmpresaLinguaPaisSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = EmpresaLinguaPaisSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class TipoAcaoAPIView(APIView):
	queryset = TipoAcao.objects.all()
	serializer_class = TipoAcaoSerializer
	template_name = 'instantprod/apitipoacao.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = TipoAcaoSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = TipoAcaoSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class AgendaPermissaoAPIView(APIView):
	queryset = AgendaPermissao.objects.all()
	serializer_class = AgendaPermissaoSerializer
	template_name = 'instantprod/apiagendapermissao.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = AgendaPermissaoSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = AgendaPermissaoSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class TipoClassListaAPIView(APIView):
	queryset = TipoClassLista.objects.all()
	serializer_class = TipoClassListaSerializer
	template_name = 'instantprod/apitipoclasslista.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = TipoClassListaSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = TipoClassListaSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class TipoStatusListaAPIView(APIView):
	queryset = TipoStatusLista.objects.all()
	serializer_class = TipoStatusListaSerializer
	template_name = 'instantprod/apitipostatuslista.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = TipoStatusListaSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = TipoStatusListaSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class ListaContatoAPIView(APIView):
	queryset = ListaContato.objects.all()
	serializer_class = ListaContatoSerializer
	template_name = 'instantprod/apilistacontato.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = ListaContatoSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = ListaContatoSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class ListaEmailAPIView(APIView):
	queryset = ListaEmail.objects.all()
	serializer_class = ListaEmailSerializer
	template_name = 'instantprod/apilistaemail.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = ListaEmailSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = ListaEmailSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class FilmeAPIView(APIView):
	queryset = Filme.objects.all()
	serializer_class = FilmeSerializer
	template_name = 'instantprod/apifilme.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = FilmeSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = FilmeSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class RelDiagLicPlanoAPIView(APIView):
	queryset = RelDiagLicPlano.objects.all()
	serializer_class = RelDiagLicPlanoSerializer
	template_name = 'instantprod/apireldiaglicplano.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = RelDiagLicPlanoSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = RelDiagLicPlanoSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class ItemLocacaoBalcaoAPIView(APIView):
	queryset = ItemLocacaoBalcao.objects.all()
	serializer_class = ItemLocacaoBalcaoSerializer
	template_name = 'instantprod/apiitemlocacaobalcao.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = ItemLocacaoBalcaoSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = ItemLocacaoBalcaoSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class TipoAcaoCampanhaAPIView(APIView):
	queryset = TipoAcaoCampanha.objects.all()
	serializer_class = TipoAcaoCampanhaSerializer
	template_name = 'instantprod/apitipoacaocampanha.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = TipoAcaoCampanhaSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = TipoAcaoCampanhaSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class TipoStatusCampanhaAPIView(APIView):
	queryset = TipoStatusCampanha.objects.all()
	serializer_class = TipoStatusCampanhaSerializer
	template_name = 'instantprod/apitipostatuscampanha.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = TipoStatusCampanhaSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = TipoStatusCampanhaSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class TipoCategoriaModeloCampanhaAPIView(APIView):
	queryset = TipoCategoriaModeloCampanha.objects.all()
	serializer_class = TipoCategoriaModeloCampanhaSerializer
	template_name = 'instantprod/apitipocategoriamodelocampanha.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = TipoCategoriaModeloCampanhaSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = TipoCategoriaModeloCampanhaSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class TipoModeloCampanhaAPIView(APIView):
	queryset = TipoModeloCampanha.objects.all()
	serializer_class = TipoModeloCampanhaSerializer
	template_name = 'instantprod/apitipomodelocampanha.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = TipoModeloCampanhaSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = TipoModeloCampanhaSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class ModeloCampanhaAPIView(APIView):
	queryset = ModeloCampanha.objects.all()
	serializer_class = ModeloCampanhaSerializer
	template_name = 'instantprod/apimodelocampanha.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = ModeloCampanhaSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = ModeloCampanhaSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class CampanhaAPIView(APIView):
	queryset = Campanha.objects.all()
	serializer_class = CampanhaSerializer
	template_name = 'instantprod/apicampanha.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = CampanhaSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = CampanhaSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class TipoPerfilLocutorAPIView(APIView):
	queryset = TipoPerfilLocutor.objects.all()
	serializer_class = TipoPerfilLocutorSerializer
	template_name = 'instantprod/apitipoperfillocutor.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = TipoPerfilLocutorSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = TipoPerfilLocutorSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class ItemTipoPerfilLocutorAPIView(APIView):
	queryset = ItemTipoPerfilLocutor.objects.all()
	serializer_class = ItemTipoPerfilLocutorSerializer
	template_name = 'instantprod/apiitemtipoperfillocutor.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = ItemTipoPerfilLocutorSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = ItemTipoPerfilLocutorSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class TipoCategoriaServicoAPIView(APIView):
	queryset = TipoCategoriaServico.objects.all()
	serializer_class = TipoCategoriaServicoSerializer
	template_name = 'instantprod/apitipocategoriaservico.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = TipoCategoriaServicoSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = TipoCategoriaServicoSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class ItemCategoriaServicoAPIView(APIView):
	queryset = ItemCategoriaServico.objects.all()
	serializer_class = ItemCategoriaServicoSerializer
	template_name = 'instantprod/apiitemcategoriaservico.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = ItemCategoriaServicoSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = ItemCategoriaServicoSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class TipoTamanhoAPIView(APIView):
	queryset = TipoTamanho.objects.all()
	serializer_class = TipoTamanhoSerializer
	template_name = 'instantprod/apitipotamanho.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = TipoTamanhoSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = TipoTamanhoSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class ModeloDocumentoAPIView(APIView):
	queryset = ModeloDocumento.objects.all()
	serializer_class = ModeloDocumentoSerializer
	template_name = 'instantprod/apimodelodocumento.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = ModeloDocumentoSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = ModeloDocumentoSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class TipoLicConvenioAPIView(APIView):
	queryset = TipoLicConvenio.objects.all()
	serializer_class = TipoLicConvenioSerializer
	template_name = 'instantprod/apitipolicconvenio.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = TipoLicConvenioSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = TipoLicConvenioSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class RelDiagLicConvenioAPIView(APIView):
	queryset = RelDiagLicConvenio.objects.all()
	serializer_class = RelDiagLicConvenioSerializer
	template_name = 'instantprod/apireldiaglicconvenio.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = RelDiagLicConvenioSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = RelDiagLicConvenioSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class MedidaNotaItemAPIView(APIView):
	queryset = MedidaNotaItem.objects.all()
	serializer_class = MedidaNotaItemSerializer
	template_name = 'instantprod/apimedidanotaitem.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = MedidaNotaItemSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = MedidaNotaItemSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class NotaItemAPIView(APIView):
	queryset = NotaItem.objects.all()
	serializer_class = NotaItemSerializer
	template_name = 'instantprod/apinotaitem.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = NotaItemSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = NotaItemSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class PrestadorPreferencialAPIView(APIView):
	queryset = PrestadorPreferencial.objects.all()
	serializer_class = PrestadorPreferencialSerializer
	template_name = 'instantprod/apiprestadorpreferencial.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = PrestadorPreferencialSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = PrestadorPreferencialSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class ComercialAPIView(APIView):
	queryset = Comercial.objects.all()
	serializer_class = ComercialSerializer
	template_name = 'instantprod/apicomercial.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = ComercialSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = ComercialSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class OpcaoMenuAPIView(APIView):
	queryset = OpcaoMenu.objects.all()
	serializer_class = OpcaoMenuSerializer
	template_name = 'instantprod/apiopcaomenu.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = OpcaoMenuSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = OpcaoMenuSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class TipoPercPgtoAPIView(APIView):
	queryset = TipoPercPgto.objects.all()
	serializer_class = TipoPercPgtoSerializer
	template_name = 'instantprod/apitipopercpgto.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = TipoPercPgtoSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = TipoPercPgtoSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class PgtoSinalClienteAPIView(APIView):
	queryset = PgtoSinalCliente.objects.all()
	serializer_class = PgtoSinalClienteSerializer
	template_name = 'instantprod/apipgtosinalcliente.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = PgtoSinalClienteSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = PgtoSinalClienteSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class TipoPercntDesmbAPIView(APIView):
	queryset = TipoPercntDesmb.objects.all()
	serializer_class = TipoPercntDesmbSerializer
	template_name = 'instantprod/apitipopercntdesmb.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = TipoPercntDesmbSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = TipoPercntDesmbSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class PgtoColabAPIView(APIView):
	queryset = PgtoColab.objects.all()
	serializer_class = PgtoColabSerializer
	template_name = 'instantprod/apipgtocolab.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = PgtoColabSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = PgtoColabSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class TipoEnderecamentoAPIView(APIView):
	queryset = TipoEnderecamento.objects.all()
	serializer_class = TipoEnderecamentoSerializer
	template_name = 'instantprod/apitipoenderecamento.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = TipoEnderecamentoSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = TipoEnderecamentoSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class EnderecamentoAPIView(APIView):
	queryset = Enderecamento.objects.all()
	serializer_class = EnderecamentoSerializer
	template_name = 'instantprod/apienderecamento.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = EnderecamentoSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = EnderecamentoSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class TipoObraLiterariaAPIView(APIView):
	queryset = TipoObraLiteraria.objects.all()
	serializer_class = TipoObraLiterariaSerializer
	template_name = 'instantprod/apitipoobraliteraria.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = TipoObraLiterariaSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = TipoObraLiterariaSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class ItemObraLiterariaAPIView(APIView):
	queryset = ItemObraLiteraria.objects.all()
	serializer_class = ItemObraLiterariaSerializer
	template_name = 'instantprod/apiitemobraliteraria.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = ItemObraLiterariaSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = ItemObraLiterariaSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class TipoObraCientificaAPIView(APIView):
	queryset = TipoObraCientifica.objects.all()
	serializer_class = TipoObraCientificaSerializer
	template_name = 'instantprod/apitipoobracientifica.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = TipoObraCientificaSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = TipoObraCientificaSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class ItemObraCientificaAPIView(APIView):
	queryset = ItemObraCientifica.objects.all()
	serializer_class = ItemObraCientificaSerializer
	template_name = 'instantprod/apiitemobracientifica.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = ItemObraCientificaSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = ItemObraCientificaSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class TipoPcDAPIView(APIView):
	queryset = TipoPcD.objects.all()
	serializer_class = TipoPcDSerializer
	template_name = 'instantprod/apitipopcd.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = TipoPcDSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = TipoPcDSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class TipoItemCompEqpTempoAPIView(APIView):
	queryset = TipoItemCompEqpTempo.objects.all()
	serializer_class = TipoItemCompEqpTempoSerializer
	template_name = 'instantprod/apitipoitemcompeqptempo.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = TipoItemCompEqpTempoSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = TipoItemCompEqpTempoSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class ItemCompEqpAPIView(APIView):
	queryset = ItemCompEqp.objects.all()
	serializer_class = ItemCompEqpSerializer
	template_name = 'instantprod/apiitemcompeqp.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = ItemCompEqpSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = ItemCompEqpSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class TipoAssociacaoAPIView(APIView):
	queryset = TipoAssociacao.objects.all()
	serializer_class = TipoAssociacaoSerializer
	template_name = 'instantprod/apitipoassociacao.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = TipoAssociacaoSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = TipoAssociacaoSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class AssociadoParteAPIView(APIView):
	queryset = AssociadoParte.objects.all()
	serializer_class = AssociadoParteSerializer
	template_name = 'instantprod/apiassociadoparte.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = AssociadoParteSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = AssociadoParteSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class AssociadoEmpresaAPIView(APIView):
	queryset = AssociadoEmpresa.objects.all()
	serializer_class = AssociadoEmpresaSerializer
	template_name = 'instantprod/apiassociadoempresa.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = AssociadoEmpresaSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = AssociadoEmpresaSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class AssociacaoAPIView(APIView):
	queryset = Associacao.objects.all()
	serializer_class = AssociacaoSerializer
	template_name = 'instantprod/apiassociacao.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = AssociacaoSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = AssociacaoSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class TipoFluenciaVerbAPIView(APIView):
	queryset = TipoFluenciaVerb.objects.all()
	serializer_class = TipoFluenciaVerbSerializer
	template_name = 'instantprod/apitipofluenciaverb.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = TipoFluenciaVerbSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = TipoFluenciaVerbSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class TipoPerfilGerentProjetoAPIView(APIView):
	queryset = TipoPerfilGerentProjeto.objects.all()
	serializer_class = TipoPerfilGerentProjetoSerializer
	template_name = 'instantprod/apitipoperfilgerentprojeto.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = TipoPerfilGerentProjetoSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = TipoPerfilGerentProjetoSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class ItemTipoPerfilGerProjetoAPIView(APIView):
	queryset = ItemTipoPerfilGerProjeto.objects.all()
	serializer_class = ItemTipoPerfilGerProjetoSerializer
	template_name = 'instantprod/apiitemtipoperfilgerprojeto.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = ItemTipoPerfilGerProjetoSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = ItemTipoPerfilGerProjetoSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class ItemTipoEventoAPIView(APIView):
	queryset = ItemTipoEvento.objects.all()
	serializer_class = ItemTipoEventoSerializer
	template_name = 'instantprod/apiitemtipoevento.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = ItemTipoEventoSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = ItemTipoEventoSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class TipoSistemasInformacaoAPIView(APIView):
	queryset = TipoSistemasInformacao.objects.all()
	serializer_class = TipoSistemasInformacaoSerializer
	template_name = 'instantprod/apitiposistemasinformacao.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = TipoSistemasInformacaoSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = TipoSistemasInformacaoSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class ItemSistemasInformacaoAPIView(APIView):
	queryset = ItemSistemasInformacao.objects.all()
	serializer_class = ItemSistemasInformacaoSerializer
	template_name = 'instantprod/apiitemsistemasinformacao.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = ItemSistemasInformacaoSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = ItemSistemasInformacaoSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class ItemTipoPcDAPIView(APIView):
	queryset = ItemTipoPcD.objects.all()
	serializer_class = ItemTipoPcDSerializer
	template_name = 'instantprod/apiitemtipopcd.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = ItemTipoPcDSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = ItemTipoPcDSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class TipoObraArtisticaAPIView(APIView):
	queryset = TipoObraArtistica.objects.all()
	serializer_class = TipoObraArtisticaSerializer
	template_name = 'instantprod/apitipoobraartistica.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = TipoObraArtisticaSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = TipoObraArtisticaSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class ItemObraArtisticaAPIView(APIView):
	queryset = ItemObraArtistica.objects.all()
	serializer_class = ItemObraArtisticaSerializer
	template_name = 'instantprod/apiitemobraartistica.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = ItemObraArtisticaSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = ItemObraArtisticaSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class TipoVolumeMedioVendaSemanalAPIView(APIView):
	queryset = TipoVolumeMedioVendaSemanal.objects.all()
	serializer_class = TipoVolumeMedioVendaSemanalSerializer
	template_name = 'instantprod/apitipovolumemediovendasemanal.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = TipoVolumeMedioVendaSemanalSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = TipoVolumeMedioVendaSemanalSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class TipoModuloAPIView(APIView):
	queryset = TipoModulo.objects.all()
	serializer_class = TipoModuloSerializer
	template_name = 'instantprod/apitipomodulo.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = TipoModuloSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = TipoModuloSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class PermissaoAPIView(APIView):
	queryset = Permissao.objects.all()
	serializer_class = PermissaoSerializer
	template_name = 'instantprod/apipermissao.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = PermissaoSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = PermissaoSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class TipoEstiloLocucaoAPIView(APIView):
	queryset = TipoEstiloLocucao.objects.all()
	serializer_class = TipoEstiloLocucaoSerializer
	template_name = 'instantprod/apitipoestilolocucao.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = TipoEstiloLocucaoSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = TipoEstiloLocucaoSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class ItemTipoEstiloLocucaoAPIView(APIView):
	queryset = ItemTipoEstiloLocucao.objects.all()
	serializer_class = ItemTipoEstiloLocucaoSerializer
	template_name = 'instantprod/apiitemtipoestilolocucao.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = ItemTipoEstiloLocucaoSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = ItemTipoEstiloLocucaoSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class TipoVozGeneroAPIView(APIView):
	queryset = TipoVozGenero.objects.all()
	serializer_class = TipoVozGeneroSerializer
	template_name = 'instantprod/apitipovozgenero.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = TipoVozGeneroSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = TipoVozGeneroSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class ItemTipoVozGeneroAPIView(APIView):
	queryset = ItemTipoVozGenero.objects.all()
	serializer_class = ItemTipoVozGeneroSerializer
	template_name = 'instantprod/apiitemtipovozgenero.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = ItemTipoVozGeneroSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = ItemTipoVozGeneroSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class TipoFocoLocucaoAPIView(APIView):
	queryset = TipoFocoLocucao.objects.all()
	serializer_class = TipoFocoLocucaoSerializer
	template_name = 'instantprod/apitipofocolocucao.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = TipoFocoLocucaoSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = TipoFocoLocucaoSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class ItemTipoFocoLocucaoAPIView(APIView):
	queryset = ItemTipoFocoLocucao.objects.all()
	serializer_class = ItemTipoFocoLocucaoSerializer
	template_name = 'instantprod/apiitemtipofocolocucao.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = ItemTipoFocoLocucaoSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = ItemTipoFocoLocucaoSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class TipoVozIdadeAPIView(APIView):
	queryset = TipoVozIdade.objects.all()
	serializer_class = TipoVozIdadeSerializer
	template_name = 'instantprod/apitipovozidade.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = TipoVozIdadeSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = TipoVozIdadeSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class ItemTipoVozIdadeAPIView(APIView):
	queryset = ItemTipoVozIdade.objects.all()
	serializer_class = ItemTipoVozIdadeSerializer
	template_name = 'instantprod/apiitemtipovozidade.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = ItemTipoVozIdadeSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = ItemTipoVozIdadeSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class TipoVozAmostraAPIView(APIView):
	queryset = TipoVozAmostra.objects.all()
	serializer_class = TipoVozAmostraSerializer
	template_name = 'instantprod/apitipovozamostra.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = TipoVozAmostraSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = TipoVozAmostraSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class ItemTipoVozAmostraAPIView(APIView):
	queryset = ItemTipoVozAmostra.objects.all()
	serializer_class = ItemTipoVozAmostraSerializer
	template_name = 'instantprod/apiitemtipovozamostra.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = ItemTipoVozAmostraSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = ItemTipoVozAmostraSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class AgendaAtividadeHistoricoAPIView(APIView):
	queryset = AgendaAtividadeHistorico.objects.all()
	serializer_class = AgendaAtividadeHistoricoSerializer
	template_name = 'instantprod/apiagendaatividadehistorico.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = AgendaAtividadeHistoricoSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = AgendaAtividadeHistoricoSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class HardwareAPIView(APIView):
	queryset = Hardware.objects.all()
	serializer_class = HardwareSerializer
	template_name = 'instantprod/apihardware.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = HardwareSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = HardwareSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class TipoProficCategAPIView(APIView):
	queryset = TipoProficCateg.objects.all()
	serializer_class = TipoProficCategSerializer
	template_name = 'instantprod/apitipoproficcateg.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = TipoProficCategSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = TipoProficCategSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class ParteLinguaPaisTipoProficCategAPIView(APIView):
	queryset = ParteLinguaPaisTipoProficCateg.objects.all()
	serializer_class = ParteLinguaPaisTipoProficCategSerializer
	template_name = 'instantprod/apipartelinguapaistipoproficcateg.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = ParteLinguaPaisTipoProficCategSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = ParteLinguaPaisTipoProficCategSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class ParEmpresaLinguaPaisAPIView(APIView):
	queryset = ParEmpresaLinguaPais.objects.all()
	serializer_class = ParEmpresaLinguaPaisSerializer
	template_name = 'instantprod/apiparempresalinguapais.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = ParEmpresaLinguaPaisSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = ParEmpresaLinguaPaisSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class TipoFaseLuaAPIView(APIView):
	queryset = TipoFaseLua.objects.all()
	serializer_class = TipoFaseLuaSerializer
	template_name = 'instantprod/apitipofaselua.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = TipoFaseLuaSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = TipoFaseLuaSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class TipoLingProgAPIView(APIView):
	queryset = TipoLingProg.objects.all()
	serializer_class = TipoLingProgSerializer
	template_name = 'instantprod/apitipolingprog.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = TipoLingProgSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = TipoLingProgSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class ParteTipoLingProgAPIView(APIView):
	queryset = ParteTipoLingProg.objects.all()
	serializer_class = ParteTipoLingProgSerializer
	template_name = 'instantprod/apipartetipolingprog.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = ParteTipoLingProgSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = ParteTipoLingProgSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class TipoLocacaoAPIView(APIView):
	queryset = TipoLocacao.objects.all()
	serializer_class = TipoLocacaoSerializer
	template_name = 'instantprod/apitipolocacao.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = TipoLocacaoSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = TipoLocacaoSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class RelDiagLocEquipamentoAPIView(APIView):
	queryset = RelDiagLocEquipamento.objects.all()
	serializer_class = RelDiagLocEquipamentoSerializer
	template_name = 'instantprod/apireldiaglocequipamento.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = RelDiagLocEquipamentoSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = RelDiagLocEquipamentoSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class RelDiagInterpretacaoAPIView(APIView):
	queryset = RelDiagInterpretacao.objects.all()
	serializer_class = RelDiagInterpretacaoSerializer
	template_name = 'instantprod/apireldiaginterpretacao.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = RelDiagInterpretacaoSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = RelDiagInterpretacaoSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class CertificacaoAPIView(APIView):
	queryset = Certificacao.objects.all()
	serializer_class = CertificacaoSerializer
	template_name = 'instantprod/apicertificacao.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = CertificacaoSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = CertificacaoSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class TipoRestricaoAPIView(APIView):
	queryset = TipoRestricao.objects.all()
	serializer_class = TipoRestricaoSerializer
	template_name = 'instantprod/apitiporestricao.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = TipoRestricaoSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = TipoRestricaoSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class TipoBiometriaAPIView(APIView):
	queryset = TipoBiometria.objects.all()
	serializer_class = TipoBiometriaSerializer
	template_name = 'instantprod/apitipobiometria.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = TipoBiometriaSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = TipoBiometriaSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class ListaRestricaoAPIView(APIView):
	queryset = ListaRestricao.objects.all()
	serializer_class = ListaRestricaoSerializer
	template_name = 'instantprod/apilistarestricao.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = ListaRestricaoSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = ListaRestricaoSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class BiometriaAPIView(APIView):
	queryset = Biometria.objects.all()
	serializer_class = BiometriaSerializer
	template_name = 'instantprod/apibiometria.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = BiometriaSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = BiometriaSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class LinguaPaisAPIView(APIView):
	queryset = LinguaPais.objects.all()
	serializer_class = LinguaPaisSerializer
	template_name = 'instantprod/apilinguapais.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = LinguaPaisSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = LinguaPaisSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class TipoLicOportunidadeAPIView(APIView):
	queryset = TipoLicOportunidade.objects.all()
	serializer_class = TipoLicOportunidadeSerializer
	template_name = 'instantprod/apitipolicoportunidade.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = TipoLicOportunidadeSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = TipoLicOportunidadeSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class RelDiagLicOportunidadeAPIView(APIView):
	queryset = RelDiagLicOportunidade.objects.all()
	serializer_class = RelDiagLicOportunidadeSerializer
	template_name = 'instantprod/apireldiaglicoportunidade.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = RelDiagLicOportunidadeSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = RelDiagLicOportunidadeSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class InventarioAPIView(APIView):
	queryset = Inventario.objects.all()
	serializer_class = InventarioSerializer
	template_name = 'instantprod/apiinventario.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = InventarioSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = InventarioSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class ConvenioParteEmpresaAPIView(APIView):
	queryset = ConvenioParteEmpresa.objects.all()
	serializer_class = ConvenioParteEmpresaSerializer
	template_name = 'instantprod/apiconvenioparteempresa.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = ConvenioParteEmpresaSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = ConvenioParteEmpresaSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class ConvenioItemAPIView(APIView):
	queryset = ConvenioItem.objects.all()
	serializer_class = ConvenioItemSerializer
	template_name = 'instantprod/apiconvenioitem.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = ConvenioItemSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = ConvenioItemSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class LinguaPaisEmpresaAPIView(APIView):
	queryset = LinguaPaisEmpresa.objects.all()
	serializer_class = LinguaPaisEmpresaSerializer
	template_name = 'instantprod/apilinguapaisempresa.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = LinguaPaisEmpresaSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = LinguaPaisEmpresaSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class EmpresaLinguaPaisTipoProficCategAPIView(APIView):
	queryset = EmpresaLinguaPaisTipoProficCateg.objects.all()
	serializer_class = EmpresaLinguaPaisTipoProficCategSerializer
	template_name = 'instantprod/apiempresalinguapaistipoproficcateg.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = EmpresaLinguaPaisTipoProficCategSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = EmpresaLinguaPaisTipoProficCategSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class ParEmpresaLinguaInstCertificAPIView(APIView):
	queryset = ParEmpresaLinguaInstCertific.objects.all()
	serializer_class = ParEmpresaLinguaInstCertificSerializer
	template_name = 'instantprod/apiparempresalinguainstcertific.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = ParEmpresaLinguaInstCertificSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = ParEmpresaLinguaInstCertificSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class TipoEstacAnoAPIView(APIView):
	queryset = TipoEstacAno.objects.all()
	serializer_class = TipoEstacAnoSerializer
	template_name = 'instantprod/apitipoestacano.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = TipoEstacAnoSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = TipoEstacAnoSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class TipoEstacAnoIniAPIView(APIView):
	queryset = TipoEstacAnoIni.objects.all()
	serializer_class = TipoEstacAnoIniSerializer
	template_name = 'instantprod/apitipoestacanoini.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = TipoEstacAnoIniSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = TipoEstacAnoIniSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class TipoDataComDAAPIView(APIView):
	queryset = TipoDataComDA.objects.all()
	serializer_class = TipoDataComDASerializer
	template_name = 'instantprod/apitipodatacomda.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = TipoDataComDASerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = TipoDataComDASerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class ParteTipoSuporteContAPIView(APIView):
	queryset = ParteTipoSuporteCont.objects.all()
	serializer_class = ParteTipoSuporteContSerializer
	template_name = 'instantprod/apipartetiposuportecont.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = ParteTipoSuporteContSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = ParteTipoSuporteContSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class RelDiagServAdClosedCaptionAPIView(APIView):
	queryset = RelDiagServAdClosedCaption.objects.all()
	serializer_class = RelDiagServAdClosedCaptionSerializer
	template_name = 'instantprod/apireldiagservadclosedcaption.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = RelDiagServAdClosedCaptionSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = RelDiagServAdClosedCaptionSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class RelDiagServAdDigitacaoAPIView(APIView):
	queryset = RelDiagServAdDigitacao.objects.all()
	serializer_class = RelDiagServAdDigitacaoSerializer
	template_name = 'instantprod/apireldiagservaddigitacao.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = RelDiagServAdDigitacaoSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = RelDiagServAdDigitacaoSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class ConsignadoAPIView(APIView):
	queryset = Consignado.objects.all()
	serializer_class = ConsignadoSerializer
	template_name = 'instantprod/apiconsignado.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = ConsignadoSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = ConsignadoSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class ItemCompEqpCargoAPIView(APIView):
	queryset = ItemCompEqpCargo.objects.all()
	serializer_class = ItemCompEqpCargoSerializer
	template_name = 'instantprod/apiitemcompeqpcargo.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = ItemCompEqpCargoSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = ItemCompEqpCargoSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class BancoImagemTraducaoAPIView(APIView):
	queryset = BancoImagemTraducao.objects.all()
	serializer_class = BancoImagemTraducaoSerializer
	template_name = 'instantprod/apibancoimagemtraducao.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = BancoImagemTraducaoSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = BancoImagemTraducaoSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class AuditoriaAPIView(APIView):
	queryset = Auditoria.objects.all()
	serializer_class = AuditoriaSerializer
	template_name = 'instantprod/apiauditoria.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = AuditoriaSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = AuditoriaSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class LivroTraducaoAPIView(APIView):
	queryset = LivroTraducao.objects.all()
	serializer_class = LivroTraducaoSerializer
	template_name = 'instantprod/apilivrotraducao.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = LivroTraducaoSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = LivroTraducaoSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class ItemLinguaPaisAPIView(APIView):
	queryset = ItemLinguaPais.objects.all()
	serializer_class = ItemLinguaPaisSerializer
	template_name = 'instantprod/apiitemlinguapais.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = ItemLinguaPaisSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = ItemLinguaPaisSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class ExperienciaAdminTraducaoAPIView(APIView):
	queryset = ExperienciaAdminTraducao.objects.all()
	serializer_class = ExperienciaAdminTraducaoSerializer
	template_name = 'instantprod/apiexperienciaadmintraducao.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = ExperienciaAdminTraducaoSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = ExperienciaAdminTraducaoSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class ExperienciaComercialDescritivaAPIView(APIView):
	queryset = ExperienciaComercialDescritiva.objects.all()
	serializer_class = ExperienciaComercialDescritivaSerializer
	template_name = 'instantprod/apiexperienciacomercialdescritiva.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = ExperienciaComercialDescritivaSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = ExperienciaComercialDescritivaSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class VendaAPIView(APIView):
	queryset = Venda.objects.all()
	serializer_class = VendaSerializer
	template_name = 'instantprod/apivenda.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = VendaSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = VendaSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class TipoDataAnoOrdnAPIView(APIView):
	queryset = TipoDataAnoOrdn.objects.all()
	serializer_class = TipoDataAnoOrdnSerializer
	template_name = 'instantprod/apitipodataanoordn.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = TipoDataAnoOrdnSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = TipoDataAnoOrdnSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class EventoDetalheDominioUmAPIView(APIView):
	queryset = EventoDetalheDominioUm.objects.all()
	serializer_class = EventoDetalheDominioUmSerializer
	template_name = 'instantprod/apieventodetalhedominioum.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = EventoDetalheDominioUmSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = EventoDetalheDominioUmSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class RanqueamentoCargoAPIView(APIView):
	queryset = RanqueamentoCargo.objects.all()
	serializer_class = RanqueamentoCargoSerializer
	template_name = 'instantprod/apiranqueamentocargo.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = RanqueamentoCargoSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = RanqueamentoCargoSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class FilmeTraducaoAPIView(APIView):
	queryset = FilmeTraducao.objects.all()
	serializer_class = FilmeTraducaoSerializer
	template_name = 'instantprod/apifilmetraducao.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = FilmeTraducaoSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = FilmeTraducaoSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class AssinaturaBancoArquivoAPIView(APIView):
	queryset = AssinaturaBancoArquivo.objects.all()
	serializer_class = AssinaturaBancoArquivoSerializer
	template_name = 'instantprod/apiassinaturabancoarquivo.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = AssinaturaBancoArquivoSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = AssinaturaBancoArquivoSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class TipoPergSegurAPIView(APIView):
	queryset = TipoPergSegur.objects.all()
	serializer_class = TipoPergSegurSerializer
	template_name = 'instantprod/apitipopergsegur.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = TipoPergSegurSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = TipoPergSegurSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class SegurancaAPIView(APIView):
	queryset = Seguranca.objects.all()
	serializer_class = SegurancaSerializer
	template_name = 'instantprod/apiseguranca.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = SegurancaSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = SegurancaSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class BancoArquivoTraducaoAPIView(APIView):
	queryset = BancoArquivoTraducao.objects.all()
	serializer_class = BancoArquivoTraducaoSerializer
	template_name = 'instantprod/apibancoarquivotraducao.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = BancoArquivoTraducaoSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = BancoArquivoTraducaoSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class TipoListaContatoAPIView(APIView):
	queryset = TipoListaContato.objects.all()
	serializer_class = TipoListaContatoSerializer
	template_name = 'instantprod/apitipolistacontato.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = TipoListaContatoSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = TipoListaContatoSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class ItemPermissaoAPIView(APIView):
	queryset = ItemPermissao.objects.all()
	serializer_class = ItemPermissaoSerializer
	template_name = 'instantprod/apiitempermissao.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = ItemPermissaoSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = ItemPermissaoSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class ParParteLinguaPaisAPIView(APIView):
	queryset = ParParteLinguaPais.objects.all()
	serializer_class = ParParteLinguaPaisSerializer
	template_name = 'instantprod/apiparpartelinguapais.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = ParParteLinguaPaisSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = ParParteLinguaPaisSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class TipoCalendLunarAPIView(APIView):
	queryset = TipoCalendLunar.objects.all()
	serializer_class = TipoCalendLunarSerializer
	template_name = 'instantprod/apitipocalendlunar.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = TipoCalendLunarSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = TipoCalendLunarSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class RelDiagServAdLegendagemAPIView(APIView):
	queryset = RelDiagServAdLegendagem.objects.all()
	serializer_class = RelDiagServAdLegendagemSerializer
	template_name = 'instantprod/apireldiagservadlegendagem.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = RelDiagServAdLegendagemSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = RelDiagServAdLegendagemSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class RelDiagServAdRedacaoAPIView(APIView):
	queryset = RelDiagServAdRedacao.objects.all()
	serializer_class = RelDiagServAdRedacaoSerializer
	template_name = 'instantprod/apireldiagservadredacao.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = RelDiagServAdRedacaoSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = RelDiagServAdRedacaoSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class RelDiagServAdConsulLinguisticaAPIView(APIView):
	queryset = RelDiagServAdConsulLinguistica.objects.all()
	serializer_class = RelDiagServAdConsulLinguisticaSerializer
	template_name = 'instantprod/apireldiagservadconsullinguistica.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = RelDiagServAdConsulLinguisticaSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = RelDiagServAdConsulLinguisticaSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class RelDiagServAdAuditLinguisticaAPIView(APIView):
	queryset = RelDiagServAdAuditLinguistica.objects.all()
	serializer_class = RelDiagServAdAuditLinguisticaSerializer
	template_name = 'instantprod/apireldiagservadauditlinguistica.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = RelDiagServAdAuditLinguisticaSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = RelDiagServAdAuditLinguisticaSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class RelDiagServAdDublagemAPIView(APIView):
	queryset = RelDiagServAdDublagem.objects.all()
	serializer_class = RelDiagServAdDublagemSerializer
	template_name = 'instantprod/apireldiagservaddublagem.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = RelDiagServAdDublagemSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = RelDiagServAdDublagemSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class RelDiagServAdLocucaoAPIView(APIView):
	queryset = RelDiagServAdLocucao.objects.all()
	serializer_class = RelDiagServAdLocucaoSerializer
	template_name = 'instantprod/apireldiagservadlocucao.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = RelDiagServAdLocucaoSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = RelDiagServAdLocucaoSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class CodigoPromocionalAPIView(APIView):
	queryset = CodigoPromocional.objects.all()
	serializer_class = CodigoPromocionalSerializer
	template_name = 'instantprod/apicodigopromocional.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = CodigoPromocionalSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = CodigoPromocionalSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class PlanoAPIView(APIView):
	queryset = Plano.objects.all()
	serializer_class = PlanoSerializer
	template_name = 'instantprod/apiplano.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = PlanoSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = PlanoSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class EtapaAPIView(APIView):
	queryset = Etapa.objects.all()
	serializer_class = EtapaSerializer
	template_name = 'instantprod/apietapa.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = EtapaSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = EtapaSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class ExperienciaAdministratOutraAPIView(APIView):
	queryset = ExperienciaAdministratOutra.objects.all()
	serializer_class = ExperienciaAdministratOutraSerializer
	template_name = 'instantprod/apiexperienciaadministratoutra.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = ExperienciaAdministratOutraSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = ExperienciaAdministratOutraSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class ExperienciaComercialOutraAPIView(APIView):
	queryset = ExperienciaComercialOutra.objects.all()
	serializer_class = ExperienciaComercialOutraSerializer
	template_name = 'instantprod/apiexperienciacomercialoutra.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = ExperienciaComercialOutraSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = ExperienciaComercialOutraSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class RelDiagServAdRevisaoTextoAPIView(APIView):
	queryset = RelDiagServAdRevisaoTexto.objects.all()
	serializer_class = RelDiagServAdRevisaoTextoSerializer
	template_name = 'instantprod/apireldiagservadrevisaotexto.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = RelDiagServAdRevisaoTextoSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = RelDiagServAdRevisaoTextoSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class RelDiagServAdDiagramacaoAPIView(APIView):
	queryset = RelDiagServAdDiagramacao.objects.all()
	serializer_class = RelDiagServAdDiagramacaoSerializer
	template_name = 'instantprod/apireldiagservaddiagramacao.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = RelDiagServAdDiagramacaoSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = RelDiagServAdDiagramacaoSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class RelDiagServAdTranscricaoAudioAPIView(APIView):
	queryset = RelDiagServAdTranscricaoAudio.objects.all()
	serializer_class = RelDiagServAdTranscricaoAudioSerializer
	template_name = 'instantprod/apireldiagservadtranscricaoaudio.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = RelDiagServAdTranscricaoAudioSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = RelDiagServAdTranscricaoAudioSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class RelDiagServAdAudiodescricaoAPIView(APIView):
	queryset = RelDiagServAdAudiodescricao.objects.all()
	serializer_class = RelDiagServAdAudiodescricaoSerializer
	template_name = 'instantprod/apireldiagservadaudiodescricao.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = RelDiagServAdAudiodescricaoSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = RelDiagServAdAudiodescricaoSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class DescricaoAdicionalAPIView(APIView):
	queryset = DescricaoAdicional.objects.all()
	serializer_class = DescricaoAdicionalSerializer
	template_name = 'instantprod/apidescricaoadicional.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = DescricaoAdicionalSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = DescricaoAdicionalSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class PreferenciaAdicionalEmpresaAPIView(APIView):
	queryset = PreferenciaAdicionalEmpresa.objects.all()
	serializer_class = PreferenciaAdicionalEmpresaSerializer
	template_name = 'instantprod/apipreferenciaadicionalempresa.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = PreferenciaAdicionalEmpresaSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = PreferenciaAdicionalEmpresaSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class EmpresaTraducaoAPIView(APIView):
	queryset = EmpresaTraducao.objects.all()
	serializer_class = EmpresaTraducaoSerializer
	template_name = 'instantprod/apiempresatraducao.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = EmpresaTraducaoSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = EmpresaTraducaoSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class CodigoEndPostDescAPIView(APIView):
	queryset = CodigoEndPostDesc.objects.all()
	serializer_class = CodigoEndPostDescSerializer
	template_name = 'instantprod/apicodigoendpostdesc.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = CodigoEndPostDescSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = CodigoEndPostDescSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
# View para acesso das tabelas pelo instant
class TipoFeriadoAPIView(APIView):
	queryset = TipoFeriado.objects.all()
	serializer_class = TipoFeriadoSerializer
	template_name = 'instantprod/apitipoferiado.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):

		serializer = TipoFeriadoSerializer()
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		
		serializer = TipoFeriadoSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'serializer': serializer}, status=status.HTTP_201_CREATED)
		else:
			return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    
