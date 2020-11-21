# from django.shortcuts import render, redirect
# from django.http import HttpResponse, FileResponse
# from django.template import (
# 	loader, 
# 	Context, 
# 	Template, 
# 	engines, 
# 	RequestContext
# )
# from . import models
# from . import forms
# from django.template import (
# 	loader,
# 	Context, 
# 	Template, 
# 	RequestContext
# )
# import io
# from random import randrange
# from datetime import datetime
# from django.db.models import Q
# from django.conf import settings
# from django.core.mail import(
# 	EmailMessage, 
# 	send_mail, 
# 	EmailMultiAlternatives
# )
# from django.forms import widgets 
# from django.contrib.auth.decorators import login_required
# from django.contrib.auth import authenticate, login
# from django.utils import timezone
# from django.views import View
# from django.views.generic.base import TemplateView
# from xhtml2pdf import pisa
# import os
# from django.conf import settings
# import string
# from django.views.generic import (
# 	DetailView, 
# 	ListView,
# 	CreateView,
# )
# from django.views.generic.detail import SingleObjectMixin
# from django.views.generic.edit import FormView
# from django.contrib.auth.models import User
# from django.contrib.auth.hashers import check_password
# from django.contrib.auth import password_validation as p_v
# import re


# def RecebeDadosPost(request, Nome):
# 	try:
# 		return request.POST.getlist(Nome)
# 	except:
# 		return []


# @login_required
# def Contrato(request):
# 	if request.method == 'POST':
# 		form = forms.PARTESForm(request.POST or None)
# 		if form.is_valid():
# 			instance = form.save()
# 			instance.IdUsuario = request.POST['id_ru']
# 			instance.save()
# 			return redirect ('tela_proposta')
# 	else:
# 		form = forms.PARTESForm()       
			
# 	context = {'form' : form}
# 	return render(request, 'cadastro_tela_1.html', context)

# # mudar
# class propostaView(FormView, View):

# 	template_name = "instantprod/tela_proposta.html"
# 	success_url = 'tela_2_proposta.html'

# 	def form_valid(self, form):

# 		# print ('Entrou na validação')
# 		# print (form.data, end = '\n\n')
# 		# for key in form.data:
# 		# 	if key in DadosForm.key:
# 		# 		DadosForm[key].append
# 		# print (super().form_valid(form))
		
# 		return form.data

# 	def get_context_data(self, request):
        
# 		print ('get_context_data propostaView')
# 		form1 = forms.PropostaR1Form(request.POST or None)
# 		form2 = forms.PropostaR2Form(request.POST or None)
# 		form3 = forms.PropostaR3Form(request.POST or None)
# 		form4 = forms.PropostaR4Form(request.POST or None)
# 		form5_0 = forms.PropostaR5_0Form(request.POST or None)
# 		form5_1 = forms.PropostaR5_1Form(request.POST or None)
# 		form6_0 = forms.PropostaR6_0Form(request.POST or None)
# 		form6_1 = forms.PropostaR6_1Form(request.POST or None)
# 		form7_0 = forms.PropostaR7_0Form(request.POST or None)
# 		form7_1 = forms.PropostaR7_1Form(request.POST or None)
# 		form8 = forms.PropostaR8Form(request.POST or None) 
		
# 		context = {
# 			'form1' : form1,
# 			'form2' : form2,
# 			'form3' : form3,
# 			'form4' : form4,
# 			'form5_0' : form5_0,
# 			'form5_1' : form5_1,
# 			'form6_0' : form6_0,
# 			'form6_1' : form6_1,
# 			'form7_0' : form7_0,
# 			'form7_1' : form7_1,
# 			'form8' : form8,
# 		}
        
# 		return context

# 	def save(self, JsonDados):
		
# 		try:
# 			# print ('time')
# 			# print(str(timezone.now()))
# 			Dados = dict(JsonDados)
# 			del Dados["csrfmiddlewaretoken"]
			
# 			# print ('Dados \n')
# 			# print (Dados)

# 			Bdados= models.Pedido(
# 				Cliente = 'cliente ' + str(timezone.now()),
# 				Dados = str(Dados),
# 			)
# 			Bdados.save()

# 			# print('bdados id')
# 			# print (Bdados.id)

# 			return Bdados.id
# 		except:
# 			return False

# 	def get(self, request, **kwargs):

# 		return render(
# 			request, 
# 			self.template_name, 
# 			self.get_context_data(
# 				request
# 			)
# 		)
	
# 	def post(self, request, **kwargs):

# 		DadosForm = {}
		
# 		for valor in self.get_context_data(request).values():

# 			DadosForm = self.form_valid(valor)

# 		# print('dados finais\n')
# 		DadosFinal = dict(DadosForm)
		
# 		idpedido = self.save(DadosForm)

