from django import forms
from django.forms import ModelForm
from django.template import (
	loader, 
	Context, 
	Template, 
	engines, 
	RequestContext,
)
import time
from . import var
from django.utils import timezone
from django.contrib.auth.models import User
import string
from . import models
from django.db.models import Q


def AjusteVetor(parametro = models.Dados.objects.all() ):
	# print (parametro)
	catserv = []
	tp = []
	r = []
	tr = []
	# print (len(parametro), 'Tamanho do parametro')
	
	for i in parametro:
		catserv.append(i)

	# print(catserv, 'servi')
	
	for n in range(len(catserv)):
		# print(n)
		# print (catserv[n])
		r.append(models.Item.objects.all().filter(Categoria = catserv[n]))
		# print (r)
		tc = []
		te = []
		for i in r[n] :
			#print (i)
			te.append(i) 
			tc.append((i,i))
			# print (tc)
			# print (te)
		tp.append(tuple(tc))
		tr.append(te)

	return (tp, tr, catserv)


class PARTESForm(forms.Form):

	NomeCompleto = forms.CharField(
		widget = forms.TextInput(
			attrs={
				'class' : 'form-control', 
				'placeholder' : ''
			}
		),
		label = 'Nome Completo'
	)

	Cpf = forms.CharField(
		widget = forms.TextInput(
			attrs={
				'class' : 'form-control', 
				'placeholder' : ''
			}
		),
		label = 'CPF'
	)

	DataNascimento = forms.CharField(
		widget=forms.TextInput(
			attrs={
				'class' : 'AniIn form-control', 
				'placeholder' : '',
				'autocomplete' : 'off'
			}
		),
		label = 'Data de Nascimento'
	)

	Celular = forms.CharField(
		widget = forms.TextInput(
			attrs={
				'class' : 'form-control', 
				'placeholder' : '0XX XXXXX-XXXX',
				'type':'tel',
				'pattern':'[0-9]{3} [0-9]{5}-[0-9]{4}'
			}
		),
		label = 'Celular'
	)

	TelefoneFixo = forms.CharField(
		widget = forms.TextInput(
			attrs={
				'class' : 'form-control', 
				'placeholder' : '0XX XXXX-XXXX',
				'type':'tel',
				'pattern':'[0-9]{3} [0-9]{4}-[0-9]{4}'
			}
		),
		label = 'Telefone Fixo'
	)

	Ramal = forms.CharField(
		widget = forms.TextInput(
			attrs={
				'class' : 'form-control', 
				'placeholder' : 'XXXX',
				'type':'tel',
				'pattern':'[0-9]{4}'
			}
		),
		label = 'Ramal'
	)
	
	Email = forms.EmailField(
		widget = forms.EmailInput(
			attrs={
				'class' : 'form-control', 
				'placeholder' : ''
			}
		),
		label = 'Email Secundário'
	)

	Cep = forms.CharField(
		widget = forms.TextInput(
			attrs={
				'class' : 'form-control', 
				'placeholder' : ''
			}
		),
		label = 'CEP'
	)

	EnderecoTipo = forms.CharField(
		widget = forms.TextInput(
			attrs={
				'class' : 'form-control', 
				'placeholder' : ''
			}
		),
		label = 'Tipo de Endereço '
	)

	EnderecoNome = forms.CharField(
		widget = forms.TextInput(
			attrs={
				'class' : 'form-control', 
				'placeholder' : ''
			}
		),
		label = 'Endereço ',
	)
	
	EnderecoNumero = forms.IntegerField(
		widget = forms.NumberInput(
			attrs={
				'class' : 'form-control', 
				'placeholder' : ''
			}
		),
		label = 'Número'
		
	)

	EnderecoComplemento = forms.CharField(
		widget = forms.TextInput(
			attrs={
				'class' : 'form-control',
				'placeholder' : ''
			}
		),
		label = 'Complemento'
	)

	EnderecoBairro = forms.CharField(
		widget = forms.TextInput(
			attrs={
				'class' : 'form-control', 
				'placeholder' : ''
			}
		),
		label = 'Bairro'
	)

	EnderecoCidade = forms.CharField(
		widget = forms.TextInput(
			attrs={
				'class' : 'form-control', 
				'placeholder' : ''
			}
		),
		label = 'Cidade'
	)

	Uf = forms.CharField(
		widget = forms.TextInput(
			attrs={
				'class' : 'form-control', 
				'placeholder' : ''
			}
		),
		label = 'UF'
	)

	Pais = forms.CharField(
		widget = forms.TextInput(
			attrs={
				'class' : 'form-control', 
				'placeholder' : ''
			}
		),
		label = 'País',
	)

	TipoPessoa = forms.CharField(
		widget = forms.TextInput(
			attrs={
				'class' : 'form-control', 
				'placeholder' : ''
			}
		),
		label = 'a (Fisica, Juridica)',
	)Tipo Pesso

	TipoDireito = forms.CharField(
		widget = forms.TextInput(
			attrs={
				'class' : 'form-control', 
				'placeholder' : ''
			}
		),
		label = 'Tipo Direito (Privado, Publico...)',
	)

	NomeEmpresarial = forms.CharField(
		label = 'Nome Empresarial',
		widget = forms.TextInput(
			attrs={
				'class' : 'form-control', 
				'placeholder' : ''
			}
		)
	)


	Cnpj = forms.CharField(
		widget = forms.TextInput(
			attrs={
				'class' : 'form-control', 
				'placeholder' : ''
			}
		),
		label = 'CNPJ',
	)

	Rg = forms.CharField(
		widget = forms.TextInput(
			attrs={
				'class' : 'form-control', 
				'placeholder' : ''
			}
		),
		label = 'RG'
	)


	OrgaoEmissor = forms.CharField(
		widget = forms.TextInput(
			attrs={
				'class' : 'form-control', 
				'placeholder' : ''
			}
		),
		label = 'Orgão Emissor'
	)

	Naturalidade = forms.CharField(
		widget = forms.TextInput(
			attrs={
				'class' : 'form-control', 
				'placeholder' : ''
			}
		),
		label = 'Naturalidade'
	)

	Nacionalidade = forms.CharField(
		widget = forms.TextInput(
			attrs={
				'class' : 'form-control', 
				'placeholder' : ''
			}
		),
		label = 'Nacionalidade'
	)

	EstadoCivil = forms.CharField(
		widget = forms.TextInput(
			attrs={
				'class' : 'form-control', 
				'placeholder' : ''
			}
		),
		label = 'Estado Civil'
	)

	def save(self):

		NomeEmpresarial = self.cleaned_data.get('NomeEmpresarial')
		TipoPessoa = self.cleaned_data.get('TipoPessoa')
		TipoDireito = self.cleaned_data.get('TipoDireito')
		CNPJ = self.cleaned_data.get('Cnpj')
		EnderecoTipo = self.cleaned_data.get('EnderecoTipo')
		EnderecoNome = self.cleaned_data.get('EnderecoNome')
		EnderecoNumero = self.cleaned_data.get('EnderecoNumero')
		EnderecoComplemento = self.cleaned_data.get('EnderecoBairro')
		EnderecoBairro = self.cleaned_data.get('EnderecoBairro')
		EnderecoCidade =self.cleaned_data.get('EnderecoCidade')
		UF = self.cleaned_data.get('Uf')
		CEP = self.cleaned_data.get('Cep')
		NomeCompleto = self.cleaned_data.get('NomeCompleto')
		Nacionalidade = self.cleaned_data.get('Nacionalidade')
		EstadoCivil = self.cleaned_data.get('EstadoCivil')
		RG = self.cleaned_data.get('Rg')
		OrgaoEmissor = self.cleaned_data.get('OrgaoEmissor')
		CPF = self.cleaned_data.get('Cpf')
		email = self.cleaned_data.get ('Email')
		TelefoneFixo = self.cleaned_data.get('TelefoneFixo')
		Celular = self.cleaned_data.get('Celular')
		IdUsuario = self.cleaned_data.get(None)
		Ramal =  self.cleaned_data.get('Ramal')
		Pais = self.cleaned_data.get('Pais')
		DataNascimento = self.cleaned_data.get('DataNascimento')
		Naturalidade = self.cleaned_data.get('Naturalidade')
					 
		Bdados = models.Parte(
			
			NomeEmpresarial = NomeEmpresarial,
			TipoPessoa = TipoPessoa,
			TipoDireito = TipoDireito,
			CNPJ = CNPJ,
			EnderecoTipo = EnderecoTipo,
			EnderecoNome = EnderecoNome,
			EnderecoNumero = EnderecoNumero,
			EnderecoComplemento = EnderecoComplemento,
			EnderecoBairro = EnderecoBairro,
			EnderecoCidade = EnderecoCidade,
			UF = UF,
			CEP = CEP,
			NomeCompleto = NomeCompleto,
			Nacionalidade = Nacionalidade,
			EstadoCivil = EstadoCivil,
			RG = RG,
			OrgaoEmissor = OrgaoEmissor,
			CPF = CPF,
			email = email,
			TelefoneFixo = TelefoneFixo,
			Celular = Celular,
			IdUsuario = IdUsuario,
			Ramal = Ramal,
			DataNascimento = DataNascimento,
			Pais = Pais,
			Naturalidade = Naturalidade
		)   
		
		Bdados.save()	
			
		return Bdados 


class ItemForm(forms.Form):
	
	#user = forms.ModelChoiceField(queryset=Partes.objects.all())
	Codigo = forms.IntegerField(
		widget = forms.NumberInput()
	)

	Nome = forms.CharField(
		widget = forms.TextInput(
			attrs={
				'class' : 'form-control', 
				'placeholder' : ''
			}
		)
	)

	Valor = forms.IntegerField(
		widget = forms.NumberInput()
	)

	Categoria = forms.CharField(
		widget = forms.TextInput(
			attrs={
				'class' : 'form-control', 
				'placeholder' : ''
			}
		)
	)

	Expli = forms.CharField(
		widget =forms.Textarea(
			attrs={
				'cols': '60', 
				'rows': '20'
			}
		)
	)
	
	Mensagem = forms.CharField(
		widget =forms.Textarea(
			attrs={
				'cols': '60', 
				'rows': '20'
			}
		)
	)

	Equipe = forms.CharField(
		widget =forms.Textarea(
			attrs={
				'cols': '60', 
				'rows': '20'
			}
		)
	)

	Obs = forms.CharField(
		widget = forms.Textarea(
			attrs={
				'cols': '60', 
				'rows': '20'
			}
		)
	)

	InfoAd = forms.CharField(
		widget =forms.Textarea(
			attrs={
				'cols': '60', 
				'rows': '20'
			}
		)
	)


class PropostaForm(forms.Form):  

	tp, tr, catserv = AjusteVetor()
	
	usuario = forms.ModelChoiceField(
		queryset= models.Parte.objects.all(),
		label= 'Cliente',
	)

	funcionario = forms.ModelChoiceField(
		queryset= models.Parte.objects.all(),
		label= "Atendente",
	)

	for i in range(len(catserv)):

		locals()['Entrada%d' % i] = (
			forms.MultipleChoiceField (
				required = False, 
				widget = forms.CheckboxSelectMultiple(
					attrs={
						'class' : 'form-check-input', 
						'placeholder' : catserv[i],
						'name' : catserv[i],
					},
				),
				choices= tp[i],
				label= catserv[i],
			)
		)
		for n in tr[i]:
			# print (n)
			locals()['Quantidade%s' % str(n)]  = forms.IntegerField(
			widget = forms.NumberInput(
				attrs={
					'class' : 'form-check-input', 
					'placeholder' : str(n),
					'name' : 'Quantidade%s' % str(n),
				},
			),
			label= "Quantidade",
	)


class PropostaR1Form(forms.Form):  

	CatAjuste = list(models.Dados.objects.all().filter(Tipo = "R1"))
	tp, tr, catserv = AjusteVetor(CatAjuste)
	


	for i in range(len(catserv)):
		
		locals()[str(catserv[i])] = (
			forms.MultipleChoiceField (
				required = False, 
				widget = forms.CheckboxSelectMultiple(
					attrs={
						'class' : 'checkbox checkbox-traducao', 
						'placeholder' : catserv[i],
					},
				),
				choices= tp[i],
				label= catserv[i],
			)
		)
	

class PropostaR2Form(forms.Form):  

	# CatAjuste = ["Serviços de Interpretação"]
	CatAjuste = list(models.Dados.objects.all().filter(Tipo = "R2"))
	tp, tr, catserv = AjusteVetor(CatAjuste)
	

	for i in range(len(catserv)):

		locals()[str(catserv[i])] = (
			forms.MultipleChoiceField (
				required = False, 
				widget = forms.CheckboxSelectMultiple(
					attrs={
						'class' : 'checkbox checkbox-interpretacao', 
						'placeholder' : catserv[i],
						'name' : catserv[i],
					},
				),
				choices= tp[i],
				label= catserv[i],
			)
		)
		

class PropostaR3Form(forms.Form):  

	# CatAjuste = ["Cursos de Línguas Estrangeiras", "Cursos de Língua Portuguesa", "Cursos de Qualificação Profissional"]
	CatAjuste = list(models.Dados.objects.all().filter(Tipo = "R3"))
	# try:
	# 	Cat = [CatAjuste[0], CatAjuste[1], CatAjuste[2]]
	# 	Tipo = [CatAjuste[3], CatAjuste[4], CatAjuste[5], CatAjuste[6]]
	# except:
	# 	Cat = []
	# 	Tipo = []
	

	tp, tr, catserv = AjusteVetor(CatAjuste)

	vetorajuste = []
	# for i in Tipo:
	# 	vetorajuste.append((i,i))

	# Tipo = tuple(vetorajuste)

	for i in range(len(catserv)):

		locals()[str(catserv[i])] = (
			forms.MultipleChoiceField (
				required = False, 
				widget = forms.CheckboxSelectMultiple(
					attrs={
						'class' : 'checkbox checkbox-cursos', 
						'placeholder' : catserv[i],
						'name' : catserv[i],
					},
				),
				choices= tp[i],
				label= catserv[i],
			)
		)


