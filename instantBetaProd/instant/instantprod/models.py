from django.db import models
from django.utils import timezone
from xhtml2pdf import pisa
import io
import os
from django.conf import settings
import string
from django.contrib.auth.models import User
from django.template import (
    loader,
    Context,
    Template,
    engines,
    RequestContext,
)



class LanguageCode(models.Model):
	
	CodAlfanumerico = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 100
	)

	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 50
	)

	Descricao = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 255
	)

	Ordem = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		'self',
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.CodAlfanumerico


class PalavraChave(models.Model):
	
	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 255
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Nome


class TipoBancoImagem(models.Model):
	
	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 255
	)

	Principal = models.BooleanField(
		blank = True,
		default = None
	)

	Ordem = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Nome


class BancoImagem(models.Model):
	
	Arquivo = models.TextField(
		null = True,
		blank = True,
		default = None,
		max_length = 1000000
	)

	TipoBancoImagem = models.ForeignKey(
		TipoBancoImagem,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	PalavraChave = models.ForeignKey(
		PalavraChave,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Principal = models.BooleanField(
		blank = True,
		default = None
	)

	NaoVisivel = models.BooleanField(
		blank = True,
		default = None
	)

	ProibirImpressao = models.BooleanField(
		blank = True,
		default = None
	)

	ProibirDownload = models.BooleanField(
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Arquivo


class Continente(models.Model):
	
	CodAlfanumerico = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 10
	)

	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 255
	)

	Gentilico = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 200
	)

	CodigoContinente = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 2
	)

	Ordem = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.CodAlfanumerico


class TipoHemisferio(models.Model):
	
	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 50
	)

	Ordem = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Nome


class AreaGeografica(models.Model):
	
	CodAlfanumerico = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 10
	)

	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 50
	)

	Gentilico = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 50
	)

	Continente = models.ForeignKey(
		Continente,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Ordem = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.CodAlfanumerico


class Pais(models.Model):
	
	CodAlfanumerico = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 10
	)

	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 50
	)

	NomeOficial = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 100
	)

	Gentilico = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 50
	)

	Soberania = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 100
	)

	CodigoISODois = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 2
	)

	CodigoISOTres = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 3
	)

	InternetccTLD = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 12
	)

	DataFundacao = models.DateField(
		null = True,
		blank = True
	)

	Continente = models.ForeignKey(
		Continente,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	TipoHemisferio = models.ForeignKey(
		TipoHemisferio,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	CodigoDiscagem = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 10
	)

	Ordem = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	AreaGeografica = models.ForeignKey(
		AreaGeografica,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	BancoImagem = models.ManyToManyField(
		BancoImagem,
		related_name = 'PaisBancoImagem'
	)

	objects = models.Manager()

	def __str__(self):
		return self.CodAlfanumerico


class Regiao(models.Model):
	
	CodAlfanumerico = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 10
	)

	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 255
	)

	Pais = models.ForeignKey(
		Pais,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Ordem = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.CodAlfanumerico


class TipoOrgaoEmiss(models.Model):
	
	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 255
	)

	Sigla = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 15
	)

	Comentario = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 255
	)

	Visivel = models.BooleanField(
		blank = True,
		default = None
	)

	Pais = models.ForeignKey(
		Pais,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Ordem = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Nome


class Estado(models.Model):
	
	CodAlfanumerico = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 10
	)

	Sigla = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 5
	)

	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 100
	)

	Gentilico = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 50
	)

	Capital = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 50
	)

	DataFundacao = models.DateField(
		null = True,
		blank = True
	)

	Regiao = models.ForeignKey(
		Regiao,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Ordem = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	Pais = models.ForeignKey(
		Pais,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	TipoOrgaoEmiss = models.ManyToManyField(
		TipoOrgaoEmiss,
		related_name = 'EstadoTipoOrgaoEmiss'
	)

	objects = models.Manager()

	def __str__(self):
		return self.CodAlfanumerico


class Cidade(models.Model):
	
	CodAlfanumerico = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 10
	)

	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 255
	)

	Gentilico = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 50
	)

	DataFundacao = models.DateField(
		null = True,
		blank = True
	)

	Estado = models.ForeignKey(
		Estado,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Pais = models.ForeignKey(
		Pais,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	CodigoDiscagem = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 4
	)

	AreaCidade = models.FloatField(
		null = True,
		blank = True,
		default = None
	)

	DensidadeDemografica = models.FloatField(
		null = True,
		blank = True,
		default = None
	)

	Ordem = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	BancoImagem = models.ManyToManyField(
		BancoImagem,
		related_name = 'CidadeBancoImagem'
	)

	objects = models.Manager()

	def __str__(self):
		return self.Nome


class TipoLogradouro(models.Model):
	
	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 50
	)

	Abreviatura = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 15
	)

	Ordem = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Nome


class CodigoEndPostal(models.Model):
	
	CodigoPostal = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 11
	)

	TipoLogradouro = models.ForeignKey(
		TipoLogradouro,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Logradouro = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 255
	)

	ComplementoLogra = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 100
	)

	Bairro = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 120
	)

	Cidade = models.ForeignKey(
		Cidade,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Estado = models.ForeignKey(
		Estado,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Pais = models.ForeignKey(
		Pais,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Latitude = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 30
	)

	Longitude = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 30
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	AreaRestricaoEntregaDiferenciada = models.BooleanField(
		blank = True,
		default = None
	)

	AreaRestricaoEntregaInterna = models.BooleanField(
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.CodigoPostal


class TipoComplemento(models.Model):
	
	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 100
	)

	Abreviatura = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 15
	)

	Ordem = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Nome


class TipoEndereco(models.Model):
	
	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 255
	)

	Ordem = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Nome


class Endereco(models.Model):
	
	Logradouro = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 255
	)

	Numero = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	Complemento = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 255
	)

	CaixaPostal = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 10
	)

	Bairro = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 50
	)

	CodigoEndPostal = models.ForeignKey(
		CodigoEndPostal,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	CodigoPostal = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 20
	)

	TipoEndereco = models.ForeignKey(
		TipoEndereco,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	TipoLogradouro = models.ForeignKey(
		TipoLogradouro,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Regiao = models.ForeignKey(
		Regiao,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Cidade = models.ForeignKey(
		Cidade,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	CidadeNome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 255
	)

	Estado = models.ForeignKey(
		Estado,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Pais = models.ForeignKey(
		Pais,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	PontoReferencia = models.TextField(
		null = True,
		blank = True,
		default = None,
		max_length = 2000
	)

	CopiaComprovante = models.BinaryField(
		null = True,
		blank = True,
		default = None
	)

	Latitude = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 30
	)

	Longitude = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 30
	)

	Ajustelatlong = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 50
	)

	NaoExibirLogradouro = models.BooleanField(
		blank = True,
		default = None
	)

	NaoExibirNumero = models.BooleanField(
		blank = True,
		default = None
	)

	NaoExibirComplemento = models.BooleanField(
		blank = True,
		default = None
	)

	NaoExibirCaixaPostal = models.BooleanField(
		blank = True,
		default = None
	)

	NaoExibirBairro = models.BooleanField(
		blank = True,
		default = None
	)

	NaoExibirPontoReferencia = models.BooleanField(
		blank = True,
		default = None
	)

	NaoExibirLatitude = models.BooleanField(
		blank = True,
		default = None
	)

	NaoExibirLongitude = models.BooleanField(
		blank = True,
		default = None
	)

	NaoExibirEndereco = models.BooleanField(
		blank = True,
		default = None
	)

	NaoExibirLocalizacao = models.BooleanField(
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	TipoComplemento = models.ManyToManyField(
		TipoComplemento,
		related_name = 'EnderecoTipoComplemento'
	)

	BancoImagem = models.ManyToManyField(
		BancoImagem,
		related_name = 'EnderecoBancoImagem'
	)

	objects = models.Manager()

	def __str__(self):
		return self.Logradouro


class TipoContatoTecn(models.Model):
	
	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 200
	)

	Ordem = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	CodioIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Nome


class TipoContato(models.Model):
	
	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 50
	)

	Visivel = models.BooleanField(
		blank = True,
		default = None
	)

	HabilitarPropTecComercial = models.BooleanField(
		blank = True,
		default = None
	)

	TipoContatoTecn = models.ForeignKey(
		TipoContatoTecn,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Ordem = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Nome


class TipoOpTelefonia(models.Model):
	
	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 50
	)

	Codigo = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	Pais = models.ForeignKey(
		Pais,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Ordem = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Nome


class Contato(models.Model):
	
	CodigoDiscagemInternacional = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 4,
		verbose_name = "DDI"
	)

	TipoContato = models.ForeignKey(
		TipoContato,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None,
		verbose_name = "Tipo"
	)

	Pais = models.ForeignKey(
		Pais,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None,
	)

	Cidade = models.ForeignKey(
		Cidade,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	TipoOpTelefonia = models.ForeignKey(
		TipoOpTelefonia,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None,
		verbose_name = "Operadora"
	)

	CodigoDiscagemNacional = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	Identificacao = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 250,
		verbose_name = "Identificação"
	)

	Ramal = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 5
	)

	NomeRecado = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 100
	)

	Principal = models.BooleanField(
		blank = True,
		default = None
	)

	NaoExibirContato = models.BooleanField(
		blank = True,
		default = None,
		verbose_name = "Não exibir contato"
	)

	objects = models.Manager()

	def __str__(self):
		return self.CodigoDiscagemInternacional


class TipoPcDCateg(models.Model):
	
	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 100
	)

	Ordem = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Nome


class TipoDiaSemana(models.Model):
	
	NumeroDiaSemana = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	Ordem = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.NumeroDiaSemana


class TipoHorarioFuncionamento(models.Model):
	
	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 200
	)

	Ordem = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Nome


class HorarioFuncionamento(models.Model):
	
	Fechado = models.BooleanField(
		blank = True,
		default = None
	)

	TipoDiaSemana = models.ForeignKey(
		TipoDiaSemana,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	HoraInicio = models.TimeField(
		null = True,
		blank = True
	)

	HoraFim = models.TimeField(
		null = True,
		blank = True
	)

	TipoHorarioFuncionamento = models.ForeignKey(
		TipoHorarioFuncionamento,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Fechado


class TipoUrl(models.Model):
	
	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 100
	)

	Ordem = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Nome


class Url(models.Model):
	
	Endereco = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 255
	)

	TipoUrl = models.ForeignKey(
		TipoUrl,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Principal = models.BooleanField(
		blank = True,
		default = None
	)

	NaoExibirUrl = models.BooleanField(
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Endereco


class TipoPDV(models.Model):
	
	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 200
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Nome


class PDV(models.Model):
	
	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 200
	)

	TipoPDV = models.ForeignKey(
		TipoPDV,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Url = models.ForeignKey(
		Url,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	DNS = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 50
	)

	MacAddress = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 50
	)

	objects = models.Manager()

	def __str__(self):
		return self.Nome


class ItemTipoArea(models.Model):
	
	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 80
	)

	Ordem = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	CodigoMenu = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 2
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Nome


class Microsite(models.Model):
	
	Endereco = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 200
	)

	NaoExibirMicrosite = models.BooleanField(
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Endereco


class Unidade(models.Model):
	
	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 200
	)

	HomeBased = models.BooleanField(
		blank = True,
		default = None
	)

	Escritorio = models.BooleanField(
		blank = True,
		default = None
	)

	EscolaIdioma = models.BooleanField(
		blank = True,
		default = None
	)

	Endereco = models.ForeignKey(
		Endereco,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	TipoPcDCateg = models.ForeignKey(
		TipoPcDCateg,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Contato = models.ForeignKey(
		Contato,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Microsite = models.ForeignKey(
		Microsite,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	EnderecoIgualSede = models.BooleanField(
		blank = True,
		default = None
	)

	EmailIgualSede = models.BooleanField(
		blank = True,
		default = None
	)

	LimiteFinanceiro = models.FloatField(
		null = True,
		blank = True,
		default = None
	)

	ContatoIgualSede = models.BooleanField(
		blank = True,
		default = None
	)

	MicrositeIgualSede = models.BooleanField(
		blank = True,
		default = None
	)

	PDV = models.ManyToManyField(
		PDV,
		related_name = 'UnidadePDV'
	)

	ItemTipoArea = models.ManyToManyField(
		ItemTipoArea,
		related_name = 'UnidadeItemTipoArea'
	)

	HorarioFuncionamento = models.ManyToManyField(
		HorarioFuncionamento,
		related_name = 'UnidadeHorarioFuncionamento'
	)

	objects = models.Manager()

	def __str__(self):
		return self.Nome


class TipoPromocao(models.Model):
	
	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 255
	)

	Ordem = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	PercentualMensal = models.FloatField(
		null = True,
		blank = True,
		default = None
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Unidade = models.ForeignKey(
		Unidade,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Nome


class TipoProgressao(models.Model):
	
	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 255
	)

	Ordem = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	PercentualMensal = models.FloatField(
		null = True,
		blank = True,
		default = None
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Unidade = models.ForeignKey(
		Unidade,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Nome


class TipoCargo(models.Model):
	
	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 255
	)

	RemuneracaoMensal = models.FloatField(
		null = True,
		blank = True,
		default = None
	)

	TipoProgressao = models.ForeignKey(
		TipoProgressao,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	TipoPromocao = models.ForeignKey(
		TipoPromocao,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Unidade = models.ForeignKey(
		Unidade,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Ordem = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Nome


class TipoDocumento(models.Model):
	
	Ordem = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 600
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Ordem


class TipoSetor(models.Model):
	
	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 255
	)

	Ordem = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Nome


class TipoFuncioTurno(models.Model):
	
	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 255
	)

	IntervaloHorario = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 100
	)

	Unidade = models.ForeignKey(
		Unidade,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Ordem = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Nome


class TipoRelacao(models.Model):
	
	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 255
	)

	Ordem = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Nome


class Cargo(models.Model):
	
	QuantidadesFuncionamentoTurno = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 255
	)

	GraficoGenero = models.BinaryField(
		null = True,
		blank = True,
		default = None
	)

	GraficoFaixaEtaria = models.BinaryField(
		null = True,
		blank = True,
		default = None
	)

	GraficoExperiencia = models.BinaryField(
		null = True,
		blank = True,
		default = None
	)

	TipoCargo = models.ForeignKey(
		TipoCargo,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	TipoSetor = models.ForeignKey(
		TipoSetor,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	TipoFuncioTurno = models.ForeignKey(
		TipoFuncioTurno,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	TipoRelacao = models.ForeignKey(
		TipoRelacao,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	TipoDocumento = models.ManyToManyField(
		TipoDocumento,
		related_name = 'CargoTipoDocumento'
	)

	objects = models.Manager()

	def __str__(self):
		return self.QuantidadesFuncionamentoTurno


class TipoCargoTrad(models.Model):
	
	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 255
	)

	Superior = models.TextField(
		null = True,
		blank = True,
		default = None,
		max_length = 4000
	)

	Atribuicao = models.TextField(
		null = True,
		blank = True,
		default = None,
		max_length = 4000
	)

	Competencia = models.TextField(
		null = True,
		blank = True,
		default = None,
		max_length = 4000
	)

	Ordem = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	Cargo = models.ForeignKey(
		Cargo,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Nome


class TipoCtrlQualidade(models.Model):
	
	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 200
	)

	Nota = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	Ordem = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Nome


class TipoProficienciaLingua(models.Model):
	
	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 100
	)

	Escala = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 50
	)

	TipoCtrlQualidade = models.ForeignKey(
		TipoCtrlQualidade,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Ordem = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Nome


class TipoMoeda(models.Model):
	
	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 50
	)

	Codigo = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	EmUso = models.BooleanField(
		blank = True,
		default = None
	)

	Simbolo = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 3
	)

	ISO = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 13
	)

	Cotacao =  models.DecimalField(
		null = True,
		blank = True,
		default = None,
		max_digits = 10,
		decimal_places = 3
	)

	Tipo = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 1
	)

	DataExclusaoPTAX = models.DateField(
		null = True,
		blank = True
	)

	Ordem = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Pais = models.ManyToManyField(
		Pais,
		related_name = 'TipoMoedaPais'
	)

	objects = models.Manager()

	def __str__(self):
		return self.Nome


class TipoVolumeAcumuladoVenda(models.Model):
	
	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 100
	)

	Ordem = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	Unidade = models.ForeignKey(
		Unidade,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Nome


class TipoDomUmGdArCo(models.Model):
	
	CodAlfanumerico = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 10
	)

	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 100
	)

	Ordem = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.CodAlfanumerico


class TipoDomUmSbArCo(models.Model):
	
	CodAlfanumerico = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 10
	)

	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 100
	)

	Ordem = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.CodAlfanumerico


class TipoDominioUm(models.Model):
	
	CodAlfanumerico = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 10
	)

	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 250
	)

	TipoDomUmGdArCo = models.ForeignKey(
		TipoDomUmGdArCo,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	TipoDomUmSbArCo = models.ForeignKey(
		TipoDomUmSbArCo,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Ordem = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.CodAlfanumerico


class TipoLinguaClasf(models.Model):
	
	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 255
	)

	Ordem = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Nome


class Lingua(models.Model):
	
	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 100
	)

	Visivel = models.BooleanField(
		blank = True,
		default = None
	)

	TipoLinguaClasf = models.ForeignKey(
		TipoLinguaClasf,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Ordem = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Nome


class TipoImposto(models.Model):
	
	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 255
	)

	Visivel = models.BooleanField(
		blank = True,
		default = None
	)

	Pais = models.ForeignKey(
		Pais,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Ordem = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Nome


class TipoNotaComunicacao(models.Model):
	
	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 200
	)

	Ordem = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	Nota = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Nome


class TipoNotaQualidade(models.Model):
	
	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 200
	)

	Ordem = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	Nota = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Nome


class TipoNotaGeral(models.Model):
	
	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 200
	)

	Nota = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	Ordem = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Nome


class CtrlQualidade(models.Model):
	
	Prazo = models.BooleanField(
		blank = True,
		default = None
	)

	AtendeExpectativa = models.BooleanField(
		blank = True,
		default = None
	)

	Indica = models.BooleanField(
		blank = True,
		default = None
	)

	Depoimento = models.TextField(
		null = True,
		blank = True,
		default = None,
		max_length = 200000
	)

	Data = models.DateTimeField(
		null = True,
		blank = True,
		default = None
	)

	TipoNotaGeral = models.ForeignKey(
		TipoNotaGeral,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	TipoNotaComunicacao = models.ForeignKey(
		TipoNotaComunicacao,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	TipoNotaQualidade = models.ForeignKey(
		TipoNotaQualidade,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	TipoCtrlQualidade = models.ForeignKey(
		TipoCtrlQualidade,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Prazo


class TipoMargemLucro(models.Model):
	
	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 200
	)

	Ordem = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Nome


class MargemLucro(models.Model):
	
	Aliquota =  models.DecimalField(
		null = True,
		blank = True,
		default = None,
		max_digits = 5,
		decimal_places = 3
	)

	Unidade = models.ForeignKey(
		Unidade,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	TipoMargemLucro = models.ForeignKey(
		TipoMargemLucro,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Aliquota


class Titulo(models.Model):
	
	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 200
	)

	Ordem = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	Preposicao = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 50
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Nome


class SubTituloServico(models.Model):
	
	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 200
	)

	Ordem = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	Preposicao = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 50
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Nome


class SubTipoDocumento(models.Model):
	
	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 200
	)

	Ordem = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	Preposicao = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 50
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Nome


class ItemCategoria(models.Model):
	
	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 200
	)

	Ordem = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	ItemTipoArea = models.ForeignKey(
		ItemTipoArea,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	BancoImagem = models.ForeignKey(
		BancoImagem,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Nome


class TipoDomDoisSec(models.Model):
	
	CodAlfanumerico = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 10
	)

	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 200
	)

	Ordem = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.CodAlfanumerico


class TipoDomDoisDiv(models.Model):
	
	CodAlfanumerico = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 10
	)

	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 200
	)

	Ordem = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.CodAlfanumerico


class TipoDomDoisGrup(models.Model):
	
	CodAlfanumerico = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 10
	)

	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 200
	)

	Ordem = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.CodAlfanumerico


class TipoDomDoisClas(models.Model):
	
	CodAlfanumerico = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 10
	)

	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 200
	)

	Ordem = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.CodAlfanumerico