# 		if idpedido == False:
# 			return HttpResponse('<h1><strong> Ocorreu um erro <br> Tente novamente mais tarde</strong></h1>')

# 		del DadosFinal["csrfmiddlewaretoken"]
# 		# print ('\n\nDadosForm\n')
# 		# print (DadosForm)

# 		context = {
# 			'escolhas' : DadosFinal,
# 			'idpedido' : idpedido,
# 		} 
			
# 		return render(request, 'instantprod/tela_2_proposta.html', context)
	

# class relatorioView(FormView, TemplateView):

# 	template_name = "instantprod/relatorio_0.html"

# 	def DecideRelatorio(self, vetor):

# 		r1 = [
# 			'Tradução com Revisão de Texto',
# 			'Tradução Automática com Revisão de Texto',
# 			'Tradução Juramentada',
# 			'Localização de Software, Aplicativo ou Site',
# 		]
# 		r2 = [  
# 			'Interpretação Simultânea',
# 			'Interpretação Consecutiva',
# 			'Interpretação em Acompanhamento',
# 			'Interpretação Sussurrada',
# 			'Interpretação Remota',
# 			'Dupla Interpretação',
# 			'Interpretação em Língua Brasileira de Sinais (Libras)',
# 		]
# 		r3 = [
# 			"Curso de Inglês",
# 			"Curso de Espanhol",
# 			"Curso de Francês",
# 			"Curso de Alemão",
# 			"Curso de Italiano",
# 			"Curso de Japonês",
# 			"Curso de Holandês",
# 			"Curso de Chinês",
# 			"Curso de Árabe",
# 			"Curso de Coreano",
# 			"Curso de Português",
# 			"Curso de Português para Estrangeiros",
# 			"Curso de Redação de Documentos Oficiais",
# 			"Curso de Língua Brasileira de Sinais (Libras)",
# 			"Curso de Inglês para Concursos, Enem e Vestibulares",
# 			"Curso de Espanhol para Concursos, Enem e Vestibulares",
# 			"Curso de Português para Concursos, Enem e Vestibulares",
# 			"Curso de Redação para Concursos, Enem e Vestibulares",
# 			"Curso de Inglês para Advogados",
# 			"Curso de Inglês para Forças Armadas",
# 			"Curso de Inglês para Lojistas, Comerciantes e MEI",
# 			"Curso de Inglês para Pedreiros",
# 			"Curso de Inglês para Profissionais de Enfermagem",
# 			"Curso de Inglês para Recepcionistas e Garçons",
# 			"Curso de Inglês para Transportadoras e Logística",
# 			"Curso de Inglês para Turismo e Hotelaria",
# 			"Curso de Espanhol para Advogados",
# 			"Curso de Espanhol para Lojistas, Comerciantes e MEI",
# 			"Curso de Espanhol para Turismo e Hotelaria",
# 			"Conversação em Inglês",
# 			"Conversação em Espanhol",
# 			"Intercâmbio na Argentina",
# 			"Intercâmbio nos Estados Unidos",
# 			"Inglês - Cambridge English Proficiency - CPE",
# 			"Inglês - Graduate Management Admission Test - GMAT",
# 			"Inglês - International English Language Testing System - IELTS",
# 			"Inglês - Test of English as a Foreign Language - TOEFL",
# 			"Inglês - Test of English for International Communication - TOEIC",
# 			"Espanhol - Diploma de Español como Lengua Extranjera - DELE",
# 			"Curso de Audiodescrição",
# 			"Curso de Auditoria Linguística",
# 			"Curso de Closed Caption",
# 			"Curso de Consultoria Linguística",
# 			"Curso de Diagramação",
# 			"Curso de Digitação",
# 			"Curso de Dublagem para Atores",
# 			"Curso de Edição de Áudio Digital",
# 			"Curso de Estenotipia",
# 			"Curso de Ferramentas de Apoio a Tradução",
# 			"Curso de Legendagem",
# 			"Curso de Locução",
# 			"Curso de Oratória",
# 			"Curso de Transcrição de Áudio",
# 		]

# 		r4 = [
# 			'Franqueamento Home-Based',
# 			'Franqueamento Escola de Idiomas',
# 			'Franqueamento Escritório de Tradução e Interpretação',
# 		]

# 		r5 = [ 
# 			'Audiodescrição',
# 			'Auditoria Linguística',
# 			'Closed Caption',
# 			'Consultoria Linguística',
# 			'Diagramação',
# 			'Digitação',
# 			'Dublagem',
# 			'Legendagem',
# 			'Locução',
# 			'Redação',
# 			'Revisão de Texto',
# 			'Transcrição de Áudio',
# 			'Transcrição para Braille com Revisão de Texto',
# 		]