class PropostaR4Form(forms.Form):  

	# CatAjuste = ["Franqueamento", "Planos"]
	CatAjuste = list(models.Dados.objects.all().filter(Tipo = "R4"))
	tp, tr, catserv = AjusteVetor(CatAjuste)
	

	for i in range(len(catserv)):

		locals()[str(catserv[i])] = (
			forms.ChoiceField(
				required = False, 
				widget = forms.RadioSelect(
					attrs={
						'class' : 'radio radio-licenciamento', 
						'placeholder' : catserv[i],
						'name' : catserv[i],
					},
				),
				choices= tp[i],
				label= catserv[i],
			)
		)
		

class PropostaR5_0Form(forms.Form):  

	# CatAjuste = ["Interpretação simultânea", "Interpretação consecutiva", "Interpretação em acompanhamento"]
	CatAjuste = list(models.Dados.objects.all().filter(Tipo = "R5"))
	tp, tr, catserv = AjusteVetor(CatAjuste)
	
	for i in range(len(catserv)):

		locals()[str(catserv[i])] = (
			forms.MultipleChoiceField(
				required = False, 
				widget = forms.CheckboxSelectMultiple(
					attrs={
						'class' : 'checkbox checkbox-equipamentos', 
						'name' : catserv[i],
					},
				),
				choices= tp[i],
				label= catserv[i],
			)
		)


class PropostaR5_1Form(forms.Form): 
	
	CatAjuste = list(models.Dados.objects.all().filter(Tipo = "R5"))
	tp, tr, catserv = AjusteVetor(CatAjuste)

	for i in range(len(catserv)):
		cont = 0
		for n in tr[i]:
			# print ("Aqui tem", n)
			locals()[str(catserv[i]) + '%s' % str(cont)] = forms.IntegerField(
				widget = forms.NumberInput(
					attrs={
						'class' : 'form-control-sm', 
						'placeholder' : str(n),
						'name' : str(catserv[i]) + '%s' % str(cont),
					},
				),
				label= "",
				required=False,
			)
			cont = cont + 1


class PropostaR6_0Form(forms.Form):  

	# CatAjuste = ["Materiais", "Didádicos", "Papelaria", "Uniformes", "Cantina"]
	CatAjuste = list(models.Dados.objects.all().filter(Tipo = "R6"))
	tp, tr, catserv = AjusteVetor(CatAjuste)
	

	for i in range(len(catserv)):

		locals()[str(catserv[i])]= (
			forms.MultipleChoiceField (
				required = False, 
				widget = forms.CheckboxSelectMultiple(
					attrs={
						'class' : 'checkbox checkbox-livraria', 
						'placeholder' : catserv[i],
						'name' : catserv[i],
					},
				),
				choices= tp[i],
				label= catserv[i],
			)
		)
		

class PropostaR6_1Form(forms.Form): 
	
	CatAjuste = list(models.Dados.objects.all().filter(Tipo = "R6"))
	tp, tr, catserv = AjusteVetor(CatAjuste)

	for i in range(len(catserv)):
		cont = 0
		for n in tr[i]:
			# print ("Aqui tem", n)
			locals()[str(catserv[i]) + '%s' % str(cont)] = forms.IntegerField(
				widget = forms.NumberInput(
					attrs={
						'class' : 'form-control-sm', 
						'placeholder' : str(n),
						'name' : str(catserv[i]) + '%s' % str(cont),
					},
				),
				label= "",
				required=False,
			)
			cont = cont + 1


class PropostaR7_0Form(forms.Form):  

	# CatAjuste = [
	# 	"Cessão ou locação de mão-de-obra para o Setor de Serviços - Cargos de Tradução", 
	# 	"Cessão ou locação de mão-de-obra para o Setor de Serviços - Cargos de Interpretação", 
	# 	"Cessão ou locação de mão-de-obra para o Setor de Serviços - Cargos de Serviços Adicionais", 
	# 	"Cessão ou locação de mão-de-obra para o Setor Administrativo", 
	# 	"Cessão ou locação de mão-de-obra para o Setor Educacional"
	# ]
	CatAjuste = list(models.Dados.objects.all().filter(Tipo = "R7"))
	tp, tr, catserv = AjusteVetor(CatAjuste)

	for i in range(len(catserv)):

		locals()[str(catserv[i])] = (
			forms.MultipleChoiceField (
				required = False, 
				widget = forms.CheckboxSelectMultiple(
					attrs={
						'class' : 'checkbox checkbox-terceiro', 
						'placeholder' : catserv[i],
					},
				),
				choices= tp[i],
				label= catserv[i],
			)
		)


class PropostaR7_1Form(forms.Form):
	
	CatAjuste = list(models.Dados.objects.all().filter(Tipo = "R7"))
	tp, tr, catserv = AjusteVetor(CatAjuste)
	
	for i in range(len(catserv)):
		cont = 0
		for n in tr[i]:
			# print ("Aqui tem", n)
			locals()[str(catserv[i]) + '%s' % str(cont)] = forms.IntegerField(
				widget = forms.NumberInput(
					attrs={
						'class' : 'form-control-sm', 
						'placeholder' : str(n),
						'name' : str(catserv[i]) + '%s' % str(cont),
					},
				),
				label= "",
				required=False,
			)
			cont = cont + 1


class PropostaR8Form(forms.Form): 

	# CatAjuste = ["Serviços Adicionais"]
	CatAjuste = list(models.Dados.objects.all().filter(Tipo = "R8"))
	tp, tr, catserv = AjusteVetor(CatAjuste)
	# print ("r8", tp, tr, catserv)
	for i in range(len(catserv)):
		
		locals()[str(catserv[i])] = (
			forms.MultipleChoiceField (
				required = False, 
				widget = forms.CheckboxSelectMultiple(
					attrs={
						'class' : 'checkbox checkbox-adicionais', 
						'placeholder' : catserv[i],
						'name' : catserv[i],
					},
				),
				choices= tp[i],
				label= catserv[i],
			)
		)
		

# class RelatoriodeDiagnosticoForm(forms.Form):

# 	TipodeConteudo = forms.CharField(
# 		widget = forms.SelectMultiple(
# 			attrs={
# 				'class' : 'custom-select', 
# 				'placeholder' : ''
# 			},
# 			choices = var.Conteudo()
# 		),
# 		label='Tipo de conteúdo ',	
# 	)

# 	NumeroPalavras = forms.IntegerField(
# 		widget = forms.NumberInput(), 
# 		label='Número de palavras',
# 		min_value = 0,
# 	)
		
# 	DataEntrega = forms.CharField(
# 		widget=forms.TextInput(
# 			attrs={
# 				'class' : 'DataIn form-control', 
# 				'placeholder' : '',
# 				'autocomplete' : 'off'
# 			}
# 		), 
# 		label='Data de entrega do serviço'
# 	)

# 	Urgencia = forms.BooleanField(
# 		required = False, 
# 		initial= False,
# 		label='Urgência do serviço', 
# 		widget= forms.CheckboxInput(
# 			attrs={
# 				'class' : 'form',
# 				'placeholder' : ''
# 			}
# 		)
# 	)

# 	DireitosAutorais  = forms.BooleanField(
# 		required = False, 
# 		initial= False,
# 		label='Direitos autorais', 
# 		widget= forms.CheckboxInput(
# 			attrs={
# 				'class' : 'form',
# 				'placeholder' : ''
# 			}
# 		)
# 	)

# 	ModoEntrega = forms.CharField(
# 		widget = forms.SelectMultiple(
# 			attrs={
# 				'class' : 'custom-select', 
# 				'placeholder' : ''
# 			},
# 			choices = var.ModoEntrega()
# 		),
# 		label='Modo de entrega'
# 	)

# 	SuporteConteudoPartida = forms.CharField(
# 		widget = forms.SelectMultiple(
# 			attrs={
# 				'class' : 'custom-select', 
# 				'placeholder' : ''
# 			},
# 			choices = var.SuportePartida()
# 		),
# 		label='Suporte do conteúdo (partida)'
# 	)

# 	ExtensaoPartida = forms.CharField(
# 		widget = forms.SelectMultiple(
# 			attrs={
# 				'class' : 'custom-select', 
# 				'placeholder' : ''
# 			},
# 			choices = var.ArquivoPartida()
# 		),
# 		label='Extensão de arquivo (partida)'
# 	)

# 	SuporteConteudoChegada = forms.CharField(
# 		widget = forms.SelectMultiple(
# 			attrs={
# 				'class' : 'custom-select', 
# 				'placeholder' : ''
# 			},
# 			choices = var.SuporteChegada()
# 		),
# 		label='Suporte do conteúdo (chegada)'
# 	)

# 	ExtensaoChegada = forms.CharField(
# 		widget = forms.SelectMultiple(
# 			attrs={
# 				'class' : 'custom-select', 
# 				'placeholder' : ''
# 			},
# 			choices = var.ArquivoChegada()
# 		),
# 		label='Extensão de conteúdo (chegada)'
# 	)

# 	ValidadeProposta = forms.CharField(
# 		widget = forms.Select(
# 			attrs={
# 				'class' : 'custom-select', 
# 				'placeholder' : ''
# 			},
# 			choices = var.Validade()
# 		),
# 		label='Validade da proposta',
# 	)

# 	CodigoPromocional = forms.CharField(
# 		widget = forms.TextInput(
# 			attrs={
# 				'class' : 'form-control', 
# 				'placeholder' : ''
# 			}
# 		), 
# 		label='Código promocional',
# 		required = False,
# 	)

# 	ComoConheceu = forms.CharField(
# 		widget = forms.Select(
# 			attrs={
# 				'class' : 'custom-select', 
# 				'placeholder' : ''
# 			},
# 			choices = var.ComoConheceu()
# 		),
# 		required = False, 
# 		label='Como nos conheceu?'
# 	)			

# 	def save(self):

# 		IdProposta = self.data.get('IdProposta')
# 		TipodeServico = self.data.get('TipodeServico')
# 		LingPartida =self.data.get('LingPartida')
# 		LingChegada = self.data.get('LingChegada')
# 		TipodeConteudo = self.data.get('TipodeConteudo')
# 		NumeroPalavras = self.data.get('NumeroPalavras')
# 		DataEntrega= self.data.get('DataEntrega')
# 		LingPartida = self.data.get('LingPartida')
# 		LingChegada = self.data.get('LingChegada')
# 		TipodeConteudo = self.data.get('TipodeConteudo')
# 		NumeroPalavras = self.data.get('NumeroPalavras')
# 		Urgencia = self.data.get('Urgencia')
# 		DireitosAutorais = self.data.get('DireitosAutorais')
# 		Dominio1 = self.data.get('Dominio1')
# 		Dominio2 = self.data.get('Dominio2')
# 		ModoEntrega = self.data.get('ModoEntrega')
# 		SuporteConteudoPartida = self.data.get('SuporteConteudoPartida')
# 		ExtensaoPartida = self.data.get ('ExtensaoPartida')
# 		SuporteConteudoChegada = self.data.get('SuporteConteudoChegada')
# 		ExtensaoChegada = self.data.get('ExtensaoChegada')
# 		# TraducaoJuramentada = self.data.get('TraducaoJuramentada')
# 		TraducaoJuramentada = False
# 		ValidadeProposta = self.data.get('ValidadeProposta')
# 		CodigoPromocional = self.data.get('CodigoPromocional')
# 		ComoConheceu = self.data.get('ComoConheceu')
					 
# 		Bdados= models.RelatoriodeDiagnostico(
# 			IdProposta = IdProposta,
# 			TipodeServico = TipodeServico,
# 			LingPartida = LingPartida,
# 			LingChegada = LingChegada,
# 			TipodeConteudo = TipodeConteudo,
# 			NumeroPalavras = NumeroPalavras,
# 			DataEntrega = DataEntrega,
# 			Urgencia = Urgencia,
# 			DireitosAutorais = DireitosAutorais,
# 			Dominio1 = Dominio1,
# 			Dominio2 = Dominio2,
# 			ModoEntrega = ModoEntrega,
# 			SuporteConteudoPartida = SuporteConteudoPartida,
# 			ExtensaoPartida = ExtensaoPartida,
# 			SuporteConteudoChegada = SuporteConteudoChegada,
# 			ExtensaoChegada = ExtensaoChegada,
# 			TraducaoJuramentada = TraducaoJuramentada,
# 			ValidadeProposta = ValidadeProposta,
# 			CodigoPromocional = CodigoPromocional,
# 			ComoConheceu = ComoConheceu,
# 		)   
# 		Bdados.save()	
			
# 		return Bdados 


# class RelatoriodeDiagnosticoCursosForm(forms.Form):


# 	NomeAluno = forms.CharField(
# 		widget = forms.TextInput(
# 			attrs={
# 				'class' : 'form-control', 
# 				'placeholder' : ''
# 			}
# 		), 
# 		label='Nome do aluno'
# 	) 

# 	FaixaEtaria = forms.CharField(
# 		widget = forms.Select(
# 			attrs={
# 				'class' : 'custom-select', 
# 				'placeholder' : ''
# 			},
# 			choices = var.Faixaetaria()
# 		),
# 		label='Faixa Etária'
# 	)
	
# 	NivelAluno = forms.CharField(
# 		widget = forms.Select(
# 			attrs={
# 				'class' : 'custom-select', 
# 				'placeholder' : ''
# 			},
# 			choices = var.NivelAluno()
# 		),
# 		label='Nível do(s) aluno(s) na língua buscada para o curso',
		
# 	)
	
# 	RegimeEnsino = forms.CharField(
# 		widget = forms.Select(
# 			attrs={
# 				'class' : 'custom-select', 
# 				'placeholder' : ''
# 			},
# 			choices = var.RegimeEnsino()
# 		),
# 		label='Regime de ensino',	
# 	)
	
# 	NomeUnidade = forms.CharField(
# 		widget = forms.Select(
# 			attrs={
# 				'class' : 'custom-select', 
# 				'placeholder' : ''
# 			},
# 			choices = var.Unidade()
# 		),
# 		label='Nome da unidade de sua preferência'
# 	)
	
# 	TipodeCurso = forms.CharField(
# 		widget = forms.Select(
# 			attrs={
# 				'class' : 'custom-select', 
# 				'placeholder' : ''
# 			},
# 			choices = var.TipoCurso()
# 		),
# 		label='Modalidade do Curso',
# 	)