class TipoDominioDois(models.Model):
	
	CodAlfanumerico = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 10
	)

	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 200
	)

	TipoDomDoisSec = models.ForeignKey(
		TipoDomDoisSec,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	TipoDomDoisDiv = models.ForeignKey(
		TipoDomDoisDiv,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	TipoDomDoisGrup = models.ForeignKey(
		TipoDomDoisGrup,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	TipoDomDoisClas = models.ForeignKey(
		TipoDomDoisClas,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Ordem = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.CodAlfanumerico


class Funcao(models.Model):
	
	QuantidadesFuncionamentoTurno = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 255
	)

	PercentGratificMensalAdicional =  models.DecimalField(
		null = True,
		blank = True,
		default = None,
		max_digits = 5,
		decimal_places = 3
	)

	GraficoGenero = models.BinaryField(
		null = True,
		blank = True,
		default = None
	)

	GraficoFaixaEtaria = models.BinaryField(
		null = True,
		blank = True,
		default = None
	)

	GraficoExperiencia = models.BinaryField(
		null = True,
		blank = True,
		default = None
	)

	TipoCargo = models.ForeignKey(
		TipoCargo,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	TipoSetor = models.ForeignKey(
		TipoSetor,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	TipoFuncioTurno = models.ForeignKey(
		TipoFuncioTurno,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.QuantidadesFuncionamentoTurno


class TipoExtCategoria(models.Model):
	
	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 255
	)

	Ordem = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Nome


class TipoExtensao(models.Model):
	
	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 200
	)

	TipoExtCategoria = models.ForeignKey(
		TipoExtCategoria,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Ordem = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Nome


class CodigoValidacao(models.Model):
	
	Codigo = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 30
	)

	TipoDocumento = models.ForeignKey(
		TipoDocumento,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Codigo


class Imposto(models.Model):
	
	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 200
	)

	Aliquota =  models.DecimalField(
		null = True,
		blank = True,
		default = None,
		max_digits = 5,
		decimal_places = 3
	)

	TipoImposto = models.ForeignKey(
		TipoImposto,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Cidade = models.ForeignKey(
		Cidade,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Estado = models.ForeignKey(
		Estado,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Pais = models.ForeignKey(
		Pais,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Lingua = models.ForeignKey(
		Lingua,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Nome


class PadraoDocumento(models.Model):
	
	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 200
	)

	TipoDocumento = models.ForeignKey(
		TipoDocumento,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Titulo = models.ForeignKey(
		Titulo,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	SubTituloServico = models.ForeignKey(
		SubTituloServico,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	TipoCargoTrad = models.ForeignKey(
		TipoCargoTrad,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	SubTipoDocumento = models.ForeignKey(
		SubTipoDocumento,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Nome


class BancoArquivo(models.Model):
	
	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 200
	)

	CodigoAgrupamento = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	TipoExtensao = models.ForeignKey(
		TipoExtensao,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	DataCriacao = models.DateTimeField(
		null = True,
		blank = True,
		default = None
	)

	Arquivo = models.BinaryField(
		null = True,
		blank = True,
		default = None
	)

	CodigoValidacao = models.ForeignKey(
		CodigoValidacao,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	ProibirImpressao = models.BooleanField(
		blank = True,
		default = None
	)

	ProibirDownload = models.BooleanField(
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Nome


class Item(models.Model):
	
	Consignavel = models.BooleanField(
		blank = True,
		default = None
	)

	NaoExibirUrl = models.BooleanField(
		blank = True,
		default = None
	)

	Indisponivel = models.BooleanField(
		blank = True,
		default = None
	)

	TipoDominioUm = models.ForeignKey(
		TipoDominioUm,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	TipoDominioDois = models.ForeignKey(
		TipoDominioDois,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	MargemLucro = models.ForeignKey(
		MargemLucro,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	ParLinguaExigido = models.BooleanField(
		blank = True,
		default = None
	)

	ExisteItemModelo = models.BooleanField(
		blank = True,
		default = None
	)

	ItemCategoria = models.ForeignKey(
		ItemCategoria,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	PadraoDocumento = models.ManyToManyField(
		PadraoDocumento,
		related_name = 'ItemPadraoDocumento'
	)

	Imposto = models.ManyToManyField(
		Imposto,
		related_name = 'ItemImposto'
	)

	Funcao = models.ManyToManyField(
		Funcao,
		related_name = 'ItemFuncao'
	)

	CtrlQualidade = models.ManyToManyField(
		CtrlQualidade,
		related_name = 'ItemCtrlQualidade'
	)

	BancoImagem = models.ManyToManyField(
		BancoImagem,
		related_name = 'ItemBancoImagem'
	)

	BancoArquivo = models.ManyToManyField(
		BancoArquivo,
		related_name = 'ItemBancoArquivo'
	)

	objects = models.Manager()

	def __str__(self):
		return self.Consignavel


class CapacidadeDiaria(models.Model):
	
	Descricao = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 255
	)

	Quantidade = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Item = models.ManyToManyField(
		Item,
		related_name = 'CapacidadeDiariaItem'
	)

	objects = models.Manager()

	def __str__(self):
		return self.Descricao


class TipoMedidaServ(models.Model):
	
	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 100
	)

	Ordem = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Nome


class TipoMedida(models.Model):
	
	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 255
	)

	Ordem = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	TipoMedidaServ = models.ManyToManyField(
		TipoMedidaServ,
		related_name = 'TipoMedidaTipoMedidaServ'
	)

	objects = models.Manager()

	def __str__(self):
		return self.Nome


class TipoCompLingua(models.Model):
	
	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 200
	)

	Ordem = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Nome


class TipoAnoInicioAtuacao(models.Model):
	
	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 255
	)

	Ordem = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Nome


class Valor(models.Model):
	
	ValorIdeal =  models.DecimalField(
		null = True,
		blank = True,
		default = None,
		max_digits = 7,
		decimal_places = 3
	)

	MedidaValorIdeal = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	NaoVisivelValorIdeal = models.BooleanField(
		blank = True,
		default = None
	)

	ValorMinimo =  models.DecimalField(
		null = True,
		blank = True,
		default = None,
		max_digits = 7,
		decimal_places = 3
	)

	MedidaValorMinimo = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	NaoVisivelValorMinimo = models.BooleanField(
		blank = True,
		default = None
	)

	ValorUrgencia =  models.DecimalField(
		null = True,
		blank = True,
		default = None,
		max_digits = 7,
		decimal_places = 3
	)

	MedidaValorUrgencia = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	NaoVisivelValorUrgencia = models.BooleanField(
		blank = True,
		default = None
	)

	AceitoNegociarValorMenor = models.BooleanField(
		blank = True,
		default = None
	)

	AplicarTodosParesidiomas = models.BooleanField(
		blank = True,
		default = None
	)

	AceitoTrabalhosSemLucro = models.BooleanField(
		blank = True,
		default = None
	)

	TipoProficienciaLingua = models.ForeignKey(
		TipoProficienciaLingua,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	NaoVisivelValorOutorga = models.BooleanField(
		blank = True,
		default = None
	)

	DisponivelAtendimentoPcD = models.BooleanField(
		blank = True,
		default = None
	)

	TipoCargoTrad = models.ForeignKey(
		TipoCargoTrad,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	TipoMedida = models.ForeignKey(
		TipoMedida,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	TipoMoeda = models.ForeignKey(
		TipoMoeda,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	TipoAnoInicioAtuacao = models.ForeignKey(
		TipoAnoInicioAtuacao,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	CapacidadeDiaria = models.ForeignKey(
		CapacidadeDiaria,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	TipoVolumeAcumuladoVenda = models.ForeignKey(
		TipoVolumeAcumuladoVenda,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	TipoCompLingua = models.ForeignKey(
		TipoCompLingua,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.ValorIdeal


class TipoFuncaoTrad(models.Model):
	
	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 255
	)

	Superior = models.TextField(
		null = True,
		blank = True,
		default = None,
		max_length = 4000
	)

	Atribuicao = models.TextField(
		null = True,
		blank = True,
		default = None,
		max_length = 4000
	)

	Competencia = models.TextField(
		null = True,
		blank = True,
		default = None,
		max_length = 4000
	)

	Funcao = models.ForeignKey(
		Funcao,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Ordem = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Nome


class PosicaoClausulaDocumento(models.Model):
	
	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 200
	)

	Ordem = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Nome


class TipoClausula(models.Model):
	
	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 200
	)

	Ordem = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Nome


class Clausula(models.Model):
	
	NomeClausula = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 300
	)

	ConteudoClausula = models.TextField(
		null = True,
		blank = True,
		default = None,
		max_length = 4000
	)

	ComentarioClausula = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 600
	)

	DataCadastro = models.DateTimeField(
		null = True,
		blank = True,
		default = None
	)

	OcultarNomeClausula = models.BooleanField(
		blank = True,
		default = None
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	Minuta = models.BooleanField(
		blank = True,
		default = None
	)

	PosicaoClausulaDocumento = models.ForeignKey(
		PosicaoClausulaDocumento,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	TipoClausula = models.ForeignKey(
		TipoClausula,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Titulo = models.ManyToManyField(
		Titulo,
		related_name = 'ClausulaTitulo'
	)

	TipoFuncaoTrad = models.ManyToManyField(
		TipoFuncaoTrad,
		related_name = 'ClausulaTipoFuncaoTrad'
	)

	TipoDocumento = models.ManyToManyField(
		TipoDocumento,
		related_name = 'ClausulaTipoDocumento'
	)

	TipoCargoTrad = models.ManyToManyField(
		TipoCargoTrad,
		related_name = 'ClausulaTipoCargoTrad'
	)

	SubTituloServico = models.ManyToManyField(
		SubTituloServico,
		related_name = 'ClausulaSubTituloServico'
	)

	SubTipoDocumento = models.ManyToManyField(
		SubTipoDocumento,
		related_name = 'ClausulaSubTipoDocumento'
	)

	objects = models.Manager()

	def __str__(self):
		return self.NomeClausula


class TipoIdentificacao(models.Model):
	
	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 255
	)

	Sigla = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 15
	)

	Comentario = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 255
	)

	Visivel = models.BooleanField(
		blank = True,
		default = None
	)

	AceitoComoIdentidade = models.BooleanField(
		blank = True,
		default = None
	)

	UserName = models.BooleanField(
		blank = True,
		default = None
	)

	Ordem = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	Unidade = models.ForeignKey(
		Unidade,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Pais = models.ForeignKey(
		Pais,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Nome


class Identificacao(models.Model):
	
	Numero = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 20,
		verbose_name = "N° do Documento"
	)

	TipoIdentificacao = models.ForeignKey(
		TipoIdentificacao,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	TipoOrgaoEmiss = models.ForeignKey(
		TipoOrgaoEmiss,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	ValidadeData = models.DateField(
		null = True,
		blank = True
	)

	Estado = models.ForeignKey(
		Estado,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Pais = models.ForeignKey(
		Pais,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	EmissaoPrimeiraData = models.DateField(
		null = True,
		blank = True
	)

	EmissaoAtualData = models.DateField(
		null = True,
		blank = True
	)

	DataCadastro = models.DateTimeField(
		null = True,
		blank = True,
		default = None
	)

	BancoImagem = models.ManyToManyField(
		BancoImagem,
		related_name = 'IdentificacaoBancoImagem'
	)

	objects = models.Manager()

	def __str__(self):
		return self.Numero


class TipoSituacao(models.Model):
	
	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 50
	)

	Ordem = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Nome


class TipoCargoProjeto(models.Model):
	
	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 50
	)

	Ordem = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Nome


class TipoVinculo(models.Model):
	
	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 200
	)

	Ordem = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Nome


class TipoCtrlPrazo(models.Model):
	
	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 200
	)

	Ordem = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	Recorrencia = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 255
	)

	Quantidade = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Unidade = models.ForeignKey(
		Unidade,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Nome


class CtrlPrazo(models.Model):
	
	TempoInicio = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	TempoFim = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	TipoCtrlPrazo = models.ForeignKey(
		TipoCtrlPrazo,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.TempoInicio


class Projeto(models.Model):
	
	Titulo = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 100
	)

	DescricaoProjeto = models.TextField(
		null = True,
		blank = True,
		default = None,
		max_length = 4000
	)

	CtrlQualidade = models.ForeignKey(
		CtrlQualidade,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Url = models.ForeignKey(
		Url,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	ValorProjeto = models.FloatField(
		null = True,
		blank = True,
		default = None
	)

	TipoSituacao = models.ForeignKey(
		TipoSituacao,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	DataInicio = models.DateField(
		null = True,
		blank = True
	)

	DataFim = models.DateField(
		null = True,
		blank = True
	)

	CargaHoraria = models.FloatField(
		null = True,
		blank = True,
		default = None
	)

	TipoCargoProjeto = models.ForeignKey(
		TipoCargoProjeto,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	TipoVinculo = models.ForeignKey(
		TipoVinculo,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	VinculoEmpregaticio = models.BooleanField(
		blank = True,
		default = None
	)

	Freelance = models.BooleanField(
		blank = True,
		default = None
	)

	EquipeProjeto = models.TextField(
		null = True,
		blank = True,
		default = None,
		max_length = 4000
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	CtrlPrazo = models.ManyToManyField(
		CtrlPrazo,
		related_name = 'ProjetoCtrlPrazo'
	)

	objects = models.Manager()

	def __str__(self):
		return self.Titulo


class Outorga(models.Model):
	
	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	Item = models.ForeignKey(
		Item,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.CodigoIDezoitoN


class TipoEmail(models.Model):
	
	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 100
	)

	Ordem = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Nome


class Email(models.Model):
	
	Endereco = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 150
	)

	TipoEmail = models.ForeignKey(
		TipoEmail,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	NaoResponda = models.BooleanField(
		blank = True,
		default = None
	)

	Principal = models.BooleanField(
		blank = True,
		default = None
	)

	NaoExibirEmail = models.BooleanField(
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Endereco


class TipoDataDiaCard(models.Model):
	
	DiaCard = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	DiaExtMasc = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 20
	)

	Ordem = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.DiaCard


class TipoDataAnoCard(models.Model):
	
	AnoCard = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	AnoExtMasc = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 80
	)

	Ordem = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.AnoCard


class TipoRedeSocial(models.Model):
	
	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 100
	)

	Visivel = models.BooleanField(
		blank = True,
		default = None
	)

	Unidade = models.ForeignKey(
		Unidade,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Ordem = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Nome


class RedeSocial(models.Model):
	
	Endereco = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 250
	)

	TipoRedeSocial = models.ForeignKey(
		TipoRedeSocial,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Principal = models.BooleanField(
		blank = True,
		default = None
	)

	NaoExibirRedeSocial = models.BooleanField(
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Endereco


class TipoPronomeTratamento(models.Model):
	
	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 50
	)

	Unidade = models.ForeignKey(
		Unidade,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Ordem = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Nome


class Referencia(models.Model):
	
	TipoPronomeTratamento = models.ForeignKey(
		TipoPronomeTratamento,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 200
	)

	Empresa = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 150
	)

	Email = models.ForeignKey(
		Email,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Contato = models.ForeignKey(
		Contato,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	TipoDiaSemana = models.ForeignKey(
		TipoDiaSemana,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Hora = models.TimeField(
		null = True,
		blank = True
	)

	objects = models.Manager()

	def __str__(self):
		return self.TipoPronomeTratamento


class TipoAreaGeoAtu(models.Model):
	
	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 200
	)

	Unidade = models.ForeignKey(
		Unidade,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Ordem = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	Estado = models.ForeignKey(
		Estado,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Pais = models.ForeignKey(
		Pais,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	CodigoEndPostal = models.ManyToManyField(
		CodigoEndPostal,
		related_name = 'TipoAreaGeoAtuCodigoEndPostal'
	)

	objects = models.Manager()

	def __str__(self):
		return self.Nome



class TipoFiliacao(models.Model):
	
	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 100
	)

	Ordem = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Nome


class OrdemPagamentoBrasil(models.Model):
	
	NomeSacador = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 100
	)

	Identificacao = models.ForeignKey(
		Identificacao,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	User = models.ForeignKey(
		User,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	TipoFiliacao = models.ForeignKey(
		TipoFiliacao,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	NomeFiliacao = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 100
	)

	objects = models.Manager()

	def __str__(self):
		return self.NomeSacador


class QRCode(models.Model):
	
	Codigo = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 255
	)

	BancoImagem = models.ForeignKey(
		BancoImagem,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Codigo


class TipoMetodoPgto(models.Model):
	
	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 255
	)

	Visivel = models.BooleanField(
		blank = True,
		default = None
	)

	Pais = models.ForeignKey(
		Pais,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Ordem = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Nome


class TipoBanco(models.Model):
	
	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 100
	)

	CodigoCompensacao = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 10
	)

	Url = models.ForeignKey(
		Url,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Ordem = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	Pais = models.ForeignKey(
		Pais,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Nome


class TipoConta(models.Model):
	
	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 100
	)

	Ordem = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Nome


class DadoBancario(models.Model):
	
	Agencia = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 50
	)

	TipoBanco = models.ForeignKey(
		TipoBanco,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	TipoConta = models.ForeignKey(
		TipoConta,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Conta = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 100
	)

	DV = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 5
	)

	objects = models.Manager()

	def __str__(self):
		return self.Agencia


class TipoFaturacao(models.Model):
	
	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 200
	)

	Ordem = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	TipoImposto = models.ManyToManyField(
		TipoImposto,
		related_name = 'TipoFaturacaoTipoImposto'
	)

	objects = models.Manager()

	def __str__(self):
		return self.Nome


class TipoCriptomoeda(models.Model):
	
	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 50
	)

	Codigo = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 6
	)

	ValorMercado = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 10
	)

	PrecoReal = models.FloatField(
		null = True,
		blank = True,
		default = None
	)

	VolumeVinteQuatroHoras = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 10
	)

	VariacaoVinteQuatroHoras = models.FloatField(
		null = True,
		blank = True,
		default = None
	)

	Unidade = models.ForeignKey(
		Unidade,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Ordem = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Nome


class Criptomoeda(models.Model):
	
	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 255
	)

	TipoCriptomoeda = models.ForeignKey(
		TipoCriptomoeda,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	NumeroCarteira = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	Url = models.ForeignKey(
		Url,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Carteira = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Nome


class TipoPrimeiroDiaSemana(models.Model):
	
	Descricao = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 200
	)

	TipoDiaSemana = models.ForeignKey(
		TipoDiaSemana,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Ordem = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Descricao


class TipoDispHoraSemana(models.Model):
	
	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 200
	)

	Unidade = models.ForeignKey(
		Unidade,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Ordem = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Nome


class TipoFacilidade(models.Model):
	
	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 255
	)

	BancoImagem = models.ForeignKey(
		BancoImagem,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Unidade = models.ForeignKey(
		Unidade,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Ordem = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Nome


class TipoSegmentoInteresse(models.Model):
	
	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 255
	)

	Unidade = models.ForeignKey(
		Unidade,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Ordem = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Nome


class TipoDataMesCard(models.Model):
	
	MesCard = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	Mes = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 20
	)

	Ordem = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.MesCard


class TipoTurnoTrab(models.Model):
	
	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 50
	)

	Unidade = models.ForeignKey(
		Unidade,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Ordem = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Nome


class DispTurnoPreferido(models.Model):
	
	TipoTurnoTrab = models.ForeignKey(
		TipoTurnoTrab,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	TipoDiaSemana = models.ForeignKey(
		TipoDiaSemana,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.TipoTurnoTrab


class TipoAmenidade(models.Model):
	
	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 255
	)

	BancoImagem = models.ForeignKey(
		BancoImagem,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Unidade = models.ForeignKey(
		Unidade,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Ordem = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Nome


class TipoPagamentoOnline(models.Model):
	
	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 100
	)

	Unidade = models.ForeignKey(
		Unidade,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Ordem = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Nome


class PagamentoOnline(models.Model):
	
	Conta = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 200
	)

	TipoPagamentoOnline = models.ForeignKey(
		TipoPagamentoOnline,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Conta


class TipoMarcador(models.Model):
	
	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 200
	)

	Ordem = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Nome


class DispDiaPreferido(models.Model):
	
	TipoDiaSemana = models.ForeignKey(
		TipoDiaSemana,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.TipoDiaSemana


class TipoPerfilConta(models.Model):
	
	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 200
	)

	Ordem = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Nome


class TipoEmpresa(models.Model):
	
	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 100
	)

	Unidade = models.ForeignKey(
		Unidade,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Ordem = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Nome


class TipoBandeiraCartao(models.Model):
	
	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 50
	)

	Ordem = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Nome


class CartaoCredito(models.Model):
	
	Numero = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 16
	)

	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 50
	)

	Validade = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 4
	)

	Seguranca = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	TipoBandeiraCartao = models.ForeignKey(
		TipoBandeiraCartao,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Numero


class PersonificacaoDominio(models.Model):
	
	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 200
	)

	Dns = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	Ip = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 128
	)

	objects = models.Manager()

	def __str__(self):
		return self.Nome


class TipoSocio(models.Model):
	
	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 200
	)

	Ordem = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Nome


class QuadroSocio(models.Model):
	
	Percentual = models.FloatField(
		null = True,
		blank = True,
		default = None
	)

	TipoSocio = models.ForeignKey(
		TipoSocio,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Percentual


class TipoFerramentaIntegracao(models.Model):
	
	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 200
	)

	Ordem = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Nome


class Integracao(models.Model):
	
	Codigo = models.TextField(
		null = True,
		blank = True,
		default = None,
		max_length = 200000
	)

	TipoFerramentaIntegracao = models.ForeignKey(
		TipoFerramentaIntegracao,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Codigo


class TransfSWIFT(models.Model):
	
	Codigo = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	NumeroConta = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	NomeTitulaConta = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 100
	)

	NomeBanco = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 200
	)

	objects = models.Manager()

	def __str__(self):
		return self.Codigo


class TransfItalia(models.Model):
	
	ABI = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 100
	)

	CAB = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 100
	)

	NumeroContaItalia = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	IBAN = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 100
	)

	BIC = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 100
	)

	NomeTitular = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 100
	)

	objects = models.Manager()

	def __str__(self):
		return self.ABI


class TransfUniaoEuropeia(models.Model):
	
	VatId = models.BooleanField(
		blank = True,
		default = None
	)

	CodigoFiscal = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.VatId


class EsquemaCor(models.Model):
	
	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 200
	)

	CorFonteCabecalhoTopo = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 7
	)

	CorFundoCabecalhoTopo = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 7
	)

	CorFonteCabecalho = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 7
	)

	CorFundoCabecalho = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 7
	)

	CorCabecalhoMenu = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 7
	)

	CorFonteCabecalhoMenu = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 7
	)

	CorFundoCabelhacoMenu = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 7
	)

	CorFontePrincipal = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 7
	)

	CorFundoPrincipal = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 7
	)

	CorFonteRodape = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 7
	)

	CorFundoRodape = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 7
	)

	CorFonteRodapeMenu = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 7
	)

	CorFundoRodapeMenu = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 7
	)

	CorFonteRodapeBase = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 7
	)

	CorFundoRodapeBase = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 7
	)

	objects = models.Manager()

	def __str__(self):
		return self.Nome


class SaldoMensagem(models.Model):
	
	SaldoAtual = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	SaldoAposEnvio = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.SaldoAtual


class RanqueamentoGeral(models.Model):
	
	TipoServicoLinguisticoPrestado = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	MediaRecebQualidServPrestado = models.FloatField(
		null = True,
		blank = True,
		default = None
	)

	MediaRecebPrazoServPrestado = models.FloatField(
		null = True,
		blank = True,
		default = None
	)

	IdiomaOrigemDestinoLingaMatern = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	NumeroParticipacaoProjeto = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	DominioUmProxAreaConhecimento = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	DominioDoisProxSetorEconomico = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	FormAcadem = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	CapacidadeDiariaTrabalho = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	CertificacoeConquistada = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	PrecoCadastradoCargo = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	ProximidadeLocalServico = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	Peso = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	Nota = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	Media = models.FloatField(
		null = True,
		blank = True,
		default = None
	)

	MediaGeral = models.FloatField(
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.TipoServicoLinguisticoPrestado


class Notificacao(models.Model):
	
	AceiteNotificacaoEmpresa = models.BooleanField(
		blank = True,
		default = None
	)

	AceiteNotificacaoExterna = models.BooleanField(
		blank = True,
		default = None
	)

	AceiteNotificacaoCaridade = models.BooleanField(
		blank = True,
		default = None
	)

	AceiteNotificCompartilhamento = models.BooleanField(
		blank = True,
		default = None
	)

	AceiteNotificacaoNoticias = models.BooleanField(
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.AceiteNotificacaoEmpresa


class Comissao(models.Model):
	
	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 200
	)

	Percentual = models.FloatField(
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Nome


class TipoRegimTribut(models.Model):
	
	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 100
	)

	Ordem = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Nome


class TipoEmpresaTamanho(models.Model):
	
	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 255
	)

	Ordem = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Nome


class TipoContrib(models.Model):
	
	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 100
	)

	Ordem = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Nome