# 		for i in r1:
# 			if i == vetor:
# 				return 'instantprod/Relatorio.html'
# 		for i in r2:
# 			if i == vetor:
# 				return 'instantprod/Relatorio_1.html'
# 		for i in r3:
# 			if i == vetor:
# 				return 'instantprod/Relatorio_2.html'
# 		for i in r4:
# 			if i == vetor:
# 				return 'instantprod/Relatorio_3.html'
# 		for i in r5:
# 			if i == vetor:
# 				return 'instantprod/Relatorio_4.html'
			
# 	def form_valid(self, form):
# 		try:
# 			# print ('Entrou na validação')
# 			# print (form.data, end = '\n\n')
# 			form.save()		
# 			return True
# 		except:
# 			return False
		
# 	def get_context_data(self, request, kwargs):
        
# 		Relatorio = self.DecideRelatorio(kwargs['relatorio_tipo'])

# 		if Relatorio == 'instantprod/Relatorio.html':
			
# 			form = forms.RelatoriodeDiagnosticoForm(request.POST or None)
# 		elif Relatorio == 'instantprod/Relatorio_1.html':

# 			form = forms.RelatoriodeDiagnosticoInterpretaForm(request.POST or None)
# 		elif Relatorio == 'instantprod/Relatorio_2.html':

# 			form = forms.RelatoriodeDiagnosticoCursosForm(request.POST or None)
# 		elif Relatorio == 'instantprod/Relatorio_3.html':

# 			form = forms.RelatoriodeDiagnosticoFranquiasForm(request.POST or None)
# 		elif Relatorio == 'instantprod/Relatorio_4.html':

# 			form = forms.RelatoriodeDiagnosticoServiForm(request.POST or None)
# 		else:
# 			form = {}
		
# 		context = {
# 			'form' : form,
# 			'idpedido' : kwargs['idpedido'],
# 			'relatorio_tipo' : kwargs['relatorio_tipo'],
# 			'relatorio_pg' : Relatorio,
# 		}

# 		print ('get_context_data')
# 		print (context)

# 		return context
	
# 	def get(self, request, **kwargs):

# 		print (kwargs)
		
# 		return render(
# 			request,
# 			self.template_name,
# 			self.get_context_data(
# 				request,
# 				kwargs
# 			)
# 		)
		
# 	def post(self, request, **kwargs):

# 		print (kwargs)
# 		Contexto =  self.get_context_data(request, kwargs)

# 		CheckForm = self.form_valid(Contexto['form'])

# 		if CheckForm == False:
# 		 	return HttpResponse('<h1><strong> Ocorreu um erro <br> Tente novamente mais tarde</strong></h1>')

# 		return HttpResponse("<h5><strong>Relatorio Salvo</strong></h5>")


# class salvamentoView(CreateView):
# 	model = User
# 	fields = (
# 		'username',
# 		'password',
# 		'email',
# 		'first_name',
# 		'last_name',
# 	)
		
# 	template_name = "instantprod/NovoUsuarioLogin.html"
# 	success_url = 'tela_proposta'
# 	cadastro_url = 'Cadastro'

# 	def form_valid(self, form):

# 		# print ('Entrou na validação')
# 		form.save()
# 		return form.data

# 	def get_context_data(self, request, dados):
        
# 		print ('get_context_data salvamentoView')
# 		form = forms.UsuarioLogin(request.POST or None)
# 		print('form')
# 		# print(form)
# 		formCliente = forms.PropostaClienteForm(request.POST or None)
# 		print('formCliente')
# 		# print(formCliente)

		
# 		if dados['Tipo'] == 'inscreva-se':
# 			context = {
# 				'form' : form,
# 				'formCliente' : formCliente,
# 			}
# 		else:
		
# 			context = {
# 				'form' : form,
# 				'formCliente' : formCliente,
# 				'idpedido': dados['idpedido']
# 			}
        
# 		return context

# 	def save(self, Dados):

# 		print(Dados)

# 		try:

# 			del Dados["csrfmiddlewaretoken"]
# 			del Dados["id_relatorio"]
			
# 			Usuario = User.objects.create_user(
# 				Dados["username"][0],
# 				Dados["email"][0],
# 				Dados["password"][0],
# 			)
# 			Usuario.last_name = Dados["last_name"][0]
# 			Usuario.first_name = Dados["first_name"][0]
# 			Usuario.save()
	
# 			return('funcionou')
		
# 		except:
# 			return False

# 	def email(self, Dados):

# 		try:
# 			# Dados["email"][0],
				