# 	CEP = forms.CharField(
# 		widget = forms.TextInput(
# 			attrs={
# 				'class' : 'form-control', 
# 				'placeholder' : ''
# 			}
# 		),
# 		label = 'CEP',
# 	)

# 	EnderecoRealizacaoCurso = forms.CharField(
# 		widget = forms.TextInput(
# 			attrs={
# 				'class' : 'form-control', 
# 				'placeholder' : ''
# 			}
# 		), 
# 		label='Endereço de realização do curso'
# 	)
	
# 	EnderecoNumero = forms.IntegerField(
# 		widget = forms.NumberInput(
# 			attrs={
# 				'class' : 'form-control', 
# 				'placeholder' : ''
# 			}
# 		),
# 		label = 'Número'	
# 	)

# 	EnderecoComplemento = forms.CharField(
# 		widget = forms.TextInput(
# 			attrs={
# 				'class' : 'form-control',
# 				'placeholder' : ''
# 			}
# 		),
# 		label = 'Complemento'
# 	)

# 	EnderecoBairro = forms.CharField(
# 		widget = forms.TextInput(
# 			attrs={
# 				'class' : 'form-control', 
# 				'placeholder' : ''
# 			}
# 		),
# 		label = 'Bairro'
# 	)

# 	EnderecoCidade = forms.CharField(
# 		widget = forms.TextInput(
# 			attrs={
# 				'class' : 'form-control', 
# 				'placeholder' : ''
# 			}
# 		),
# 		label = 'Cidade'
# 	)
	
# 	NumeroParticipantes = forms.IntegerField(
# 		widget = forms.NumberInput(), 
# 		label='Número de participantes do curso',
# 		min_value = 0,
# 	)
	
# 	Convenio = forms.CharField(
# 		widget = forms.Select(
# 			attrs={
# 				'class' : 'custom-select', 
# 				'placeholder' : ''
# 			},
# 			choices = var.Convenio()
# 		),
# 		label='Convênio',	
# 	)
	
# 	LocalPresencial = forms.CharField(
# 		widget = forms.TextInput(
# 			attrs={
# 				'class' : 'form-control', 
# 				'placeholder' : ''
# 			}
# 		), 
# 		label='Nome da empresa conveniada'
# 	)

# 	Periodicidade = forms.CharField(
# 		widget = forms.SelectMultiple(
# 			attrs={
# 				'class' : 'custom-select', 
# 				'placeholder' : ''
# 			},
# 			choices = var.PeriodicidadeAula()
# 		),
# 		label='Preferência de Realização da Aula',
		
# 	)
	
# 	DataInicio = forms.CharField(
# 		widget=forms.TextInput(
# 			attrs={
# 				'class' : 'DataIn form-control', 
# 				'placeholder' : '',
# 				'autocomplete' : 'off'
# 			}
# 		), 
# 		label='Preferência de data de início do curso (dd/mm/aaaa)'
# 	)
	
# 	DataTermino = forms.CharField(
# 		widget=forms.TextInput(
# 			attrs={
# 				'class' : 'DataIn form-control', 
# 				'placeholder' : '',
# 				'autocomplete' : 'off'
# 			}
# 		), 
# 		label='Preferência data de término do curso (dd/mm/aaaa)'
# 	)
	
# 	HoraInicio = forms.CharField(
# 		widget = forms.TextInput(
# 			attrs={
# 				'class' : 'form-control time', 
# 				'placeholder' : '',
# 				'autocomplete' : 'off'
# 			}
# 		),
# 		required=False,
# 		label='Preferência na hora de início da aula (hh:mm)',
# 	)
	
# 	DuracaoAula = forms.CharField(
# 		widget = forms.NumberInput(
# 			attrs={
# 				'class' : 'form-control', 
# 				'placeholder' : '',
# 				'min': "1"
# 			}
# 		), 
# 		label='Preferência de duração da aula (Em horas)',
# 	)
	
# 	RepeticaoCurso = forms.CharField(
# 		widget = forms.Select(
# 			attrs={
# 				'class' : 'custom-select', 
# 				'placeholder' : ''
# 			},
# 			choices = var.RepeticaoCurso()
# 		),
# 		label='Preferência de repetição do curso',	
# 	)
	
# 	ProfessoresCertificados = forms.BooleanField(
# 		required = False, 
# 		initial= False,
# 		label='Professores certificados', 
# 		widget= forms.CheckboxInput(
# 			attrs={
# 				'class' : 'form',
# 				'placeholder' : '',
# 			}
# 		)
# 	)
	
# 	ValidadeProposta = forms.CharField(
# 		widget = forms.Select(
# 			attrs={
# 				'class' : 'custom-select', 
# 				'placeholder' : ''
# 			},
# 			choices = var.Validade()
# 		),
# 		label='Validade da proposta',
# 	)
	
# 	CodigoPromocional = forms.CharField(
# 		widget = forms.TextInput(
# 			attrs={
# 				'class' : 'form-control', 
# 				'placeholder' : ''
# 			}
# 		), 
# 		label='Código promocional',
# 		required = False,
# 	)
	
# 	ComoConheceu = forms.CharField(
# 		widget = forms.Select(
# 			attrs={
# 				'class' : 'custom-select', 
# 				'placeholder' : ''
# 			},
# 			choices = var.ComoConheceu()
# 		),
# 		required = False, 
# 		label='Como nos conheceu?'
# 	)

# 	def save(self):

# 		IdProposta = self.data.get('IdProposta')
# 		TipodeServico = self.data.get('TipodeServico')
# 		LingPartida =self.data.get('LingPartida')
# 		LingChegada = self.data.get('LingChegada')
# 		NomeRepresentante = self.data.get('NomeRepresentante')
# 		NomeAluno = self.data.get('NomeAluno')
# 		FaixaEtaria = self.data.get('FaixaEtaria')
# 		NivelAluno = self.data.get('NivelAluno')
# 		RegimeEnsino = self.data.get('RegimeEnsino')
# 		LocalPresencial = self.data.get('LocalPresencial')
# 		NomeUnidade = self.data.get('NomeUnidade')
# 		Convenio = self.data.get('Convenio')
# 		TipodeCurso = self.data.get('TipodeCurso')
# 		EnderecoRealizacaoCurso = self.data.get('EnderecoRealizacaoCurso')
# 		NumeroParticipantes =self.data.get('NumeroParticipantes')
# 		Periodicidade = self.data.get('Periodicidade')
# 		DataInicio = self.data.get('DataInicio')
# 		DataTermino = self.data.get('DataTermino')
# 		HoraInicio = self.data.get('HoraInicio')
# 		DuracaoAula = self.data.get('DuracaoAula')
# 		RepeticaoCurso = self.data.get('RepeticaoCurso')
# 		ProfessoresCertificados = self.data.get('ProfessoresCertificados')
# 		ValidadeProposta = self.data.get('ValidadeProposta')
# 		CodigoPromocional = self.data.get('CodigoPromocional')
# 		ComoConheceu = self.data.get('ComoConheceu')
# 		CEP = self.data.get('CEP')
# 		EnderecoNumero = self.data.get('EnderecoNumero')
# 		EnderecoComplemento = self.data.get('EnderecoBairro')
# 		EnderecoBairro = self.data.get('EnderecoBairro')
# 		EnderecoCidade =self.data.get('EnderecoCidade')
		
					 
# 		Bdados= models.RelatoriodeDiagnosticoCursos(
# 			IdProposta = IdProposta,
# 			TipodeServico = TipodeServico,
# 			LingPartida = LingPartida,
# 			LingChegada = LingChegada,
# 			NomeRepresentante = NomeRepresentante,
# 			NomeAluno = NomeAluno,
# 			FaixaEtaria = FaixaEtaria,
# 			NivelAluno = NivelAluno,
# 			RegimeEnsino = RegimeEnsino,
# 			LocalPresencial = LocalPresencial,
# 			NomeUnidade = NomeUnidade,
# 			Convenio = Convenio,
# 			TipodeCurso = TipodeCurso,
# 			EnderecoRealizacaoCurso = EnderecoRealizacaoCurso,
# 			NumeroParticipantes = NumeroParticipantes,
# 			Periodicidade = Periodicidade,
# 			DataInicio = DataInicio,
# 			DataTermino = DataTermino,
# 			HoraInicio = HoraInicio,
# 			DuracaoAula = DuracaoAula,
# 			RepeticaoCurso = RepeticaoCurso,
# 			ProfessoresCertificados = ProfessoresCertificados,
# 			ValidadeProposta = ValidadeProposta,
# 			CodigoPromocional = CodigoPromocional,
# 			ComoConheceu = ComoConheceu,
# 			CEP = CEP,
# 			EnderecoNumero = EnderecoNumero,
# 			EnderecoComplemento = EnderecoComplemento,
# 			EnderecoBairro = EnderecoBairro,
# 			EnderecoCidade = EnderecoCidade,
# 		)   
# 		Bdados.save()	
			
# 		return Bdados 


# class RelatoriodeDiagnosticoFranquiasForm(forms.Form):

# 	Investimento = forms.CharField(
# 		widget = forms.Select(
# 			attrs={
# 				'class' : 'custom-select', 
# 				'placeholder' : ''
# 			},
# 			choices = var.Investimento()
# 		),
# 		label='1.	Qual investimento inicial pretende aportar?',	
# 	)

# 	CapitalGiro = forms.CharField(
# 		widget = forms.Select(
# 			attrs={
# 				'class' : 'custom-select', 
# 				'placeholder' : ''
# 			},
# 			choices = var.Capital()
# 		),
# 		label='2.	Quanto em capital de giro possui disponível?',	
# 	)

# 	AreaMinima = forms.CharField(
# 		widget = forms.Select(
# 			attrs={
# 				'class' : 'custom-select', 
# 				'placeholder' : ''
# 			},
# 			choices = var.Area()
# 		),
# 		label='3.	Qual área mínima possui disponível?',
		
# 	)

# 	ImovelProprio = forms.CharField(
# 		widget = forms.Select(
# 			attrs={
# 				'class' : 'custom-select', 
# 				'placeholder' : ''
# 			},
# 			choices = var.Imovel()
# 		),
# 		label='4.	Possui imóvel próprio? ',
		
# 	)

# 	ZonaGeografica = forms.CharField(
# 		widget = forms.Select(
# 			attrs={
# 				'class' : 'custom-select', 
# 				'placeholder' : ''
# 			},
# 			choices = var.Zona()
# 		),
# 		label='5.	Se importa em compartilhar delimitação geográfica de sua zona?',	
# 	)

# 	UnidadesSite  = forms.CharField(
# 		widget = forms.Select(
# 			attrs={
# 				'class' : 'custom-select', 
# 				'placeholder' : ''
# 			},
# 			choices = var.Convenio()
# 		),
# 		label='6.	Se importa em não figurar entre as unidades no site da simões?',	
# 	)

# 	Funcionarios  = forms.CharField(
# 		widget = forms.Select(
# 			attrs={
# 				'class' : 'custom-select', 
# 				'placeholder' : ''
# 			},
# 			choices = var.Func()
# 		),
# 		label='7.	Quantos funcionários dispõe ou pretende possuir?)',
# 	)

# 	def save(self):

# 		IdProposta = self.data.get('IdProposta')
# 		TipodeServico = self.data.get('TipodeServico')
# 		Investimento = self.data.get('Investimento')
# 		CapitalGiro = self.data.get('CapitalGiro')
# 		AreaMinima = self.data.get('AreaMinima')
# 		ImovelProprio = self.data.get('ImovelProprio')
# 		ZonaGeografica = self.data.get('ZonaGeografica')
# 		UnidadesSite  = self.data.get('UnidadesSite')
# 		Funcionarios  = self.data.get('Funcionarios')
					
# 		Bdados= models.RelatoriodeDiagnosticoFranquias(
# 			IdProposta = IdProposta,
# 			TipodeServico = TipodeServico,
# 			Investimento = Investimento,
# 			CapitalGiro = CapitalGiro,
# 			AreaMinima = AreaMinima,
# 			ImovelProprio = ImovelProprio,
# 			ZonaGeografica = ZonaGeografica,
# 			UnidadesSite  = UnidadesSite,
# 			Funcionarios  = Funcionarios,
# 		)   
# 		Bdados.save()	
		
# 		return Bdados 

		
# class RelatoriodeDiagnosticoInterpretaForm(forms.Form):
	
# 	NomeProprietaria = forms.CharField(
# 		widget = forms.TextInput(
# 			attrs={
# 				'class' : 'form-control', 
# 				'placeholder' : ''
# 			}
# 		), 
# 		label='Nome da proprietária do evento'
# 	) 

# 	NomeOrganizador = forms.CharField(
# 		widget = forms.TextInput(
# 			attrs={
# 				'class' : 'form-control', 
# 				'placeholder' : ''
# 			}
# 		), 
# 		label='Nome da(s) organizadora(s) do evento'
# 	) 

# 	NomeEvento = forms.CharField(
# 		widget = forms.TextInput(
# 			attrs={
# 				'class' : 'form-control', 
# 				'placeholder' : ''
# 			}
# 		), 
# 		label='Nome do evento'
# 	) 
	
# 	TemaEvento = forms.CharField(
# 		widget = forms.TextInput(
# 			attrs={
# 				'class' : 'form-control', 
# 				'placeholder' : ''
# 			}
# 		), 
# 		label='Tema do evento'
# 	) 

# 	CEP = forms.CharField(
# 		widget = forms.TextInput(
# 			attrs={
# 				'class' : 'form-control', 
# 				'placeholder' : ''
# 			}
# 		),
# 		label = 'CEP',
# 	)

# 	EnderecoEvento = forms.CharField(
# 		widget = forms.TextInput(
# 			attrs={
# 				'class' : 'form-control', 
# 				'placeholder' : ''
# 			}
# 		), 
# 		label='Endereço de realização do evento'
# 	) 

# 	EnderecoNumero = forms.IntegerField(
# 		widget = forms.NumberInput(
# 			attrs={
# 				'class' : 'form-control', 
# 				'placeholder' : ''
# 			}
# 		),
# 		label = 'Número'
		