class Empresa(models.Model):
	
	NomeEmpresarial = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 255
	)

	NomeFantasia = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 255
	)

	Sigla = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 15
	)

	Cnae = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 10
	)

	IsentoIE = models.BooleanField(
		blank = True,
		default = None
	)

	VIP = models.BooleanField(
		blank = True,
		default = None
	)

	SetorComercial = models.BooleanField(
		blank = True,
		default = None
	)

	TipoEmpresa = models.ForeignKey(
		TipoEmpresa,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	TipoRegimTribut = models.ForeignKey(
		TipoRegimTribut,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	TipoEmpresaTamanho = models.ForeignKey(
		TipoEmpresaTamanho,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	TipoContrib = models.ForeignKey(
		TipoContrib,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	TipoDataDiaCard = models.ForeignKey(
		TipoDataDiaCard,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	TipoDataMesCard = models.ForeignKey(
		TipoDataMesCard,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	TipoDataAnoCard = models.ForeignKey(
		TipoDataAnoCard,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	PreferenciaFiscalInformada = models.BooleanField(
		blank = True,
		default = None
	)

	NomeSiteSimoes = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 255
	)

	ConveniadaSimoes = models.BooleanField(
		blank = True,
		default = None
	)

	Associacao = models.BooleanField(
		blank = True,
		default = None
	)

	ResponsavelFinanceiro = models.BooleanField(
		blank = True,
		default = None
	)

	LimiteFinanceiro = models.FloatField(
		null = True,
		blank = True,
		default = None
	)

	Pais = models.ForeignKey(
		Pais,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	RanqueamentoGeral = models.ForeignKey(
		RanqueamentoGeral,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	PercentualPreenchimento = models.FloatField(
		null = True,
		blank = True,
		default = None
	)

	NaoExibirMoeda = models.BooleanField(
		blank = True,
		default = None
	)

	QRCode = models.ForeignKey(
		QRCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	IndisponivelAte = models.DateField(
		null = True,
		blank = True
	)

	TipoPrimeiroDiaSemana = models.ForeignKey(
		TipoPrimeiroDiaSemana,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	TipoDispHoraSemana = models.ForeignKey(
		TipoDispHoraSemana,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	EsquemaCor = models.ForeignKey(
		EsquemaCor,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	TipoPerfilConta = models.ForeignKey(
		TipoPerfilConta,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Valor = models.ManyToManyField(
		Valor,
		related_name = 'EmpresaValor'
	)

	Url = models.ManyToManyField(
		Url,
		related_name = 'EmpresaUrl'
	)

	Unidade = models.ManyToManyField(
		Unidade,
		related_name = 'EmpresaUnidade'
	)

	TransfUniaoEuropeia = models.ManyToManyField(
		TransfUniaoEuropeia,
		related_name = 'EmpresaTransfUniaoEuropeia'
	)

	TransfSWIFT = models.ManyToManyField(
		TransfSWIFT,
		related_name = 'EmpresaTransfSWIFT'
	)

	TransfItalia = models.ManyToManyField(
		TransfItalia,
		related_name = 'EmpresaTransfItalia'
	)

	TipoSegmentoInteresse = models.ManyToManyField(
		TipoSegmentoInteresse,
		related_name = 'EmpresaTipoSegmentoInteresse'
	)

	TipoMoeda = models.ManyToManyField(
		TipoMoeda,
		related_name = 'EmpresaTipoMoeda'
	)

	TipoMetodoPgto = models.ManyToManyField(
		TipoMetodoPgto,
		related_name = 'EmpresaTipoMetodoPgto'
	)

	TipoMarcador = models.ManyToManyField(
		TipoMarcador,
		related_name = 'EmpresaTipoMarcador'
	)

	TipoFaturacao = models.ManyToManyField(
		TipoFaturacao,
		related_name = 'EmpresaTipoFaturacao'
	)

	TipoFacilidade = models.ManyToManyField(
		TipoFacilidade,
		related_name = 'EmpresaTipoFacilidade'
	)

	TipoDominioUm = models.ManyToManyField(
		TipoDominioUm,
		related_name = 'EmpresaTipoDominioUm'
	)

	TipoDominioDois = models.ManyToManyField(
		TipoDominioDois,
		related_name = 'EmpresaTipoDominioDois'
	)

	TipoAreaGeoAtu = models.ManyToManyField(
		TipoAreaGeoAtu,
		related_name = 'EmpresaTipoAreaGeoAtu'
	)

	TipoAmenidade = models.ManyToManyField(
		TipoAmenidade,
		related_name = 'EmpresaTipoAmenidade'
	)

	SaldoMensagem = models.ManyToManyField(
		SaldoMensagem,
		related_name = 'EmpresaSaldoMensagem'
	)

	Referencia = models.ManyToManyField(
		Referencia,
		related_name = 'EmpresaReferencia'
	)

	RedeSocial = models.ManyToManyField(
		RedeSocial,
		related_name = 'EmpresaRedeSocial'
	)

	QuadroSocio = models.ManyToManyField(
		QuadroSocio,
		related_name = 'EmpresaQuadroSocio'
	)

	Projeto = models.ManyToManyField(
		Projeto,
		related_name = 'EmpresaProjeto'
	)

	PersonificacaoDominio = models.ManyToManyField(
		PersonificacaoDominio,
		related_name = 'EmpresaPersonificacaoDominio'
	)

	PagamentoOnline = models.ManyToManyField(
		PagamentoOnline,
		related_name = 'EmpresaPagamentoOnline'
	)

	Outorga = models.ManyToManyField(
		Outorga,
		related_name = 'EmpresaOutorga'
	)

	OrdemPagamentoBrasil = models.ManyToManyField(
		OrdemPagamentoBrasil,
		related_name = 'EmpresaOrdemPagamentoBrasil'
	)

	Notificacao = models.ManyToManyField(
		Notificacao,
		related_name = 'EmpresaNotificacao'
	)

	Microsite = models.ManyToManyField(
		Microsite,
		related_name = 'EmpresaMicrosite'
	)

	MargemLucro = models.ManyToManyField(
		MargemLucro,
		related_name = 'EmpresaMargemLucro'
	)

	Integracao = models.ManyToManyField(
		Integracao,
		related_name = 'EmpresaIntegracao'
	)

	Imposto = models.ManyToManyField(
		Imposto,
		related_name = 'EmpresaImposto'
	)

	Identificacao = models.ManyToManyField(
		Identificacao,
		related_name = 'EmpresaIdentificacao'
	)

	HorarioFuncionamento = models.ManyToManyField(
		HorarioFuncionamento,
		related_name = 'EmpresaHorarioFuncionamento'
	)

	Endereco = models.ManyToManyField(
		Endereco,
		related_name = 'EmpresaEndereco'
	)

	Email = models.ManyToManyField(
		Email,
		related_name = 'EmpresaEmail'
	)

	DispTurnoPreferido = models.ManyToManyField(
		DispTurnoPreferido,
		related_name = 'EmpresaDispTurnoPreferido'
	)

	DispDiaPreferido = models.ManyToManyField(
		DispDiaPreferido,
		related_name = 'EmpresaDispDiaPreferido'
	)

	DadoBancario = models.ManyToManyField(
		DadoBancario,
		related_name = 'EmpresaDadoBancario'
	)

	CtrlQualidade = models.ManyToManyField(
		CtrlQualidade,
		related_name = 'EmpresaCtrlQualidade'
	)

	Criptomoeda = models.ManyToManyField(
		Criptomoeda,
		related_name = 'EmpresaCriptomoeda'
	)

	Contato = models.ManyToManyField(
		Contato,
		related_name = 'EmpresaContato'
	)

	Comissao = models.ManyToManyField(
		Comissao,
		related_name = 'EmpresaComissao'
	)

	CodigoEndPostal = models.ManyToManyField(
		CodigoEndPostal,
		related_name = 'EmpresaCodigoEndPostal'
	)

	Clausula = models.ManyToManyField(
		Clausula,
		related_name = 'EmpresaClausula'
	)

	CartaoCredito = models.ManyToManyField(
		CartaoCredito,
		related_name = 'EmpresaCartaoCredito'
	)

	BancoImagem = models.ManyToManyField(
		BancoImagem,
		related_name = 'EmpresaBancoImagem'
	)

	BancoArquivo = models.ManyToManyField(
		BancoArquivo,
		related_name = 'EmpresaBancoArquivo'
	)

	objects = models.Manager()

	def __str__(self):
		return self.NomeEmpresarial


class SalaAula(models.Model):
	
	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 200
	)

	Virtual = models.BooleanField(
		blank = True,
		default = None
	)

	Contato = models.ForeignKey(
		Contato,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Url = models.ForeignKey(
		Url,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	DisponivelArCordicionado = models.BooleanField(
		blank = True,
		default = None
	)

	DisponivelQuadroBranco = models.BooleanField(
		blank = True,
		default = None
	)

	DisponivelComputador = models.BooleanField(
		blank = True,
		default = None
	)

	DisponivelInternet = models.BooleanField(
		blank = True,
		default = None
	)

	DisponivelDataShow = models.BooleanField(
		blank = True,
		default = None
	)

	DisponivelTelaProjecao = models.BooleanField(
		blank = True,
		default = None
	)

	AssentoDisponivelAluno = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	AssentoDisponivelColaborador = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	DisponivelTV = models.BooleanField(
		blank = True,
		default = None
	)

	DisponivelCaixaSom = models.BooleanField(
		blank = True,
		default = None
	)

	Unidade = models.ManyToManyField(
		Unidade,
		related_name = 'SalaAulaUnidade'
	)

	HorarioFuncionamento = models.ManyToManyField(
		HorarioFuncionamento,
		related_name = 'SalaAulaHorarioFuncionamento'
	)

	objects = models.Manager()

	def __str__(self):
		return self.Nome


class TipoNivelAluno(models.Model):
	
	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 200
	)

	Ordem = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Nome


class Turma(models.Model):
	
	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 200
	)

	Unidade = models.ForeignKey(
		Unidade,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	HorarioFuncionamento = models.ForeignKey(
		HorarioFuncionamento,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	SalaAula = models.ForeignKey(
		SalaAula,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Item = models.ForeignKey(
		Item,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	TipoNivelAluno = models.ForeignKey(
		TipoNivelAluno,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Nome


class TipoExtDigEdit(models.Model):
	
	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 100
	)

	Partida = models.BooleanField(
		blank = True,
		default = None
	)

	Chegada = models.BooleanField(
		blank = True,
		default = None
	)

	TipoExtensao = models.ForeignKey(
		TipoExtensao,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Ordem = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Nome


class TipoPeriferico(models.Model):
	
	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 50
	)

	Unidade = models.ForeignKey(
		Unidade,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Ordem = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Nome


class TipoSistemaOperacional(models.Model):
	
	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 100
	)

	Visivel = models.BooleanField(
		blank = True,
		default = None
	)

	Unidade = models.ForeignKey(
		Unidade,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Ordem = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Nome


class TipoSoftwareTraducao(models.Model):
	
	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 50
	)

	Unidade = models.ForeignKey(
		Unidade,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Ordem = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Nome


class TipoSoftwareLocaliz(models.Model):
	
	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 100
	)

	Unidade = models.ForeignKey(
		Unidade,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Ordem = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Nome


class TipoSoftwareDTP(models.Model):
	
	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 50
	)

	Unidade = models.ForeignKey(
		Unidade,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Ordem = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Nome


class TipoSoftwarePacEsc(models.Model):
	
	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 50
	)

	Unidade = models.ForeignKey(
		Unidade,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Ordem = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Nome


class TipoSoftwareModTresD(models.Model):
	
	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 50
	)

	Unidade = models.ForeignKey(
		Unidade,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Ordem = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Nome


class TipoSoftwareTransc(models.Model):
	
	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 50
	)

	Unidade = models.ForeignKey(
		Unidade,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Ordem = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Nome


class TipoSoftwareLeitor(models.Model):
	
	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 50
	)

	Unidade = models.ForeignKey(
		Unidade,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Ordem = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Nome


class TipoEngineGame(models.Model):
	
	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 50
	)

	Unidade = models.ForeignKey(
		Unidade,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Ordem = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Nome


class ProtocoloAtendimento(models.Model):
	
	Codigo = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 8
	)

	Data = models.DateTimeField(
		null = True,
		blank = True,
		default = None
	)

	Unidade = models.ForeignKey(
		Unidade,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Codigo


class TipoHardwareComputador(models.Model):
	
	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 50
	)

	Ordem = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Nome


class TipoBancoDados(models.Model):
	
	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 50
	)

	Visivel = models.BooleanField(
		blank = True,
		default = None
	)

	Unidade = models.ForeignKey(
		Unidade,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Ordem = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Nome


class TipoExtDiagramacao(models.Model):
	
	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 200
	)

	TipoExtensao = models.ForeignKey(
		TipoExtensao,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Partida = models.BooleanField(
		blank = True,
		default = None
	)

	Chegada = models.BooleanField(
		blank = True,
		default = None
	)

	Ordem = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Nome


class TipoExtAudio(models.Model):
	
	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 200
	)

	TipoExtensao = models.ForeignKey(
		TipoExtensao,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Partida = models.BooleanField(
		blank = True,
		default = None
	)

	Chegada = models.BooleanField(
		blank = True,
		default = None
	)

	Ordem = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Nome


class TipoExtLocalizacao(models.Model):
	
	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 200
	)

	TipoExtensao = models.ForeignKey(
		TipoExtensao,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Partida = models.BooleanField(
		blank = True,
		default = None
	)

	Chegada = models.BooleanField(
		blank = True,
		default = None
	)

	Ordem = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Nome


class TipoExtVideo(models.Model):
	
	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 200
	)

	TipoExtensao = models.ForeignKey(
		TipoExtensao,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Partida = models.BooleanField(
		blank = True,
		default = None
	)

	Chegada = models.BooleanField(
		blank = True,
		default = None
	)

	Ordem = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Nome


class TipoIntervaloTempo(models.Model):
	
	HoraInicio = models.TimeField(
		null = True,
		blank = True
	)

	HoraFim = models.TimeField(
		null = True,
		blank = True
	)

	Ordem = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	Unidade = models.ForeignKey(
		Unidade,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.HoraInicio


class TipoParte(models.Model):
	
	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 255
	)

	Ordem = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	Pais = models.ForeignKey(
		Pais,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Nome


class TipoInstCertific(models.Model):
	
	Abreviatura = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 50
	)

	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 200
	)

	Url = models.ForeignKey(
		Url,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	TipoCtrlQualidade = models.ForeignKey(
		TipoCtrlQualidade,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Visivel = models.BooleanField(
		blank = True,
		default = None
	)

	Pais = models.ForeignKey(
		Pais,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Ordem = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Abreviatura


class ExameProficiencia(models.Model):
	
	Ponto = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	Validade = models.DateField(
		null = True,
		blank = True
	)

	CopiaComprovante = models.BinaryField(
		null = True,
		blank = True,
		default = None
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	TipoInstCertific = models.ForeignKey(
		TipoInstCertific,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Ponto


class TipoExtDigNaoEdit(models.Model):
	
	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 255
	)

	TipoExtensao = models.ForeignKey(
		TipoExtensao,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Partida = models.BooleanField(
		blank = True,
		default = None
	)

	Chegada = models.BooleanField(
		blank = True,
		default = None
	)

	Ordem = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	CodigoIDezeoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Nome


class TipoReligiao(models.Model):
	
	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 100
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	Ordem = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Nome


class TipoHobbie(models.Model):
	
	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 255
	)

	BancoImagem = models.ForeignKey(
		BancoImagem,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Ordem = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Nome


class TipoAcessoInternet(models.Model):
	
	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 100
	)

	Ordem = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Nome


class TipoExpLocaliza(models.Model):
	
	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 100
	)

	Ordem = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Nome


class ParteTraducao(models.Model):
	
	Ordem = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	ImportanciaTrabalhoEquipe = models.TextField(
		null = True,
		blank = True,
		default = None,
		max_length = 4000
	)

	Proatividade = models.TextField(
		null = True,
		blank = True,
		default = None,
		max_length = 4000
	)

	Organizacao = models.TextField(
		null = True,
		blank = True,
		default = None,
		max_length = 4000
	)

	Concentracao = models.TextField(
		null = True,
		blank = True,
		default = None,
		max_length = 4000
	)

	FocoProdutividade = models.TextField(
		null = True,
		blank = True,
		default = None,
		max_length = 4000
	)

	AlcanceObjetivo = models.TextField(
		null = True,
		blank = True,
		default = None,
		max_length = 4000
	)

	AtencaoDetalhes = models.TextField(
		null = True,
		blank = True,
		default = None,
		max_length = 4000
	)

	ProcessosMapeados = models.TextField(
		null = True,
		blank = True,
		default = None,
		max_length = 4000
	)

	ComunicacaoTrabalhoEquipe = models.TextField(
		null = True,
		blank = True,
		default = None,
		max_length = 4000
	)

	AdaptacaoCulturaEmpresa = models.TextField(
		null = True,
		blank = True,
		default = None,
		max_length = 4000
	)

	CapacidadeAprendizado = models.TextField(
		null = True,
		blank = True,
		default = None,
		max_length = 4000
	)

	Flexibilidade = models.TextField(
		null = True,
		blank = True,
		default = None,
		max_length = 4000
	)

	BagagemCultural = models.TextField(
		null = True,
		blank = True,
		default = None,
		max_length = 4000
	)

	Resumo = models.TextField(
		null = True,
		blank = True,
		default = None,
		max_length = 4000
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Ordem


class TipoFonte(models.Model):
	
	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 200
	)

	Ordem = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Nome


class AssinaturaDigital(models.Model):
	
	Assinatura = models.BinaryField(
		null = True,
		blank = True,
		default = None
	)

	AssinaturaUm = models.BinaryField(
		null = True,
		blank = True,
		default = None
	)

	AssinaturaUmPrincipal = models.BooleanField(
		blank = True,
		default = None
	)

	AssinaturaDois = models.BinaryField(
		null = True,
		blank = True,
		default = None
	)

	AssinaturaDoisPrincipal = models.BooleanField(
		blank = True,
		default = None
	)

	AssinaturaTres = models.BinaryField(
		null = True,
		blank = True,
		default = None
	)

	RubricaUm = models.BinaryField(
		null = True,
		blank = True,
		default = None
	)

	RubricaUmPrincipal = models.BooleanField(
		blank = True,
		default = None
	)

	RubricaDois = models.BinaryField(
		null = True,
		blank = True,
		default = None
	)

	SelfieIdentificacao = models.BinaryField(
		null = True,
		blank = True,
		default = None
	)

	TipoFonte = models.ForeignKey(
		TipoFonte,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Assinatura


class DispHoraSemana(models.Model):
	
	TipoDispHoraSemana = models.ForeignKey(
		TipoDispHoraSemana,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.TipoDispHoraSemana


class BancoCurriculo(models.Model):
	
	Arquivo = models.BinaryField(
		null = True,
		blank = True,
		default = None
	)

	ProibirImpressao = models.BooleanField(
		blank = True,
		default = None
	)

	ProibirDownload = models.BooleanField(
		blank = True,
		default = None
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Arquivo


class TipoRelacionamento(models.Model):
	
	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 50
	)

	Ordem = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Nome


class Relacionamento(models.Model):
	
	Parte = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	TipoRelacionamento = models.ForeignKey(
		TipoRelacionamento,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Parte


class TipoUnidComprimento(models.Model):
	
	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 50
	)

	Abreviatura = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 5
	)

	Ordem = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Nome


class TipoUnidMassa(models.Model):
	
	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 50
	)

	Abreviatura = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 5
	)

	Ordem = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Nome


class TipoSexo(models.Model):
	
	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 255
	)

	Ordem = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	CodigoDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Nome


class TipoGenero(models.Model):
	
	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 255
	)

	Ordem = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	CodigoDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Nome


class Parte(models.Model):
	
	Iniciais = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 15
	)

	SetorComercial = models.BooleanField(
		blank = True,
		default = None
	)

	User = models.ForeignKey(
		User,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	TipoSexo = models.ForeignKey(
		TipoSexo,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	TipoParte = models.ForeignKey(
		TipoParte,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	TipoPronomeTratamento = models.ForeignKey(
		TipoPronomeTratamento,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Cargo = models.ForeignKey(
		Cargo,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Funcao = models.ForeignKey(
		Funcao,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	TipoRelacao = models.ForeignKey(
		TipoRelacao,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	VIP = models.BooleanField(
		blank = True,
		default = None
	)

	RegistroConselho = models.BooleanField(
		blank = True,
		default = None
	)

	Estrangeiro = models.BooleanField(
		blank = True,
		default = None
	)

	PreferenciaFiscalInformada = models.BooleanField(
		blank = True,
		default = None
	)

	BancoCurriculo = models.ForeignKey(
		BancoCurriculo,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	AceitaCartao = models.BooleanField(
		blank = True,
		default = None
	)

	LimiteFinanceiro = models.FloatField(
		null = True,
		blank = True,
		default = None
	)

	AssinaturaDigital = models.ForeignKey(
		AssinaturaDigital,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	ResponsavelFinanceiro = models.BooleanField(
		blank = True,
		default = None
	)

	RanqueamentoGeral = models.ForeignKey(
		RanqueamentoGeral,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Observacao = models.TextField(
		null = True,
		blank = True,
		default = None,
		max_length = 2000000
	)

	PercentualPreenchimento = models.FloatField(
		null = True,
		blank = True,
		default = None
	)

	NaoExibirMoeda = models.BooleanField(
		blank = True,
		default = None
	)

	QRCode = models.ForeignKey(
		QRCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	IndisponivelAte = models.DateField(
		null = True,
		blank = True
	)

	TipoPrimeiroDiaSemana = models.ForeignKey(
		TipoPrimeiroDiaSemana,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	DispHoraSemana = models.ForeignKey(
		DispHoraSemana,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	EsquemaCor = models.ForeignKey(
		EsquemaCor,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	DataAceiteCandidato = models.DateTimeField(
		null = True,
		blank = True,
		default = None
	)

	DataAceiteColaborador = models.DateTimeField(
		null = True,
		blank = True,
		default = None
	)

	DataNascimento = models.DateField(
		null = True,
		blank = True,
		verbose_name = "Data de Nascimento"
	)

	OcultarAnoDataNascimento = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 1
	)

	ParteAtualmDisp = models.BooleanField(
		blank = True,
		default = None
	)

	TipoPerfilConta = models.ForeignKey(
		TipoPerfilConta,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	UnidadeMassa = models.FloatField(
		null = True,
		blank = True,
		default = None
	)

	UnidadeComprimento = models.FloatField(
		null = True,
		blank = True,
		default = None
	)

	IMC = models.FloatField(
		null = True,
		blank = True,
		default = None
	)

	TipoUnidMassa = models.ForeignKey(
		TipoUnidMassa,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	ParteTraducao = models.ForeignKey(
		ParteTraducao,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	TipoUnidComprimento = models.ForeignKey(
		TipoUnidComprimento,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Valor = models.ManyToManyField(
		Valor,
		related_name = 'ParteValor'
	)

	Url = models.ManyToManyField(
		Url,
		related_name = 'ParteUrl'
	)

	Turma = models.ManyToManyField(
		Turma,
		related_name = 'ParteTurma'
	)

	TransfUniaoEuropeia = models.ManyToManyField(
		TransfUniaoEuropeia,
		related_name = 'ParteTransfUniaoEuropeia'
	)

	TransfSWIFT = models.ManyToManyField(
		TransfSWIFT,
		related_name = 'ParteTransfSWIFT'
	)

	TransfItalia = models.ManyToManyField(
		TransfItalia,
		related_name = 'ParteTransfItalia'
	)

	TipoSoftwareTransc = models.ManyToManyField(
		TipoSoftwareTransc,
		related_name = 'ParteTipoSoftwareTransc'
	)

	TipoSoftwareTraducao = models.ManyToManyField(
		TipoSoftwareTraducao,
		related_name = 'ParteTipoSoftwareTraducao'
	)

	TipoSoftwarePacEsc = models.ManyToManyField(
		TipoSoftwarePacEsc,
		related_name = 'ParteTipoSoftwarePacEsc'
	)

	TipoSoftwareModTresD = models.ManyToManyField(
		TipoSoftwareModTresD,
		related_name = 'ParteTipoSoftwareModTresD'
	)

	TipoSoftwareLocaliz = models.ManyToManyField(
		TipoSoftwareLocaliz,
		related_name = 'ParteTipoSoftwareLocaliz'
	)

	TipoSoftwareLeitor = models.ManyToManyField(
		TipoSoftwareLeitor,
		related_name = 'ParteTipoSoftwareLeitor'
	)

	TipoSoftwareDTP = models.ManyToManyField(
		TipoSoftwareDTP,
		related_name = 'ParteTipoSoftwareDTP'
	)

	TipoSistemaOperacional = models.ManyToManyField(
		TipoSistemaOperacional,
		related_name = 'ParteTipoSistemaOperacional'
	)

	TipoSegmentoInteresse = models.ManyToManyField(
		TipoSegmentoInteresse,
		related_name = 'ParteTipoSegmentoInteresse'
	)

	TipoReligiao = models.ManyToManyField(
		TipoReligiao,
		related_name = 'ParteTipoReligiao'
	)

	TipoPeriferico = models.ManyToManyField(
		TipoPeriferico,
		related_name = 'ParteTipoPeriferico'
	)

	TipoMoeda = models.ManyToManyField(
		TipoMoeda,
		related_name = 'ParteTipoMoeda'
	)

	TipoMetodoPgto = models.ManyToManyField(
		TipoMetodoPgto,
		related_name = 'ParteTipoMetodoPgto'
	)

	TipoMarcador = models.ManyToManyField(
		TipoMarcador,
		related_name = 'ParteTipoMarcador'
	)

	TipoIntervaloTempo = models.ManyToManyField(
		TipoIntervaloTempo,
		related_name = 'ParteTipoIntervaloTempo'
	)

	TipoHobbie = models.ManyToManyField(
		TipoHobbie,
		related_name = 'ParteTipoHobbie'
	)

	TipoHardwareComputador = models.ManyToManyField(
		TipoHardwareComputador,
		related_name = 'ParteTipoHardwareComputador'
	)

	TipoGenero = models.ManyToManyField(
		TipoGenero,
		related_name = 'ParteTipoGenero'
	)

	TipoFaturacao = models.ManyToManyField(
		TipoFaturacao,
		related_name = 'ParteTipoFaturacao'
	)

	TipoExtVideo = models.ManyToManyField(
		TipoExtVideo,
		related_name = 'ParteTipoExtVideo'
	)

	TipoExtLocalizacao = models.ManyToManyField(
		TipoExtLocalizacao,
		related_name = 'ParteTipoExtLocalizacao'
	)

	TipoExtDigNaoEdit = models.ManyToManyField(
		TipoExtDigNaoEdit,
		related_name = 'ParteTipoExtDigNaoEdit'
	)

	TipoExtDigEdit = models.ManyToManyField(
		TipoExtDigEdit,
		related_name = 'ParteTipoExtDigEdit'
	)

	TipoExtDiagramacao = models.ManyToManyField(
		TipoExtDiagramacao,
		related_name = 'ParteTipoExtDiagramacao'
	)

	TipoExtAudio = models.ManyToManyField(
		TipoExtAudio,
		related_name = 'ParteTipoExtAudio'
	)

	TipoExpLocaliza = models.ManyToManyField(
		TipoExpLocaliza,
		related_name = 'ParteTipoExpLocaliza'
	)

	TipoEngineGame = models.ManyToManyField(
		TipoEngineGame,
		related_name = 'ParteTipoEngineGame'
	)

	TipoDominioUm = models.ManyToManyField(
		TipoDominioUm,
		related_name = 'ParteTipoDominioUm'
	)

	TipoDominioDois = models.ManyToManyField(
		TipoDominioDois,
		related_name = 'ParteTipoDominioDois'
	)

	TipoBancoDados = models.ManyToManyField(
		TipoBancoDados,
		related_name = 'ParteTipoBancoDados'
	)

	TipoAreaGeoAtu = models.ManyToManyField(
		TipoAreaGeoAtu,
		related_name = 'ParteTipoAreaGeoAtu'
	)

	TipoAcessoInternet = models.ManyToManyField(
		TipoAcessoInternet,
		related_name = 'ParteTipoAcessoInternet'
	)

	SaldoMensagem = models.ManyToManyField(
		SaldoMensagem,
		related_name = 'ParteSaldoMensagem'
	)

	Relacionamento = models.ManyToManyField(
		Relacionamento,
		related_name = 'ParteRelacionamento'
	)

	Referencia = models.ManyToManyField(
		Referencia,
		related_name = 'ParteReferencia'
	)

	RedeSocial = models.ManyToManyField(
		RedeSocial,
		related_name = 'ParteRedeSocial'
	)

	QuadroSocio = models.ManyToManyField(
		QuadroSocio,
		related_name = 'ParteQuadroSocio'
	)

	ProtocoloAtendimento = models.ManyToManyField(
		ProtocoloAtendimento,
		related_name = 'ParteProtocoloAtendimento'
	)

	Projeto = models.ManyToManyField(
		Projeto,
		related_name = 'ParteProjeto'
	)

	PersonificacaoDominio = models.ManyToManyField(
		PersonificacaoDominio,
		related_name = 'PartePersonificacaoDominio'
	)

	Pais = models.ManyToManyField(
		Pais,
		related_name = 'PartePais'
	)

	PagamentoOnline = models.ManyToManyField(
		PagamentoOnline,
		related_name = 'PartePagamentoOnline'
	)

	PDV = models.ManyToManyField(
		PDV,
		related_name = 'PartePDV'
	)

	Outorga = models.ManyToManyField(
		Outorga,
		related_name = 'ParteOutorga'
	)

	OrdemPagamentoBrasil = models.ManyToManyField(
		OrdemPagamentoBrasil,
		related_name = 'ParteOrdemPagamentoBrasil'
	)

	Notificacao = models.ManyToManyField(
		Notificacao,
		related_name = 'ParteNotificacao'
	)

	Microsite = models.ManyToManyField(
		Microsite,
		related_name = 'ParteMicrosite'
	)

	MargemLucro = models.ManyToManyField(
		MargemLucro,
		related_name = 'ParteMargemLucro'
	)

	Integracao = models.ManyToManyField(
		Integracao,
		related_name = 'ParteIntegracao'
	)

	Imposto = models.ManyToManyField(
		Imposto,
		related_name = 'ParteImposto'
	)

	Identificacao = models.ManyToManyField(
		Identificacao,
		related_name = 'ParteIdentificacao'
	)

	ExameProficiencia = models.ManyToManyField(
		ExameProficiencia,
		related_name = 'ParteExameProficiencia'
	)

	Endereco = models.ManyToManyField(
		Endereco,
		related_name = 'ParteEndereco'
	)

	Empresa = models.ManyToManyField(
		Empresa,
		related_name = 'ParteEmpresa'
	)

	Email = models.ManyToManyField(
		Email,
		related_name = 'ParteEmail'
	)

	DispTurnoPreferido = models.ManyToManyField(
		DispTurnoPreferido,
		related_name = 'ParteDispTurnoPreferido'
	)

	DispDiaPreferido = models.ManyToManyField(
		DispDiaPreferido,
		related_name = 'ParteDispDiaPreferido'
	)

	DadoBancario = models.ManyToManyField(
		DadoBancario,
		related_name = 'ParteDadoBancario'
	)

	CtrlQualidade = models.ManyToManyField(
		CtrlQualidade,
		related_name = 'ParteCtrlQualidade'
	)

	Criptomoeda = models.ManyToManyField(
		Criptomoeda,
		related_name = 'ParteCriptomoeda'
	)

	Contato = models.ManyToManyField(
		Contato,
		related_name = 'ParteContato'
	)

	Comissao = models.ManyToManyField(
		Comissao,
		related_name = 'ParteComissao'
	)

	CodigoEndPostal = models.ManyToManyField(
		CodigoEndPostal,
		related_name = 'ParteCodigoEndPostal'
	)

	Clausula = models.ManyToManyField(
		Clausula,
		related_name = 'ParteClausula'
	)

	Cidade = models.ManyToManyField(
		Cidade,
		related_name = 'ParteCidade'
	)

	CartaoCredito = models.ManyToManyField(
		CartaoCredito,
		related_name = 'ParteCartaoCredito'
	)

	BancoImagem = models.ManyToManyField(
		BancoImagem,
		related_name = 'ParteBancoImagem'
	)

	BancoArquivo = models.ManyToManyField(
		BancoArquivo,
		related_name = 'ParteBancoArquivo'
	)

	objects = models.Manager()

	def __str__(self):
		return self.Iniciais


class Secao(models.Model):
	
	Data = models.DateTimeField(
		null = True,
		blank = True,
		default = None
	)

	Ip = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 128
	)

	Cidade = models.ForeignKey(
		Cidade,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Estado = models.ForeignKey(
		Estado,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Pais = models.ForeignKey(
		Pais,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	TipoSistemaOperacional = models.ForeignKey(
		TipoSistemaOperacional,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	ProtocoloAtendimento = models.ForeignKey(
		ProtocoloAtendimento,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	CtrlQualidade = models.ForeignKey(
		CtrlQualidade,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Item = models.ManyToManyField(
		Item,
		related_name = 'SecaoItem'
	)

	objects = models.Manager()

	def __str__(self):
		return self.Data


class TipoDesconto(models.Model):
	
	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 200
	)

	Unidade = models.ForeignKey(
		Unidade,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Ordem = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Nome


class Desconto(models.Model):
	
	QuantidadeMaxima = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	Unidade = models.ForeignKey(
		Unidade,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Item = models.ForeignKey(
		Item,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	TipoDesconto = models.ForeignKey(
		TipoDesconto,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.QuantidadeMaxima


class TipoComoConheceu(models.Model):
	
	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 300
	)

	Ordem = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Nome


class OrdemExeServico(models.Model):
	
	Codigo = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 8
	)

	TipoDataMesCard = models.ForeignKey(
		TipoDataMesCard,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	TipoDataAnoCard = models.ForeignKey(
		TipoDataAnoCard,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	DataCriacao = models.DateTimeField(
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Codigo


class Convenio(models.Model):
	
	ConvenioAtivo = models.BooleanField(
		blank = True,
		default = None
	)

	DataInicio = models.DateField(
		null = True,
		blank = True
	)

	DataFim = models.DateField(
		null = True,
		blank = True
	)

	Empresa = models.ForeignKey(
		Empresa,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.ConvenioAtivo


class TipoRelDiag(models.Model):
	
	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 200
	)

	Ordem = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Nome


class TipoModoEntrega(models.Model):
	
	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 255
	)

	Ordem = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Nome


class RelDiag(models.Model):
	
	Codigo = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 8
	)

	Secao = models.ForeignKey(
		Secao,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	TipoRelDiag = models.ForeignKey(
		TipoRelDiag,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	ValidadeProposta = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	TipoModoEntrega = models.ForeignKey(
		TipoModoEntrega,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Desconto = models.ForeignKey(
		Desconto,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	TipoComoConheceu = models.ForeignKey(
		TipoComoConheceu,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	DataCriacao = models.DateTimeField(
		null = True,
		blank = True,
		default = None
	)

	Convenio = models.ForeignKey(
		Convenio,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	CodigoValidacao = models.ForeignKey(
		CodigoValidacao,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Unidade = models.ForeignKey(
		Unidade,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	PDV = models.ForeignKey(
		PDV,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	CtrlQualidade = models.ForeignKey(
		CtrlQualidade,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	ContratoCDC = models.BooleanField(
		blank = True,
		default = None
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	TipoDominioUm = models.ManyToManyField(
		TipoDominioUm,
		related_name = 'RelDiagTipoDominioUm'
	)

	TipoDominioDois = models.ManyToManyField(
		TipoDominioDois,
		related_name = 'RelDiagTipoDominioDois'
	)

	Parte = models.ManyToManyField(
		Parte,
		related_name = 'RelDiagParte'
	)

	OrdemExeServico = models.ManyToManyField(
		OrdemExeServico,
		related_name = 'RelDiagOrdemExeServico'
	)

	Empresa = models.ManyToManyField(
		Empresa,
		related_name = 'RelDiagEmpresa'
	)

	objects = models.Manager()

	def __str__(self):
		return self.Codigo


class ItemModelo(models.Model):
	
	Codigo = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 20
	)

	CFOP = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	SKU = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 20
	)

	Item = models.ForeignKey(
		Item,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	ItemTipoArea = models.ForeignKey(
		ItemTipoArea,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Codigo


class ItemModeloTraducao(models.Model):
	
	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 200
	)

	ItemModelo = models.ForeignKey(
		ItemModelo,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Explicacao = models.TextField(
		null = True,
		blank = True,
		default = None,
		max_length = 2000000
	)

	CodigoBarra = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	Url = models.ForeignKey(
		Url,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	BancoArquivo = models.ForeignKey(
		BancoArquivo,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	QRCode = models.ForeignKey(
		QRCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Nome


class ItemTraducao(models.Model):
	
	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 2000
	)

	Explicacao = models.TextField(
		null = True,
		blank = True,
		default = None,
		max_length = 10485760
	)

	Mensagem = models.TextField(
		null = True,
		blank = True,
		default = None,
		max_length = 10485760
	)

	Observacao = models.TextField(
		null = True,
		blank = True,
		default = None,
		max_length = 10485760
	)

	InfoAdicional = models.TextField(
		null = True,
		blank = True,
		default = None,
		max_length = 10485760
	)

	CondicaoPagamento = models.TextField(
		null = True,
		blank = True,
		default = None,
		max_length = 10485760
	)

	ListaBrinde = models.TextField(
		null = True,
		blank = True,
		default = None,
		max_length = 10485760
	)

	Convenio = models.TextField(
		null = True,
		blank = True,
		default = None,
		max_length = 10485760
	)

	ProgramaCurso = models.TextField(
		null = True,
		blank = True,
		default = None,
		max_length = 10485760
	)

	AulaParticular = models.TextField(
		null = True,
		blank = True,
		default = None,
		max_length = 10485760
	)

	InCompany = models.TextField(
		null = True,
		blank = True,
		default = None,
		max_length = 10485760
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	Item = models.ForeignKey(
		Item,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Nome


class TipoSuporteCont(models.Model):
	
	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 50
	)

	Ordem = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Nome


class TipoConteudoCategoria(models.Model):
	
	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 255
	)

	Ordem = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	Descricao = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 500
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Nome


class TipoConteudo(models.Model):
	
	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 200
	)

	Ordem = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	TipoConteudoCategoria = models.ForeignKey(
		TipoConteudoCategoria,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Nome


class TipoSuporteContIO(models.Model):
	
	PartidaChegada = models.BooleanField(
		blank = True,
		default = None
	)

	Ordem = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	TipoSuporteCont = models.ForeignKey(
		TipoSuporteCont,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.PartidaChegada


class TipoExtDigEdtIO(models.Model):
	
	PartidaChegada = models.BooleanField(
		blank = True,
		default = None
	)

	Ordem = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	TipoExtDigEdit = models.ForeignKey(
		TipoExtDigEdit,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.PartidaChegada


class RelDiagServAd(models.Model):
	
	DataEntrega = models.DateField(
		null = True,
		blank = True
	)

	RelDiag = models.ForeignKey(
		RelDiag,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	HoraEntrega = models.TimeField(
		null = True,
		blank = True
	)

	UrgenciaServico = models.BooleanField(
		blank = True,
		default = None
	)

	DireitosAutorais = models.BooleanField(
		blank = True,
		default = None
	)

	TipoSuporteCont = models.ForeignKey(
		TipoSuporteCont,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Secao = models.ForeignKey(
		Secao,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Cargo = models.ForeignKey(
		Cargo,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Item = models.ForeignKey(
		Item,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	ItemTraducao = models.ForeignKey(
		ItemTraducao,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	ItemModeloTraducao = models.ForeignKey(
		ItemModeloTraducao,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Quantidade = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	Preco = models.FloatField(
		null = True,
		blank = True,
		default = None
	)

	TipoSuporteContIO = models.ManyToManyField(
		TipoSuporteContIO,
		related_name = 'RelDiagServAdTipoSuporteContIO'
	)

	TipoExtDigEdtIO = models.ManyToManyField(
		TipoExtDigEdtIO,
		related_name = 'RelDiagServAdTipoExtDigEdtIO'
	)

	TipoConteudo = models.ManyToManyField(
		TipoConteudo,
		related_name = 'RelDiagServAdTipoConteudo'
	)

	BancoArquivo = models.ManyToManyField(
		BancoArquivo,
		related_name = 'RelDiagServAdBancoArquivo'
	)

	objects = models.Manager()

	def __str__(self):
		return self.DataEntrega


class TipoFusoHorario(models.Model):
	
	TZdatabaseName = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 100
	)

	UTCOff = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 100
	)

	UTCDSToff = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 100
	)

	LatitudeLongitudeDDMMDDDMM = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 255
	)

	PartePaisCoberto = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 100
	)

	Status = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 100
	)

	Ordem = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	Visivel = models.BooleanField(
		blank = True,
		default = None
	)

	Cidade = models.ForeignKey(
		Cidade,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Pais = models.ForeignKey(
		Pais,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Continente = models.ForeignKey(
		Continente,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.TZdatabaseName


class TipoAgenda(models.Model):
	
	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 200
	)

	Ordem = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Nome


class Agenda(models.Model):
	
	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 50
	)

	Descricao = models.TextField(
		null = True,
		blank = True,
		default = None,
		max_length = 500
	)

	TipoAgenda = models.ForeignKey(
		TipoAgenda,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	VisivelUrl = models.BooleanField(
		blank = True,
		default = None
	)

	TipoFusoHorario = models.ForeignKey(
		TipoFusoHorario,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Nome


class AgendaDisponivel(models.Model):
	
	Dia = models.DateField(
		null = True,
		blank = True
	)

	TipoIntervaloTempo = models.ForeignKey(
		TipoIntervaloTempo,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Unidade = models.ForeignKey(
		Unidade,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Dia


class TipoStatusMensagem(models.Model):
	
	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 200
	)

	Ordem = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Unidade = models.ForeignKey(
		Unidade,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Nome


class TipoMensagem(models.Model):
	
	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 200
	)

	Ordem = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Nome


class Mensagem(models.Model):
	
	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 150
	)

	Codigo = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 6
	)

	Email = models.ForeignKey(
		Email,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	TipoRedeSocial = models.ForeignKey(
		TipoRedeSocial,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	RedeSocial = models.ForeignKey(
		RedeSocial,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	TipoContato = models.ForeignKey(
		TipoContato,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Contato = models.ForeignKey(
		Contato,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Cidade = models.ForeignKey(
		Cidade,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Estado = models.ForeignKey(
		Estado,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Pais = models.ForeignKey(
		Pais,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	TipoDominioDois = models.ForeignKey(
		TipoDominioDois,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	TipoComoConheceu = models.ForeignKey(
		TipoComoConheceu,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Assunto = models.TextField(
		null = True,
		blank = True,
		default = None,
		max_length = 500
	)

	Corpo = models.TextField(
		null = True,
		blank = True,
		default = None,
		max_length = 2000000
	)

	HoraInicio = models.DateTimeField(
		null = True,
		blank = True,
		default = None
	)

	HoraFim = models.DateTimeField(
		null = True,
		blank = True,
		default = None
	)

	Agenda = models.ForeignKey(
		Agenda,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	AgendaDisponivel = models.ForeignKey(
		AgendaDisponivel,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Unidade = models.ForeignKey(
		Unidade,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	TipoMensagem = models.ForeignKey(
		TipoMensagem,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	TipoStatusMensagem = models.ForeignKey(
		TipoStatusMensagem,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Ip = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 128
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	PersonificacaoDominio = models.ForeignKey(
		PersonificacaoDominio,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	TipoSetor = models.ManyToManyField(
		TipoSetor,
		related_name = 'MensagemTipoSetor'
	)

	BancoArquivo = models.ManyToManyField(
		BancoArquivo,
		related_name = 'MensagemBancoArquivo'
	)

	objects = models.Manager()

	def __str__(self):
		return self.Nome


class TipoFormCompl(models.Model):
	
	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 50
	)

	TipoCtrlQualidade = models.ForeignKey(
		TipoCtrlQualidade,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Unidade = models.ForeignKey(
		Unidade,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Ordem = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Nome


class TipoCertificacao(models.Model):
	
	Abreviatura = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 50
	)

	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 200
	)

	EscalaVisivel = models.BooleanField(
		blank = True,
		default = None
	)

	TipoFormCompl = models.ForeignKey(
		TipoFormCompl,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Url = models.ForeignKey(
		Url,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	TipoCtrlQualidade = models.ForeignKey(
		TipoCtrlQualidade,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Visivel = models.BooleanField(
		blank = True,
		default = None
	)

	Pais = models.ForeignKey(
		Pais,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Ordem = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Abreviatura


class TipoDataMesOrdn(models.Model):
	
	Mes = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 35
	)

	TipoDataMesCard = models.ForeignKey(
		TipoDataMesCard,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Ordem = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Mes


class TipoPeriodoAnoAtual(models.Model):
	
	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 50
	)

	Ordem = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Nome


class TipoStatusForm(models.Model):
	
	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 50
	)

	Ordem = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Nome


class TipoDuracaoCurso(models.Model):
	
	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 50
	)

	Ordem = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Nome


class TipoUnidTempo(models.Model):
	
	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 50
	)

	Abreviatura = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 10
	)

	Quantidade = models.FloatField(
		null = True,
		blank = True,
		default = None
	)

	Decada = models.BooleanField(
		blank = True,
		default = None
	)

	Ano = models.BooleanField(
		blank = True,
		default = None
	)

	Mes = models.BooleanField(
		blank = True,
		default = None
	)

	Dia = models.BooleanField(
		blank = True,
		default = None
	)

	Minuto = models.BooleanField(
		blank = True,
		default = None
	)

	MilesimoSegundo = models.BooleanField(
		blank = True,
		default = None
	)

	Ordem = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Nome


class FormCompl(models.Model):
	
	Abreviatura = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 50
	)

	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 200
	)

	FormacaoDesc = models.TextField(
		null = True,
		blank = True,
		default = None,
		max_length = 4000
	)

	Url = models.ForeignKey(
		Url,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Parte = models.ForeignKey(
		Parte,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	TipoFormCompl = models.ForeignKey(
		TipoFormCompl,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	TipoInstCertific = models.ForeignKey(
		TipoInstCertific,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	TipoCertificacao = models.ForeignKey(
		TipoCertificacao,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	TipoProficienciaLingua = models.ForeignKey(
		TipoProficienciaLingua,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	TipoStatusForm = models.ForeignKey(
		TipoStatusForm,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	TipoPeriodoAnoAtual = models.ForeignKey(
		TipoPeriodoAnoAtual,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	TipoDuracaoCurso = models.ForeignKey(
		TipoDuracaoCurso,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	TipoDataDiaCard = models.ForeignKey(
		TipoDataDiaCard,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	TipoDataMesOrdn = models.ForeignKey(
		TipoDataMesOrdn,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	TipoDataAnoCard = models.ForeignKey(
		TipoDataAnoCard,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Duracao = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	TipoUnidTempo = models.ForeignKey(
		TipoUnidTempo,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	BancoArquivo = models.ForeignKey(
		BancoArquivo,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	ComprovanteVerificado = models.BooleanField(
		blank = True,
		default = None
	)

	TipoCtrlQualidade = models.ForeignKey(
		TipoCtrlQualidade,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Visivel = models.BooleanField(
		blank = True,
		default = None
	)

	Lingua = models.ForeignKey(
		Lingua,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Pais = models.ForeignKey(
		Pais,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Abreviatura


class TipoFormAcadem(models.Model):
	
	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 55
	)

	TipoCtrlQualidade = models.ForeignKey(
		TipoCtrlQualidade,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Ordem = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Nome


class FormAcadem(models.Model):
	
	Abreviatura = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 50
	)

	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 200
	)

	FormacaoDesc = models.TextField(
		null = True,
		blank = True,
		default = None,
		max_length = 4000
	)

	Url = models.ForeignKey(
		Url,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Parte = models.ForeignKey(
		Parte,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	TipoFormAcadem = models.ForeignKey(
		TipoFormAcadem,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	TipoInstCertific = models.ForeignKey(
		TipoInstCertific,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	TipoCertificacao = models.ForeignKey(
		TipoCertificacao,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	TipoStatusForm = models.ForeignKey(
		TipoStatusForm,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	TipoPeriodoAnoAtual = models.ForeignKey(
		TipoPeriodoAnoAtual,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	TipoDuracaoCurso = models.ForeignKey(
		TipoDuracaoCurso,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	TipoDataDiaCard = models.ForeignKey(
		TipoDataDiaCard,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	TipoDataMesOrdn = models.ForeignKey(
		TipoDataMesOrdn,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	TipoDataAnoCard = models.ForeignKey(
		TipoDataAnoCard,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Duracao = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	TipoUnidTempo = models.ForeignKey(
		TipoUnidTempo,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	BancoArquivo = models.ForeignKey(
		BancoArquivo,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	ComprovanteVerificado = models.BooleanField(
		blank = True,
		default = None
	)

	TipoCtrlQualidade = models.ForeignKey(
		TipoCtrlQualidade,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Visivel = models.BooleanField(
		blank = True,
		default = None
	)

	Lingua = models.ForeignKey(
		Lingua,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Pais = models.ForeignKey(
		Pais,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Abreviatura


class TipoDiaSemTrad(models.Model):
	
	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 50
	)

	NomeAbreviado = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 30
	)

	TipoDiaSemana = models.ForeignKey(
		TipoDiaSemana,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Ordem = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Nome


class TipoDataDiaOrdn(models.Model):
	
	DiaExtMasc = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 50
	)

	DiaOrdinal = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 35
	)

	TipoDataDiaCard = models.ForeignKey(
		TipoDataDiaCard,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Ordem = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.DiaExtMasc


class TipoDataComDetl(models.Model):
	
	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 100
	)

	Ordem = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Nome


class TipoDataComAssu(models.Model):
	
	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 100
	)

	Ordem = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	CodigoDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Nome


class TipoDataCom(models.Model):
	
	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 400
	)

	TipoDataDiaCard = models.ForeignKey(
		TipoDataDiaCard,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	TipoDataMesOrdn = models.ForeignKey(
		TipoDataMesOrdn,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	TipoDataComDetl = models.ForeignKey(
		TipoDataComDetl,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	TipoDataComAssu = models.ForeignKey(
		TipoDataComAssu,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	EnviarTodos = models.BooleanField(
		blank = True,
		default = None
	)

	AssuntoEMail = models.TextField(
		null = True,
		blank = True,
		default = None,
		max_length = 40000
	)

	MsgEMail = models.TextField(
		null = True,
		blank = True,
		default = None,
		max_length = 40000
	)

	MsgEmailAt = models.BooleanField(
		blank = True,
		default = None
	)

	MsgSMS = models.TextField(
		null = True,
		blank = True,
		default = None,
		max_length = 40000
	)

	MsgSMSAt = models.BooleanField(
		blank = True,
		default = None
	)

	MsgRedeSocLon = models.TextField(
		null = True,
		blank = True,
		default = None,
		max_length = 40000
	)

	MsgRedeSocLonAt = models.BooleanField(
		blank = True,
		default = None
	)

	MsgRedeSocCur = models.TextField(
		null = True,
		blank = True,
		default = None,
		max_length = 40000
	)

	MsgRedeSocCurAt = models.BooleanField(
		blank = True,
		default = None
	)

	Visivel = models.BooleanField(
		blank = True,
		default = None
	)

	AnoInicio = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	AnoTermino = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	Fixo = models.BooleanField(
		blank = True,
		default = None
	)

	Municipal = models.BooleanField(
		blank = True,
		default = None
	)

	Estadual = models.BooleanField(
		blank = True,
		default = None
	)

	Nacional = models.BooleanField(
		blank = True,
		default = None
	)

	Continental = models.BooleanField(
		blank = True,
		default = None
	)

	Continente = models.ForeignKey(
		Continente,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Internacional = models.BooleanField(
		blank = True,
		default = None
	)

	PontoFacultativo = models.BooleanField(
		blank = True,
		default = None
	)

	LembrarDiasAntecedencia = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	Movel = models.BooleanField(
		blank = True,
		default = None
	)

	TipoDataDiaOrdn = models.ForeignKey(
		TipoDataDiaOrdn,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	QuantDias = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	TipoDiaSemTrad = models.ForeignKey(
		TipoDiaSemTrad,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	BancoImagem = models.ForeignKey(
		BancoImagem,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Unidade = models.ForeignKey(
		Unidade,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Ordem = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	TipoReligiao = models.ManyToManyField(
		TipoReligiao,
		related_name = 'TipoDataComTipoReligiao'
	)

	TipoDominioUm = models.ManyToManyField(
		TipoDominioUm,
		related_name = 'TipoDataComTipoDominioUm'
	)

	TipoDominioDois = models.ManyToManyField(
		TipoDominioDois,
		related_name = 'TipoDataComTipoDominioDois'
	)

	Pais = models.ManyToManyField(
		Pais,
		related_name = 'TipoDataComPais'
	)

	Estado = models.ManyToManyField(
		Estado,
		related_name = 'TipoDataComEstado'
	)

	Cidade = models.ManyToManyField(
		Cidade,
		related_name = 'TipoDataComCidade'
	)

	objects = models.Manager()

	def __str__(self):
		return self.Nome


class TipoEstagioProposta(models.Model):
	
	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 50
	)

	Ordem = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	Codigo = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Nome


class PropTecComercial(models.Model):
	
	Codigo = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 8
	)

	Secao = models.ForeignKey(
		Secao,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	TipoEstagioProposta = models.ForeignKey(
		TipoEstagioProposta,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	DataEnvio = models.DateTimeField(
		null = True,
		blank = True,
		default = None
	)

	UltimaAlteracao = models.DateTimeField(
		null = True,
		blank = True,
		default = None
	)

	UltimaConsulta = models.DateTimeField(
		null = True,
		blank = True,
		default = None
	)

	TipoRedeSocial = models.ForeignKey(
		TipoRedeSocial,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	TipoContato = models.ForeignKey(
		TipoContato,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	AgendaDisponivel = models.ForeignKey(
		AgendaDisponivel,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Sintal = models.FloatField(
		null = True,
		blank = True,
		default = None
	)

	ValidacaoCliente = models.DateTimeField(
		null = True,
		blank = True,
		default = None
	)

	SolicitaRepresentanteComercial = models.BooleanField(
		blank = True,
		default = None
	)

	AgendaRepresentanteComercial = models.DateTimeField(
		null = True,
		blank = True,
		default = None
	)

	Parte = models.ManyToManyField(
		Parte,
		related_name = 'PropTecComercialParte'
	)

	Empresa = models.ManyToManyField(
		Empresa,
		related_name = 'PropTecComercialEmpresa'
	)

	objects = models.Manager()

	def __str__(self):
		return self.Codigo


class TipoPeriodicidade(models.Model):
	
	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 200
	)

	Ordem = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Nome


class Lembrete(models.Model):
	
	Mensagem = models.TextField(
		null = True,
		blank = True,
		default = None,
		max_length = 200000
	)

	TipoPeriodicidade = models.ForeignKey(
		TipoPeriodicidade,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Mensagem


class AgendaAtividade(models.Model):
	
	DiaInicio = models.DateField(
		null = True,
		blank = True
	)

	HoraInicio = models.TimeField(
		null = True,
		blank = True
	)

	DiaFim = models.DateField(
		null = True,
		blank = True
	)

	HoraFim = models.TimeField(
		null = True,
		blank = True
	)

	Ordem = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	PropTecComercial = models.ForeignKey(
		PropTecComercial,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Mensagem = models.ForeignKey(
		Mensagem,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Email = models.ForeignKey(
		Email,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	DiaInteiro = models.BooleanField(
		blank = True,
		default = None
	)

	Contato = models.ForeignKey(
		Contato,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Endereco = models.ForeignKey(
		Endereco,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	RedeSocial = models.ForeignKey(
		RedeSocial,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Agenda = models.ForeignKey(
		Agenda,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Url = models.ForeignKey(
		Url,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Microsite = models.ForeignKey(
		Microsite,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Repeticao = models.BooleanField(
		blank = True,
		default = None
	)

	TipoDataCom = models.ForeignKey(
		TipoDataCom,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	HorarioFuncionamento = models.ForeignKey(
		HorarioFuncionamento,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Lembrete = models.ForeignKey(
		Lembrete,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Unidade = models.ManyToManyField(
		Unidade,
		related_name = 'AgendaAtividadeUnidade'
	)

	Parte = models.ManyToManyField(
		Parte,
		related_name = 'AgendaAtividadeParte'
	)

	Empresa = models.ManyToManyField(
		Empresa,
		related_name = 'AgendaAtividadeEmpresa'
	)

	objects = models.Manager()

	def __str__(self):
		return self.DiaInicio


class Combo(models.Model):
	
	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 200
	)

	PrecoVenda = models.FloatField(
		null = True,
		blank = True,
		default = None
	)

	QuantidadeVenda = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	PrecoAluguel = models.FloatField(
		null = True,
		blank = True,
		default = None
	)

	QuantidadeAluguel = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	DataCadastro = models.DateTimeField(
		null = True,
		blank = True,
		default = None
	)

	DataVencimento = models.DateField(
		null = True,
		blank = True
	)

	objects = models.Manager()

	def __str__(self):
		return self.Nome


class ItemUnidade(models.Model):
	
	PrecoVenda = models.FloatField(
		null = True,
		blank = True,
		default = None
	)

	QuantidadeVenda = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	PrecoAluguel = models.FloatField(
		null = True,
		blank = True,
		default = None
	)

	QuantidadeAluguel = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	QuantidadeEmprestimo = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	DataCadastro = models.DateTimeField(
		null = True,
		blank = True,
		default = None
	)

	DataVencimento = models.DateField(
		null = True,
		blank = True
	)

	ItemModelo = models.ForeignKey(
		ItemModelo,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Unidade = models.ForeignKey(
		Unidade,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Combo = models.ManyToManyField(
		Combo,
		related_name = 'ItemUnidadeCombo'
	)

	objects = models.Manager()

	def __str__(self):
		return self.PrecoVenda


class Produto(models.Model):
	
	DisponivelAluguel = models.BooleanField(
		blank = True,
		default = None
	)

	DisponivelVenda = models.BooleanField(
		blank = True,
		default = None
	)

	DisponivelEmprestimo = models.BooleanField(
		blank = True,
		default = None
	)

	NumeroSerie = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 20
	)

	NumeroPatrimonio = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 20
	)

	DataVencimento = models.DateField(
		null = True,
		blank = True
	)

	ItemUnidade = models.ForeignKey(
		ItemUnidade,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.DisponivelAluguel


class TipoLingua(models.Model):
	
	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 200
	)

	Ordem = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Nome


class RelDiagLinguaPais(models.Model):
	
	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	RelDiag = models.ForeignKey(
		RelDiag,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	TipoLingua = models.ForeignKey(
		TipoLingua,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.CodigoIDezoitoN


class TipoDispAmbient(models.Model):
	
	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 200
	)

	Ordem = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	BancoImagem = models.ForeignKey(
		BancoImagem,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Nome


class TipoAutodeclaracao(models.Model):
	
	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 50
	)

	Ordem = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Nome


class EventoInterpCargo(models.Model):
	
	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	TipoCargo = models.ForeignKey(
		TipoCargo,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	ProfissionaisCertificados = models.BooleanField(
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.CodigoIDezoitoN


class RepeticaoInterpretacao(models.Model):
	
	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 200
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Nome


class RepeticaoEvento(models.Model):
	
	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 255
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Nome


class NumeroRecepAuriculares(models.Model):
	
	Numero = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Numero


class EventoDetalhe(models.Model):
	
	BlocoPavilhao = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 200
	)

	Predio = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 200
	)

	Andar = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	Sala = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 200
	)

	LocalApresentaRisco = models.BooleanField(
		blank = True,
		default = None
	)

	TipoDispAmbient = models.ForeignKey(
		TipoDispAmbient,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	RepeticaoEvento = models.ForeignKey(
		RepeticaoEvento,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	NumeroUsuariosFinais = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	NecessitaCabine = models.BooleanField(
		blank = True,
		default = None
	)

	NumeroRecepAuriculares = models.ForeignKey(
		NumeroRecepAuriculares,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	RepeticaoInterpretacao = models.ForeignKey(
		RepeticaoInterpretacao,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	DataInicio = models.DateField(
		null = True,
		blank = True
	)

	HoraInicio = models.TimeField(
		null = True,
		blank = True
	)

	Duracao = models.TimeField(
		null = True,
		blank = True
	)

	QuantidadeInterpretes = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	ProfissionalCertificado = models.BooleanField(
		blank = True,
		default = None
	)

	TipoAutodeclaracao = models.ForeignKey(
		TipoAutodeclaracao,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	NumeroRecepcionistaEvento = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	NecessitaGravacaoAudio = models.BooleanField(
		blank = True,
		default = None
	)

	NecessitaTranscricaoAudio = models.BooleanField(
		blank = True,
		default = None
	)

	NecessitaLegendagemAudio = models.BooleanField(
		blank = True,
		default = None
	)

	InterpreteCoordenadorLingua = models.BooleanField(
		blank = True,
		default = None
	)

	NecessitaTransmissao = models.BooleanField(
		blank = True,
		default = None
	)

	RecepcionistaLingua = models.BooleanField(
		blank = True,
		default = None
	)

	TecnicoOperadorLingua = models.BooleanField(
		blank = True,
		default = None
	)

	SrvTraducaoTranscricaoLingua = models.BooleanField(
		blank = True,
		default = None
	)

	SrvTraducaoLegendagemLingua = models.BooleanField(
		blank = True,
		default = None
	)

	NecessitaSrvComplementares = models.BooleanField(
		blank = True,
		default = None
	)

	NecessitaLocacaoEquipamentos = models.BooleanField(
		blank = True,
		default = None
	)

	Item = models.ForeignKey(
		Item,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	ItemTraducao = models.ForeignKey(
		ItemTraducao,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	ItemModeloTraducao = models.ForeignKey(
		ItemModeloTraducao,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	ItemModelo = models.ForeignKey(
		ItemModelo,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Produto = models.ForeignKey(
		Produto,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	TipoDominioDois = models.ManyToManyField(
		TipoDominioDois,
		related_name = 'EventoDetalheTipoDominioDois'
	)

	RelDiagLinguaPais = models.ManyToManyField(
		RelDiagLinguaPais,
		related_name = 'EventoDetalheRelDiagLinguaPais'
	)

	EventoInterpCargo = models.ManyToManyField(
		EventoInterpCargo,
		related_name = 'EventoDetalheEventoInterpCargo'
	)

	BancoArquivo = models.ManyToManyField(
		BancoArquivo,
		related_name = 'EventoDetalheBancoArquivo'
	)

	objects = models.Manager()

	def __str__(self):
		return self.BlocoPavilhao


class Responsavel(models.Model):
	
	Parte = models.ForeignKey(
		Parte,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Empresa = models.ForeignKey(
		Empresa,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Parte


class TipoLocalPresencial(models.Model):
	
	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 200
	)

	Ordem = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Unidade = models.ForeignKey(
		Unidade,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Nome


class TipoPreferenciaAula(models.Model):
	
	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 200
	)

	Ordem = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Unidade = models.ForeignKey(
		Unidade,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Nome


class TipoFaixaEtaria(models.Model):
	
	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 200
	)

	Ordem = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Nome


class TipoRegimeEnsino(models.Model):
	
	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 200
	)

	Ordem = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Nome


class TipoModalidade(models.Model):
	
	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 200
	)

	Ordem = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Nome


class TipoRepeticaoCurso(models.Model):
	
	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 255
	)

	Ordem = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Nome


class RelDiagCurso(models.Model):
	
	NumeroParticipante = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	RelDiag = models.ForeignKey(
		RelDiag,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	TipoFaixaEtaria = models.ForeignKey(
		TipoFaixaEtaria,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	TipoNivelAluno = models.ForeignKey(
		TipoNivelAluno,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	TipoRegimeEnsino = models.ForeignKey(
		TipoRegimeEnsino,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Unidade = models.ForeignKey(
		Unidade,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	TipoModalidade = models.ForeignKey(
		TipoModalidade,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	TipoContato = models.ForeignKey(
		TipoContato,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Empresa = models.ForeignKey(
		Empresa,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	TipoPreferenciaAula = models.ForeignKey(
		TipoPreferenciaAula,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	DataInicioCurso = models.DateField(
		null = True,
		blank = True
	)

	HoraInicioCurso = models.TimeField(
		null = True,
		blank = True
	)

	DataFimCurso = models.DateField(
		null = True,
		blank = True
	)

	DuracaoAula = models.TimeField(
		null = True,
		blank = True
	)

	TipoRepeticaoCurso = models.ForeignKey(
		TipoRepeticaoCurso,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	ProfessoresCertificados = models.BooleanField(
		blank = True,
		default = None
	)

	Responsavel = models.ForeignKey(
		Responsavel,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Item = models.ForeignKey(
		Item,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	ItemTraducao = models.ForeignKey(
		ItemTraducao,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	ItemModeloTraducao = models.ForeignKey(
		ItemModeloTraducao,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Preco = models.FloatField(
		null = True,
		blank = True,
		default = None
	)

	TipoLocalPresencial = models.ForeignKey(
		TipoLocalPresencial,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	UrgenciaServico = models.BooleanField(
		blank = True,
		default = None
	)

	ConfirmaTransporteEscolar = models.BooleanField(
		blank = True,
		default = None
	)

	ConfirmaTransporteAplicativo = models.BooleanField(
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.NumeroParticipante


class TipoResidenciaContrato(models.Model):
	
	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 50
	)

	Unidade = models.ForeignKey(
		Unidade,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Ordem = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Nome


class TipoHabilitacao(models.Model):
	
	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 100
	)

	Pais = models.ForeignKey(
		Pais,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Visivel = models.BooleanField(
		blank = True,
		default = None
	)

	Ordem = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Nome


class TipoPcDAparelho(models.Model):
	
	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 100
	)

	Ordem = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Nome


class TipoEstadoCivil(models.Model):
	
	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 50
	)

	Ordem = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Nome


class TipoResidencia(models.Model):
	
	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 50
	)

	Ordem = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Nome


class TipoTrabalhoVoluntario(models.Model):
	
	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 50
	)

	Ordem = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Nome


class TipoMorador(models.Model):
	
	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 50
	)

	Ordem = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Nome


class TipoRendaFamiliar(models.Model):
	
	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 50
	)

	Ordem = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Nome


class TipoFilhoQuant(models.Model):
	
	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 30
	)

	Ordem = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Nome


class DadosPessoais(models.Model):
	
	NomeSocialArtistico = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 50
	)

	BancoImagem = models.ForeignKey(
		BancoImagem,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Pais = models.ForeignKey(
		Pais,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Estado = models.ForeignKey(
		Estado,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	TipoAutodeclaracao = models.ForeignKey(
		TipoAutodeclaracao,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	TipoPcDAparelho = models.ForeignKey(
		TipoPcDAparelho,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	TipoPcDCateg = models.ForeignKey(
		TipoPcDCateg,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	TipoEstadoCivil = models.ForeignKey(
		TipoEstadoCivil,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	TipoResidencia = models.ForeignKey(
		TipoResidencia,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	TipoResidenciaContrato = models.ForeignKey(
		TipoResidenciaContrato,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	TipoMorador = models.ForeignKey(
		TipoMorador,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	TipoRendaFamiliar = models.ForeignKey(
		TipoRendaFamiliar,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	TipoFilhoQuant = models.ForeignKey(
		TipoFilhoQuant,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	TipoTrabalhoVoluntario = models.ForeignKey(
		TipoTrabalhoVoluntario,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	TipoHabilitacao = models.ForeignKey(
		TipoHabilitacao,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Fumante = models.BooleanField(
		blank = True,
		default = None
	)

	OAB = models.BooleanField(
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.NomeSocialArtistico


class TipoImovel(models.Model):
	
	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 200
	)

	Ordem = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Unidade = models.ForeignKey(
		Unidade,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Nome


class TipoFuncionarioQuant(models.Model):
	
	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 200
	)

	Ordem = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Unidade = models.ForeignKey(
		Unidade,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Nome


class TipoLicFranquia(models.Model):
	
	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 200
	)

	Ordem = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Nome


class TipoInvestimentoInicial(models.Model):
	
	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 200
	)

	Ordem = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Nome


class TipoCapitalGiro(models.Model):
	
	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 200
	)

	Ordem = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Nome


class TipoAreaMinima(models.Model):
	
	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 200
	)

	Ordem = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Nome


class TipoCompartGeo(models.Model):
	
	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 200
	)

	Ordem = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Nome


class RelDiagLicFranquia(models.Model):
	
	Preco = models.FloatField(
		null = True,
		blank = True,
		default = None
	)

	RelDiag = models.ForeignKey(
		RelDiag,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Parte = models.ForeignKey(
		Parte,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	TipoLicFranquia = models.ForeignKey(
		TipoLicFranquia,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	TipoInvestimentoInicial = models.ForeignKey(
		TipoInvestimentoInicial,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	TipoCapitalGiro = models.ForeignKey(
		TipoCapitalGiro,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	TipoAreaMinima = models.ForeignKey(
		TipoAreaMinima,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	TipoImovel = models.ForeignKey(
		TipoImovel,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	TipoCompartGeo = models.ForeignKey(
		TipoCompartGeo,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	FigurarSiteSimoes = models.BooleanField(
		blank = True,
		default = None
	)

	TipoFuncionarioQuant = models.ForeignKey(
		TipoFuncionarioQuant,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Item = models.ForeignKey(
		Item,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	ItemTraducao = models.ForeignKey(
		ItemTraducao,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	ItemModeloTraducao = models.ForeignKey(
		ItemModeloTraducao,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Preco


class RelDiagTrad(models.Model):
	
	NumeroPalavras = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	Conteudo = models.TextField(
		null = True,
		blank = True,
		default = None
	)

	Url = models.ForeignKey(
		Url,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	DataEntrega = models.DateField(
		null = True,
		blank = True
	)

	HoraEntrega = models.TimeField(
		null = True,
		blank = True
	)

	TipoFusoHorario = models.ForeignKey(
		TipoFusoHorario,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	UrgenciaServico = models.BooleanField(
		blank = True,
		default = None
	)

	ProfissionalRegistrado = models.BooleanField(
		blank = True,
		default = None
	)

	DireitosAutorais = models.BooleanField(
		blank = True,
		default = None
	)

	RelDiag = models.ForeignKey(
		RelDiag,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Secao = models.ForeignKey(
		Secao,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Item = models.ForeignKey(
		Item,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	ItemTraducao = models.ForeignKey(
		ItemTraducao,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	ItemModeloTraducao = models.ForeignKey(
		ItemModeloTraducao,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Preco = models.FloatField(
		null = True,
		blank = True,
		default = None
	)

	TipoSuporteContIO = models.ManyToManyField(
		TipoSuporteContIO,
		related_name = 'RelDiagTradTipoSuporteContIO'
	)

	TipoExtDigEdtIO = models.ManyToManyField(
		TipoExtDigEdtIO,
		related_name = 'RelDiagTradTipoExtDigEdtIO'
	)

	TipoConteudo = models.ManyToManyField(
		TipoConteudo,
		related_name = 'RelDiagTradTipoConteudo'
	)

	BancoArquivo = models.ManyToManyField(
		BancoArquivo,
		related_name = 'RelDiagTradBancoArquivo'
	)

	objects = models.Manager()

	def __str__(self):
		return self.NumeroPalavras


class EventoEndereco(models.Model):
	
	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 255
	)

	Endereco = models.ForeignKey(
		Endereco,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	CodigoEndPostal = models.ForeignKey(
		CodigoEndPostal,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	TipoLogradouro = models.ForeignKey(
		TipoLogradouro,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Logradouro = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 255
	)

	Numero = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	Complemento = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 255
	)

	Bairro = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 200
	)

	Regiao = models.ForeignKey(
		Regiao,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Cidade = models.ForeignKey(
		Cidade,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Estado = models.ForeignKey(
		Estado,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Pais = models.ForeignKey(
		Pais,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	PontoReferencia = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 255
	)

	Latitude = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 200
	)

	Longitute = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 200
	)

	EventoDetalhe = models.ManyToManyField(
		EventoDetalhe,
		related_name = 'EventoEnderecoEventoDetalhe'
	)

	objects = models.Manager()

	def __str__(self):
		return self.Nome


class TipoEvento(models.Model):
	
	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 50
	)

	Unidade = models.ForeignKey(
		Unidade,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Ordem = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Nome


class Evento(models.Model):
	
	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 255
	)

	TemaEvento = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 255
	)

	ProprietarioEvento = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 255
	)

	OrganizadorEvento = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 255
	)

	TipoFusoHorario = models.ForeignKey(
		TipoFusoHorario,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	TipoEvento = models.ForeignKey(
		TipoEvento,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	DataInicioEvento = models.DateField(
		null = True,
		blank = True
	)

	HoraInicioEvento = models.TimeField(
		null = True,
		blank = True
	)

	DataFimEvento = models.DateField(
		null = True,
		blank = True
	)

	HoraFimEvento = models.TimeField(
		null = True,
		blank = True
	)

	PublicoEstimado = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	TipoSuporteCont = models.ManyToManyField(
		TipoSuporteCont,
		related_name = 'EventoTipoSuporteCont'
	)

	TipoExtDigEdit = models.ManyToManyField(
		TipoExtDigEdit,
		related_name = 'EventoTipoExtDigEdit'
	)

	EventoEndereco = models.ManyToManyField(
		EventoEndereco,
		related_name = 'EventoEventoEndereco'
	)

	objects = models.Manager()

	def __str__(self):
		return self.Nome


class TipoPretensaoBolsaEstagio(models.Model):
	
	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 50
	)

	Visivel = models.BooleanField(
		blank = True,
		default = None
	)

	Pais = models.ForeignKey(
		Pais,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Ordem = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Nome


class TipoProgrIcentEducacao(models.Model):
	
	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 50
	)

	Pais = models.ForeignKey(
		Pais,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Ordem = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Nome


class TipoDisponibilEstagiar(models.Model):
	
	Horario = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 50
	)

	Unidade = models.ForeignKey(
		Unidade,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Ordem = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Horario


class TipoTurnoEdu(models.Model):
	
	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 50
	)

	Ordem = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Nome


class ItemBolsaEstagio(models.Model):
	
	Matricula = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 20
	)

	Parte = models.ForeignKey(
		Parte,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	TipoPretensaoBolsaEstagio = models.ForeignKey(
		TipoPretensaoBolsaEstagio,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Valor = models.ForeignKey(
		Valor,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	NotaEnem = models.FloatField(
		null = True,
		blank = True,
		default = None
	)

	TipoProgrIcentEducacao = models.ForeignKey(
		TipoProgrIcentEducacao,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	CoeficienteRendimento = models.FloatField(
		null = True,
		blank = True,
		default = None
	)

	NomeCurso = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 255
	)

	TipoTurnoEdu = models.ForeignKey(
		TipoTurnoEdu,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	TipoDisponibilEstagiar = models.ForeignKey(
		TipoDisponibilEstagiar,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Item = models.ForeignKey(
		Item,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	FoiJovemAprendiz = models.BooleanField(
		blank = True,
		default = None
	)

	AtuandoOutraEmpresa = models.BooleanField(
		blank = True,
		default = None
	)

	DisponibilidadeViagem = models.BooleanField(
		blank = True,
		default = None
	)

	DisponibilidadeTrabalhoExterno = models.BooleanField(
		blank = True,
		default = None
	)

	DisponibilidadeInicioImediato = models.BooleanField(
		blank = True,
		default = None
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Matricula


class Livro(models.Model):
	
	MarcII = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 200
	)

	NumeroControleLCCN = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 50
	)

	ISBN = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 50
	)

	Produto = models.ForeignKey(
		Produto,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.MarcII


class RelDiagLivraria(models.Model):
	
	RelDiag = models.ForeignKey(
		RelDiag,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Produto = models.ForeignKey(
		Produto,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Livro = models.ForeignKey(
		Livro,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Item = models.ForeignKey(
		Item,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	ItemTraducao = models.ForeignKey(
		ItemTraducao,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	ItemModeloTraducao = models.ForeignKey(
		ItemModeloTraducao,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	ItemTipoArea = models.ForeignKey(
		ItemTipoArea,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	ItemModelo = models.ForeignKey(
		ItemModelo,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.RelDiag


class CabecalhoTopo(models.Model):
	
	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 200
	)

	Conteudo = models.TextField(
		null = True,
		blank = True,
		default = None,
		max_length = 200000
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Nome


class Rodape(models.Model):
	
	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 200
	)

	Conteudo = models.TextField(
		null = True,
		blank = True,
		default = None,
		max_length = 200000
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Nome


class RodapeMenu(models.Model):
	
	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 200
	)

	objects = models.Manager()

	def __str__(self):
		return self.Nome


class RodapeBase(models.Model):
	
	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 200
	)

	Conteudo = models.TextField(
		null = True,
		blank = True,
		default = None,
		max_length = 200000
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Nome


class Cabecalho(models.Model):
	
	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 200
	)

	Conteudo = models.TextField(
		null = True,
		blank = True,
		default = None,
		max_length = 200000
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Nome


class CabecalhoMenu(models.Model):
	
	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 200
	)

	objects = models.Manager()

	def __str__(self):
		return self.Nome


class Principal(models.Model):
	
	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 200
	)

	Conteudo = models.TextField(
		null = True,
		blank = True,
		default = None,
		max_length = 200000
	)

	Senha = models.BooleanField(
		blank = True,
		default = None
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Nome


class Site(models.Model):
	
	CabecalhoTopo = models.ForeignKey(
		CabecalhoTopo,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Cabecalho = models.ForeignKey(
		Cabecalho,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	CabecalhoMenu = models.ForeignKey(
		CabecalhoMenu,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Principal = models.ForeignKey(
		Principal,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Rodape = models.ForeignKey(
		Rodape,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	RodapeMenu = models.ForeignKey(
		RodapeMenu,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	RodapeBase = models.ForeignKey(
		RodapeBase,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Unidade = models.ForeignKey(
		Unidade,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.CabecalhoTopo


class TipoPainelAtendimento(models.Model):
	
	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 200
	)

	Ordem = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Unidade = models.ForeignKey(
		Unidade,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Nome


class TipoPosicaoAtendimento(models.Model):
	
	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 200
	)

	Ordem = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Unidade = models.ForeignKey(
		Unidade,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Nome


class TipoOrientacao(models.Model):
	
	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 50
	)

	Ordem = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Nome


class PainelAtendimento(models.Model):
	
	Codigo = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 4
	)

	ProtocoloAtendimento = models.ForeignKey(
		ProtocoloAtendimento,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Data = models.DateTimeField(
		null = True,
		blank = True,
		default = None
	)

	PDV = models.ForeignKey(
		PDV,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	TipoPainelAtendimento = models.ForeignKey(
		TipoPainelAtendimento,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Unidade = models.ForeignKey(
		Unidade,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Identificacao = models.ForeignKey(
		Identificacao,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	TipoPosicaoAtendimento = models.ForeignKey(
		TipoPosicaoAtendimento,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Mensagem = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 50
	)

	TipoOrientacao = models.ForeignKey(
		TipoOrientacao,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	BancoImagem = models.ManyToManyField(
		BancoImagem,
		related_name = 'PainelAtendimentoBancoImagem'
	)

	objects = models.Manager()

	def __str__(self):
		return self.Codigo


class TipoClienteAtende(models.Model):
	
	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 100
	)

	Unidade = models.ForeignKey(
		Unidade,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Ordem = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Nome


class FormatoHora(models.Model):
	
	Ordem = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 100
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Ordem


class TipoSituacOcup(models.Model):
	
	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 100
	)

	Ordem = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Nome


class TipoFormatoData(models.Model):
	
	Formato = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 255
	)

	Ordem = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Formato


class PreferenciaAdicional(models.Model):
	
	ExibirGMT = models.BooleanField(
		blank = True,
		default = None
	)

	UrgenciaServico = models.BooleanField(
		blank = True,
		default = None
	)

	Parte = models.ForeignKey(
		Parte,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	TipoSituacOcup = models.ForeignKey(
		TipoSituacOcup,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	TipoFusoHorario = models.ForeignKey(
		TipoFusoHorario,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	NaoExibirFusoHorario = models.BooleanField(
		blank = True,
		default = None
	)

	TipoFormatoData = models.ForeignKey(
		TipoFormatoData,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	NaoExibirFormatoData = models.BooleanField(
		blank = True,
		default = None
	)

	FormatoHora = models.ForeignKey(
		FormatoHora,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	NaoExibirFormatoHora = models.BooleanField(
		blank = True,
		default = None
	)

	TipoClienteAtende = models.ForeignKey(
		TipoClienteAtende,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Pais = models.ForeignKey(
		Pais,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	TipoComoConheceu = models.ForeignKey(
		TipoComoConheceu,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.ExibirGMT


class Software(models.Model):
	
	Parte = models.ForeignKey(
		Parte,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	TipoSoftwareTraducao = models.ForeignKey(
		TipoSoftwareTraducao,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	TipoSoftwareLocaliz = models.ForeignKey(
		TipoSoftwareLocaliz,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	TipoSoftwareDTP = models.ForeignKey(
		TipoSoftwareDTP,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	TipoSoftwarePacEsc = models.ForeignKey(
		TipoSoftwarePacEsc,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	TipoSoftwareModTresD = models.ForeignKey(
		TipoSoftwareModTresD,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	TipoSoftwareTransc = models.ForeignKey(
		TipoSoftwareTransc,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	TipoSoftwareLeitor = models.ForeignKey(
		TipoSoftwareLeitor,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Parte


class InstituicaoEnsino(models.Model):
	
	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 255
	)

	Parte = models.ForeignKey(
		Parte,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Empresa = models.ForeignKey(
		Empresa,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Ordem = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	Endereco = models.ForeignKey(
		Endereco,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Contato = models.ForeignKey(
		Contato,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Email = models.ForeignKey(
		Email,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Url = models.ForeignKey(
		Url,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	RedeSocial = models.ForeignKey(
		RedeSocial,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Nome


class TipoServTerceiro(models.Model):
	
	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 200
	)

	Ordem = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Nome


class RelDiagServTerceiro(models.Model):
	
	Quantidade = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	Preco = models.FloatField(
		null = True,
		blank = True,
		default = None
	)

	Evento = models.ForeignKey(
		Evento,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	DataRetirada = models.DateField(
		null = True,
		blank = True
	)

	HoraRetirada = models.TimeField(
		null = True,
		blank = True
	)

	DataDevolucao = models.DateField(
		null = True,
		blank = True
	)

	HoraDevolucao = models.TimeField(
		null = True,
		blank = True
	)

	RelDiag = models.ForeignKey(
		RelDiag,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Cargo = models.ForeignKey(
		Cargo,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	TipoServTerceiro = models.ForeignKey(
		TipoServTerceiro,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Item = models.ForeignKey(
		Item,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	ItemTraducao = models.ForeignKey(
		ItemTraducao,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	ItemModeloTraducao = models.ForeignKey(
		ItemModeloTraducao,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Quantidade


class ParteLinguaPais(models.Model):
	
	LinguaMaterna = models.BooleanField(
		blank = True,
		default = None
	)

	LinguaMaternaVerificada = models.BooleanField(
		blank = True,
		default = None
	)

	Parte = models.ForeignKey(
		Parte,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Lingua = models.ForeignKey(
		Lingua,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Pais = models.ForeignKey(
		Pais,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	TipoProficienciaLingua = models.ForeignKey(
		TipoProficienciaLingua,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Ordem = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	TipoCargoTrad = models.ManyToManyField(
		TipoCargoTrad,
		related_name = 'ParteLinguaPaisTipoCargoTrad'
	)

	FormCompl = models.ManyToManyField(
		FormCompl,
		related_name = 'ParteLinguaPaisFormCompl'
	)

	objects = models.Manager()

	def __str__(self):
		return self.LinguaMaterna


class TipoNota(models.Model):
	
	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 100
	)

	Ordem = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Nome


class Nota(models.Model):
	
	Numero = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	Serie = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 5
	)

	ChaveAcesso = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 50
	)

	TributoAproxMunicipal = models.FloatField(
		null = True,
		blank = True,
		default = None
	)

	TributoAproxEstadual = models.FloatField(
		null = True,
		blank = True,
		default = None
	)

	TributoAproxFederal = models.FloatField(
		null = True,
		blank = True,
		default = None
	)

	SimplesConferencia = models.BooleanField(
		blank = True,
		default = None
	)

	RelDiag = models.ForeignKey(
		RelDiag,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Unidade = models.ForeignKey(
		Unidade,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Parte = models.ForeignKey(
		Parte,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	TipoNota = models.ForeignKey(
		TipoNota,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	QRCode = models.ForeignKey(
		QRCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Numero


class ListaCampanha(models.Model):
	
	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 255
	)

	Parte = models.ForeignKey(
		Parte,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Descricao = models.TextField(
		null = True,
		blank = True,
		default = None,
		max_length = 20000
	)

	DataCriacao = models.DateTimeField(
		null = True,
		blank = True,
		default = None
	)

	QuantContato = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	CtrlQualidade = models.ForeignKey(
		CtrlQualidade,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Nome


class EmpresaLinguaPais(models.Model):
	
	Nativo = models.BooleanField(
		blank = True,
		default = None
	)

	Empresa = models.ForeignKey(
		Empresa,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Lingua = models.ForeignKey(
		Lingua,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Pais = models.ForeignKey(
		Pais,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	FormCompl = models.ManyToManyField(
		FormCompl,
		related_name = 'EmpresaLinguaPaisFormCompl'
	)

	objects = models.Manager()

	def __str__(self):
		return self.Nativo


class TipoAcao(models.Model):
	
	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 100
	)

	Ordem = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	HoraInicio = models.TimeField(
		null = True,
		blank = True
	)

	HoraFim = models.TimeField(
		null = True,
		blank = True
	)

	Unidade = models.ForeignKey(
		Unidade,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Nome


class AgendaPermissao(models.Model):
	
	Agenda = models.ForeignKey(
		Agenda,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	TipoAcao = models.ForeignKey(
		TipoAcao,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Unidade = models.ManyToManyField(
		Unidade,
		related_name = 'AgendaPermissaoUnidade'
	)

	Parte = models.ManyToManyField(
		Parte,
		related_name = 'AgendaPermissaoParte'
	)

	Empresa = models.ManyToManyField(
		Empresa,
		related_name = 'AgendaPermissaoEmpresa'
	)

	objects = models.Manager()

	def __str__(self):
		return self.Agenda


class TipoClassLista(models.Model):
	
	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 200
	)

	Ordem = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Nome


class TipoStatusLista(models.Model):
	
	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 200
	)

	Ordem = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Nome


class ListaContato(models.Model):
	
	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 200
	)

	DataNascimento = models.DateField(
		null = True,
		blank = True
	)

	Contato = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 20
	)

	Ativo = models.BooleanField(
		blank = True,
		default = None
	)

	Numero = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	Texto = models.TextField(
		null = True,
		blank = True,
		default = None,
		max_length = 200000
	)

	Cidade = models.ForeignKey(
		Cidade,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Bairro = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 120
	)

	TipoContato = models.ForeignKey(
		TipoContato,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	TipoStatusLista = models.ForeignKey(
		TipoStatusLista,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	TipoClassLista = models.ForeignKey(
		TipoClassLista,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	DataAtualizacao = models.DateTimeField(
		null = True,
		blank = True,
		default = None
	)

	DataCriacao = models.DateTimeField(
		null = True,
		blank = True,
		default = None
	)

	ListaCampanha = models.ManyToManyField(
		ListaCampanha,
		related_name = 'ListaContatoListaCampanha'
	)

	objects = models.Manager()

	def __str__(self):
		return self.Nome


class ListaEmail(models.Model):
	
	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 200
	)

	Email = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 250
	)

	Ativo = models.BooleanField(
		blank = True,
		default = None
	)

	DataNascimento = models.DateField(
		null = True,
		blank = True
	)

	Numero = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	Texto = models.TextField(
		null = True,
		blank = True,
		default = None,
		max_length = 200000
	)

	Cidade = models.ForeignKey(
		Cidade,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Bairro = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 120
	)

	TipoStatusLista = models.ForeignKey(
		TipoStatusLista,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	TipoClassLista = models.ForeignKey(
		TipoClassLista,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	DataAtualizacao = models.DateTimeField(
		null = True,
		blank = True,
		default = None
	)

	DataCriacao = models.DateTimeField(
		null = True,
		blank = True,
		default = None
	)

	TipoEmail = models.ForeignKey(
		TipoEmail,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	ListaCampanha = models.ManyToManyField(
		ListaCampanha,
		related_name = 'ListaEmailListaCampanha'
	)

	objects = models.Manager()

	def __str__(self):
		return self.Nome


class Filme(models.Model):
	
	ClassificacaoEtaria = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	Duracao = models.DateTimeField(
		null = True,
		blank = True,
		default = None
	)

	ProporcaoTela = models.FloatField(
		null = True,
		blank = True,
		default = None
	)

	Produto = models.ForeignKey(
		Produto,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Pais = models.ForeignKey(
		Pais,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Url = models.ManyToManyField(
		Url,
		related_name = 'FilmeUrl'
	)

	BancoImagem = models.ManyToManyField(
		BancoImagem,
		related_name = 'FilmeBancoImagem'
	)

	objects = models.Manager()

	def __str__(self):
		return self.ClassificacaoEtaria


class RelDiagLicPlano(models.Model):
	
	Preco = models.FloatField(
		null = True,
		blank = True,
		default = None
	)

	RelDiag = models.ForeignKey(
		RelDiag,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Parte = models.ForeignKey(
		Parte,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Item = models.ForeignKey(
		Item,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	ItemTraducao = models.ForeignKey(
		ItemTraducao,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	ItemModeloTraducao = models.ForeignKey(
		ItemModeloTraducao,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Preco


class ItemLocacaoBalcao(models.Model):
	
	Quantidade = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	Item = models.ForeignKey(
		Item,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	ItemTraducao = models.ForeignKey(
		ItemTraducao,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	ItemModeloTraducao = models.ForeignKey(
		ItemModeloTraducao,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	ItemModelo = models.ForeignKey(
		ItemModelo,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Produto = models.ForeignKey(
		Produto,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Quantidade


class TipoAcaoCampanha(models.Model):
	
	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 20
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	Ordem = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Nome


class TipoStatusCampanha(models.Model):
	
	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 20
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	Ordem = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Nome


class TipoCategoriaModeloCampanha(models.Model):
	
	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 200
	)

	CodigoIDezeoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	Ordem = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Nome


class TipoModeloCampanha(models.Model):
	
	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 255
	)

	Ordem = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	CorpoTextoSimples = models.TextField(
		null = True,
		blank = True,
		default = None,
		max_length = 200000
	)

	CorpoHTML = models.TextField(
		null = True,
		blank = True,
		default = None,
		max_length = 200000
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	TipoCategoriaModeloCampanha = models.ForeignKey(
		TipoCategoriaModeloCampanha,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	DataCriacao = models.DateTimeField(
		null = True,
		blank = True,
		default = None
	)

	DataAtualizacao = models.DateTimeField(
		null = True,
		blank = True,
		default = None
	)

	Url = models.ForeignKey(
		Url,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Nome


class ModeloCampanha(models.Model):
	
	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 200
	)

	TipoModeloCampanha = models.ForeignKey(
		TipoModeloCampanha,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	ValidarAntiSpam = models.BooleanField(
		blank = True,
		default = None
	)

	DataCriacao = models.DateTimeField(
		null = True,
		blank = True,
		default = None
	)

	DataAtualizacao = models.DateTimeField(
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Nome


class Campanha(models.Model):
	
	NomeCampanha = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 200
	)

	AssuntoEmail = models.TextField(
		null = True,
		blank = True,
		default = None,
		max_length = 500
	)

	NomeRemetente = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 100
	)

	EmailEnvio = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 200
	)

	ContatoEnvio = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 20
	)

	DataCriacao = models.DateTimeField(
		null = True,
		blank = True,
		default = None
	)

	QuantidadeMensagem = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	QuantContato = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	TipoStatusCampanha = models.ForeignKey(
		TipoStatusCampanha,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	ModeloCampanha = models.ForeignKey(
		ModeloCampanha,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	TipoAcaoCampanha = models.ForeignKey(
		TipoAcaoCampanha,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Mensagem = models.ManyToManyField(
		Mensagem,
		related_name = 'CampanhaMensagem'
	)

	ListaCampanha = models.ManyToManyField(
		ListaCampanha,
		related_name = 'CampanhaListaCampanha'
	)

	objects = models.Manager()

	def __str__(self):
		return self.NomeCampanha


class TipoPerfilLocutor(models.Model):
	
	FichaTecnica = models.TextField(
		null = True,
		blank = True,
		default = None,
		max_length = 4000
	)

	RadioAtuacao = models.TextField(
		null = True,
		blank = True,
		default = None,
		max_length = 4000
	)

	Equipamentos = models.TextField(
		null = True,
		blank = True,
		default = None,
		max_length = 4000
	)

	CapacidadeProducao = models.TextField(
		null = True,
		blank = True,
		default = None,
		max_length = 4000
	)

	CaracteristicasVocais = models.TextField(
		null = True,
		blank = True,
		default = None,
		max_length = 4000
	)

	Ordem = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.FichaTecnica


class ItemTipoPerfilLocutor(models.Model):
	
	Parte = models.ForeignKey(
		Parte,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Item = models.ForeignKey(
		Item,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	TipoPerfilLocutor = models.ForeignKey(
		TipoPerfilLocutor,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Valor = models.ForeignKey(
		Valor,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Parte


class TipoCategoriaServico(models.Model):
	
	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 50
	)

	Unidade = models.ForeignKey(
		Unidade,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Ordem = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Nome


class ItemCategoriaServico(models.Model):
	
	Parte = models.ForeignKey(
		Parte,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Item = models.ForeignKey(
		Item,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	TipoCategoriaServico = models.ForeignKey(
		TipoCategoriaServico,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Valor = models.ForeignKey(
		Valor,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Parte


class TipoTamanho(models.Model):
	
	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 50
	)

	Ordem = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Nome


class ModeloDocumento(models.Model):
	
	CodigoFonte = models.TextField(
		null = True,
		blank = True,
		default = None,
		max_length = 4000
	)

	TipoOrientacao = models.ForeignKey(
		TipoOrientacao,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	TipoTamanho = models.ForeignKey(
		TipoTamanho,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	PapelTimbrado = models.BooleanField(
		blank = True,
		default = None
	)

	BancoArquivo = models.ForeignKey(
		BancoArquivo,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	BancoImagem = models.ForeignKey(
		BancoImagem,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.CodigoFonte


class TipoLicConvenio(models.Model):
	
	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 200
	)

	Ordem = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Nome


class RelDiagLicConvenio(models.Model):
	
	Preco = models.FloatField(
		null = True,
		blank = True,
		default = None
	)

	Aliquota =  models.DecimalField(
		null = True,
		blank = True,
		default = None,
		max_digits = 5,
		decimal_places = 3
	)

	DataInicio = models.DateField(
		null = True,
		blank = True
	)

	DataFim = models.DateField(
		null = True,
		blank = True
	)

	RelDiag = models.ForeignKey(
		RelDiag,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Parte = models.ForeignKey(
		Parte,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	TipoLicConvenio = models.ForeignKey(
		TipoLicConvenio,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	ConvenioAtivo = models.BooleanField(
		blank = True,
		default = None
	)

	Secao = models.ForeignKey(
		Secao,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Preco


class MedidaNotaItem(models.Model):
	
	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 100
	)

	Ordem = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Nome


class NotaItem(models.Model):
	
	Quantidade = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	Preco = models.FloatField(
		null = True,
		blank = True,
		default = None
	)

	Nota = models.ForeignKey(
		Nota,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	ItemModeloTraducao = models.ForeignKey(
		ItemModeloTraducao,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	MedidaNotaItem = models.ForeignKey(
		MedidaNotaItem,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Imposto = models.ForeignKey(
		Imposto,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Quantidade


class PrestadorPreferencial(models.Model):
	
	Unidade = models.ForeignKey(
		Unidade,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Cargo = models.ForeignKey(
		Cargo,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Parte = models.ManyToManyField(
		Parte,
		related_name = 'PrestadorPreferencialParte'
	)

	Empresa = models.ManyToManyField(
		Empresa,
		related_name = 'PrestadorPreferencialEmpresa'
	)

	objects = models.Manager()

	def __str__(self):
		return self.Unidade


class Comercial(models.Model):
	
	Unidade = models.ForeignKey(
		Unidade,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	PropTecComercial = models.ManyToManyField(
		PropTecComercial,
		related_name = 'ComercialPropTecComercial'
	)

	Parte = models.ManyToManyField(
		Parte,
		related_name = 'ComercialParte'
	)

	Empresa = models.ManyToManyField(
		Empresa,
		related_name = 'ComercialEmpresa'
	)

	objects = models.Manager()

	def __str__(self):
		return self.Unidade


class OpcaoMenu(models.Model):
	
	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 200
	)

	Ordem = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	Url = models.ForeignKey(
		Url,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	RodapeMenu = models.ManyToManyField(
		RodapeMenu,
		related_name = 'OpcaoMenuRodapeMenu'
	)

	CabecalhoMenu = models.ManyToManyField(
		CabecalhoMenu,
		related_name = 'OpcaoMenuCabecalhoMenu'
	)

	objects = models.Manager()

	def __str__(self):
		return self.Nome


class TipoPercPgto(models.Model):
	
	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 200
	)

	Ordem = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	Percentual = models.FloatField(
		null = True,
		blank = True,
		default = None
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Unidade = models.ForeignKey(
		Unidade,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Nome


class PgtoSinalCliente(models.Model):
	
	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 200
	)

	TempoInicio = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	TempoFim = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	Outorga = models.ForeignKey(
		Outorga,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Item = models.ForeignKey(
		Item,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Criterio = models.TextField(
		null = True,
		blank = True,
		default = None,
		max_length = 2000000
	)

	Unidade = models.ForeignKey(
		Unidade,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	TipoPercPgto = models.ForeignKey(
		TipoPercPgto,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Nome


class TipoPercntDesmb(models.Model):
	
	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 200
	)

	Ordem = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	Percentual = models.FloatField(
		null = True,
		blank = True,
		default = None
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Unidade = models.ForeignKey(
		Unidade,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Nome


class PgtoColab(models.Model):
	
	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 200
	)

	TempoInicio = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	TempoFim = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	Outorga = models.ForeignKey(
		Outorga,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Item = models.ForeignKey(
		Item,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Criterio = models.TextField(
		null = True,
		blank = True,
		default = None,
		max_length = 200000
	)

	Unidade = models.ForeignKey(
		Unidade,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	TipoPercntDesmb = models.ForeignKey(
		TipoPercntDesmb,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Nome


class TipoEnderecamento(models.Model):
	
	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 200
	)

	Ordem = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Unidade = models.ForeignKey(
		Unidade,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Nome


class Enderecamento(models.Model):
	
	TipoEnderecamento = models.ForeignKey(
		TipoEnderecamento,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Mensagem = models.ForeignKey(
		Mensagem,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Parte = models.ManyToManyField(
		Parte,
		related_name = 'EnderecamentoParte'
	)

	Empresa = models.ManyToManyField(
		Empresa,
		related_name = 'EnderecamentoEmpresa'
	)

	objects = models.Manager()

	def __str__(self):
		return self.TipoEnderecamento


class TipoObraLiteraria(models.Model):
	
	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 100
	)

	Ordem = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Nome


class ItemObraLiteraria(models.Model):
	
	Parte = models.ForeignKey(
		Parte,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Item = models.ForeignKey(
		Item,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	TipoObraLiteraria = models.ForeignKey(
		TipoObraLiteraria,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Valor = models.ForeignKey(
		Valor,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Parte


class TipoObraCientifica(models.Model):
	
	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 50
	)

	Ordem = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Nome


class ItemObraCientifica(models.Model):
	
	Parte = models.ForeignKey(
		Parte,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Item = models.ForeignKey(
		Item,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	TipoObraCientifica = models.ForeignKey(
		TipoObraCientifica,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Valor = models.ForeignKey(
		Valor,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Parte


class TipoPcD(models.Model):
	
	Produz = models.BooleanField(
		blank = True,
		default = None
	)

	TipoPcDCateg = models.ForeignKey(
		TipoPcDCateg,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Ordem = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Produz


class TipoItemCompEqpTempo(models.Model):
	
	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 100
	)

	Ordem = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	Percentual =  models.DecimalField(
		null = True,
		blank = True,
		default = None,
		max_digits = 5,
		decimal_places = 3
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Nome


class ItemCompEqp(models.Model):
	
	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 200
	)

	Ordem = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	Item = models.ForeignKey(
		Item,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Descricao = models.TextField(
		null = True,
		blank = True,
		default = None,
		max_length = 20000
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	TipoItemCompEqpTempo = models.ManyToManyField(
		TipoItemCompEqpTempo,
		related_name = 'ItemCompEqpTipoItemCompEqpTempo'
	)

	objects = models.Manager()

	def __str__(self):
		return self.Nome


class TipoAssociacao(models.Model):
	
	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 200
	)

	Ordem = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Nome


class AssociadoParte(models.Model):
	
	Parte = models.ForeignKey(
		Parte,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	CodigoAssociado = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 15
	)

	objects = models.Manager()

	def __str__(self):
		return self.Parte


class AssociadoEmpresa(models.Model):
	
	Empresa = models.ForeignKey(
		Empresa,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	CodigoAssociado = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 15
	)

	objects = models.Manager()

	def __str__(self):
		return self.Empresa


class Associacao(models.Model):
	
	TipoAssociacao = models.ForeignKey(
		TipoAssociacao,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Outorga = models.ManyToManyField(
		Outorga,
		related_name = 'AssociacaoOutorga'
	)

	AssociadoParte = models.ManyToManyField(
		AssociadoParte,
		related_name = 'AssociacaoAssociadoParte'
	)

	AssociadoEmpresa = models.ManyToManyField(
		AssociadoEmpresa,
		related_name = 'AssociacaoAssociadoEmpresa'
	)

	objects = models.Manager()

	def __str__(self):
		return self.TipoAssociacao


class TipoFluenciaVerb(models.Model):
	
	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 50
	)

	TipoCtrlQualidade = models.ForeignKey(
		TipoCtrlQualidade,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Ordem = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Nome


class TipoPerfilGerentProjeto(models.Model):
	
	OrganizaProjeto = models.TextField(
		null = True,
		blank = True,
		default = None,
		max_length = 4000
	)

	PraticaLideranca = models.TextField(
		null = True,
		blank = True,
		default = None,
		max_length = 4000
	)

	PraticaComunicacao = models.TextField(
		null = True,
		blank = True,
		default = None,
		max_length = 4000
	)

	RealizaNegociacao = models.TextField(
		null = True,
		blank = True,
		default = None,
		max_length = 4000
	)

	GerenciaCrises = models.TextField(
		null = True,
		blank = True,
		default = None,
		max_length = 4000
	)

	TomadaDecisao = models.TextField(
		null = True,
		blank = True,
		default = None,
		max_length = 4000
	)

	Ordem = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	Persistencia = models.TextField(
		null = True,
		blank = True,
		default = None,
		max_length = 4000
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.OrganizaProjeto


class ItemTipoPerfilGerProjeto(models.Model):
	
	Parte = models.ForeignKey(
		Parte,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Item = models.ForeignKey(
		Item,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	TipoPerfilGerentProjeto = models.ForeignKey(
		TipoPerfilGerentProjeto,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Valor = models.ForeignKey(
		Valor,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Parte


class ItemTipoEvento(models.Model):
	
	Parte = models.ForeignKey(
		Parte,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Item = models.ForeignKey(
		Item,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	TipoEvento = models.ForeignKey(
		TipoEvento,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Valor = models.ForeignKey(
		Valor,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Parte


class TipoSistemasInformacao(models.Model):
	
	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 50
	)

	Unidade = models.ForeignKey(
		Unidade,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Ordem = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Nome


class ItemSistemasInformacao(models.Model):
	
	Parte = models.ForeignKey(
		Parte,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Item = models.ForeignKey(
		Item,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	TipoSistemasInformacao = models.ForeignKey(
		TipoSistemasInformacao,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Valor = models.ForeignKey(
		Valor,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Parte


class ItemTipoPcD(models.Model):
	
	Parte = models.ForeignKey(
		Parte,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Item = models.ForeignKey(
		Item,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	TipoPcD = models.ForeignKey(
		TipoPcD,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Valor = models.ForeignKey(
		Valor,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Parte


class TipoObraArtistica(models.Model):
	
	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 50
	)

	Ordem = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Nome


class ItemObraArtistica(models.Model):
	
	Parte = models.ForeignKey(
		Parte,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Item = models.ForeignKey(
		Item,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	TipoObraArtistica = models.ForeignKey(
		TipoObraArtistica,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Valor = models.ForeignKey(
		Valor,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Parte


class TipoVolumeMedioVendaSemanal(models.Model):
	
	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 100
	)

	Visivel = models.BooleanField(
		blank = True,
		default = None
	)

	Unidade = models.ForeignKey(
		Unidade,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Pais = models.ForeignKey(
		Pais,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Ordem = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Nome


class TipoModulo(models.Model):
	
	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 50
	)

	Ordem = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Nome


class Permissao(models.Model):
	
	SomenteLeitura = models.BooleanField(
		blank = True,
		default = None
	)

	AlterarGravar = models.BooleanField(
		blank = True,
		default = None
	)

	Excluir = models.BooleanField(
		blank = True,
		default = None
	)

	Parte = models.ForeignKey(
		Parte,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Outorga = models.ForeignKey(
		Outorga,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	TipoModulo = models.ForeignKey(
		TipoModulo,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.SomenteLeitura


class TipoEstiloLocucao(models.Model):
	
	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 50
	)

	Ordem = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Nome


class ItemTipoEstiloLocucao(models.Model):
	
	Parte = models.ForeignKey(
		Parte,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Item = models.ForeignKey(
		Item,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	TipoEstiloLocucao = models.ForeignKey(
		TipoEstiloLocucao,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Valor = models.ForeignKey(
		Valor,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Parte


class TipoVozGenero(models.Model):
	
	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 50
	)

	Ordem = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Nome


class ItemTipoVozGenero(models.Model):
	
	Parte = models.ForeignKey(
		Parte,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Item = models.ForeignKey(
		Item,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	TipoVozGenero = models.ForeignKey(
		TipoVozGenero,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Valor = models.ForeignKey(
		Valor,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Parte


class TipoFocoLocucao(models.Model):
	
	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 70
	)

	Unidade = models.ForeignKey(
		Unidade,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Ordem = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Nome


class ItemTipoFocoLocucao(models.Model):
	
	Parte = models.ForeignKey(
		Parte,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Item = models.ForeignKey(
		Item,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	TipoFocoLocucao = models.ForeignKey(
		TipoFocoLocucao,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Valor = models.ForeignKey(
		Valor,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Parte


class TipoVozIdade(models.Model):
	
	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 50
	)

	Ordem = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Nome


class ItemTipoVozIdade(models.Model):
	
	Parte = models.ForeignKey(
		Parte,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Item = models.ForeignKey(
		Item,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	TipoVozIdade = models.ForeignKey(
		TipoVozIdade,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Valor = models.ForeignKey(
		Valor,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Parte


class TipoVozAmostra(models.Model):
	
	Arquivo = models.BinaryField(
		null = True,
		blank = True,
		default = None
	)

	Ordem = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Arquivo


class ItemTipoVozAmostra(models.Model):
	
	Parte = models.ForeignKey(
		Parte,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Item = models.ForeignKey(
		Item,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	TipoVozAmostra = models.ForeignKey(
		TipoVozAmostra,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Valor = models.ForeignKey(
		Valor,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Parte


class AgendaAtividadeHistorico(models.Model):
	
	Concluido = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	EComoFoi = models.TextField(
		null = True,
		blank = True,
		default = None,
		max_length = 20000
	)

	QuandoFoi = models.TextField(
		null = True,
		blank = True,
		default = None,
		max_length = 20000
	)

	Data = models.DateTimeField(
		null = True,
		blank = True,
		default = None
	)

	AgendaAtividade = models.ForeignKey(
		AgendaAtividade,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Parte = models.ForeignKey(
		Parte,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	CtrlQualidade = models.ForeignKey(
		CtrlQualidade,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Concluido


class Hardware(models.Model):
	
	Parte = models.ForeignKey(
		Parte,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	TipoHardwareComputador = models.ForeignKey(
		TipoHardwareComputador,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	TipoPeriferico = models.ForeignKey(
		TipoPeriferico,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	TipoSuporteCont = models.ForeignKey(
		TipoSuporteCont,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Parte


class TipoProficCateg(models.Model):
	
	Descricao = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 200
	)

	TipoCtrlQualidade = models.ForeignKey(
		TipoCtrlQualidade,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Ordem = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Descricao


class ParteLinguaPaisTipoProficCateg(models.Model):
	
	Ordem = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	ParteLinguaPais = models.ForeignKey(
		ParteLinguaPais,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	TipoProficCateg = models.ForeignKey(
		TipoProficCateg,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	TipoFluenciaVerb = models.ForeignKey(
		TipoFluenciaVerb,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	TipoCtrlQualidade = models.ForeignKey(
		TipoCtrlQualidade,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Ordem


class ParEmpresaLinguaPais(models.Model):
	
	Partida = models.BooleanField(
		blank = True,
		default = None
	)

	Chegada = models.BooleanField(
		blank = True,
		default = None
	)

	EmpresaLinguaPais = models.ForeignKey(
		EmpresaLinguaPais,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Valor = models.ForeignKey(
		Valor,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	TipoCargoTrad = models.ManyToManyField(
		TipoCargoTrad,
		related_name = 'ParEmpresaLinguaPaisTipoCargoTrad'
	)

	objects = models.Manager()

	def __str__(self):
		return self.Partida


class TipoFaseLua(models.Model):
	
	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 80
	)

	Abreviatura = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 10
	)

	Descricao = models.TextField(
		null = True,
		blank = True,
		default = None,
		max_length = 40000
	)

	TipoHemisferio = models.ForeignKey(
		TipoHemisferio,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	BancoImagem = models.ForeignKey(
		BancoImagem,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Ordem = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Nome


class TipoLingProg(models.Model):
	
	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 50
	)

	Visivel = models.BooleanField(
		blank = True,
		default = None
	)

	Unidade = models.ForeignKey(
		Unidade,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Ordem = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Nome


class ParteTipoLingProg(models.Model):
	
	Parte = models.ForeignKey(
		Parte,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	TipoLingProg = models.ForeignKey(
		TipoLingProg,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	TipoEngineGame = models.ForeignKey(
		TipoEngineGame,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Parte


class TipoLocacao(models.Model):
	
	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 200
	)

	Ordem = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Unidade = models.ForeignKey(
		Unidade,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Nome


class RelDiagLocEquipamento(models.Model):
	
	DataRetirada = models.DateField(
		null = True,
		blank = True
	)

	HoraRetirada = models.TimeField(
		null = True,
		blank = True
	)

	DataDevolucao = models.DateField(
		null = True,
		blank = True
	)

	HoraDevolucao = models.TimeField(
		null = True,
		blank = True
	)

	RelDiag = models.ForeignKey(
		RelDiag,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	TipoLocacao = models.ForeignKey(
		TipoLocacao,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Evento = models.ForeignKey(
		Evento,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.DataRetirada


class RelDiagInterpretacao(models.Model):
	
	NomeEvento = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 200
	)

	RelDiag = models.ForeignKey(
		RelDiag,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Evento = models.ForeignKey(
		Evento,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	TemaEvento = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 200
	)

	InstituicaoEvento = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 200
	)

	TituloPalestra = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 50
	)

	UrgenciaServico = models.BooleanField(
		blank = True,
		default = None
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.NomeEvento


class Certificacao(models.Model):
	
	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 100
	)

	Parte = models.ForeignKey(
		Parte,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	TipoCertificacao = models.ForeignKey(
		TipoCertificacao,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	TipoDataAnoCard = models.ForeignKey(
		TipoDataAnoCard,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Nome


class TipoRestricao(models.Model):
	
	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 200
	)

	Ordem = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Unidade = models.ForeignKey(
		Unidade,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Nome


class TipoBiometria(models.Model):
	
	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 200
	)

	Unidade = models.ForeignKey(
		Unidade,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Ordem = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Nome


class ListaRestricao(models.Model):
	
	Data = models.DateTimeField(
		null = True,
		blank = True,
		default = None
	)

	TipoRestricao = models.ForeignKey(
		TipoRestricao,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Parte = models.ManyToManyField(
		Parte,
		related_name = 'ListaRestricaoParte'
	)

	Empresa = models.ManyToManyField(
		Empresa,
		related_name = 'ListaRestricaoEmpresa'
	)

	objects = models.Manager()

	def __str__(self):
		return self.Data


class Biometria(models.Model):
	
	Codigo = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	Parte = models.ForeignKey(
		Parte,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	TipoBiometria = models.ForeignKey(
		TipoBiometria,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	BancoImagem = models.ManyToManyField(
		BancoImagem,
		related_name = 'BiometriaBancoImagem'
	)

	objects = models.Manager()

	def __str__(self):
		return self.Codigo


class LinguaPais(models.Model):
	
	HabilitarLinguaSite = models.BooleanField(
		blank = True,
		default = None
	)

	Lingua = models.ForeignKey(
		Lingua,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Pais = models.ForeignKey(
		Pais,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Ordem = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return str(self.Pais)


class TipoLicOportunidade(models.Model):
	
	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 200
	)

	Ordem = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Nome


class RelDiagLicOportunidade(models.Model):
	
	RelDiag = models.ForeignKey(
		RelDiag,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Parte = models.ForeignKey(
		Parte,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	TipoLicOportunidade = models.ForeignKey(
		TipoLicOportunidade,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.RelDiag


class Inventario(models.Model):
	
	DataIventario = models.DateField(
		null = True,
		blank = True
	)

	QuantidadeInventariada = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	DataProximoIventario = models.DateField(
		null = True,
		blank = True
	)

	Observacao = models.TextField(
		null = True,
		blank = True,
		default = None,
		max_length = 10485760
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	Parte = models.ForeignKey(
		Parte,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Produto = models.ForeignKey(
		Produto,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.DataIventario


class ConvenioParteEmpresa(models.Model):
	
	Aliquota =  models.DecimalField(
		null = True,
		blank = True,
		default = None,
		max_digits = 5,
		decimal_places = 3
	)

	Convenio = models.ForeignKey(
		Convenio,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Parte = models.ForeignKey(
		Parte,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Empresa = models.ForeignKey(
		Empresa,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Aliquota


class ConvenioItem(models.Model):
	
	Preco = models.FloatField(
		null = True,
		blank = True,
		default = None
	)

	Item = models.ForeignKey(
		Item,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	ItemTraducao = models.ForeignKey(
		ItemTraducao,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	ItemModeloTraducao = models.ForeignKey(
		ItemModeloTraducao,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	AliquotaMax =  models.DecimalField(
		null = True,
		blank = True,
		default = None,
		max_digits = 5,
		decimal_places = 3
	)

	objects = models.Manager()

	def __str__(self):
		return self.Preco


class LinguaPaisEmpresa(models.Model):
	
	Lingua = models.ForeignKey(
		Lingua,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Pais = models.ForeignKey(
		Pais,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Empresa = models.ForeignKey(
		Empresa,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Lingua


class EmpresaLinguaPaisTipoProficCateg(models.Model):
	
	EmpresaLinguaPais = models.ForeignKey(
		EmpresaLinguaPais,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	TipoProficCateg = models.ForeignKey(
		TipoProficCateg,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	TipoFluenciaVerb = models.ForeignKey(
		TipoFluenciaVerb,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.EmpresaLinguaPais


class ParEmpresaLinguaInstCertific(models.Model):
	
	Outro = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 255
	)

	ParEmpresaLinguaPais = models.ForeignKey(
		ParEmpresaLinguaPais,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	TipoInstCertific = models.ForeignKey(
		TipoInstCertific,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Url = models.ForeignKey(
		Url,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Outro


class TipoEstacAno(models.Model):
	
	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 50
	)

	Ordem = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Nome


class TipoEstacAnoIni(models.Model):
	
	Data = models.DateField(
		null = True,
		blank = True
	)

	Hora = models.TimeField(
		null = True,
		blank = True
	)

	TipoHemisferio = models.ForeignKey(
		TipoHemisferio,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Descricao = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 500
	)

	Equinocio = models.BooleanField(
		blank = True,
		default = None
	)

	Solsticio = models.BooleanField(
		blank = True,
		default = None
	)

	TipoEstacAno = models.ForeignKey(
		TipoEstacAno,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Ordem = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Data


class TipoDataComDA(models.Model):
	
	TipoDataDiaCard = models.ForeignKey(
		TipoDataDiaCard,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	TipoDataMesOrdn = models.ForeignKey(
		TipoDataMesOrdn,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	TipoDataCom = models.ForeignKey(
		TipoDataCom,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.TipoDataDiaCard


class ParteTipoSuporteCont(models.Model):
	
	Parte = models.ForeignKey(
		Parte,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	TipoSuporteCont = models.ForeignKey(
		TipoSuporteCont,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Partida = models.BooleanField(
		blank = True,
		default = None
	)

	Chegada = models.BooleanField(
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Parte


class RelDiagServAdClosedCaption(models.Model):
	
	RelDiagServAd = models.ForeignKey(
		RelDiagServAd,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Evento = models.ForeignKey(
		Evento,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.RelDiagServAd


class RelDiagServAdDigitacao(models.Model):
	
	NumeroPagina = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	RelDiagServAd = models.ForeignKey(
		RelDiagServAd,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	TipoTamanho = models.ForeignKey(
		TipoTamanho,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.NumeroPagina


class Consignado(models.Model):
	
	Quantidade = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	DataInicio = models.DateField(
		null = True,
		blank = True
	)

	DataFim = models.DateField(
		null = True,
		blank = True
	)

	Item = models.ForeignKey(
		Item,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Empresa = models.ForeignKey(
		Empresa,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Quantidade


class ItemCompEqpCargo(models.Model):
	
	Quantidade = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	Cargo = models.ForeignKey(
		Cargo,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	ItemCompEqp = models.ForeignKey(
		ItemCompEqp,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	QuantidadeMinRaqueamentoCargo = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Quantidade


class BancoImagemTraducao(models.Model):
	
	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 255
	)

	Descricao = models.TextField(
		null = True,
		blank = True,
		default = None,
		max_length = 200000
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	BancoImagem = models.ForeignKey(
		BancoImagem,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Nome


class Auditoria(models.Model):
	
	NomeAuditoria = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 255
	)

	User = models.ForeignKey(
		User,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Conteudo = models.TextField(
		null = True,
		blank = True,
		default = None,
		max_length = 4000
	)

	TipoModulo = models.ForeignKey(
		TipoModulo,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Data = models.DateTimeField(
		null = True,
		blank = True,
		default = None
	)

	Ip = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 128
	)

	NomeDispositivo = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 100
	)

	MacAddress = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 100
	)

	objects = models.Manager()

	def __str__(self):
		return self.NomeAuditoria


class LivroTraducao(models.Model):
	
	Autor = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 200
	)

	InformacaoTitulo = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 100
	)

	Edicao = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 50
	)

	InformacaoPublicacao = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 200
	)

	DescricaoFisica = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 255
	)

	EntradaSecundarioSerie = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 255
	)

	MencaoSerie = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 255
	)

	NotaResumo = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 255
	)

	CabecalhoAssuntoTopico = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 255
	)

	EntradaSecundariaNomePessoal = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 255
	)

	Livro = models.ForeignKey(
		Livro,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Autor


class ItemLinguaPais(models.Model):
	
	Item = models.ForeignKey(
		Item,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Item


class ExperienciaAdminTraducao(models.Model):
	
	AtuacaoLideranca = models.TextField(
		null = True,
		blank = True,
		default = None,
		max_length = 4000
	)

	AssumirResponsabilidades = models.TextField(
		null = True,
		blank = True,
		default = None,
		max_length = 4000
	)

	CompreensaoNovasTecnologias = models.TextField(
		null = True,
		blank = True,
		default = None,
		max_length = 4000
	)

	LiderarPeloExemplo = models.TextField(
		null = True,
		blank = True,
		default = None,
		max_length = 4000
	)

	CapacidadePedirAjuda = models.TextField(
		null = True,
		blank = True,
		default = None,
		max_length = 4000
	)

	InteligenciaColetiva = models.TextField(
		null = True,
		blank = True,
		default = None,
		max_length = 4000
	)

	TomadaDecisoes = models.TextField(
		null = True,
		blank = True,
		default = None,
		max_length = 4000
	)

	ReconhecimentoMeritos = models.TextField(
		null = True,
		blank = True,
		default = None,
		max_length = 4000
	)

	Feedback = models.TextField(
		null = True,
		blank = True,
		default = None,
		max_length = 4000
	)

	LimitesPessoais = models.TextField(
		null = True,
		blank = True,
		default = None,
		max_length = 4000
	)

	Parte = models.ForeignKey(
		Parte,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.AtuacaoLideranca


class ExperienciaComercialDescritiva(models.Model):
	
	Motivacao = models.TextField(
		null = True,
		blank = True,
		default = None,
		max_length = 4000
	)

	Dinamismo = models.TextField(
		null = True,
		blank = True,
		default = None,
		max_length = 4000
	)

	Proatividade = models.TextField(
		null = True,
		blank = True,
		default = None,
		max_length = 4000
	)

	HabilidadeNegociacao = models.TextField(
		null = True,
		blank = True,
		default = None,
		max_length = 4000
	)

	RelacionamentoPessoal = models.TextField(
		null = True,
		blank = True,
		default = None,
		max_length = 4000
	)

	ApresentacaoCliente = models.TextField(
		null = True,
		blank = True,
		default = None,
		max_length = 4000
	)

	AssumirRiscos = models.TextField(
		null = True,
		blank = True,
		default = None,
		max_length = 4000
	)

	ValorEticoMoral = models.TextField(
		null = True,
		blank = True,
		default = None,
		max_length = 4000
	)

	ProspectarNovoCliente = models.TextField(
		null = True,
		blank = True,
		default = None,
		max_length = 4000
	)

	AssumirResponsabilidade = models.TextField(
		null = True,
		blank = True,
		default = None,
		max_length = 4000
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	Parte = models.ForeignKey(
		Parte,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Motivacao


class Venda(models.Model):
	
	PercentualMinimoSobreVendas = models.FloatField(
		null = True,
		blank = True,
		default = None
	)

	TipoVolumeMedioVendaSemanal = models.ForeignKey(
		TipoVolumeMedioVendaSemanal,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	TipoVolumeAcumuladoVenda = models.ForeignKey(
		TipoVolumeAcumuladoVenda,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.PercentualMinimoSobreVendas


class TipoDataAnoOrdn(models.Model):
	
	AnoOrdinal = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 150
	)

	AnoExtMasc = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 200
	)

	TipoDataAnoCard = models.ForeignKey(
		TipoDataAnoCard,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Ordem = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.AnoOrdinal


class EventoDetalheDominioUm(models.Model):
	
	EventoDetalhe = models.ForeignKey(
		EventoDetalhe,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	TipoDominioUm = models.ForeignKey(
		TipoDominioUm,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.EventoDetalhe


class RanqueamentoCargo(models.Model):
	
	TipoServicoLinguisticoPrestado = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	MediaRecebQualidServPrestado = models.FloatField(
		null = True,
		blank = True,
		default = None
	)

	MediaRecebPrazoServPrestado = models.FloatField(
		null = True,
		blank = True,
		default = None
	)

	IdiomaOrigemDestinoLingaMatern = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	NumeroParticipacaoProjeto = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	DominioUmProxAreaConhecimento = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	DominioDoisProxSetorEconomico = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	FormAcadem = models.ForeignKey(
		FormAcadem,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	CapacidadeDiariaTrabalho = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	CertificacoeConquistada = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	PrecoCadastradoCargo = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	ProximidadeLocalServico = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	Peso = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	Nota = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	Media = models.FloatField(
		null = True,
		blank = True,
		default = None
	)

	MediaGeral = models.FloatField(
		null = True,
		blank = True,
		default = None
	)

	Cargo = models.ForeignKey(
		Cargo,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.TipoServicoLinguisticoPrestado


class FilmeTraducao(models.Model):
	
	Titulo = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 50
	)

	Sinopse = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 255
	)

	Genero = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 100
	)

	Diretor = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 100
	)

	Roteirista = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 100
	)

	Elenco = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 255
	)

	Cor = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 200
	)

	Produtora = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 200
	)

	Locacao = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 255
	)

	Filme = models.ForeignKey(
		Filme,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Titulo


class AssinaturaBancoArquivo(models.Model):
	
	BancoArquivo = models.ForeignKey(
		BancoArquivo,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Parte = models.ForeignKey(
		Parte,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Data = models.DateTimeField(
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.BancoArquivo


class TipoPergSegur(models.Model):
	
	Pergunta = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 255
	)

	Ordem = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Pergunta


class Seguranca(models.Model):
	
	TipoPergSegur = models.ForeignKey(
		TipoPergSegur,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None,
		verbose_name = "Pergunta de Segurança"
	)

	RespostaPerguntaSeguranca = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 500,
		verbose_name = "Resposta da pergunta"
	)

	AceitoTermoUso = models.BooleanField(
		blank = True,
		default = None,
		verbose_name = "Aceitar Termo de Uso"
	)

	Parte = models.ForeignKey(
		Parte,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	DeclaracaoMaiorDezesseisAnos = models.BooleanField(
		blank = True,
		default = None,
		verbose_name = "Declaro ser maior de 16 anos"
	)

	objects = models.Manager()

	def __str__(self):
		return self.TipoPergSegur


class BancoArquivoTraducao(models.Model):
	
	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 50
	)

	Descricao = models.TextField(
		null = True,
		blank = True,
		default = None,
		max_length = 200000
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	BancoArquivo = models.ForeignKey(
		BancoArquivo,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Nome


class TipoListaContato(models.Model):
	
	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 200
	)

	Ordem = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Unidade = models.ForeignKey(
		Unidade,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Nome


class ItemPermissao(models.Model):
	
	Unidade = models.ForeignKey(
		Unidade,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	Item = models.ForeignKey(
		Item,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	NaoExibirUrl = models.BooleanField(
		blank = True,
		default = None
	)

	NaoExibirInstant = models.BooleanField(
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Unidade


class ParParteLinguaPais(models.Model):
	
	ParteLinguaPaisPartida = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	ParteLinguaPaisChegada = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	Ordem = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	FormCompl = models.ManyToManyField(
		FormCompl,
		related_name = 'ParParteLinguaPaisFormCompl'
	)

	FormAcadem = models.ManyToManyField(
		FormAcadem,
		related_name = 'ParParteLinguaPaisFormAcadem'
	)

	objects = models.Manager()

	def __str__(self):
		return self.ParteLinguaPaisPartida


class TipoCalendLunar(models.Model):
	
	Data = models.DateField(
		null = True,
		blank = True
	)

	TipoFaseLua = models.ForeignKey(
		TipoFaseLua,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	EclipseSolar = models.BooleanField(
		blank = True,
		default = None
	)

	EclipseLunar = models.BooleanField(
		blank = True,
		default = None
	)

	Ordem = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Data


class RelDiagServAdLegendagem(models.Model):
	
	QuantMinutosIniciais = models.TimeField(
		null = True,
		blank = True
	)

	QuantMinutosReais = models.TimeField(
		null = True,
		blank = True
	)

	RelDiagServAd = models.ForeignKey(
		RelDiagServAd,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.QuantMinutosIniciais


class RelDiagServAdRedacao(models.Model):
	
	NumPalavrasIniciais = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	NumPalavrasReais = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	RelDiagServAd = models.ForeignKey(
		RelDiagServAd,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.NumPalavrasIniciais


class RelDiagServAdConsulLinguistica(models.Model):
	
	QuantHoraInicial = models.TimeField(
		null = True,
		blank = True
	)

	QuantHoraReal = models.TimeField(
		null = True,
		blank = True
	)

	RelDiagServAd = models.ForeignKey(
		RelDiagServAd,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.QuantHoraInicial


class RelDiagServAdAuditLinguistica(models.Model):
	
	QuantHoraInicial = models.TimeField(
		null = True,
		blank = True
	)

	QuantHoraReal = models.TimeField(
		null = True,
		blank = True
	)

	RelDiagServAd = models.ForeignKey(
		RelDiagServAd,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.QuantHoraInicial


class RelDiagServAdDublagem(models.Model):
	
	RelDiagServAd = models.ForeignKey(
		RelDiagServAd,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.RelDiagServAd


class RelDiagServAdLocucao(models.Model):
	
	RelDiagServAd = models.ForeignKey(
		RelDiagServAd,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	TempoDuracaoAudio = models.TimeField(
		null = True,
		blank = True
	)

	objects = models.Manager()

	def __str__(self):
		return self.RelDiagServAd


class CodigoPromocional(models.Model):
	
	Codigo = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 8
	)

	Desconto = models.ForeignKey(
		Desconto,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Codigo


class Plano(models.Model):
	
	PagamentoAssociado = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 50
	)

	PagamentoAnual = models.FloatField(
		null = True,
		blank = True,
		default = None
	)

	ItemUnidade = models.ForeignKey(
		ItemUnidade,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	PagamentoMensal = models.FloatField(
		null = True,
		blank = True,
		default = None
	)

	ConsultaAvulsaCurriculo = models.FloatField(
		null = True,
		blank = True,
		default = None
	)

	ModCadastramentoCurriculo = models.BooleanField(
		blank = True,
		default = None
	)

	ModRecrutamentoSelecao = models.BooleanField(
		blank = True,
		default = None
	)

	ModCadastro = models.BooleanField(
		blank = True,
		default = None
	)

	ModAutenticacaoDocumento = models.BooleanField(
		blank = True,
		default = None
	)

	ModContaReceber = models.BooleanField(
		blank = True,
		default = None
	)

	ModContaPagar = models.BooleanField(
		blank = True,
		default = None
	)

	ModCadastramentoTabelaPreco = models.BooleanField(
		blank = True,
		default = None
	)

	ModProjeto = models.BooleanField(
		blank = True,
		default = None
	)

	ModEmissaoPropostaInstantanea = models.BooleanField(
		blank = True,
		default = None
	)

	ModCrm = models.BooleanField(
		blank = True,
		default = None
	)

	ModLance = models.BooleanField(
		blank = True,
		default = None
	)

	ModContrato = models.BooleanField(
		blank = True,
		default = None
	)

	ModFinanceiro = models.BooleanField(
		blank = True,
		default = None
	)

	ModPedagogico = models.BooleanField(
		blank = True,
		default = None
	)

	ModPortalAluno = models.BooleanField(
		blank = True,
		default = None
	)

	ModIndicador = models.BooleanField(
		blank = True,
		default = None
	)

	ModAgenda = models.BooleanField(
		blank = True,
		default = None
	)

	ModControleFrequencia = models.BooleanField(
		blank = True,
		default = None
	)

	ModIntegracao = models.BooleanField(
		blank = True,
		default = None
	)

	ModPerfilUsuarioColaborador = models.BooleanField(
		blank = True,
		default = None
	)

	ModCustomizacao = models.BooleanField(
		blank = True,
		default = None
	)

	ModPesClimaAvaliacaoDesempenho = models.BooleanField(
		blank = True,
		default = None
	)

	Usuario = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	Suporte = models.FloatField(
		null = True,
		blank = True,
		default = None
	)

	Capacidade = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 30
	)

	objects = models.Manager()

	def __str__(self):
		return self.PagamentoAssociado


class Etapa(models.Model):
	
	Titulo = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 255
	)

	Descricao = models.TextField(
		null = True,
		blank = True,
		default = None,
		max_length = 2000
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Titulo


class ExperienciaAdministratOutra(models.Model):
	
	ExperienciaVendas = models.BooleanField(
		blank = True,
		default = None
	)

	ExperienciaPreviaNegocProprio = models.BooleanField(
		blank = True,
		default = None
	)

	DisponibilidadeViagens = models.BooleanField(
		blank = True,
		default = None
	)

	ExperienciaFranquias = models.BooleanField(
		blank = True,
		default = None
	)

	ExperienciaCapitalInicial = models.BooleanField(
		blank = True,
		default = None
	)

	Parte = models.ForeignKey(
		Parte,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.ExperienciaVendas


class ExperienciaComercialOutra(models.Model):
	
	PossuiEmpresa = models.BooleanField(
		blank = True,
		default = None
	)

	VeiculoProprio = models.BooleanField(
		blank = True,
		default = None
	)

	ExperienciaVendasSegmento = models.BooleanField(
		blank = True,
		default = None
	)

	PossuiEstruturaPropria = models.BooleanField(
		blank = True,
		default = None
	)

	CarteiraClientes = models.BooleanField(
		blank = True,
		default = None
	)

	DisponibilidadeViagens = models.BooleanField(
		blank = True,
		default = None
	)

	Parte = models.ForeignKey(
		Parte,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.PossuiEmpresa


class RelDiagServAdRevisaoTexto(models.Model):
	
	QuantPalavrasIniciais = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	QuantPalavrasReais = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	RelDiagServAd = models.ForeignKey(
		RelDiagServAd,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.QuantPalavrasIniciais


class RelDiagServAdDiagramacao(models.Model):
	
	QuantPaginasIniciais = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	QuantPaginasReais = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	RelDiagServAd = models.ForeignKey(
		RelDiagServAd,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.QuantPaginasIniciais


class RelDiagServAdTranscricaoAudio(models.Model):
	
	RelDiagServAd = models.ForeignKey(
		RelDiagServAd,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.RelDiagServAd


class RelDiagServAdAudiodescricao(models.Model):
	
	QuantidadeImagens = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	DuracaoVideo = models.TimeField(
		null = True,
		blank = True
	)

	DuracaoDescricao = models.TimeField(
		null = True,
		blank = True
	)

	RelDiagServAd = models.ForeignKey(
		RelDiagServAd,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.QuantidadeImagens


class DescricaoAdicional(models.Model):
	
	PremiosRecebidos = models.TextField(
		null = True,
		blank = True,
		default = None,
		max_length = 4000
	)

	FluxoTrabalho = models.TextField(
		null = True,
		blank = True,
		default = None,
		max_length = 4000
	)

	ProcessoQualidade = models.TextField(
		null = True,
		blank = True,
		default = None,
		max_length = 4000
	)

	LivreApresentacao = models.TextField(
		null = True,
		blank = True,
		default = None,
		max_length = 4000
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.PremiosRecebidos


class PreferenciaAdicionalEmpresa(models.Model):
	
	ContratoEstagiario = models.BooleanField(
		blank = True,
		default = None
	)

	SubContrataOutraEmpresa = models.BooleanField(
		blank = True,
		default = None
	)

	OportunidadeColaborador = models.BooleanField(
		blank = True,
		default = None
	)

	OportunidadeFreelancer = models.BooleanField(
		blank = True,
		default = None
	)

	OportunidadePcD = models.BooleanField(
		blank = True,
		default = None
	)

	Empresa = models.ForeignKey(
		Empresa,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.ContratoEstagiario


class EmpresaTraducao(models.Model):
	
	Slogan = models.TextField(
		null = True,
		blank = True,
		default = None,
		max_length = 4000
	)

	Visao = models.TextField(
		null = True,
		blank = True,
		default = None,
		max_length = 4000
	)

	ProdutosServicos = models.TextField(
		null = True,
		blank = True,
		default = None,
		max_length = 4000
	)

	Descricao = models.TextField(
		null = True,
		blank = True,
		default = None,
		max_length = 4000
	)

	Missao = models.TextField(
		null = True,
		blank = True,
		default = None,
		max_length = 4000
	)

	Valor = models.TextField(
		null = True,
		blank = True,
		default = None,
		max_length = 150
	)

	ValorDescricao = models.TextField(
		null = True,
		blank = True,
		default = None,
		max_length = 4000
	)

	CodigoIDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	Apresentacao = models.TextField(
		null = True,
		blank = True,
		default = None,
		max_length = 2000000
	)

	Observacao = models.TextField(
		null = True,
		blank = True,
		default = None,
		max_length = 4000
	)

	SobreEmpresa = models.TextField(
		null = True,
		blank = True,
		default = None,
		max_length = 4000
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Slogan


class CodigoEndPostDesc(models.Model):
	
	Population = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	CodigoEndPostal = models.ForeignKey(
		CodigoEndPostal,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	HouseholdsPerZipcode = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	WhitePopulation = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	BlackPopulation = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	HispanicPopulation = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	AsianPopulation = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	HawaiianPopulation = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	IndianPopulation = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	OtherPopulation = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	MalePopulation = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	FemalePopulation = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	PersonsPerHousehold =  models.DecimalField(
		null = True,
		blank = True,
		default = None,
		max_digits = 7,
		decimal_places = 3
	)

	AverageHouseValue = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	IncomePerHousehold = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	MedianAge =  models.DecimalField(
		null = True,
		blank = True,
		default = None,
		max_digits = 6,
		decimal_places = 3
	)

	MedianAgeMale =  models.DecimalField(
		null = True,
		blank = True,
		default = None,
		max_digits = 6,
		decimal_places = 3
	)

	MedianAgeFemale =  models.DecimalField(
		null = True,
		blank = True,
		default = None,
		max_digits = 6,
		decimal_places = 3
	)

	Elevation = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	State = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 2
	)

	StateFullName = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 35
	)

	CityType = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 1
	)

	CityAliasAbbreviation = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 13
	)

	AreaCode = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 55
	)

	City = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 35
	)

	CityAliasName = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 35
	)

	County = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 45
	)

	CountyFIPS = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 2
	)

	StateFIPS = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 2
	)

	TimeZone = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 2
	)

	DayLightSaving = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 1
	)

	MSA = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 35
	)

	PMSA = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 4
	)

	CSA = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 3
	)

	CBSA = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 5
	)

	CBSA_DIV = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 5
	)

	CBSA_Type = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 5
	)

	CBSA_Name = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 150
	)

	MSA_Name = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 150
	)

	PMSA_Name = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 150
	)

	Region = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 10
	)

	Division = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 20
	)

	MailingName = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 1
	)

	NumberOfBusinesses = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	NumberOfEmployees = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	BusinessFirstQuarterPayroll = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	BusinessAnnualPayroll = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	BusinessEmploymentFlag = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 1
	)

	GrowthRank = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	GrowingCountiesA = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	GrowingCountiesB = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	GrowthIncreaseNumber = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	GrowthIncreasePercentage =  models.DecimalField(
		null = True,
		blank = True,
		default = None,
		max_digits = 6,
		decimal_places = 3
	)

	CBSAPopulation = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	CBSADivisionPopulation = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	CongressionalDistrict = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 150
	)

	CongressionalLandArea = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 150
	)

	DeliveryResidential = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	DeliveryBusiness = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	DeliveryTotal = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	PreferredLastLineKey = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 10
	)

	ClassificationCode = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 1
	)

	MultiCounty = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 1
	)

	CSAName = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 150
	)

	CBSA_DIV_Name = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 150
	)

	CityStateKey = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 6
	)

	PopulationEstimate = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	LandArea =  models.DecimalField(
		null = True,
		blank = True,
		default = None,
		max_digits = 21,
		decimal_places = 3
	)

	WaterArea =  models.DecimalField(
		null = True,
		blank = True,
		default = None,
		max_digits = 21,
		decimal_places = 3
	)

	CityAliasCode = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 5
	)

	CityMixedCase = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 35
	)

	CityAliasMixedCase = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 35
	)

	BoxCount = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	SFDU = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	MFDU = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	StateANSI = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 2
	)

	CountyANSI = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 3
	)

	ZIPIntroDate = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 15
	)

	AliasIntroDate = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 15
	)

	FacilityCode = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 1
	)

	CityDeliveryIndicator = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 1
	)

	CarrierRouteRateSortation = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 1
	)

	FinanceNumber = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 10
	)

	UniqueZIPName = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 1
	)

	SSAStateCountyCode = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 255
	)

	MedicareCBSACode = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 255
	)

	MedicareCBSAName = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 255
	)

	MedicareCBSAType = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 255
	)

	MarketRatingAreaID = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	STATE = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 2
	)

	STATEFIPS = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 2
	)

	PLACEFIPS = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 5
	)

	PLACENAME = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 255
	)

	PLACETYPE = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 255
	)

	COUNTY = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 255
	)

	FUNCSTAT = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 1
	)

	FUNCSTATTEXT = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 255
	)

	CLASSFP = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 2
	)

	GEOID = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 7
	)

	POPPT = models.BigIntegerField(
		null = True,
		blank = True,
		default = None
	)

	HUPT = models.BigIntegerField(
		null = True,
		blank = True,
		default = None
	)

	AREAPT = models.BigIntegerField(
		null = True,
		blank = True,
		default = None
	)

	AREALANDPT = models.BigIntegerField(
		null = True,
		blank = True,
		default = None
	)

	ZPOP = models.BigIntegerField(
		null = True,
		blank = True,
		default = None
	)

	ZHU = models.BigIntegerField(
		null = True,
		blank = True,
		default = None
	)

	ZAREA = models.BigIntegerField(
		null = True,
		blank = True,
		default = None
	)

	ZAREALAND = models.BigIntegerField(
		null = True,
		blank = True,
		default = None
	)

	PLPOP = models.BigIntegerField(
		null = True,
		blank = True,
		default = None
	)

	PLHU = models.BigIntegerField(
		null = True,
		blank = True,
		default = None
	)

	PLAREA = models.BigIntegerField(
		null = True,
		blank = True,
		default = None
	)

	PLAREALAND = models.BigIntegerField(
		null = True,
		blank = True,
		default = None
	)

	ZPOPPCT =  models.DecimalField(
		null = True,
		blank = True,
		default = None,
		max_digits = 15,
		decimal_places = 3
	)

	ZHUPCT =  models.DecimalField(
		null = True,
		blank = True,
		default = None,
		max_digits = 15,
		decimal_places = 3
	)

	ZAREAPCT =  models.DecimalField(
		null = True,
		blank = True,
		default = None,
		max_digits = 15,
		decimal_places = 3
	)

	ZAREALANDPCT =  models.DecimalField(
		null = True,
		blank = True,
		default = None,
		max_digits = 15,
		decimal_places = 3
	)

	PLPOPPCT =  models.DecimalField(
		null = True,
		blank = True,
		default = None,
		max_digits = 15,
		decimal_places = 3
	)

	PLHUPCT =  models.DecimalField(
		null = True,
		blank = True,
		default = None,
		max_digits = 15,
		decimal_places = 3
	)

	PLAREAPCT =  models.DecimalField(
		null = True,
		blank = True,
		default = None,
		max_digits = 15,
		decimal_places = 3
	)

	PLAREALANDPCT =  models.DecimalField(
		null = True,
		blank = True,
		default = None,
		max_digits = 15,
		decimal_places = 3
	)

	City = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 255
	)

	AreaCode = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 10
	)

	ProvinceName = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 255
	)

	CityFlag = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 255
	)

	TimeZone = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 255
	)

	Elevation = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 255
	)

	PrivateDwellings = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 255
	)

	AreaName = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 255
	)

	MunicipalityName = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 255
	)

	imprecise = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 255
	)

	military = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 255
	)

	objects = models.Manager()

	def __str__(self):
		return self.Population


class TipoFeriado(models.Model):
	
	Nome = models.CharField(
		null = True,
		blank = True,
		default = None,
		max_length = 100
	)

	Ordem = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	CodigoDezoitoN = models.IntegerField(
		null = True,
		blank = True,
		default = None
	)

	LanguageCode = models.ForeignKey(
		LanguageCode,
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		default = None
	)

	objects = models.Manager()

	def __str__(self):
		return self.Nome