# 			subject = 'Email de Teste'
# 			email_from = settings.EMAIL_HOST_USER
# 			print('enviando email')
# 			# send_mail( 
# 			# 	subject, 
# 			# 	message, 
# 			# 	email_from, 
# 			# 	recipient_list,
# 			# 	fail_silently=False,
# 			# )
# 			to = ['programa01@simoes.trd.br','programa02@simoes.trd.br']
# 			text_content = 'Bem vindo ao Instant.'
# 			html_content = '<p>Bem vindo ao Instant <strong>{last_name}</strong>.</p><h1><strong>INSERIR LINK DE CONFIRMAÇÃO</strong></h1>'
# 			html_content = html_content.format(last_name = Dados["last_name"][0])
# 			msg = EmailMultiAlternatives(subject, text_content, email_from, to)
# 			msg.attach_alternative(html_content, "text/html")
# 			msg.send()
# 			print('email enviado')
# 			return 0
# 		except:
# 			return 1

# 	def get(self, request, **kwargs):

# 		print (kwargs)
# 		print('get')
# 		# print ('sessions\n')
# 		# print(request.session.values())
		
# 		try:
# 			return render(
# 				request, 
# 				self.template_name, 
# 				self.get_context_data(
# 					request, 
# 					kwargs
# 				)
# 			)
# 		except:
# 			return HttpResponse('<h1>Tente novamente mais tarde</h1>')

# 	def post(self, request, **kwargs):
# 		print('post')
# 		try:
# 			print('kwargs')
# 			print(kwargs)

# 			Contexto = self.get_context_data(
# 				request,
# 				kwargs
# 			)

# 			print (Contexto)

# 			DadosPagina = []

# 			try:
# 				DadosPagina.append(
# 					self.form_valid(
# 						Contexto['formCliente']
# 					)
# 				)
# 			except:
# 				try:
# 					DadosPagina.append(
# 						self.form_valid(
# 							Contexto['form']
# 						)
# 					)
# 				except:
# 					print ('erro no except')
				
			
# 			DadosPagina = dict(DadosPagina[0])
# 			print ('DadosPagina')
# 			print (DadosPagina)

# 			try:

# 				user = authenticate(
# 					request, 
# 					username = DadosPagina['username'][0], 
# 					password = DadosPagina['password'][0]
# 				)
				
# 				print (user)
# 				if user == None:
# 					self.save(DadosPagina)
# 					user = authenticate(
# 						request, 
# 						username = DadosPagina['username'][0], 
# 						password = DadosPagina['password'][0]
# 					)

# 					self.email(DadosPagina)

# 					print ('user')
# 					print (user)

# 					if user is not None:
# 						login(request, user)

# 						instance = Contexto['formCliente'].save()
# 						instance.Nome = DadosPagina['username'][0]
# 						instance.IdRelatorio = kwargs['idpedido']
# 						instance.IdUsuario = str(user.id)
# 						instance.save()
# 						return redirect(self.cadastro_url)
# 					else:
# 						return HttpResponse('<h1>Tente novamente mais tarde</h1>')
					
# 				else:
# 					if user is not None:
# 						login(request, user)

# 						instance = Contexto['formCliente'].save()
# 						instance.Nome = DadosPagina['username'][0]
# 						instance.IdRelatorio = kwargs['idpedido']
# 						instance.IdUsuario = str(user.id)
# 						instance.save()
# 						return redirect(self.success_url)
# 					else:
# 						return HttpResponse('<h1>Tente novamente mais tarde</h1>')
# 			except:
# 				print('estou no if de teste online')
# 				return HttpResponse('<h1>Tente novamente mais tarde</h1>')
					
# 		except:
# 			return HttpResponse('<h1>Tente novamente mais tarde</h1>')


# class clausulasView(TemplateView):
	
# 	template_name = "instantprod/cadastro_clausulas.html"
# 	success_url = 'teste_clausulas'

# 	def form_valid(self, form):
		
# 		form.save()

# 	def get_context_data(self, request):
        
# 		form = forms.ClausulasForm(request.POST or None)
		
# 		context = {
# 			'form' : form,
# 		}
        
# 		return context

# 	def get(self, request, **kwargs):

# 		return render(
# 			request, 
# 			self.template_name, 
# 			self.get_context_data(
# 				request
# 			)
# 		)
	
# 	def post(self, request, **kwargs):
		
# 		Contexto = self.get_context_data(
# 			request
# 		)

# 		self.form_valid(Contexto['form'])
		
# 		return redirect(self.success_url)


# class contratoView(TemplateView):
	
# 	template_name = "instantprod/cria_contrato.html"
# 	success_url = 'teste_documento'

# 	def form_valid(self, form):

# 		Dados = dict(form.data)

# 		# 'TipoDocumento': TipoDocumento,
# 		# 	'Titulo': Titulo,
# 		# 	'SubTituloServico': SubTituloServico,
# 		# 	'SubTituloCargo': SubTituloCargo,
# 		# 	'SubTipoDocumento': SubTipoDocumento,

# 		del  Dados['csrfmiddlewaretoken']

# 		if not 'TipoDocumento' in Dados.keys():
# 			Dados['TipoDocumento'] = ['']