# 	)

# 	EnderecoComplemento = forms.CharField(
# 		widget = forms.TextInput(
# 			attrs={
# 				'class' : 'form-control',
# 				'placeholder' : ''
# 			}
# 		),
# 		label = 'Complemento'
# 	)

# 	EnderecoBairro = forms.CharField(
# 		widget = forms.TextInput(
# 			attrs={
# 				'class' : 'form-control', 
# 				'placeholder' : ''
# 			}
# 		),
# 		label = 'Bairro'
# 	)

# 	EnderecoCidade = forms.CharField(
# 		widget = forms.TextInput(
# 			attrs={
# 				'class' : 'form-control', 
# 				'placeholder' : ''
# 			}
# 		),
# 		label = 'Cidade'
# 	)

# 	Risco = forms.BooleanField(
# 		required = False, 
# 		initial= False,
# 		label='O local do evento apresenta risco de seguridade ou periculosidade?', 
# 		widget= forms.CheckboxInput(
# 			attrs={
# 				'class' : 'form',
# 				'placeholder' : ''
# 			}
# 		)
# 	)

# 	FusoHorario = forms.CharField(
# 		widget = forms.Select(
# 			attrs={
# 				'class' : 'custom-select', 
# 				'placeholder' : ''
# 			},
# 			choices = var.UTC()
# 		),
# 		label='Fuso horário',
		
# 	)

# 	NumeroAmbientes = forms.IntegerField(
# 		widget = forms.NumberInput(), 
# 		label='Número de ambientes',
# 		min_value = 0,
# 	)
	
# 	TipoEvento = forms.CharField(
# 		widget = forms.Select(
# 			attrs={
# 				'class' : 'custom-select', 
# 				'placeholder' : ''
# 			},
# 			choices = var.TipoEvento()
# 		),
# 		label='Indique o tipo do evento',
# 	)

# 	DataInicio = forms.CharField(
# 		widget=forms.TextInput(
# 			attrs={
# 				'class' : 'DataIn form-control', 
# 				'placeholder' : '',
# 				'autocomplete' : 'off'
# 			}
# 		), 
# 		label='Data de Início do evento (dd/mm/aaaa)'
# 	)

# 	DataTermino = forms.CharField(
# 		widget=forms.TextInput(
# 			attrs={
# 				'class' : 'DataIn form-control', 
# 				'placeholder' : '',
# 				'autocomplete' : 'off'
# 			}
# 		), 
# 		label='Data de término do evento (dd/mm/aaaa)'
# 	)
	
# 	NumeroUsuariosFinais = forms.IntegerField(
# 		widget = forms.NumberInput(), 
# 		label='Número de usuários finais',
# 		min_value = 0,
# 	)
	
# 	RepeticaoEvento = forms.CharField(
# 		widget = forms.Select(
# 			attrs={
# 				'class' : 'custom-select', 
# 				'placeholder' : ''
# 			},
# 			choices = var.RepeticaoCurso()
# 		),
# 		label='Repetição do evento',
# 	)

# 	# Interpretação

# 	LocalInterpretacao = forms.CharField(
# 		widget = forms.TextInput(
# 			attrs={
# 				'class' : 'form-control', 
# 				'placeholder' : ''
# 			}
# 		), 
# 		label='Local da interpretação'
# 	) 

# 	DisposicaoAmbiente = forms.CharField(
# 		widget = forms.Select(
# 			attrs={
# 				'class' : 'custom-select', 
# 				'placeholder' : ''
# 			},
# 			choices = var.Ambiente()
# 		),
# 		label='Disposição do ambiente',	
# 	)

# 	NumeroUsuariosFinaisLocal = forms.IntegerField(
# 		widget = forms.NumberInput(), 
# 		label='Número de usuários finais no local da interpretação',
# 		min_value = 0,
# 	)

# 	Cabine = forms.BooleanField(
# 		required = False, 
# 		initial= False,
# 		label='Necessita de cabine?', 
# 		widget= forms.CheckboxInput(
# 			attrs={
# 				'class' : 'form',
# 				'placeholder' : ''
# 			}
# 		)
# 	)
	
# 	NumeroReceptores = forms.CharField(
# 		widget = forms.Select(
# 			attrs={
# 				'class' : 'custom-select', 
# 				'placeholder' : ''
# 			},
# 			choices = var.Auricular()
# 		),
# 		required = False,
# 		label='Número de receptores e auriculares no local da interpretação',
# 	)

# 	NumeroAmbientesExtras = forms.IntegerField(
# 		widget = forms.NumberInput(), 
# 		label='Número de ambientes extras receberão a mesma interpretação',
# 		min_value = 0,
# 	)

# 	RepeticaoInterpretacao = forms.CharField(
# 		widget = forms.Select(
# 			attrs={
# 				'class' : 'custom-select', 
# 				'placeholder' : ''
# 			},
# 			choices = var.RepeticaoCurso()
# 		),
# 		label='Repetição da interpretação',	
# 	)

# 	DataInicioInterpretacao = forms.CharField(
# 		widget=forms.TextInput(
# 			attrs={
# 				'class' : 'DataIn form-control', 
# 				'placeholder' : '',
# 				'autocomplete' : 'off'
# 			}
# 		), 
# 		label='Data de Início da interpretação (dd/mm/aaaa)'
# 	)

# 	HoraInicioInterpretacao = forms.CharField(
# 		widget = forms.TextInput(
# 			attrs={
# 				'class' : 'form-control time', 
# 				'placeholder' : '',
# 				'autocomplete' : 'off'
# 			}
# 		),
# 		required=False,
# 		label='Hora de Início da interpretação (hh:mm)',
# 	)

# 	DuracaoInterpretacao = forms.IntegerField(
# 		widget = forms.NumberInput(), 
# 		label='Duração da interpretação (horas)',
# 		min_value = 0,
# 		max_value = 24,
# 	)

# 	QuantidadeInterpretes = forms.IntegerField(
# 		widget = forms.NumberInput(), 
# 		label='Quantidade de Intérpretes',
# 		min_value = 0,
# 	)

# 	ProfissionaisCertificados = forms.BooleanField(
# 		required = False, 
# 		initial= False,
# 		label='Profissionais certificados', 
# 		widget= forms.CheckboxInput(
# 			attrs={
# 				'class' : 'form',
# 				'placeholder' : ''
# 			}
# 		)
# 	)

# 	ProfissionaisAutodeclarados = forms.CharField(
# 		widget = forms.Select(
# 			attrs={
# 				'class' : 'custom-select', 
# 				'placeholder' : ''
# 			},
# 			choices = var.Profossionais()
# 		),
# 		required = False,
# 		label='Preferência por profissionais autodeclarados em eventos etnicos?',	
# 	)

# 	NumeroRecepcionista = forms.CharField(
# 		widget = forms.NumberInput(
# 			attrs={
# 				'class' : 'form-control', 
# 				'placeholder' : '',
# 				'min': "0"
# 			}
# 		), 
# 		required = False,
# 		label='Número de Recepcionista(s) de Eventos',
# 	)

# 	# Parâmetros avançados

# 	GravacaoAudio = forms.BooleanField(
# 		required = False, 
# 		initial= False,
# 		label='Gravação do áudio da Interpretação?', 
# 		widget= forms.CheckboxInput(
# 			attrs={
# 				'class' : 'form',
# 				'placeholder' : ''
# 			}
# 		)
# 	)

# 	Transcricao = forms.BooleanField(
# 		required = False, 
# 		initial= False,
# 		label='Transcrição do áudio da Interpretação gravada?', 
# 		widget= forms.CheckboxInput(
# 			attrs={
# 				'class' : 'form',
# 				'placeholder' : ''
# 			}
# 		)
# 	)

# 	LegendagemAudio = forms.BooleanField(
# 		required = False, 
# 		initial= False,
# 		label='Legendagem do áudio da Interpretação gravada?',
# 		widget= forms.CheckboxInput(
# 			attrs={
# 				'class' : 'form',
# 				'placeholder' : ''
# 			}
# 		)
# 	)

# 	ModoEntregaGravacao = forms.CharField(
# 		widget = forms.SelectMultiple(
# 			attrs={
# 				'class' : 'custom-select', 
# 				'placeholder' : ''
# 			},
# 			choices = var.ModoEntrega()
# 		),
# 		required = False,
# 		label='Modo de entrega'
# 	)


# 	SuporteConteudoPartida = forms.CharField(
# 		widget = forms.SelectMultiple(
# 			attrs={
# 				'class' : 'custom-select', 
# 				'placeholder' : ''
# 			},
# 			choices = var.SuportePartida()
# 		),
# 		required = False,
# 		label='Suporte do conteúdo'
# 	)


# 	ExtensaoChegada = forms.CharField(
# 		widget = forms.SelectMultiple(
# 			attrs={
# 				'class' : 'custom-select', 
# 				'placeholder' : ''
# 			},
# 			choices = var.ArquivoChegada()
# 		),
# 		required = False,
# 		label='Extensão de arquivo'
# 	)

# 	EquipamentosSonorizacao = forms.BooleanField(
# 		required = False, 
# 		initial= False,
# 		label='Necessita de equipamentos para sonorização?', 
# 		widget= forms.CheckboxInput(
# 			attrs={
# 				'class' : 'form',
# 				'placeholder' : ''
# 			}
# 		)
# 	)

# 	NumeroMicrofonesMesa = forms.IntegerField(
# 		widget = forms.NumberInput(), 
# 		label='Número de microfones de mesa',
# 		min_value = 0,
# 		required = False, 
# 	)

# 	NumeroMicrofonesSemFio = forms.IntegerField(
# 		widget = forms.NumberInput(), 
# 		label='Número de microfones sem fio',
# 		min_value = 0,
# 		required = False, 
# 	)

# 	NumeroMicrofonesLapela = forms.IntegerField(
# 		widget = forms.NumberInput(), 
# 		label='Número de microfones de lapela',
# 		min_value = 0,
# 		required = False, 
# 	)

# 	NumeroMicrofonesRemoviveis = forms.IntegerField(
# 		widget = forms.NumberInput(), 
# 		label='Número de microfones removíveis',
# 		min_value = 0,
# 		required = False, 
# 	)

# 	MesaSom = forms.CharField(
# 		widget = forms.Select(
# 			attrs={
# 				'class' : 'custom-select', 
# 				'placeholder' : ''
# 			},
# 			choices = var.Mesa()
# 		),
# 		required = False, 
# 		label='Mesa de Som',	
# 	)

# 	Retorno = forms.IntegerField(
# 		widget = forms.NumberInput(), 
# 		label='Retorno',	
# 		min_value = 0,
# 		required = False, 
# 	)
		
# 	KitDJ = forms.BooleanField(
# 		required = False, 
# 		initial= False,
# 		label='Kit DJ', 
# 		widget= forms.CheckboxInput(
# 			attrs={
# 				'class' : 'form',
# 				'placeholder' : ''
# 			}
# 		)
# 	)

# 	SideFill = forms.CharField(
# 		widget = forms.Select(
# 			attrs={
# 				'class' : 'custom-select', 
# 				'placeholder' : ''
# 			},
# 			choices = var.SideFill()
# 		),
# 		required = False, 
# 		label='Side-Fill',	
# 	)

# 	ServicosComplementares = forms.BooleanField(
# 		required = False, 
# 		initial= False,
# 		label='Necessita de serviços complementares? ', 
# 		widget= forms.CheckboxInput(
# 			attrs={
# 				'class' : 'form',
# 				'placeholder' : ''
# 			}
# 		)
# 	)
# 	Televisor = forms.CharField(
# 		widget = forms.Select(
# 			attrs={
# 				'class' : 'custom-select', 
# 				'placeholder' : ''
# 			},
# 			choices = var.Televisor()
# 		),
# 		label='Televisor',
# 		required = False, 	
# 	)

# 	ProjetorMultimidia = forms.CharField(
# 		widget = forms.Select(
# 			attrs={
# 				'class' : 'custom-select', 
# 				'placeholder' : ''
# 			},
# 			choices = var.Projetor()
# 		),
# 		label='Projetor Multimidia',	
# 	)

# 	AparelhoDVDMP3 = forms.BooleanField(
# 		required = False, 
# 		initial= False,
# 		label='Aparelho de DVD/MP3', 
# 		widget= forms.CheckboxInput(
# 			attrs={
# 				'class' : 'form',
# 				'placeholder' : ''
# 			}
# 		)
# 	)

# 	Notebook = forms.BooleanField(
# 		required = False, 
# 		initial= False,
# 		label='Notebook', 
# 		widget= forms.CheckboxInput(
# 			attrs={
# 				'class' : 'form',
# 				'placeholder' : ''
# 			}
# 		)
# 	)
	
# 	ValidadeProposta = forms.CharField(
# 		widget = forms.Select(
# 			attrs={
# 				'class' : 'custom-select', 
# 				'placeholder' : ''
# 			},
# 			choices = var.Validade()
# 		),
# 		label='Validade da proposta',
# 	)

# 	CodigoPromocional = forms.CharField(
# 		widget = forms.TextInput(
# 			attrs={
# 				'class' : 'form-control', 
# 				'placeholder' : ''
# 			}
# 		), 
# 		label='Código promocional',
# 		required = False,
# 	)

# 	ComoConheceu = forms.CharField(
# 		widget = forms.Select(
# 			attrs={
# 				'class' : 'custom-select', 
# 				'placeholder' : ''
# 			},
# 			choices = var.ComoConheceu()
# 		),
# 		required = False, 
# 		label='Como nos conheceu?'
# 	)

# 	def save(self):