# 		if not 'Titulo' in Dados.keys():
# 			Dados['Titulo'] = ['']
	
# 		if not 'SubTituloServico' in Dados.keys():
# 			Dados['SubTituloServico'] = ['']
			
# 		if not 'SubTituloCargo' in Dados.keys():
# 			Dados['SubTituloCargo'] = ['']
			
# 		if not 'SubTipoDocumento' in Dados.keys():
# 			Dados['SubTipoDocumento'] = ['']
		
		
# 		print ('Dados')	
# 		print (Dados)	
		
# 		return Dados

# 	def get_context_data(self, request):
        
# 		form = forms.CriaContratoForm(request.POST or None)
		
# 		context = {
# 			'form' : form,
# 		}
        
# 		return context

# 	def get(self, request, **kwargs):

# 		return render(
# 			request, 
# 			self.template_name, 
# 			self.get_context_data(
# 				request
# 			)
# 		)
	
# 	def post(self, request, **kwargs):
		
# 		Contexto = self.get_context_data(
# 			request
# 		)

# 		Dados = self.form_valid(Contexto['form'])

# 		LinguaPais = []
# 		if len(Dados['Pais']) >= len(Dados['LinguaClausula']):
# 			for i in range(len(Dados['Pais'])):
# 				try:
# 					LinguaPais.append(
# 						[
# 							Dados['LinguaClausula'][i],
# 							Dados['Pais'][i]
# 						]
# 					)
# 				except:
# 					pass
				
# 		else:
# 			for i in range(len(Dados['LinguaClausula'])):
# 				try:
# 					LinguaPais.append(
# 						[
# 							Dados['LinguaClausula'][i],
# 							Dados['Pais'][i]
# 						]
# 					)
# 				except:
# 					pass
				

# 		Dados['LinguaPais'] = LinguaPais


# 		print ('contexto')
# 		print(Dados)
		
# 		BuscaConteudo = Contexto['form'].BuscaConteudoClausulas(Dados)
# 		print ('conteudo final \n \n \n \n')
# 		print (BuscaConteudo)
# 		try:
# 			context = {
# 				'form' : Contexto['form'],
# 				'ContratosListas' : BuscaConteudo,
# 			}
# 		except:
# 			print ('lista vazia')
# 			context = {
# 				'form' : Contexto['form'],
# 			}
			
# 		return render(request, self.template_name, context) 
	

# @login_required
# def VisualizadordeClausulas(request):

# 	if request.method == 'GET':
	  
# 		form = forms.ClausulasForm()
# 		Conteudo = form.BuscaClausulas() 
# 		print ('busca', Conteudo[0].SubTituloCargo)
# 		context = {
# 			'Clausulas' : Conteudo,
# 		}
# 		template = loader.get_template('montador_clausulas.html')
# 		html = template.render(context)

# 		context = {
# 			'html' : html,
# 		}
# 		return render(request, 'visualizador_clausulas.html', context)
# 		# return HttpResponse(template.render(context)) 
# 	else:
# 		return HttpResponse('POST')

# #  mudar
# class geradorDocumento(TemplateView):

# 	Banco = models.Clausula
	
# 	def get(self, request, **kwargs):

# 		Documento = self.Banco.CriaDocumento(self.Banco, kwargs)

# 		return HttpResponse (Documento)


# class downloadDocumentos(TemplateView):

# 	Banco = models.Clausula
# 	template_name = "contrato_download.html"

# 	def link_callback(self, uri, rel):
# 		"""
# 		Convert HTML URIs to absolute system paths so xhtml2pdf can access those
# 		resources 
# 		"""
# 		# print(uri)
# 		# use short variable names
# 		sUrl = settings.STATIC_URL      # Typically /static/
# 		sRoot = settings.STATIC_ROOT    # Typically /home/userX/project_static/
# 		mUrl = settings.MEDIA_URL       # Typically /static/media/
# 		mRoot = settings.MEDIA_ROOT     # Typically /home/userX/project_static/media/
# 		# print(rel)
# 		# convert URIs to absolute system paths
# 		# print(uri, sUrl, sRoot)
# 		if uri.startswith(sUrl):
# 			# print ('no if 1')
# 			path = os.path.join(sRoot, uri.replace(sUrl, ""))
# 			# print ('path')
# 			if not os.path.isfile(path):# make sure that file exists
# 				raise Exception(
# 					'media URI must start with %s or %s' % (sUrl, mUrl)
# 				)
# 			# print (path)
# 			return path
# 		elif uri.startswith(mUrl):
# 			# print ('no if 2')
# 			path = os.path.join(mRoot, uri.replace(mUrl, ""))
# 			if not os.path.isfile(path):# make sure that file exists
# 				raise Exception(
# 					'media URI must start with %s or %s' % (sUrl, mUrl)
# 				)
# 			# print (path)
# 			return path
# 		else:
# 			# print ('no else')
# 			return uri  # handle absolute uri (ie: http://some.tld/foo.png)

# 	def GeradorPdf(self, Documento, IdContratante, IdContratado, NomeArquivo):
# 		buffer = io.BytesIO() 
# 		# print (IdContratante, IdContratado)
# 		Contratante = models.Parte.objects.filter(id = IdContratante).values()
# 		Contratado = models.Parte.objects.filter(id = IdContratado).values()
		
# 		try:
# 			Contratante = Contratante[0]
# 		except:
# 			return 'Contratante Invalido'
		
# 		try:
# 			Contratado = Contratado[0]
# 		except:
# 			return 'Contratado Invalido'

# 		# proposta = Proposta.objects.filter(IdUsuario = iD).order_by('-DataCadastro').values()[0]
# 		# print ('Partes')
# 		# print (Contratante)
# 		# print (Contratado)
# 		# print('Proposta')
# 		# print(proposta)
# 		# adicionar um metodo generico para ler o pedido.
# 		# adicionar metodo de erro caso cadastro esteja vazio
	
# 		context = {
# 			'Contratante': Contratante,
# 			'Contratado': Contratado
# 		}
		
# 		Corpo = models.ModeloDocumento.objects.get(id = 9)
# 		# print (Corpo)
# 		EstruturaPdf = str(Corpo).replace('{Conteudo}', Documento)
# 		# django_engine = engines['django']
# 		# template = django_engine.from_string(EstruturaPdf)
# 		template = Template(EstruturaPdf)
# 		context = Context(context)
# 		html = template.render(context)

# 		# print (html)
# 		print('criando pdf')
# 		pisaStatus = pisa.CreatePDF(html, dest=buffer, link_callback= self.link_callback)
# 		print (pisaStatus)
# 		print('pdf criado')
# 		# Bdados= ArQ(arq = buffer.getvalue(), NomePdf = NomeArquivo, IdUsuario = iD)
# 		# Bdados.save()

# 		return buffer.getvalue()

# 	def get(self, request, **kwargs):

# 		print (kwargs)
# 		Documento = self.Banco.CriaDocumento(self.Banco, kwargs)
# 		print ('Partes Buscadas ')
# 		print (kwargs['Contratante'])
# 		print (kwargs['Contratado'])

# 		if kwargs['Contratante'] == '0' or kwargs['Contratante'] == 'Contratante':
# 			return HttpResponse('Contratante Invalido')
# 		elif kwargs['Contratado'] == '0' or kwargs['Contratado'] == 'Contratado':
# 			return HttpResponse('Contratado Invalido')
# 		else:
# 			nome = 'Arquivo' + kwargs['Contratante']
# 			buffer = self.GeradorPdf( 
# 				Documento, 
# 				kwargs['Contratante'],
# 				kwargs['Contratado'],
# 				nome
# 			)
# 			# return HttpResponse (Documento)
# 			response = HttpResponse(buffer, content_type='application/pdf')
# 			response['Content-Disposition'] = 'attachment; filename="arquivo.pdf"' 
# 			return response


# # Todos os ajax devem estar abaixo

# class ajaxPais(View):

# 	Banco = models.LinguaPais.objects.all()
# 	Dados = models.Lingua.objects.all()

# 	def get(self, request, *args, **kwargs):

# 		print ('args')
# 		print (args)
# 		print ('kwargs')
# 		print (kwargs)
# 		if (kwargs['Pais'] == 'null'):
# 			kwargs['Pais'] = None

# 		DadosLinguaPais = self.Banco.filter(Pais = kwargs['Pais']).values()
# 		print('linguapais')
# 		print (DadosLinguaPais)
# 		DadosLingua = []
# 		TemplateString = '<option value="{id}">{nome}</option>'
# 		TemplateVazio = '<option value="" selected="">---------</option>'
		

# 		for Conteudo in DadosLinguaPais:
# 			try:
# 				Lingua = self.Dados.get(id = Conteudo['Lingua_id'])
# 				DadosLingua.append(
# 					TemplateString.format(
# 						id = Conteudo['Lingua_id'], 
# 						nome = str(
# 							Lingua
# 						)
# 					)
# 				)
# 				print (DadosLingua)
# 			except:
# 				DadosLingua.append(TemplateVazio)
		
# 		sep = '\n'
# 		TextoFinal = sep.join(DadosLingua)

# 		return HttpResponse (TextoFinal)
		

# class ajaxLingua(View):

# 	Banco = models.LinguaPais.objects.all()
# 	Dados = models.Pais.objects.all()

# 	def get(self, request, *args, **kwargs):

# 		print ('args')
# 		print (args)
# 		print ('kwargs')
# 		print (kwargs)
# 		if (kwargs['Lingua'] == 'null'):
# 			kwargs['Lingua'] = None