# 		IdProposta = self.data.get('IdProposta')
# 		TipodeServico = self.data.get('TipodeServico')
# 		NomeProprietaria = self.data.get('NomeProprietaria')
# 		NomeOrganizador = self.data.get('NomeOrganizador')
# 		NomeEvento = self.data.get('NomeEvento')
# 		TemaEvento = self.data.get('TemaEvento')
# 		EnderecoEvento = self.data.get('EnderecoEvento')
# 		Risco = self.data.get('Risco')
# 		FusoHorario = self.data.get('FusoHorario')
# 		LinguaConferencia = self.data.get('LinguaConferencia')
# 		NumeroAmbientes = self.data.get('NumeroAmbientes')
# 		TipoEvento = self.data.get('TipoEvento')
# 		NumeroUsuariosFinais = self.data.get('NumeroUsuariosFinais')
# 		Dominio1 = self.data.get('Dominio1')
# 		Dominio2 = self.data.get('Dominio2')
# 		RepeticaoEvento = self.data.get('RepeticaoEvento')
# 		DataInicio = self.data.get('DataInicio')
# 		DataTermino = self.data.get('DataTermino')
# 		LocalInterpretacao = self.data.get('LocalInterpretacao')
# 		DisposicaoAmbiente = self.data.get('DisposicaoAmbiente')
# 		NumeroUsuariosFinaisLocal = self.data.get('NumeroUsuariosFinaisLocal')
# 		LingPartida = self.data.get('LingPartida')
# 		LingChegada = self.data.get('LingChegada')
# 		Cabine = self.data.get('Cabine')
# 		NumeroReceptores = self.data.get('NumeroReceptores')
# 		NumeroAmbientesExtras = self.data.get('NumeroAmbientesExtras')
# 		SuporteConteudoPartida = self.data.get('SuporteConteudoPartida')
# 		ExtensaoChegada = self.data.get('ExtensaoChegada')
# 		TraducaoLegendagem = self.data.get('TraducaoLegendagem')
# 		TraducaoTranscricao  = self.data.get('TraducaoTranscricao')
# 		Transcricao = self.data.get('Transcricao')
# 		RepeticaoInterpretacao = self.data.get('RepeticaoInterpretacao')
# 		DataInicioInterpretacao = self.data.get('DataInicioInterpretacao')
# 		HoraInicioInterpretacao = self.data.get('HoraInicioInterpretacao')
# 		DuracaoInterpretacao = self.data.get('DuracaoInterpretacao')
# 		QuantidadeInterpretes = self.data.get('QuantidadeInterpretes')
# 		ProfissionaisCertificados = self.data.get('ProfissionaisCertificados')
# 		ProfissionaisAutodeclarados = self.data.get('ProfissionaisAutodeclarados')
# 		CoordenadorBilingue = self.data.get('CoordenadorBilingue')
# 		RecepcionistaBilingue = self.data.get('RecepcionistaBilingue')
# 		OperadorSomBilingue = self.data.get('OperadorSomBilingue')
# 		NumeroRecepcionista = str(self.data.get('NumeroRecepcionista'))
# 		GravacaoAudio = self.data.get('GravacaoAudio')
# 		LegendagemAudio = self.data.get('LegendagemAudio')
# 		ModoEntregaGravacao = self.data.get('ModoEntregaGravacao')
# 		EquipamentosSonorizacao = self.data.get('EquipamentosSonorizacao')
# 		NumeroMicrofonesMesa = self.data.get('NumeroMicrofonesMesa')
# 		NumeroMicrofonesSemFio = self.data.get('NumeroMicrofonesSemFio')
# 		NumeroMicrofonesLapela = self.data.get('NumeroMicrofonesLapela')
# 		NumeroMicrofonesRemoviveis = self.data.get('NumeroMicrofonesRemoviveis')
# 		MesaSom = self.data.get('MesaSom')
# 		Retorno = self.data.get('Retorno')
# 		KitDJ = self.data.get('KitDJ')
# 		SideFill = self.data.get('SideFill')
# 		ServicosComplementares = self.data.get('ServicosComplementares')
# 		Televisor = self.data.get('Televisor')
# 		ProjetorMultimidia = self.data.get('ProjetorMultimidia')
# 		AparelhoDVDMP3 = self.data.get('AparelhoDVDMP3')
# 		Notebook = self.data.get('Notebook')
# 		ValidadeProposta = str(self.data.get('ValidadeProposta'))
# 		CodigoPromocional = self.data.get('CodigoPromocional')
# 		ComoConheceu = self.data.get('ComoConheceu')
# 		CEP = self.data.get('CEP')
# 		EnderecoNumero = self.data.get('EnderecoNumero')
# 		EnderecoComplemento = self.data.get('EnderecoBairro')
# 		EnderecoBairro = self.data.get('EnderecoBairro')
# 		EnderecoCidade =self.data.get('EnderecoCidade')
					 
# 		Bdados= models.RelatoriodeDiagnosticoInterpreta(
# 			IdProposta = IdProposta,
# 			TipodeServico = TipodeServico,
# 			LingPartida = LingPartida,
# 			LingChegada = LingChegada,
# 			NomeProprietaria = NomeProprietaria,
# 			NomeOrganizador = NomeOrganizador,
# 			NomeEvento = NomeEvento,
# 			TemaEvento = TemaEvento,
# 			EnderecoEvento = EnderecoEvento,
# 			Risco = Risco,
# 			FusoHorario = FusoHorario,
# 			LinguaConferencia = LinguaConferencia,
# 			NumeroAmbientes = NumeroAmbientes,
# 			TipoEvento = TipoEvento,
# 			NumeroUsuariosFinais = NumeroUsuariosFinais,
# 			Dominio1 = Dominio1,
# 			Dominio2 = Dominio2,
# 			RepeticaoEvento = RepeticaoEvento,
# 			DataInicio = DataInicio,
# 			DataTermino = DataTermino,
# 			LocalInterpretacao = LocalInterpretacao,
# 			DisposicaoAmbiente = DisposicaoAmbiente,
# 			NumeroUsuariosFinaisLocal = NumeroUsuariosFinaisLocal,
# 			Cabine = Cabine,
# 			NumeroReceptores = NumeroReceptores,
# 			NumeroAmbientesExtras = NumeroAmbientesExtras,
# 			SuporteConteudoPartida = SuporteConteudoPartida,
# 			ExtensaoChegada = ExtensaoChegada,
# 			TraducaoLegendagem = TraducaoLegendagem,
# 			TraducaoTranscricao  = TraducaoTranscricao,
# 			Transcricao = Transcricao,
# 			RepeticaoInterpretacao = RepeticaoInterpretacao,
# 			DataInicioInterpretacao = DataInicioInterpretacao,
# 			HoraInicioInterpretacao = HoraInicioInterpretacao,
# 			DuracaoInterpretacao = DuracaoInterpretacao,
# 			QuantidadeInterpretes = QuantidadeInterpretes,
# 			ProfissionaisCertificados = ProfissionaisCertificados,
# 			ProfissionaisAutodeclarados = ProfissionaisAutodeclarados,
# 			CoordenadorBilingue = CoordenadorBilingue,
# 			RecepcionistaBilingue = RecepcionistaBilingue,
# 			OperadorSomBilingue = OperadorSomBilingue,
# 			NumeroRecepcionista = NumeroRecepcionista,
# 			GravacaoAudio = GravacaoAudio,
# 			LegendagemAudio = LegendagemAudio,
# 			ModoEntregaGravacao = ModoEntregaGravacao,
# 			EquipamentosSonorizacao = EquipamentosSonorizacao,
# 			NumeroMicrofonesMesa = NumeroMicrofonesMesa,
# 			NumeroMicrofonesSemFio = NumeroMicrofonesSemFio,
# 			NumeroMicrofonesLapela = NumeroMicrofonesLapela,
# 			NumeroMicrofonesRemoviveis = NumeroMicrofonesRemoviveis,
# 			MesaSom = MesaSom,
# 			Retorno = Retorno,
# 			KitDJ = KitDJ,
# 			SideFill = SideFill,
# 			ServicosComplementares = ServicosComplementares,
# 			Televisor = Televisor,
# 			ProjetorMultimidia = ProjetorMultimidia,
# 			AparelhoDVDMP3 = AparelhoDVDMP3,
# 			Notebook = Notebook,
# 			ValidadeProposta = ValidadeProposta,
# 			CodigoPromocional = CodigoPromocional,
# 			ComoConheceu = ComoConheceu,
# 			CEP = CEP,
# 			EnderecoNumero = EnderecoNumero,
# 			EnderecoComplemento = EnderecoComplemento,
# 			EnderecoBairro = EnderecoBairro,
# 			EnderecoCidade = EnderecoCidade,
# 		)   
# 		Bdados.save()	
			
# 		return Bdados 


# class RelatoriodeDiagnosticoServiForm(forms.Form):

# 	TipodeConteudo = forms.CharField(
# 		widget = forms.SelectMultiple(
# 			attrs={
# 				'class' : 'custom-select', 
# 				'placeholder' : ''
# 			},
# 			choices = var.Conteudo()
# 		),
# 		label='Tipo de conteúdo ',
# 		required = False,
# 	)
	
# 	NumeroPalavras = forms.IntegerField(
# 		widget = forms.NumberInput(), 
# 		label='Número de palavras',
# 		required = False,
# 		min_value = 0,
# 	)
		
# 	DataEntrega = forms.CharField(
# 		widget=forms.TextInput(
# 			attrs={
# 				'class' : 'DataIn form-control', 
# 				'placeholder' : '',
# 				'autocomplete' : 'off'
# 			}
# 		), 
# 		required = False,
# 		label='Data de entrega do serviço (dd/mm/aaaa)'
# 	)

# 	Urgencia = forms.BooleanField(
# 		required = False, 
# 		initial= False,
# 		label='Urgência do serviço', 
# 		widget= forms.CheckboxInput(
# 			attrs={
# 				'class' : 'form',
# 				'placeholder' : ''
# 			}
# 		)
# 	)

# 	DireitosAutorais = forms.BooleanField(
# 		required = False, 
# 		initial= False,
# 		label='Direitos autorais', 
# 		widget= forms.CheckboxInput(
# 			attrs={
# 				'class' : 'form',
# 				'placeholder' : ''
# 			}
# 		)
# 	)
	
# 	ModoEntrega = forms.CharField(
# 		widget = forms.SelectMultiple(
# 			attrs={
# 				'class' : 'custom-select', 
# 				'placeholder' : ''
# 			},
# 			choices = var.ModoEntrega()
# 		),
# 		required = False,
# 		label='Modo de entrega'
# 	)

# 	SuporteConteudoPartida = forms.CharField(
# 		widget = forms.SelectMultiple(
# 			attrs={
# 				'class' : 'custom-select', 
# 				'placeholder' : ''
# 			},
# 			choices = var.SuportePartida()
# 		),
# 		required = False,
# 		label='Suporte do conteúdo (partida)'
# 	)

# 	ExtensaoPartida = forms.CharField(
# 		widget = forms.SelectMultiple(
# 			attrs={
# 				'class' : 'custom-select', 
# 				'placeholder' : ''
# 			},
# 			choices = var.ArquivoPartida2()
# 		),
# 		required = False,
# 		label='Extensão de arquivo (partida)'
# 	)

# 	SuporteConteudoChegada = forms.CharField(
# 		widget = forms.SelectMultiple(
# 			attrs={
# 				'class' : 'custom-select', 
# 				'placeholder' : ''
# 			},
# 			choices = var.SuporteChegada()
# 		),
# 		required = False,
# 		label='Suporte do conteúdo (chegada)'
# 	)

# 	ExtensaoChegada = forms.CharField(
# 		widget = forms.SelectMultiple(
# 			attrs={
# 				'class' : 'custom-select', 
# 				'placeholder' : ''
# 			},
# 			choices = var.ArquivoChegada2()
# 		),
# 		required = False,
# 		label='Extensão de conteúdo (chegada)'
# 	)

		
# 	NumeroPaginas = forms.IntegerField(
# 		widget = forms.NumberInput(), 
# 		label='Diagramação		Número de páginas',
# 		min_value = 0,
# 		required = False,
# 	)
		
# 	DuracaoVideo = forms.CharField(
# 		widget = forms.TextInput(
# 			attrs={
# 				'class' : 'form-control', 
# 				'placeholder' : ''
# 			}
# 		),
# 		required=False,
# 		label='Legendagem		Tempo de Duração do Vídeo :',
# 	)

# 	NomeProprietariaEvento = forms.CharField(
# 		widget = forms.TextInput(
# 			attrs={
# 				'class' : 'form-control', 
# 				'placeholder' : ''
# 			}
# 		), 
# 		required = False,
# 		label='Nome da proprietária do evento'
# 	) 

# 	NomeOrganizadoraEvento = forms.CharField(
# 		widget = forms.TextInput(
# 			attrs={
# 				'class' : 'form-control', 
# 				'placeholder' : ''
# 			}
# 		),
# 		required = False, 
# 		label='Nome da(s) organizadora(s) do evento'
# 	) 

# 	ContatosResponsavelEvento = forms.CharField(
# 		widget = forms.TextInput(
# 			attrs={
# 				'class' : 'form-control', 
# 				'placeholder' : ''
# 			}
# 		), 
# 		required = False,
# 		label='Nome da(s) organizadora(s) do evento'
# 	) 

# 	ContatosResponsavelDiaEvento = forms.CharField(
# 		widget = forms.TextInput(
# 			attrs={
# 				'class' : 'form-control', 
# 				'placeholder' : ''
# 			}
# 		), 
# 		required = False,
# 		label='Nome da(s) organizadora(s) do evento'
# 	) 

# 	NomeEvento = forms.CharField(
# 		widget = forms.TextInput(
# 			attrs={
# 				'class' : 'form-control', 
# 				'placeholder' : ''
# 			}
# 		), 
# 		required = False,
# 		label='Nome do evento'
# 	) 
	
# 	TemaEvento = forms.CharField(
# 		widget = forms.TextInput(
# 			attrs={
# 				'class' : 'form-control', 
# 				'placeholder' : ''
# 			}
# 		), 
# 		required = False,
# 		label='Tema do evento'
# 	) 

# 	CEP = forms.CharField(
# 		widget = forms.TextInput(
# 			attrs={
# 				'class' : 'form-control', 
# 				'placeholder' : ''
# 			}
# 		),
# 		label = 'CEP',
# 	)

# 	EnderecoEvento = forms.CharField(
# 		widget = forms.TextInput(
# 			attrs={
# 				'class' : 'form-control', 
# 				'placeholder' : ''
# 			}
# 		), 
# 		required = False,
# 		label='Endereço de realização do evento'
# 	)
	