# 		DadosLinguaPais = self.Banco.filter(Lingua = kwargs['Lingua']).values()
# 		print('linguapais')
# 		print (DadosLinguaPais)
# 		DadosPais = []
# 		TemplateString = '<option value="{id}">{nome}</option>'
# 		TemplateVazio = '<option value="" selected="">---------</option>'
# 		for Conteudo in DadosLinguaPais:
# 			try:
# 				Pais = self.Dados.get(id = Conteudo['Pais_id'])
# 				DadosPais.append(
# 					TemplateString.format(
# 						id = Conteudo['Pais_id'], 
# 						nome = str(
# 							Pais
# 						)
# 					)
# 				)
# 				print (DadosPais)	
# 			except:
# 				DadosPais.append(TemplateVazio)

		
# 		sep = '\n'
# 		TextoFinal = sep.join(DadosPais)

# 		return HttpResponse (TextoFinal)


# class ajaxParte(View):

# 	# Banco = models.LinguaPais.objects.all()
# 	Banco = models.Parte.objects.all()

# 	def get(self, request, *args, **kwargs):

# 		print ('args')
# 		print (args)
# 		print ('kwargs')
# 		print (kwargs)
# 		if (kwargs['Parte'] == 'null'):
# 			kwargs['Parte'] = None
		
# 		try:
# 			DadosParte = self.Banco.filter(NomeCompleto = kwargs['Parte']).values()[0]
# 		except:
# 			DadosParte = {'id': 0}

		
# 		print (DadosParte)

# 		return HttpResponse (DadosParte['id'])


# class ajaxLogin(View):

# 	def conferecpf(self, username):
# 		try:
# 			confere = User.objects.filter(username = username).exists()
# 			print(confere)
# 			if confere == True:
# 				return 0
# 			else:
# 				return 1
# 		except:
# 			return 1
	
# 	def conferesenha(self, username, password):
# 		try:
# 			print ('comecou a senha')
# 			usuario = User.objects.filter(username = username).values()[0]
# 			print(usuario['password'])

# 			confere = check_password(password, usuario['password'])
# 			print(confere)

# 			if confere == True:
# 				return 0
# 			else:
# 				return 2
# 		except:
# 			return 2

# 	def get(self, request, *args, **kwargs):

# 		print ('args')
# 		print (args)
# 		print ('kwargs')
# 		print (kwargs)

# 		print (request.GET)
		
# 		try:
# 			confere = User.objects.filter(username = kwargs['username']).exists()
# 			print(confere)
# 			if confere == True:
# 				return 0
# 			else:
# 				return 2
# 		except:
# 			return 2

# 	def post(self, request, *args, **kwargs):

# 		print ('args')
# 		print (args)
# 		print ('kwargs')
# 		print (kwargs)

# 		print (request.POST)
# 		dados = dict(request.POST)

# 		ValidadorSenha = self.conferesenha(dados['username'][0], dados['password'][0])
# 		ValidadorCpf = self.conferecpf(dados['username'][0])

# 		# criar logica de validação 

# 		return HttpResponse(ValidadorSenha + ValidadorCpf)


# class ajaxInscrevase(View):

# 	def validadigito(self, digitos):
# 		SomaDigito = 0
# 		Multipli = len(digitos) + 1
# 		print ('Multiplicador ', Multipli)
# 		print ('Digitos ', digitos)

# 		for numero in digitos:
# 			SomaDigito = SomaDigito + (numero * Multipli)
								
# 			print('Soma \n', SomaDigito)
# 			print('Multiplicador \n', Multipli)
			
# 			Multipli = Multipli - 1

# 		resto = (SomaDigito * 10) % (11)

# 		if resto == 10:
# 			return 0
# 		else:
# 			return resto

# 	def validacpf(self, username):
# 		try:
# 			print ('começou a validar o cpf')
# 			cpf = []
# 			for simbolo in username:
# 				try:
# 					cpf.append(int(simbolo))
# 					print('simbolo \n', simbolo)
# 				except:
# 					print('erro no simbolo \n', simbolo)

# 			if (
# 				len(cpf) == 11 and 
# 				cpf != [0,0,0,0,0,0,0,0,0,0,0] and 
# 				cpf != [1,1,1,1,1,1,1,1,1,1,1] and 
# 				cpf != [2,2,2,2,2,2,2,2,2,2,2] and 
# 				cpf != [3,3,3,3,3,3,3,3,3,3,3] and 
# 				cpf != [4,4,4,4,4,4,4,4,4,4,4] and
# 				cpf != [5,5,5,5,5,5,5,5,5,5,5] and 
# 				cpf != [6,6,6,6,6,6,6,6,6,6,6] and 
# 				cpf != [7,7,7,7,7,7,7,7,7,7,7] and 
# 				cpf != [8,8,8,8,8,8,8,8,8,8,8] and 
# 				cpf != [9,9,9,9,9,9,9,9,9,9,9]
# 			):

# 				print(cpf[0:9])
# 				print(cpf[0:10])
# 				print(cpf[9])
# 				print(cpf[10])

# 				resto = self.validadigito(cpf[0:9])
# 				print ('resto \n', resto)
# 				if resto != cpf[9]:
# 					return 1
# 				else:
# 					resto = self.validadigito(cpf[0:10])
# 					print ('resto \n', resto)
# 					if resto != cpf[10]:
# 						return 1
# 					else:
# 						return 0
# 			else:
# 				return 1
# 		except:
# 			return 1
			
# 	def validasenha(self, dados):
# 		try:

# 			del dados['csrfmiddlewaretoken']
# 			password = dados['password'][0]
# 			del dados['password']
			
# 			# SimilarLast = re.match(dados['last_name'][0],password)
# 			# SimilarFirst = re.match(dados['first_name'][0],password)
# 			# SimilarUsername = re.match(dados['username'][0],password)
# 			# SimilarEmail = re.match(dados['email'][0],password)
# 			# print ('senha')
# 			# print(len(password))
# 			SimilarPass = len(password)
			
# 			# print(re.match(dados['last_name'][0],password))
# 			# print(re.match(dados['first_name'][0],password))
# 			# print(re.match(dados['username'][0],password))
# 			# print(re.match(dados['email'][0],password))
			
# 			# if not SimilarLast:
# 			# 	return 1
			
# 			# if not SimilarUsername:
# 			# 	return 1
			
# 			# if not SimilarEmail:
# 			# 	return 1
			
# 			# if not SimilarFirst:
# 			# 	return 1
			
# 			if SimilarPass < 6:
# 				return 1

# 			return 0
# 		except:	
# 			return 1
	
# 	def email(self, request):

# 		try:
# 			subject = 'Email de Teste'
# 			message = 'Teste do envio de email pelo gmail'
# 			email_from = settings.EMAIL_HOST_USER
# 			recipient_list = ['programa01@simoes.trd.br',]
# 			print('enviando email')
# 			# send_mail( 
# 			# 	subject, 
# 			# 	message, 
# 			# 	email_from, 
# 			# 	recipient_list,
# 			# 	fail_silently=False,
# 			# )
# 			subject, from_email, to = 'hello', email_from, 'programa01@simoes.trd.br'
# 			text_content = 'This is an important message.'
# 			html_content = '<p>This is an <strong>important</strong> message.</p>'
# 			msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
# 			msg.attach_alternative(html_content, "text/html")
# 			msg.send()
# 			print('email enviado')
# 			return 0

# 		except:
# 			return 1

# 	def repetido(self, dados):
# 		try:
# 			confere = User.objects.filter(username = dados['username']).exists()
# 			print(confere)
# 			if confere == True:
# 				return 0
# 			else:
# 				return 1
# 		except:
# 			return 1

# 	def get(self, request, *args, **kwargs):

# 		print ('args')
# 		print (args)
# 		print ('kwargs')
# 		print (kwargs)
# 		print (request.GET)
		
# 		try:
# 			confere = User.objects.filter(username = kwargs['username']).exists()
# 			print(confere)
# 			if confere == True:
# 				return 0
# 			else:
# 				return 2
# 		except:
# 			return 2

# 	def post(self, request, *args, **kwargs):

# 		print ('args')
# 		print (args)
# 		print ('kwargs')
# 		print (kwargs)

# 		print (request.POST)
# 		dados = dict(request.POST)

# 		print(dados)
# 		if kwargs['tipo'] == 'email':
# 			Valido = self.email(request)
# 			return HttpResponse(Valido)
		
# 		elif kwargs['tipo'] == 'username':
# 			Valido = self.validacpf(dados['username'][0])
# 			return HttpResponse(Valido)

# 		elif kwargs['tipo'] == 'password':
# 			Valido = self.validasenha(dados)
# 			return HttpResponse(Valido)

	
# 		# ValidadorSenha = self.conferesenha(dados['username'][0], dados['password'][0])
		
# 		# criar logica de validação


# class ajaxVazio(View):
	
# 	Mensagem = '<strong>Escolha uma Opção!</strong> Para continuar escolha pelo menos uma opção.'
# 	Alerta = '''		<div class="alert alert-warning alert-dismissible fade show" role="alert">
# 		{mensagem}
# 		<button type="button" class="close" data-dismiss="alert" aria-label="Close">
# 			<span aria-hidden="true">&times;</span>
# 		</button>
# 		</div>'''
	
# 	def get(self, request, *args, **kwargs):
# 		return HttpResponse (self.Alerta.format(mensagem = self.Mensagem))