# 	EnderecoNumero = forms.IntegerField(
# 		widget = forms.NumberInput(
# 			attrs={
# 				'class' : 'form-control', 
# 				'placeholder' : ''
# 			}
# 		),
# 		label = 'Número'
# 	)

# 	EnderecoComplemento = forms.CharField(
# 		widget = forms.TextInput(
# 			attrs={
# 				'class' : 'form-control',
# 				'placeholder' : ''
# 			}
# 		),
# 		label = 'Complemento'
# 	)

# 	EnderecoBairro = forms.CharField(
# 		widget = forms.TextInput(
# 			attrs={
# 				'class' : 'form-control', 
# 				'placeholder' : ''
# 			}
# 		),
# 		label = 'Bairro'
# 	)

# 	EnderecoCidade = forms.CharField(
# 		widget = forms.TextInput(
# 			attrs={
# 				'class' : 'form-control', 
# 				'placeholder' : ''
# 			}
# 		),
# 		label = 'Cidade'
# 	)

# 	Risco = forms.BooleanField(
# 		required = False, 
# 		initial= False,
# 		label='O local do evento apresenta risco de seguridade ou periculosidade?', 
# 		widget= forms.CheckboxInput(
# 			attrs={
# 				'class' : 'form',
# 				'placeholder' : ''
# 			}
# 		)
# 	)

# 	FusoHorario = forms.CharField(
# 		widget = forms.Select(
# 			attrs={
# 				'class' : 'custom-select', 
# 				'placeholder' : ''
# 			},
# 			choices = var.UTC()
# 		),
# 		label='Fuso horário',
# 		required = False,
		
# 	)

# 	NumeroAmbientes = forms.IntegerField(
# 		widget = forms.NumberInput(), 
# 		label='Número de ambientes',
# 		min_value = 0,
# 		required = False,
# 	)
	
# 	TipoEvento = forms.CharField(
# 		widget = forms.Select(
# 			attrs={
# 				'class' : 'custom-select', 
# 				'placeholder' : ''
# 			},
# 			choices = var.TipoEvento()
# 		),
# 		label='Indique o tipo do evento',
# 		required = False,
# 	)

# 	DataInicio = forms.CharField(
# 		widget=forms.TextInput(
# 			attrs={
# 				'class' : 'DataIn form-control', 
# 				'placeholder' : '',
# 				'autocomplete' : 'off'
# 			}
# 		), 
# 		required = False,
# 		label='Data de Início do evento (dd/mm/aaaa)'
# 	)

# 	DataTermino = forms.CharField(
# 		widget=forms.TextInput(
# 			attrs={
# 				'class' : 'DataIn form-control', 
# 				'placeholder' : '',
# 				'autocomplete' : 'off'
# 			}
# 		), 
# 		required = False,
# 		label='Data de término do evento (dd/mm/aaaa)'
# 	)
	
# 	NumeroUsuariosFinais = forms.IntegerField(
# 		widget = forms.NumberInput(), 
# 		label='Número de usuários finais',
# 		min_value = 0,
# 		required = False,
# 	)
	
# 	RepeticaoEvento = forms.CharField(
# 		widget = forms.Select(
# 			attrs={
# 				'class' : 'custom-select', 
# 				'placeholder' : ''
# 			},
# 			choices = var.RepeticaoCurso()
# 		),
# 		label='Repetição do evento',
# 		required = False,
# 	)

# 	NumeroImagens = forms.IntegerField(
# 		widget = forms.NumberInput(), 
# 		label='Audiodescrição		Número de Imagens',
# 		min_value = 0,
# 		required = False,
# 	)

# 	TempoDuracaoVideoDiagramacao = forms.CharField(
# 		widget = forms.TextInput(
# 			attrs={
# 				'class' : 'form-control', 
# 				'placeholder' : ''
# 			}
# 		),
# 		required=False,
# 		label='Audiodescrição		Tempo de Duração do Vídeo :',
# 	)

# 	NumeroPaginasRedacao = forms.IntegerField(
# 		widget = forms.NumberInput(), 
# 		label='Redação		Número de palavras',
# 		min_value = 0,
# 		required = False,
# 	)

# 	NumeroPaginasDigitacao = forms.IntegerField(
# 		widget = forms.NumberInput(), 
# 		label='Digitação		Número de paginas',
# 		min_value = 0,
# 		required = False,
# 	)
	

# 	TempoDuracaoVideo = forms.CharField(
# 		widget = forms.TextInput(
# 			attrs={
# 				'class' : 'form-control', 
# 				'placeholder' : ''
# 			}
# 		),
# 		required=False,
# 		label='Dublagem 		Tempo de Duração do Vídeo :',	
# 	)
		
# 	TempoDuracaoAudioLocucao = forms.CharField(
# 		widget = forms.TextInput(
# 			attrs={
# 				'class' : 'form-control', 
# 				'placeholder' : ''
# 			}
# 		),
# 		required=False,
# 		label='Locução 		Tempo de Duração do Áudio :',
# 	)
	
# 	ValidadeProposta = forms.CharField(
# 		widget = forms.Select(
# 			attrs={
# 				'class' : 'custom-select', 
# 				'placeholder' : ''
# 			},
# 			choices = var.Validade()
# 		),
# 		label='Validade da proposta',
# 	)

# 	CodigoPromocional = forms.CharField(
# 		widget = forms.TextInput(
# 			attrs={
# 				'class' : 'form-control', 
# 				'placeholder' : ''
# 			}
# 		), 
# 		label='Código promocional',
# 		required = False,
# 	)

# 	ComoConheceu = forms.CharField(
# 		widget = forms.Select(
# 			attrs={
# 				'class' : 'custom-select', 
# 				'placeholder' : ''
# 			},
# 			choices = var.ComoConheceu()
# 		),
# 		required = False, 
# 		label='Como nos conheceu?'
# 	)

# 	def save(self):

# 		IdProposta = self.data.get('IdProposta')
# 		TipodeServico = self.data.get('TipodeServico')
# 		LingPartida =self.data.get('LingPartida')
# 		LingChegada = self.data.get('LingChegada')
# 		TipodeConteudo = self.data.get('TipodeConteudo')
# 		NumeroPalavras = self.data.get('NumeroPalavras')
# 		DataEntrega= self.data.get('DataEntrega')
# 		NumeroPalavras = self.data.get('NumeroPalavras')
# 		Urgencia = self.data.get('Urgencia')
# 		DireitosAutorais = self.data.get('DireitosAutorais')
# 		Dominio1 = self.data.get('Dominio1')
# 		Dominio2 = self.data.get('Dominio2')
# 		ModoEntrega = self.data.get('ModoEntrega')
# 		SuporteConteudoPartida = self.data.get('SuporteConteudoPartida')
# 		ExtensaoPartida = self.data.get ('ExtensaoPartida')
# 		SuporteConteudoChegada = self.data.get('SuporteConteudoChegada')
# 		ExtensaoChegada = self.data.get('ExtensaoChegada')
# 		NumeroPaginas = self.data.get('NumeroPaginas')
# 		DuracaoVideo = self.data.get('DuracaoVideo')
# 		LingPartidaLegenda = self.data.get('LingPartidaLegenda')
# 		LingChegadaLegenda = self.data.get('LingChegadaLegenda')
# 		NomeProprietariaEvento = self.data.get('NomeProprietariaEvento')
# 		ContatosResponsavelEvento = self.data.get('ContatosResponsavelEvento')
# 		NomeOrganizadoraEvento = self.data.get('NomeOrganizadoraEvento')
# 		ContatosResponsavelDiaEvento = self.data.get('ContatosResponsavelDiaEvento')
# 		NomeEvento = self.data.get('NomeEvento')
# 		TemaEvento = self.data.get('TemaEvento')
# 		EnderecoEvento = self.data.get('EnderecoEvento')
# 		Risco = self.data.get('Risco')
# 		FusoHorario = self.data.get('FusoHorario')
# 		LinguaConferencia = self.data.get('LinguaConferencia')
# 		NumeroAmbientes = self.data.get('NumeroAmbientes')
# 		TipoEvento = self.data.get('TipoEvento')
# 		NumeroUsuariosFinais = self.data.get('NumeroUsuariosFinais')
# 		Dominio1Evento = self.data.get('Dominio1Evento')
# 		Dominio2Evento = self.data.get('Dominio2Evento')
# 		RepeticaoEvento = self.data.get('RepeticaoEvento')
# 		DataInicio = self.data.get('DataInicio')
# 		DataTermino = self.data.get('DataTermino')

# 		NumeroImagens = self.data.get('NumeroImagens')
# 		TempoDuracaoVideoDiagramacao = self.data.get('TempoDuracaoVideoDiagramacao')

# 		NumeroPaginasRedacao = self.data.get('NumeroPaginasRedacao')

# 		NumeroPaginasDigitacao = self.data.get('NumeroPaginasDigitacao')

# 		TempoDuracaoVideo = self.data.get('TempoDuracaoVideo')
# 		LingPartidaDublagem = self.data.get('LingPartidaDublagem')
# 		LingChegadaDublagem = self.data.get('LingChegadaDublagem')
	
# 		TempoDuracaoAudioLocucao = self.data.get('TempoDuracaoAudioLocucao')
	
# 		ValidadeProposta = self.data.get('ValidadeProposta')
# 		CodigoPromocional = self.data.get('CodigoPromocional')
# 		ComoConheceu = self.data.get('ComoConheceu')

# 		CEP = self.data.get('CEP')
# 		EnderecoNumero = self.data.get('EnderecoNumero')
# 		EnderecoComplemento = self.data.get('EnderecoBairro')
# 		EnderecoBairro = self.data.get('EnderecoBairro')
# 		EnderecoCidade =self.data.get('EnderecoCidade')
					
# 		Bdados= models.RelatoriodeDiagnosticoServi(
# 			IdProposta = IdProposta,
# 			TipodeServico = TipodeServico,
# 			LingPartida = LingPartida,
# 			LingChegada = LingChegada,
# 			TipodeConteudo = TipodeConteudo,
# 			NumeroPalavras = NumeroPalavras,
# 			DataEntrega = DataEntrega,
# 			Urgencia = Urgencia,
# 			DireitosAutorais = DireitosAutorais,
# 			Dominio1 = Dominio1,
# 			Dominio2 = Dominio2,
# 			ModoEntrega = ModoEntrega,
# 			SuporteConteudoPartida = SuporteConteudoPartida,
# 			ExtensaoPartida = ExtensaoPartida,
# 			SuporteConteudoChegada = SuporteConteudoChegada,
# 			ExtensaoChegada = ExtensaoChegada,
# 			NumeroPaginas = NumeroPaginas,
# 			DuracaoVideo = DuracaoVideo,
# 			LingPartidaLegenda = LingPartidaLegenda,
# 			LingChegadaLegenda = LingChegadaLegenda,
# 			NomeProprietariaEvento = NomeProprietariaEvento,
# 			ContatosResponsavelEvento = ContatosResponsavelEvento,
# 			NomeOrganizadoraEvento = NomeOrganizadoraEvento,
# 			ContatosResponsavelDiaEvento = ContatosResponsavelDiaEvento,
# 			NomeEvento = NomeEvento,
# 			TemaEvento = TemaEvento,
# 			EnderecoEvento = EnderecoEvento,
# 			Risco = Risco,
# 			FusoHorario = FusoHorario,
# 			LinguaConferencia = LinguaConferencia,
# 			NumeroAmbientes = NumeroAmbientes,
# 			TipoEvento = TipoEvento,
# 			NumeroUsuariosFinais = NumeroUsuariosFinais,
# 			Dominio1Evento = Dominio1Evento,
# 			Dominio2Evento = Dominio2Evento,
# 			RepeticaoEvento = RepeticaoEvento,
# 			DataInicio = DataInicio,
# 			DataTermino = DataTermino,
# 			NumeroImagens = NumeroImagens,
# 			TempoDuracaoVideoDiagramacao = TempoDuracaoVideoDiagramacao,
# 			NumeroPaginasRedacao = NumeroPaginasRedacao,
# 			NumeroPaginasDigitacao = NumeroPaginasDigitacao,
# 			TempoDuracaoVideo = TempoDuracaoVideo,
# 			LingPartidaDublagem = LingPartidaDublagem,
# 			LingChegadaDublagem = LingChegadaDublagem,
# 			TempoDuracaoAudioLocucao = TempoDuracaoAudioLocucao,
# 			ValidadeProposta = ValidadeProposta,
# 			CodigoPromocional = CodigoPromocional,
# 			ComoConheceu = ComoConheceu,
# 			CEP = CEP,
# 			EnderecoNumero = EnderecoNumero,
# 			EnderecoComplemento = EnderecoComplemento,
# 			EnderecoBairro = EnderecoBairro,
# 			EnderecoCidade = EnderecoCidade,
# 		)   
# 		Bdados.save()	
		
# 		return Bdados 


class DadosForm(ModelForm):
	
	class Meta:
		model = models.Dados
		fields = ('CatServ' , 'IdiomaTipo', 'Tipo')


class UsuarioLogin(ModelForm):

	class Meta:
		model = User
		fields = [
			'username',
			'password',
			'email',
			'first_name',
			'last_name',
		]
		widgets = {
			'username': forms.TextInput(
				attrs={
					'class' : 'form-control', 
					'placeholder' : 'CPF *',
					'required' : 'required'
				}
			),
			'password': forms.PasswordInput(
				attrs={
					'class' : 'form-control', 
					'placeholder' : 'Senha'
				}
			),
			'email': forms.EmailInput(
				attrs={
					'class' : 'form-control', 
					'placeholder' : 'Email',
					'required' : 'required'
				},
			),
			'first_name': forms.TextInput(
				attrs={
					'class' : 'form-control', 
					'placeholder' : 'Data de Nascimento dd/mm/aaaa *',
					'autocomplete': 'off',
				},
			),
			'last_name': forms.TextInput(
				attrs={
					'class' : 'form-control', 
					'placeholder' : 'Nome Completo *',
					'required' : 'required'
				}
			),
		}
		error_messages = {
			'username': {
				'required': 'Este Campo é Obrigatorio'	
			},
			'password': {
				'required': 'Este Campo é Obrigatorio'	
			},
			'email': {
				'required': 'Escreva um Email Válido'	
			},
			'first_name': {
				'required': 'Este Campo é Obrigatorio'	
			},
			'last_name': {
				'required': 'Este Campo é Obrigatorio'	
			},
		}


class Autenticaform(forms.Form):
	
	Nome = forms.CharField(
		widget = forms.TextInput(
			attrs={
				'class' : 'form-control', 
				'placeholder' : 'CPF'
			}
		),
		label = 'CPF'
	)

	Senha = forms.CharField(
		widget = forms.PasswordInput(
			attrs={
				'class' : 'form-control', 
				'placeholder' : 'Senha'
			}
		),
		label = 'Senha'
	)


# class PropostaClienteForm(ModelForm):

# 	class Meta:
		
# 		model = models.Proposta
# 		fields = ('Nome', 'IdRelatorio', 'IdUsuario', 'Funcionario')
	
# 		widgets = {
# 			'Nome': forms.TextInput(
# 				attrs={
# 					'class' : 'form-control', 
# 					'placeholder' : ''
# 				}
# 			),
			
# 			'IdRelatorio': forms.TextInput(
# 				attrs={
# 					'class' : 'form-control', 
# 					'placeholder' : ''
# 				}
# 			),
# 			'IdUsuario': forms.TextInput(
# 				attrs={
# 					'class' : 'form-control', 
# 					'placeholder' : ''
# 				}
# 			),
# 			'Funcionario': forms.TextInput(
# 				attrs={
# 					'class' : 'form-control', 
# 					'placeholder' : ''
# 				}
# 			),
# 		}
		
# 	def save(self):

# 		Nome = self.data.get('nome')
# 		IdRelatorio = self.data.get('id_pedido')
# 		IdUsuario = self.data.get('id_ru')
# 		Funcionario = ''
					
# 		Bdados = models.Proposta(
# 			Nome = Nome,
# 			IdRelatorio = IdRelatorio,
# 			IdUsuario = IdUsuario,
# 			Funcionario =  Funcionario,
# 		)	
# 		Bdados.save()

# 		return Bdados


class ClausulaForm(forms.Form):

	TipoDocumento = forms.ModelMultipleChoiceField(

		widget = forms.SelectMultiple(
			attrs={
				'class' : 'custom-select Enviar',
				'onclick' : 'EnviaForm()', 
			},
		),
		queryset = models.TipoDocumento.objects.all(),
		label='Tipo de documento', 
	)

	Titulo = forms.ModelMultipleChoiceField(
		widget = forms.SelectMultiple(
			attrs={
				'class' : 'custom-select Enviar',
				'onclick' : 'EnviaForm()', 
			},
		),
		queryset = models.Titulo.objects.all(),
		label='Título',
	)

	SubTituloServico = forms.ModelMultipleChoiceField(
		required = False, 
		widget = forms.SelectMultiple(
			attrs={
				'class' : 'custom-select Enviar',
				'onclick' : 'EnviaForm()', 
			},
		),
		queryset = models.SubTituloServico.objects.all(),
		label="Subtítulo do serviço"
	)

	SubTituloCargo = forms.ModelMultipleChoiceField( 
		widget = forms.SelectMultiple(
			attrs={
				'class' : 'custom-select Enviar',
				'onclick' : 'EnviaForm()', 
			},
		),
		queryset = models.SubTituloCargo.objects.all(),
		required = False,
		label = "Subtítulo do cargo"
	)

	SubTipoDocumento = forms.ModelMultipleChoiceField(
		required = False, 
		widget = forms.SelectMultiple(
			attrs={
				'class' : 'custom-select Enviar',
				'onclick' : 'EnviaForm()', 
			},
		),
		queryset = models.SubTipoDocumento.objects.all(),
		label="Subtipo do documento"
	)

	LinguaClausula = forms.ModelChoiceField(
		widget=forms.Select(
			attrs={
				'class': 'custom-select',
				'placeholder': ''
			},	
		),
		queryset = models.Lingua.objects.all(),
		label='Língua da cláusula'
	)

	Pais = forms.ModelChoiceField(
		widget=forms.Select(
			attrs={
				'class': 'custom-select',
				'placeholder': ''
			},	
		),
		queryset = models.Pais.objects.all(),
		label='País'
	)

	PosicaoDocumento = forms.ModelChoiceField(
		widget=forms.Select(
			attrs={
				'class': 'custom-select',
				'placeholder': ''
			},
		),
		queryset = models.PosicaoDocumento.objects.all(),
		label="Posição da cláusula no documento"
	)

	TipoClausula = forms.ModelChoiceField(
		widget=forms.Select(
			attrs={
				'class': 'custom-select',
				'placeholder': ''
			},	
		),
		queryset = models.TipoClausula.objects.all(),
		label='Tipo de cláusula'
	)
	
	OcultaNomeClausula = forms.BooleanField(
		required = False, 
		initial= False,
		label='Deseja ocultar o nome da cláusula?', 
		widget= forms.CheckboxInput(
			attrs={
				'class' : 'form',
				'placeholder' : ''
			}
		)
	)

	NomeClausula = forms.CharField(
		widget = forms.TextInput(
			attrs={
				'class': 'form-control',
				'placeholder': ''
			}
		),
		label='Nome da cláusula'
	)

	ComentarioClausula = forms.CharField(
		widget = forms.TextInput(
			attrs={
				'class': 'form-control',
				'placeholder': ''
			}
		),
		required=False,
		label='Comentário sobre a cláusula'
	)

	ConteudoClausula = forms.CharField(
		widget = forms.HiddenInput(
			attrs={
				'class': 'form-control',
				'placeholder': ''
			}
		),
		label='Conteudo da Cláusula'
	)
	
	def SalvaRelacao(self, VetorDados, Banco, Relacao):
		try:
			VetorDados.sort()
			# print('proximo valor => ', VetorDados)
			
			for i in VetorDados:
				print (int(i))
				print('Banco')
				print(Banco)
				Banco.add(int(i))
				print ('proximo')
				print ('relação adicionada')
			
			return True
		except:
			print ("erro ao adicionar")
			return False
	
	def save(self):
		
		NomeClausula = self.data.get('NomeClausula')
		ComentarioClausula = self.data.get('ComentarioClausula')
		LinguaClausula = self.data.get('LinguaClausula')
		ConteudoClausula = self.data.get('ConteudoClausula')
		TipoClausula_ = self.data.get('TipoClausula')
		PosicaoDocumento_ = self.data.get('PosicaoDocumento')
		TipoDocumento = self.data.getlist('TipoDocumento')
		Titulo = self.data.getlist('Titulo')
		SubTituloServico = self.data.getlist('SubTituloServico')
		SubTituloCargo = self.data.getlist('SubTituloCargo')
		SubTipoDocumento = self.data.getlist('SubTipoDocumento')
		OcultaNomeClausula = self.data.get('OcultaNomeClausula')
		Pais = self.data.get('Pais')
		 
		print("Salvando")
		print(
			'TipoDocumento', 
			TipoDocumento, 
			'Titulo',
			Titulo,
			'SubTituloServico', 
			SubTituloServico, 
			'SubTituloCargo', 
			SubTituloCargo, 
			'SubTipoDocumento', 
			SubTipoDocumento, 
			sep = '\n' 
		)

		linguapais = models.LinguaPais.objects.get(
			Q(Lingua = LinguaClausula) & 
			Q(Pais = Pais)
		)

		print(
			'linguapais', 
			linguapais.id
		)

		Bdados = models.Clausula(
			NomeClausula = NomeClausula,
			ComentarioClausula = ComentarioClausula,
			LinguaPais = linguapais,
			ConteudoClausula = ConteudoClausula,
			TipoClausula = models.TipoClausula.objects.get(id = TipoClausula_),
			PosicaoDocumento = models.PosicaoDocumento.objects.get(id = PosicaoDocumento_),
			OcultaNomeClausula = OcultaNomeClausula,
		)
		Bdados.save()
		
		TesteTipoDocumento = self.SalvaRelacao(
			TipoDocumento, 
			Bdados.TipoDocumento,
			models.TipoDocumento, 
		)
		TesteTitulo = self.SalvaRelacao(
			Titulo,
			Bdados.Titulo,
			models.Titulo
		)
		TesteSubTituloServico = self.SalvaRelacao(
			SubTituloServico,
			Bdados.SubTituloServico,
			models.SubTituloServico,
		)
		TesteSubTituloCargo = self.SalvaRelacao(
			SubTituloCargo, 
			Bdados.SubTituloCargo,
			models.SubTituloCargo,
		)
		TesteSubTipoDocumento = self.SalvaRelacao(
			SubTipoDocumento, 
			Bdados.SubTipoDocumento,
			models.SubTipoDocumento,
		)

		print (
			TesteTipoDocumento, 
			TesteTitulo, 
			TesteSubTituloServico, 
			TesteSubTituloCargo, 
			TesteSubTipoDocumento, 
			sep = '\n' 
		)
		
		print("Salvo") 

		return Bdados
		# return 'Bdados'
	
	def BuscaClausula(self):

		Busca = models.Clausula.objects.all()
		for relacao in Busca:
			print(relacao.SubTituloCargo.all())
			print(relacao.TipoClausula)
		
		# Busca = models.Clausula.objects.all().values()
		return Busca


# class CriaContratoForm(forms.Form):

# 	TipoDocumento = forms.ModelMultipleChoiceField(

# 		widget = forms.SelectMultiple(
# 			attrs={
# 				'class' : 'custom-select Enviar', 
# 			},
# 		),
# 		queryset = models.TipoDocumento.objects.all(),
# 		label='Tipo de documento', 
# 	)

# 	Titulo = forms.ModelMultipleChoiceField(
# 		widget = forms.SelectMultiple(
# 			attrs={
# 				'class' : 'custom-select Enviar', 
# 			},
# 		),
# 		queryset = models.Titulo.objects.all(),
# 		label='Título',
# 	)

# 	SubTituloServico = forms.ModelMultipleChoiceField(
# 		widget = forms.SelectMultiple(
# 			attrs={
# 				'class' : 'custom-select Enviar', 
# 			},
# 		),
# 		queryset = models.SubTituloServico.objects.all(),
# 		label="Subtítulo do serviço"
# 	)

# 	SubTituloCargo = forms.ModelMultipleChoiceField( 
# 		widget = forms.SelectMultiple(
# 			attrs={
# 				'class' : 'custom-select Enviar', 
# 			},
# 		),
# 		queryset = models.SubTituloCargo.objects.all(),
# 		required = False,
# 		label = "Subtítulo do cargo"
# 	)

# 	SubTipoDocumento = forms.ModelMultipleChoiceField(
# 		widget = forms.SelectMultiple(
# 			attrs={
# 				'class' : 'custom-select Enviar', 
# 			},
# 		),
# 		queryset = models.SubTipoDocumento.objects.all(),
# 		label="Subtipo do documento"
# 	)

# 	LinguaClausula = forms.ModelChoiceField(
# 		widget=forms.Select(
# 			attrs={
# 				'class': 'custom-select',
# 				'placeholder': '',
# 			},	
# 		),
# 		queryset = models.Lingua.objects.all(),
# 		label='Língua da cláusula',
# 	)

# 	Pais = forms.ModelChoiceField(
# 		widget=forms.Select(
# 			attrs={
# 				'class': 'custom-select',
# 				'placeholder': '',
# 			},	
# 		),
# 		queryset = models.Pais.objects.all(),
# 		label='País'
# 	)

# 	TipoClausula = forms.ModelChoiceField(
# 		widget=forms.Select(
# 			attrs={
# 				'class': 'custom-select',
# 				'placeholder': '',
# 			},	
# 		),
# 		queryset = models.TipoClausula.objects.all(),
# 		label='Tipo de cláusula',
# 	)

# 	Contratante = forms.CharField(
# 		widget=forms.TextInput(
# 			attrs={
# 				'class' : 'form-control', 
# 				'placeholder' : '',
# 				'autocomplete' : 'off',
# 				'onblur': 'RetornaParte()',
# 			}
# 		), 
# 		label='Contratante'
# 	)

# 	Contratado = forms.CharField(
# 		widget=forms.TextInput(
# 			attrs={
# 				'class' : 'form-control', 
# 				'placeholder' : '',
# 				'autocomplete' : 'off',
# 				'onblur' : 'RetornaParte()',
# 			}
# 		), 
# 		label='Contratado'
# 	)

# 	# Mudar depois
# 		# Orientação:
# 		# ( x ) Retrato
# 		# ( ) Paisagem
# 		# Tamanho:
# 		# ( x ) A4
# 		# ( ) Carta
# 		# ( ) Ofício
# 		# Papel Timbrado:
# 		# ( x ) Não
# 		# ( ) Sim


# 		# Orientação = (
# 		# 	forms.ChoiceField(
# 		# 		required = False, 
# 		# 		widget = forms.RadioSelect(
# 		# 			attrs={
# 		# 				'class' : 'form',
# 		# 				'name' : 'Orientação',
# 		# 			},
# 		# 		),
# 		# 		# choices= tp[i],
# 		# 		label= 'Orientação',
# 		# 	)
# 		# )

# 		# Tamanho = (
# 		# 	forms.ChoiceField(
# 		# 		required = False, 
# 		# 		widget = forms.RadioSelect(
# 		# 			attrs={
# 		# 				'class' : 'form', 
# 		# 				'name' : 'Tamanho',
# 		# 			},
# 		# 		),
# 		# 		# choices= ,
# 		# 		label= 'Tamanho',
# 		# 	)
# 		# )
		
# 		# PapelTimbrado = (
# 		# 	forms.ChoiceField(
# 		# 		required = False, 
# 		# 		widget = forms.RadioSelect(
# 		# 			attrs={
# 		# 				'class' : 'form', 
# 		# 				'name' : 'Papel Timbrado',
# 		# 			},
# 		# 		),
# 		# 		# choices= ,
# 		# 		label= 'Papel Timbrado',
# 		# 	)
# 		# )

# 	# obsoleta salvar para caso seja util
# 	# def MontadorHTML(self, VetorConteudo):
# 		# # CorpoHTML = TiposDeContratos.objects.filter(TipoNome ='PropostaTeste34').values()[0]
# 		# separador = "<br>"
# 		# Conteudo = separador.join(VetorConteudo)
# 		# # print(Conteudo)
# 		# # print ("--CORPO--")
# 		# # print(CorpoHTML)
# 		# # Corpo = CorpoHTML['HtmlTxt']
# 		# # HTMLFinal = Corpo.format(Conteudo)
# 		# # HTMLTemplate = string.Template(CorpoHTML['HtmlTxt'])
# 		# # HTMLFinal = HTMLTemplate.substitute(pagina1 = Conteudo)
# 		# # print(HTMLFinal)
# 		# # return str(HTMLFinal)
# 		# return str(Conteudo)

# 	# obsoleta salvar para caso seja util
# 	# def LimpaTexto(self, Texto):

# 		# Texto = Texto.replace("[","")
# 		# Texto = Texto.replace("]","")
# 		# Texto = Texto.replace("'","")
# 		# try:
# 		# 	if Texto[0] == ' ':
# 		# 		Texto = Texto[1:len(Texto)]
# 		# except:
# 		# 	print('erro na limpeza')
# 		# return Texto

# 	# obsoleta salvar para caso seja util
# 	# def LimpaVetorTexto(self, Vetor):
# 		# VetorSaida = []
# 		# # if len(Vetor)
# 		# for ConteudoTipo in Vetor:
# 		# 	if ConteudoTipo == []:
# 		# 		pass
# 		# 	else:
# 		# 		VetorSaida.append(self.LimpaTexto(ConteudoTipo))
	
# 		# return VetorSaida

# 	def CriaVetorContratos(self, DadosdoBanco, Busca):
	
# 		BibliotecaDados = {}

# 		for i in range(len(DadosdoBanco)):
# 			for Dado in DadosdoBanco[i]:
# 				print('dado')
# 				print(Dado)
# 				print('TipoDocumento')
# 				print(Dado.TipoDocumento.all())
# 				print('Titulo')
# 				print(Dado.Titulo.all())
# 				print('SubTituloServico')
# 				print(Dado.SubTituloServico.all())
# 				print('SubTituloCargo')
# 				print(Dado.SubTituloCargo.all())
# 				print('SubTipoDocumento')
# 				print(Dado.SubTipoDocumento.all())

# 				for Tipo in Dado.TipoDocumento.all().values():
# 					for Titulo in Dado.Titulo.all().values():
# 						for Servico in Dado.SubTituloServico.all().values():
# 							for Cargo in Dado.SubTituloCargo.all().values():
# 								for SubTipo in Dado.SubTipoDocumento.all().values():
# 									for BuscaTipo in Busca['TipoDocumento']:
# 										for BuscaTitulo in Busca['Titulo']:
# 											for BuscaServico in Busca['SubTituloServico']:
# 												for BuscaCargo in Busca['SubTituloCargo']:
# 													for BuscaSubTipo in Busca['SubTipoDocumento']:
# 														if BuscaTipo == []:
# 															BuscaTipo = 0

# 														if BuscaTitulo == []:
# 															BuscaTitulo = 0

# 														if BuscaServico == [] :
# 															BuscaServico = 0

# 														if BuscaCargo == []:
# 															BuscaCargo = 0

# 														if BuscaSubTipo == []:
# 															BuscaSubTipo = 0
														
# 														# melhorar filtro para mais de dois Item
# 														if (
# 															(Tipo['id'] == int(BuscaTipo) or BuscaTipo == 0)
# 															and 
# 															(Titulo['id'] == int(BuscaTitulo)  or BuscaTitulo == 0)
# 															and 
# 															(Servico['id'] == int(BuscaServico) or BuscaServico == 0)
# 															and 
# 															(Cargo['id'] == int(BuscaCargo) or BuscaCargo == 0)
# 															and 
# 															(SubTipo['id'] == int(BuscaSubTipo)  or BuscaSubTipo == 0)
# 														):
															
# 															BibliotecaDados[
# 																Tipo['Nome'] + 
# 																' ' + 
# 																Titulo['Preposicao']+ 
# 																' ' +
# 																Titulo['Nome'] + 
# 																': ' + 
# 																Servico['Nome'] + 
# 																'. ' + 
# 																Cargo['Nome'] + 
# 																' ' +
# 																SubTipo['Preposicao'] +
# 																' ' + 
# 																SubTipo['Nome'] 
# 															] = [
# 																	Tipo['id'],
# 																	Titulo['id'],
# 																	Servico['id'],
# 																	Cargo['id'],
# 																	SubTipo['id'],
# 																]
# 															print('Banco')
# 															print(Tipo['id'])
# 															print(Titulo['id'])
# 															print(Servico['id'])
# 															print(Cargo['id'])
# 															print(SubTipo['id'])
# 															print('Buscado')	
# 															print(Tipo['id'])
# 															print(Titulo['id'])
# 															print(Servico['id'])
# 															print(Cargo['id'])
# 															print(SubTipo['id'])
# 															print('fim')
																

# 		print ('Tamanho do Vetor de dados')
# 		print(len(sorted(BibliotecaDados)))
# 		return BibliotecaDados
		

# 	# obsoleta salvar para caso seja util	
# 	# def OrganizaTipodeContrato(self, DadosdoBanco, Busca):

# 		# VetorTipo = []
# 		# VetorTitulo = []
# 		# VetorSubTituloServico = []
# 		# VetorSubTituloCargo = []
# 		# VetorSubTipo = []

# 		# cont = 0
# 		# for DadoBuscado in Busca:
# 		# 	if cont == 0:
# 		# 		for Dado in DadoBuscado:
# 		# 			# print (Dado)
# 		# 			VetorParaConcatenar = self.CriaVetorContratos(
# 		# 				Dado, 
# 		# 				DadosdoBanco,
# 		# 			)
# 		# 			VetorTipo = VetorTipo + VetorParaConcatenar
# 		# 	elif cont == 1:
				
# 		# 		for Dado in DadoBuscado:
# 		# 			# print (Dado)
				
# 		# 			VetorParaConcatenar = self.CriaVetorContratos(
# 		# 				Dado, 
# 		# 				DadosdoBanco,
# 		# 			)
# 		# 			VetorTitulo = VetorTitulo + VetorParaConcatenar

# 		# 	elif cont == 2:
# 		# 		for Dado in DadoBuscado:
# 		# 			# print (Dado)
# 		# 			VetorParaConcatenar = self.CriaVetorContratos(
# 		# 				Dado, 
# 		# 				DadosdoBanco,
# 		# 			)
# 		# 			VetorSubTituloServico = VetorSubTituloServico + VetorParaConcatenar
# 		# 	elif cont == 3:
# 		# 		for Dado in DadoBuscado:
# 		# 			# print (Dado)
# 		# 			VetorParaConcatenar = self.CriaVetorContratos(
# 		# 				Dado, 
# 		# 				DadosdoBanco,
# 		# 			)
# 		# 			VetorSubTituloCargo = VetorSubTituloCargo + VetorParaConcatenar

# 		# 	elif cont == 4:
# 		# 		for Dado in DadoBuscado:
# 		# 			# print (Dado)
# 		# 			VetorParaConcatenar = self.CriaVetorContratos(
# 		# 				Dado, 
# 		# 				DadosdoBanco,
# 		# 			)
# 		# 			VetorSubTipo = VetorSubTipo + VetorParaConcatenar

# 		# 	cont = cont + 1
		
		
# 		# # print ('VetorTipo')
# 		# # print (VetorTipo)

# 		# # print (sorted(set(VetorTipo)))

# 		# return (sorted(set(VetorTipo)))

# 	def OrganizaDadosBusca(self, Busca):
# 		print ('Busca dentro do OrfanizaDadosBusca')
# 		print (Busca)

# 		VetorResultado = []
		
# 		for index in Busca:
# 			print(Busca[index])
# 			if Busca[index] == [] or Busca[index] == ['']:
# 				Busca[index] = [[]]
# 			print(Busca[index])

# 		print (Busca)
# 		for Dados0 in Busca['TipoDocumento']:
# 			if Dados0 == []:
# 				Dados0 = ''
# 			print(Dados0)
# 			for Dados1 in Busca['Titulo']:
# 				if Dados1 == []:
# 					Dados1 = ''
# 				print(Dados1)
# 				for Dados2 in Busca['SubTituloServico']:
# 					if Dados2 == []:
# 						Dados2 = ''
# 					print(Dados2)
# 					for Dados3 in Busca['SubTituloCargo']:
# 						if Dados3 == []:
# 							Dados3 = ''
# 						print(Dados3)
# 						for Dados4 in Busca['SubTipoDocumento']:
# 							if Dados4 == []:
# 								Dados4 = ''
# 							print(Dados4)
# 							for Dados5 in Busca['LinguaPais']:
# 								if Dados5 == []:
# 									Dados5 = ''
# 								print(Dados5)
# 								for Dados6 in Busca['TipoClausula']:
# 									if Dados6 == []:
# 										Dados6 = ''
# 									print(Dados6)
# 									print (
# 										'dentro do for organizador\n'
# 									)
# 									VetorResultado.append(
# 										{
# 											'TipoDocumento' : Dados0,
# 											'Titulo' : Dados1,
# 											'SubTituloServico' : Dados2,
# 											'SubTituloCargo' : Dados3,
# 											'SubTipoDocumento' : Dados4,
# 											'LinguaPais' : Dados5,
# 											'TipoClausula' : Dados6,
# 										}
# 									)
		
	
# 		print ('dados organizados')
# 		print(VetorResultado)

# 		return VetorResultado

# 	def Busca(self, DadosBuscados):
# 		DadosdoBanco = models.Clausula.objects.all()
		
# 		for tipo in DadosBuscados:
# 			print(tipo)
			
# 			if ( 
# 				DadosBuscados[tipo] == [[]] or 
# 				DadosBuscados[tipo] == '' or 
# 				DadosBuscados[tipo] == []or 
# 				DadosBuscados[tipo] ==['', '']
# 			):
# 				# print ('vazio')	
# 				pass
# 			else:
# 				if tipo == 'TipoDocumento':
						
# 					DadosdoBanco = DadosdoBanco.filter(
# 						TipoDocumento = DadosBuscados[tipo]
# 					)
				
# 					print ('0')						
# 					# print ('DadosdoBanco')
# 					# print (DadosdoBanco)
# 				elif tipo == 'Titulo':
					
# 					# print ('dados dentro de tipo', tipo)
# 					DadosdoBanco = DadosdoBanco.filter(
# 						Titulo = DadosBuscados[tipo]
# 					)

# 					print ('1')						
# 					# print ('DadosdoBanco')
# 					# print (DadosdoBanco)
# 				elif tipo == 'SubTituloServico':
					
# 					DadosdoBanco = DadosdoBanco.filter(
# 						SubTituloServico = DadosBuscados[tipo]
# 					)
					
# 					print ('2')
# 					# print ('DadosdoBanco')
# 					# print (DadosdoBanco)
# 				elif tipo == 'SubTituloCargo':
					
# 					DadosdoBanco = DadosdoBanco.filter(
# 						SubTituloCargo = DadosBuscados[tipo]
# 					)
					
# 					print ('3')
# 					# print ('DadosdoBanco')
# 					# print (DadosdoBanco)
# 				elif tipo == 'SubTipoDocumento':
					
# 					DadosdoBanco = DadosdoBanco.filter(
# 						SubTipoDocumento = DadosBuscados[tipo]
# 					)

# 					print ('4')
# 					# print ('DadosdoBanco')
# 					# print (DadosdoBanco)
# 				elif tipo == 'LinguaPais':
# 					linguapais = models.LinguaPais.objects.get(
# 						Q(Lingua = DadosBuscados[tipo][0]) & 
# 						Q(Pais = DadosBuscados[tipo][1])
# 					)
# 					DadosdoBanco = DadosdoBanco.filter(
# 						LinguaPais_id = linguapais.id
# 					)
					
# 					print ('5')
# 					# print ('DadosdoBanco')
# 					# print (DadosdoBanco)
# 				elif tipo == 'TipoClausula':
						
# 					DadosdoBanco = DadosdoBanco.filter(
# 						TipoClausula = DadosBuscados[tipo]
# 					)
				
# 					print ('6')
# 					# print ('DadosdoBanco')
# 					# print (DadosdoBanco)


# 		# print ( 'DadosBuscados \n', DadosBuscados)
# 		# print ('DadosdoBanco \n', DadosdoBanco)
		
	
# 		if DadosdoBanco == []:
# 			# print("erro na busca")
# 			return ''
# 		else:
# 			pass
# 			# print ('Busca')
		
# 		# print ('DadosdoBanco\n\n')
# 		# print (DadosdoBanco)

# 		return DadosdoBanco

# 	# obsoleta salvar para caso seja util
# 	# def TiraRepetido(self, ResultadoBusca):
# 		# Dados = []
# 		# ct = 0
# 		# for Conteudo in ResultadoBusca:
# 		# 	# print ('Resultado \n')
# 		# 	# print (Conteudo)
# 		# 	if Conteudo not in Dados:
# 		# 		Dados.append(Conteudo)
# 		# 	else:
# 		# 		ct = ct + 1
		
# 		# print('repetido')
# 		# print (ct)

# 		# # print('\n')
# 		# # for Print in Dados:
# 		# # 	print (Print)
		
# 		# return Dados

# 	def BuscaConteudoClausula(self, Busca):
		
# 		ResultadoBusca = []
# 		VetorParaBusca = self.OrganizaDadosBusca(Busca)
# 		print('BuscaConteudoClausula')
# 		print(VetorParaBusca)

# 		for DadoBuscado in VetorParaBusca:
# 			ResultadoBusca.append(self.Busca(DadoBuscado))

# 		print('Resultado Final da Busca sem Ajuste Fino \n')
				
# 		print(ResultadoBusca)

# 		ListaContratos = self.CriaVetorContratos(ResultadoBusca, Busca) 
# 		print (ListaContratos) 
# 		return ListaContratos

# 	#  continuar a mudar para biblioteca
	