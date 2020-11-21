from django.contrib.auth.models import User
from rest_framework import serializers
from instantdesenv.models import *


class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = [
			'id',
			'first_name',
			'last_name',
			'username',
			'email',
			'password'
		]
		read_only_fields = ['id']
		extra_kwargs = {
			'password': {'write_only': True}
		}


class LanguageCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = LanguageCode
        fields = [
			'id',
			'CodAlfanumerico',
			'Nome',
			'Descricao',
			'Ordem',
			'CodigoIDezoitoN',
			'LanguageCode'
		]
        

class PalavraChaveSerializer(serializers.ModelSerializer):
    class Meta:
        model = PalavraChave
        fields = [
			'id',
			'Nome',
			'CodigoIDezoitoN',
			'LanguageCode'
		]
        

class TipoBancoImagemSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoBancoImagem
        fields = [
			'id',
			'Nome',
			'Principal',
			'Ordem',
			'CodigoIDezoitoN',
			'LanguageCode'
		]
        

class BancoImagemSerializer(serializers.ModelSerializer):
    class Meta:
        model = BancoImagem
        fields = [
			'id',
			'Arquivo',
			'TipoBancoImagem',
			'PalavraChave',
			'Principal',
			'NaoVisivel',
			'ProibirImpressao',
			'ProibirDownload'
		]
        

class ContinenteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Continente
        fields = [
			'id',
			'CodAlfanumerico',
			'Nome',
			'Gentilico',
			'CodigoContinente',
			'Ordem',
			'CodigoIDezoitoN',
			'LanguageCode'
		]
        

class TipoHemisferioSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoHemisferio
        fields = [
			'id',
			'Nome',
			'Ordem',
			'CodigoIDezoitoN',
			'LanguageCode'
		]
        

class AreaGeograficaSerializer(serializers.ModelSerializer):
    class Meta:
        model = AreaGeografica
        fields = [
			'id',
			'CodAlfanumerico',
			'Nome',
			'Gentilico',
			'Continente',
			'Ordem',
			'CodigoIDezoitoN',
			'LanguageCode'
		]
        

class PaisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pais
        fields = [
			'id',
			'CodAlfanumerico',
			'Nome',
			'NomeOficial',
			'Gentilico',
			'Soberania',
			'CodigoISODois',
			'CodigoISOTres',
			'InternetccTLD',
			'DataFundacao',
			'Continente',
			'TipoHemisferio',
			'CodigoDiscagem',
			'Ordem',
			'CodigoIDezoitoN',
			'AreaGeografica',
			'LanguageCode',
			'BancoImagem'
		]
        

class RegiaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Regiao
        fields = [
			'id',
			'CodAlfanumerico',
			'Nome',
			'Pais',
			'Ordem',
			'CodigoIDezoitoN',
			'LanguageCode'
		]
        

class TipoOrgaoEmissSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoOrgaoEmiss
        fields = [
			'id',
			'Nome',
			'Sigla',
			'Comentario',
			'Visivel',
			'Pais',
			'Ordem',
			'CodigoIDezoitoN',
			'LanguageCode'
		]
        

class EstadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estado
        fields = [
			'id',
			'CodAlfanumerico',
			'Sigla',
			'Nome',
			'Gentilico',
			'Capital',
			'DataFundacao',
			'Regiao',
			'Ordem',
			'CodigoIDezoitoN',
			'Pais',
			'LanguageCode',
			'TipoOrgaoEmiss'
		]
        

class CidadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cidade
        fields = [
			'id',
			'CodAlfanumerico',
			'Nome',
			'Gentilico',
			'DataFundacao',
			'Estado',
			'Pais',
			'CodigoDiscagem',
			'AreaCidade',
			'DensidadeDemografica',
			'Ordem',
			'CodigoIDezoitoN',
			'LanguageCode',
			'BancoImagem'
		]
        

class TipoLogradouroSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoLogradouro
        fields = [
			'id',
			'Nome',
			'Abreviatura',
			'Ordem',
			'CodigoIDezoitoN',
			'LanguageCode'
		]
        

class CodigoEndPostalSerializer(serializers.ModelSerializer):
    class Meta:
        model = CodigoEndPostal
        fields = [
			'id',
			'CodigoPostal',
			'TipoLogradouro',
			'Logradouro',
			'ComplementoLogra',
			'Bairro',
			'Cidade',
			'Estado',
			'Pais',
			'Latitude',
			'Longitude',
			'LanguageCode',
			'AreaRestricaoEntregaDiferenciada',
			'AreaRestricaoEntregaInterna'
		]
        

class TipoComplementoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoComplemento
        fields = [
			'id',
			'Nome',
			'Abreviatura',
			'Ordem',
			'CodigoIDezoitoN',
			'LanguageCode'
		]
        

class TipoEnderecoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoEndereco
        fields = [
			'id',
			'Nome',
			'Ordem',
			'CodigoIDezoitoN',
			'LanguageCode'
		]
        

class EnderecoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Endereco
        fields = [
			'id',
			'Logradouro',
			'Numero',
			'Complemento',
			'CaixaPostal',
			'Bairro',
			'CodigoEndPostal',
			'CodigoPostal',
			'TipoEndereco',
			'TipoLogradouro',
			'Regiao',
			'Cidade',
			'CidadeNome',
			'Estado',
			'Pais',
			'PontoReferencia',
			'CopiaComprovante',
			'Latitude',
			'Longitude',
			'Ajustelatlong',
			'NaoExibirLogradouro',
			'NaoExibirNumero',
			'NaoExibirComplemento',
			'NaoExibirCaixaPostal',
			'NaoExibirBairro',
			'NaoExibirPontoReferencia',
			'NaoExibirLatitude',
			'NaoExibirLongitude',
			'NaoExibirEndereco',
			'NaoExibirLocalizacao',
			'LanguageCode',
			'TipoComplemento',
			'BancoImagem'
		]
        

class TipoContatoTecnSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoContatoTecn
        fields = [
			'id',
			'Nome',
			'Ordem',
			'CodioIDezoitoN',
			'LanguageCode'
		]
        

class TipoContatoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoContato
        fields = [
			'id',
			'Nome',
			'Visivel',
			'HabilitarPropTecComercial',
			'TipoContatoTecn',
			'Ordem',
			'CodigoIDezoitoN',
			'LanguageCode'
		]
        

class TipoOpTelefoniaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoOpTelefonia
        fields = [
			'id',
			'Nome',
			'Codigo',
			'Pais',
			'Ordem',
			'CodigoIDezoitoN',
			'LanguageCode'
		]
        

class ContatoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contato
        fields = [
			'id',
			'CodigoDiscagemInternacional',
			'TipoContato',
			'Pais',
			'Cidade',
			'TipoOpTelefonia',
			'CodigoDiscagemNacional',
			'Identificacao',
			'Ramal',
			'NomeRecado',
			'Principal',
			'NaoExibirContato'
		]
        

class TipoPcDCategSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoPcDCateg
        fields = [
			'id',
			'Nome',
			'Ordem',
			'CodigoIDezoitoN',
			'LanguageCode'
		]
        

class TipoDiaSemanaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoDiaSemana
        fields = [
			'id',
			'NumeroDiaSemana',
			'Ordem'
		]
        

class TipoHorarioFuncionamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoHorarioFuncionamento
        fields = [
			'id',
			'Nome',
			'Ordem',
			'CodigoIDezoitoN',
			'LanguageCode'
		]
        

class HorarioFuncionamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = HorarioFuncionamento
        fields = [
			'id',
			'Fechado',
			'TipoDiaSemana',
			'HoraInicio',
			'HoraFim',
			'TipoHorarioFuncionamento'
		]
        

class TipoUrlSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoUrl
        fields = [
			'id',
			'Nome',
			'Ordem',
			'CodigoIDezoitoN',
			'LanguageCode'
		]
        

class UrlSerializer(serializers.ModelSerializer):
    class Meta:
        model = Url
        fields = [
			'id',
			'Endereco',
			'TipoUrl',
			'Principal',
			'NaoExibirUrl'
		]
        

class TipoPDVSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoPDV
        fields = [
			'id',
			'Nome',
			'CodigoIDezoitoN',
			'LanguageCode'
		]
        

class PDVSerializer(serializers.ModelSerializer):
    class Meta:
        model = PDV
        fields = [
			'id',
			'Nome',
			'TipoPDV',
			'Url',
			'DNS',
			'MacAddress'
		]
        

class ItemTipoAreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemTipoArea
        fields = [
			'id',
			'Nome',
			'Ordem',
			'CodigoMenu',
			'CodigoIDezoitoN',
			'LanguageCode'
		]
        

class MicrositeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Microsite
        fields = [
			'id',
			'Endereco',
			'NaoExibirMicrosite'
		]
        

class UnidadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unidade
        fields = [
			'id',
			'Nome',
			'HomeBased',
			'Escritorio',
			'EscolaIdioma',
			'Endereco',
			'TipoPcDCateg',
			'Contato',
			'Microsite',
			'EnderecoIgualSede',
			'EmailIgualSede',
			'LimiteFinanceiro',
			'ContatoIgualSede',
			'MicrositeIgualSede',
			'PDV',
			'ItemTipoArea',
			'HorarioFuncionamento'
		]
        

class TipoPromocaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoPromocao
        fields = [
			'id',
			'Nome',
			'Ordem',
			'PercentualMensal',
			'CodigoIDezoitoN',
			'LanguageCode',
			'Unidade'
		]
        

class TipoProgressaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoProgressao
        fields = [
			'id',
			'Nome',
			'Ordem',
			'PercentualMensal',
			'CodigoIDezoitoN',
			'LanguageCode',
			'Unidade'
		]
        

class TipoCargoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoCargo
        fields = [
			'id',
			'Nome',
			'RemuneracaoMensal',
			'TipoProgressao',
			'TipoPromocao',
			'Unidade',
			'Ordem',
			'CodigoIDezoitoN',
			'LanguageCode'
		]
        

class TipoDocumentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoDocumento
        fields = [
			'id',
			'Ordem',
			'Nome',
			'CodigoIDezoitoN',
			'LanguageCode'
		]
        

class TipoSetorSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoSetor
        fields = [
			'id',
			'Nome',
			'Ordem',
			'CodigoIDezoitoN',
			'LanguageCode'
		]
        

class TipoFuncioTurnoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoFuncioTurno
        fields = [
			'id',
			'Nome',
			'IntervaloHorario',
			'Unidade',
			'Ordem',
			'CodigoIDezoitoN',
			'LanguageCode'
		]
        

class TipoRelacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoRelacao
        fields = [
			'id',
			'Nome',
			'Ordem',
			'CodigoIDezoitoN',
			'LanguageCode'
		]
        

class CargoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cargo
        fields = [
			'id',
			'QuantidadesFuncionamentoTurno',
			'GraficoGenero',
			'GraficoFaixaEtaria',
			'GraficoExperiencia',
			'TipoCargo',
			'TipoSetor',
			'TipoFuncioTurno',
			'TipoRelacao',
			'TipoDocumento'
		]
        

class TipoCargoTradSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoCargoTrad
        fields = [
			'id',
			'Nome',
			'Superior',
			'Atribuicao',
			'Competencia',
			'Ordem',
			'CodigoIDezoitoN',
			'Cargo',
			'LanguageCode'
		]
        

class TipoCtrlQualidadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoCtrlQualidade
        fields = [
			'id',
			'Nome',
			'Nota',
			'Ordem',
			'CodigoIDezoitoN',
			'LanguageCode'
		]
        

class TipoProficienciaLinguaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoProficienciaLingua
        fields = [
			'id',
			'Nome',
			'Escala',
			'TipoCtrlQualidade',
			'Ordem',
			'CodigoIDezoitoN',
			'LanguageCode'
		]
        

class TipoMoedaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoMoeda
        fields = [
			'id',
			'Nome',
			'Codigo',
			'EmUso',
			'Simbolo',
			'ISO',
			'Cotacao',
			'Tipo',
			'DataExclusaoPTAX',
			'Ordem',
			'CodigoIDezoitoN',
			'LanguageCode',
			'Pais'
		]
        

class TipoVolumeAcumuladoVendaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoVolumeAcumuladoVenda
        fields = [
			'id',
			'Nome',
			'Ordem',
			'Unidade',
			'CodigoIDezoitoN',
			'LanguageCode'
		]
        

class TipoDomUmGdArCoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoDomUmGdArCo
        fields = [
			'id',
			'CodAlfanumerico',
			'Nome',
			'Ordem',
			'CodigoIDezoitoN',
			'LanguageCode'
		]
        

class TipoDomUmSbArCoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoDomUmSbArCo
        fields = [
			'id',
			'CodAlfanumerico',
			'Nome',
			'Ordem',
			'CodigoIDezoitoN',
			'LanguageCode'
		]
        

class TipoDominioUmSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoDominioUm
        fields = [
			'id',
			'CodAlfanumerico',
			'Nome',
			'TipoDomUmGdArCo',
			'TipoDomUmSbArCo',
			'Ordem',
			'CodigoIDezoitoN',
			'LanguageCode'
		]
        

class TipoLinguaClasfSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoLinguaClasf
        fields = [
			'id',
			'Nome',
			'Ordem',
			'CodigoIDezoitoN',
			'LanguageCode'
		]
        

class LinguaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lingua
        fields = [
			'id',
			'Nome',
			'Visivel',
			'TipoLinguaClasf',
			'Ordem',
			'CodigoIDezoitoN',
			'LanguageCode'
		]
        

class TipoImpostoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoImposto
        fields = [
			'id',
			'Nome',
			'Visivel',
			'Pais',
			'Ordem',
			'CodigoIDezoitoN',
			'LanguageCode'
		]
        

class TipoNotaComunicacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoNotaComunicacao
        fields = [
			'id',
			'Nome',
			'Ordem',
			'CodigoIDezoitoN',
			'Nota',
			'LanguageCode'
		]
        

class TipoNotaQualidadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoNotaQualidade
        fields = [
			'id',
			'Nome',
			'Ordem',
			'CodigoIDezoitoN',
			'Nota',
			'LanguageCode'
		]
        

class TipoNotaGeralSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoNotaGeral
        fields = [
			'id',
			'Nome',
			'Nota',
			'Ordem',
			'CodigoIDezoitoN',
			'LanguageCode'
		]
        

class CtrlQualidadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CtrlQualidade
        fields = [
			'id',
			'Prazo',
			'AtendeExpectativa',
			'Indica',
			'Depoimento',
			'Data',
			'TipoNotaGeral',
			'TipoNotaComunicacao',
			'TipoNotaQualidade',
			'TipoCtrlQualidade'
		]
        

class TipoMargemLucroSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoMargemLucro
        fields = [
			'id',
			'Nome',
			'Ordem',
			'CodigoIDezoitoN',
			'LanguageCode'
		]
        

class MargemLucroSerializer(serializers.ModelSerializer):
    class Meta:
        model = MargemLucro
        fields = [
			'id',
			'Aliquota',
			'Unidade',
			'TipoMargemLucro'
		]
        

class TituloSerializer(serializers.ModelSerializer):
    class Meta:
        model = Titulo
        fields = [
			'id',
			'Nome',
			'Ordem',
			'Preposicao',
			'CodigoIDezoitoN',
			'LanguageCode'
		]
        

class SubTituloServicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubTituloServico
        fields = [
			'id',
			'Nome',
			'Ordem',
			'Preposicao',
			'CodigoIDezoitoN',
			'LanguageCode'
		]
        

class SubTipoDocumentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubTipoDocumento
        fields = [
			'id',
			'Nome',
			'Ordem',
			'Preposicao',
			'CodigoIDezoitoN',
			'LanguageCode'
		]
        

class ItemCategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemCategoria
        fields = [
			'id',
			'Nome',
			'Ordem',
			'CodigoIDezoitoN',
			'ItemTipoArea',
			'BancoImagem',
			'LanguageCode'
		]
        

class TipoDomDoisSecSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoDomDoisSec
        fields = [
			'id',
			'CodAlfanumerico',
			'Nome',
			'Ordem',
			'CodigoIDezoitoN',
			'LanguageCode'
		]
        

class TipoDomDoisDivSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoDomDoisDiv
        fields = [
			'id',
			'CodAlfanumerico',
			'Nome',
			'Ordem',
			'CodigoIDezoitoN',
			'LanguageCode'
		]
        

class TipoDomDoisGrupSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoDomDoisGrup
        fields = [
			'id',
			'CodAlfanumerico',
			'Nome',
			'Ordem',
			'CodigoIDezoitoN',
			'LanguageCode'
		]
        

class TipoDomDoisClasSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoDomDoisClas
        fields = [
			'id',
			'CodAlfanumerico',
			'Nome',
			'Ordem',
			'CodigoIDezoitoN',
			'LanguageCode'
		]
        

class TipoDominioDoisSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoDominioDois
        fields = [
			'id',
			'CodAlfanumerico',
			'Nome',
			'TipoDomDoisSec',
			'TipoDomDoisDiv',
			'TipoDomDoisGrup',
			'TipoDomDoisClas',
			'Ordem',
			'CodigoIDezoitoN',
			'LanguageCode'
		]
        

class FuncaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Funcao
        fields = [
			'id',
			'QuantidadesFuncionamentoTurno',
			'PercentGratificMensalAdicional',
			'GraficoGenero',
			'GraficoFaixaEtaria',
			'GraficoExperiencia',
			'TipoCargo',
			'TipoSetor',
			'TipoFuncioTurno'
		]
        

class TipoExtCategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoExtCategoria
        fields = [
			'id',
			'Nome',
			'Ordem',
			'CodigoIDezoitoN',
			'LanguageCode'
		]
        

class TipoExtensaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoExtensao
        fields = [
			'id',
			'Nome',
			'TipoExtCategoria',
			'Ordem',
			'CodigoIDezoitoN',
			'LanguageCode'
		]
        

class CodigoValidacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CodigoValidacao
        fields = [
			'id',
			'Codigo',
			'TipoDocumento'
		]
        

class ImpostoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Imposto
        fields = [
			'id',
			'Nome',
			'Aliquota',
			'TipoImposto',
			'Cidade',
			'Estado',
			'Pais',
			'Lingua'
		]
        

class PadraoDocumentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PadraoDocumento
        fields = [
			'id',
			'Nome',
			'TipoDocumento',
			'Titulo',
			'SubTituloServico',
			'TipoCargoTrad',
			'SubTipoDocumento',
			'CodigoIDezoitoN',
			'LanguageCode'
		]
        

class BancoArquivoSerializer(serializers.ModelSerializer):
    class Meta:
        model = BancoArquivo
        fields = [
			'id',
			'Nome',
			'CodigoAgrupamento',
			'TipoExtensao',
			'DataCriacao',
			'Arquivo',
			'CodigoValidacao',
			'ProibirImpressao',
			'ProibirDownload'
		]
        

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = [
			'id',
			'Consignavel',
			'NaoExibirUrl',
			'Indisponivel',
			'TipoDominioUm',
			'TipoDominioDois',
			'MargemLucro',
			'ParLinguaExigido',
			'ExisteItemModelo',
			'ItemCategoria',
			'PadraoDocumento',
			'Imposto',
			'Funcao',
			'CtrlQualidade',
			'BancoImagem',
			'BancoArquivo'
		]
        

class CapacidadeDiariaSerializer(serializers.ModelSerializer):
    class Meta:
        model = CapacidadeDiaria
        fields = [
			'id',
			'Descricao',
			'Quantidade',
			'CodigoIDezoitoN',
			'LanguageCode',
			'Item'
		]
        

class TipoMedidaServSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoMedidaServ
        fields = [
			'id',
			'Nome',
			'Ordem',
			'CodigoIDezoitoN',
			'LanguageCode'
		]
        

class TipoMedidaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoMedida
        fields = [
			'id',
			'Nome',
			'Ordem',
			'CodigoIDezoitoN',
			'LanguageCode',
			'TipoMedidaServ'
		]
        

class TipoCompLinguaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoCompLingua
        fields = [
			'id',
			'Nome',
			'Ordem',
			'CodigoIDezoitoN',
			'LanguageCode'
		]
        

class TipoAnoInicioAtuacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoAnoInicioAtuacao
        fields = [
			'id',
			'Nome',
			'Ordem',
			'CodigoIDezoitoN',
			'LanguageCode'
		]
        

class ValorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Valor
        fields = [
			'id',
			'ValorIdeal',
			'MedidaValorIdeal',
			'NaoVisivelValorIdeal',
			'ValorMinimo',
			'MedidaValorMinimo',
			'NaoVisivelValorMinimo',
			'ValorUrgencia',
			'MedidaValorUrgencia',
			'NaoVisivelValorUrgencia',
			'AceitoNegociarValorMenor',
			'AplicarTodosParesidiomas',
			'AceitoTrabalhosSemLucro',
			'TipoProficienciaLingua',
			'NaoVisivelValorOutorga',
			'DisponivelAtendimentoPcD',
			'TipoCargoTrad',
			'TipoMedida',
			'TipoMoeda',
			'TipoAnoInicioAtuacao',
			'CapacidadeDiaria',
			'TipoVolumeAcumuladoVenda',
			'TipoCompLingua',
			'CodigoIDezoitoN',
			'LanguageCode'
		]
        

class TipoFuncaoTradSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoFuncaoTrad
        fields = [
			'id',
			'Nome',
			'Superior',
			'Atribuicao',
			'Competencia',
			'Funcao',
			'Ordem',
			'CodigoIDezoitoN',
			'LanguageCode'
		]
        

class PosicaoClausulaDocumentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PosicaoClausulaDocumento
        fields = [
			'id',
			'Nome',
			'Ordem',
			'CodigoIDezoitoN',
			'LanguageCode'
		]
        

class TipoClausulaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoClausula
        fields = [
			'id',
			'Nome',
			'Ordem',
			'CodigoIDezoitoN',
			'LanguageCode'
		]
        

class ClausulaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clausula
        fields = [
			'id',
			'NomeClausula',
			'ConteudoClausula',
			'ComentarioClausula',
			'DataCadastro',
			'OcultarNomeClausula',
			'CodigoIDezoitoN',
			'Minuta',
			'PosicaoClausulaDocumento',
			'TipoClausula',
			'LanguageCode',
			'Titulo',
			'TipoFuncaoTrad',
			'TipoDocumento',
			'TipoCargoTrad',
			'SubTituloServico',
			'SubTipoDocumento'
		]
        

class TipoIdentificacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoIdentificacao
        fields = [
			'id',
			'Nome',
			'Sigla',
			'Comentario',
			'Visivel',
			'AceitoComoIdentidade',
			'UserName',
			'Ordem',
			'CodigoIDezoitoN',
			'Unidade',
			'Pais',
			'LanguageCode'
		]
        

class IdentificacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Identificacao
        fields = [
			'id',
			'Numero',
			'TipoIdentificacao',
			'TipoOrgaoEmiss',
			'ValidadeData',
			'Estado',
			'Pais',
			'EmissaoPrimeiraData',
			'EmissaoAtualData',
			'DataCadastro',
			'BancoImagem'
		]
        

class TipoSituacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoSituacao
        fields = [
			'id',
			'Nome',
			'Ordem',
			'CodigoIDezoitoN',
			'LanguageCode'
		]
        

class TipoCargoProjetoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoCargoProjeto
        fields = [
			'id',
			'Nome',
			'Ordem',
			'CodigoIDezoitoN',
			'LanguageCode'
		]
        

class TipoVinculoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoVinculo
        fields = [
			'id',
			'Nome',
			'Ordem',
			'CodigoIDezoitoN',
			'LanguageCode'
		]
        

class TipoCtrlPrazoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoCtrlPrazo
        fields = [
			'id',
			'Nome',
			'Ordem',
			'Recorrencia',
			'Quantidade',
			'CodigoIDezoitoN',
			'LanguageCode',
			'Unidade'
		]
        

class CtrlPrazoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CtrlPrazo
        fields = [
			'id',
			'TempoInicio',
			'TempoFim',
			'TipoCtrlPrazo'
		]
        

class ProjetoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projeto
        fields = [
			'id',
			'Titulo',
			'DescricaoProjeto',
			'CtrlQualidade',
			'Url',
			'ValorProjeto',
			'TipoSituacao',
			'DataInicio',
			'DataFim',
			'CargaHoraria',
			'TipoCargoProjeto',
			'TipoVinculo',
			'VinculoEmpregaticio',
			'Freelance',
			'EquipeProjeto',
			'CodigoIDezoitoN',
			'LanguageCode',
			'CtrlPrazo'
		]
        

class OutorgaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Outorga
        fields = [
			'id',
			'CodigoIDezoitoN',
			'Item',
			'LanguageCode'
		]
        

class TipoEmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoEmail
        fields = [
			'id',
			'Nome',
			'Ordem',
			'CodigoIDezoitoN',
			'LanguageCode'
		]
        

class EmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Email
        fields = [
			'id',
			'Endereco',
			'TipoEmail',
			'NaoResponda',
			'Principal',
			'NaoExibirEmail'
		]
        

class TipoDataDiaCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoDataDiaCard
        fields = [
			'id',
			'DiaCard',
			'DiaExtMasc',
			'Ordem',
			'CodigoIDezoitoN',
			'LanguageCode'
		]
        

class TipoDataAnoCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoDataAnoCard
        fields = [
			'id',
			'AnoCard',
			'AnoExtMasc',
			'Ordem',
			'CodigoIDezoitoN',
			'LanguageCode'
		]
        

class TipoRedeSocialSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoRedeSocial
        fields = [
			'id',
			'Nome',
			'Visivel',
			'Unidade',
			'Ordem',
			'CodigoIDezoitoN',
			'LanguageCode'
		]
        

class RedeSocialSerializer(serializers.ModelSerializer):
    class Meta:
        model = RedeSocial
        fields = [
			'id',
			'Endereco',
			'TipoRedeSocial',
			'Principal',
			'NaoExibirRedeSocial'
		]
        

class TipoPronomeTratamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoPronomeTratamento
        fields = [
			'id',
			'Nome',
			'Unidade',
			'Ordem',
			'CodigoIDezoitoN',
			'LanguageCode'
		]
        

class ReferenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Referencia
        fields = [
			'id',
			'TipoPronomeTratamento',
			'Nome',
			'Empresa',
			'Email',
			'Contato',
			'TipoDiaSemana',
			'Hora'
		]
        

class TipoAreaGeoAtuSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoAreaGeoAtu
        fields = [
			'id',
			'Nome',
			'Unidade',
			'Ordem',
			'Estado',
			'Pais',
			'CodigoEndPostal'
		]


class TipoFiliacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoFiliacao
        fields = [
			'id',
			'Nome',
			'Ordem',
			'CodigoIDezoitoN',
			'LanguageCode'
		]
        

class OrdemPagamentoBrasilSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrdemPagamentoBrasil
        fields = [
			'id',
			'NomeSacador',
			'Identificacao',
			'User',
			'TipoFiliacao',
			'NomeFiliacao'
		]
        

class QRCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = QRCode
        fields = [
			'id',
			'Codigo',
			'BancoImagem'
		]
        

class TipoMetodoPgtoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoMetodoPgto
        fields = [
			'id',
			'Nome',
			'Visivel',
			'Pais',
			'Ordem',
			'CodigoIDezoitoN',
			'LanguageCode'
		]
        

class TipoBancoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoBanco
        fields = [
			'id',
			'Nome',
			'CodigoCompensacao',
			'Url',
			'Ordem',
			'Pais'
		]
        

class TipoContaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoConta
        fields = [
			'id',
			'Nome',
			'Ordem',
			'CodigoIDezoitoN',
			'LanguageCode'
		]
        

class DadoBancarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = DadoBancario
        fields = [
			'id',
			'Agencia',
			'TipoBanco',
			'TipoConta',
			'Conta',
			'DV'
		]
        

class TipoFaturacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoFaturacao
        fields = [
			'id',
			'Nome',
			'Ordem',
			'CodigoIDezoitoN',
			'LanguageCode',
			'TipoImposto'
		]
        

class TipoCriptomoedaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoCriptomoeda
        fields = [
			'id',
			'Nome',
			'Codigo',
			'ValorMercado',
			'PrecoReal',
			'VolumeVinteQuatroHoras',
			'VariacaoVinteQuatroHoras',
			'Unidade',
			'Ordem'
		]
        

class CriptomoedaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Criptomoeda
        fields = [
			'id',
			'Nome',
			'TipoCriptomoeda',
			'NumeroCarteira',
			'Url',
			'Carteira'
		]
        

class TipoPrimeiroDiaSemanaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoPrimeiroDiaSemana
        fields = [
			'id',
			'Descricao',
			'TipoDiaSemana',
			'Ordem',
			'CodigoIDezoitoN',
			'LanguageCode'
		]
        

class TipoDispHoraSemanaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoDispHoraSemana
        fields = [
			'id',
			'Nome',
			'Unidade',
			'Ordem',
			'CodigoIDezoitoN',
			'LanguageCode'
		]
        

class TipoFacilidadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoFacilidade
        fields = [
			'id',
			'Nome',
			'BancoImagem',
			'Unidade',
			'Ordem',
			'CodigoIDezoitoN',
			'LanguageCode'
		]
        

class TipoSegmentoInteresseSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoSegmentoInteresse
        fields = [
			'id',
			'Nome',
			'Unidade',
			'Ordem',
			'CodigoIDezoitoN',
			'LanguageCode'
		]
        

class TipoDataMesCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoDataMesCard
        fields = [
			'id',
			'MesCard',
			'Mes',
			'Ordem',
			'CodigoIDezoitoN',
			'LanguageCode'
		]
        

class TipoTurnoTrabSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoTurnoTrab
        fields = [
			'id',
			'Nome',
			'Unidade',
			'Ordem',
			'CodigoIDezoitoN',
			'LanguageCode'
		]
        

class DispTurnoPreferidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = DispTurnoPreferido
        fields = [
			'id',
			'TipoTurnoTrab',
			'TipoDiaSemana'
		]
        

class TipoAmenidadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoAmenidade
        fields = [
			'id',
			'Nome',
			'BancoImagem',
			'Unidade',
			'Ordem',
			'CodigoIDezoitoN',
			'LanguageCode'
		]
        

class TipoPagamentoOnlineSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoPagamentoOnline
        fields = [
			'id',
			'Nome',
			'Unidade',
			'Ordem',
			'CodigoIDezoitoN',
			'LanguageCode'
		]
        

class PagamentoOnlineSerializer(serializers.ModelSerializer):
    class Meta:
        model = PagamentoOnline
        fields = [
			'id',
			'Conta',
			'TipoPagamentoOnline'
		]
        

class TipoMarcadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoMarcador
        fields = [
			'id',
			'Nome',
			'Ordem',
			'CodigoIDezoitoN',
			'LanguageCode'
		]
        

class DispDiaPreferidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = DispDiaPreferido
        fields = [
			'id',
			'TipoDiaSemana'
		]
        

class TipoPerfilContaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoPerfilConta
        fields = [
			'id',
			'Nome',
			'Ordem',
			'CodigoIDezoitoN',
			'LanguageCode'
		]
        

class TipoEmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoEmpresa
        fields = [
			'id',
			'Nome',
			'Unidade',
			'Ordem',
			'CodigoIDezoitoN',
			'LanguageCode'
		]
        

class TipoBandeiraCartaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoBandeiraCartao
        fields = [
			'id',
			'Nome',
			'Ordem',
			'CodigoIDezoitoN',
			'LanguageCode'
		]
        

class CartaoCreditoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartaoCredito
        fields = [
			'id',
			'Numero',
			'Nome',
			'Validade',
			'Seguranca',
			'TipoBandeiraCartao'
		]
        

class PersonificacaoDominioSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonificacaoDominio
        fields = [
			'id',
			'Nome',
			'Dns',
			'Ip'
		]
        

class TipoSocioSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoSocio
        fields = [
			'id',
			'Nome',
			'Ordem',
			'CodigoIDezoitoN',
			'LanguageCode'
		]
        

class QuadroSocioSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuadroSocio
        fields = [
			'id',
			'Percentual',
			'TipoSocio'
		]
        

class TipoFerramentaIntegracaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoFerramentaIntegracao
        fields = [
			'id',
			'Nome',
			'Ordem',
			'CodigoIDezoitoN',
			'LanguageCode'
		]
        

class IntegracaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Integracao
        fields = [
			'id',
			'Codigo',
			'TipoFerramentaIntegracao'
		]
        

class TransfSWIFTSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransfSWIFT
        fields = [
			'id',
			'Codigo',
			'NumeroConta',
			'NomeTitulaConta',
			'NomeBanco'
		]
        

class TransfItaliaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransfItalia
        fields = [
			'id',
			'ABI',
			'CAB',
			'NumeroContaItalia',
			'IBAN',
			'BIC',
			'NomeTitular'
		]
        

class TransfUniaoEuropeiaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransfUniaoEuropeia
        fields = [
			'id',
			'VatId',
			'CodigoFiscal'
		]
        

class EsquemaCorSerializer(serializers.ModelSerializer):
    class Meta:
        model = EsquemaCor
        fields = [
			'id',
			'Nome',
			'CorFonteCabecalhoTopo',
			'CorFundoCabecalhoTopo',
			'CorFonteCabecalho',
			'CorFundoCabecalho',
			'CorCabecalhoMenu',
			'CorFonteCabecalhoMenu',
			'CorFundoCabelhacoMenu',
			'CorFontePrincipal',
			'CorFundoPrincipal',
			'CorFonteRodape',
			'CorFundoRodape',
			'CorFonteRodapeMenu',
			'CorFundoRodapeMenu',
			'CorFonteRodapeBase',
			'CorFundoRodapeBase'
		]
        

class SaldoMensagemSerializer(serializers.ModelSerializer):
    class Meta:
        model = SaldoMensagem
        fields = [
			'id',
			'SaldoAtual',
			'SaldoAposEnvio'
		]
        

class RanqueamentoGeralSerializer(serializers.ModelSerializer):
    class Meta:
        model = RanqueamentoGeral
        fields = [
			'id',
			'TipoServicoLinguisticoPrestado',
			'MediaRecebQualidServPrestado',
			'MediaRecebPrazoServPrestado',
			'IdiomaOrigemDestinoLingaMatern',
			'NumeroParticipacaoProjeto',
			'DominioUmProxAreaConhecimento',
			'DominioDoisProxSetorEconomico',
			'FormAcadem',
			'CapacidadeDiariaTrabalho',
			'CertificacoeConquistada',
			'PrecoCadastradoCargo',
			'ProximidadeLocalServico',
			'Peso',
			'Nota',
			'Media',
			'MediaGeral'
		]
        

class NotificacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notificacao
        fields = [
			'id',
			'AceiteNotificacaoEmpresa',
			'AceiteNotificacaoExterna',
			'AceiteNotificacaoCaridade',
			'AceiteNotificCompartilhamento',
			'AceiteNotificacaoNoticias'
		]
        

class ComissaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comissao
        fields = [
			'id',
			'Nome',
			'Percentual'
		]
        

class TipoRegimTributSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoRegimTribut
        fields = [
			'id',
			'Nome',
			'Ordem',
			'LanguageCode'
		]
        

class TipoEmpresaTamanhoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoEmpresaTamanho
        fields = [
			'id',
			'Nome',
			'Ordem',
			'CodigoIDezoitoN',
			'LanguageCode'
		]
        

class TipoContribSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoContrib
        fields = [
			'id',
			'Nome',
			'Ordem',
			'CodigoIDezoitoN',
			'LanguageCode'
		]
        

class EmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empresa
        fields = [
			'id',
			'NomeEmpresarial',
			'NomeFantasia',
			'Sigla',
			'Cnae',
			'IsentoIE',
			'VIP',
			'SetorComercial',
			'TipoEmpresa',
			'TipoRegimTribut',
			'TipoEmpresaTamanho',
			'TipoContrib',
			'TipoDataDiaCard',
			'TipoDataMesCard',
			'TipoDataAnoCard',
			'PreferenciaFiscalInformada',
			'NomeSiteSimoes',
			'ConveniadaSimoes',
			'Associacao',
			'ResponsavelFinanceiro',
			'LimiteFinanceiro',
			'Pais',
			'RanqueamentoGeral',
			'PercentualPreenchimento',
			'NaoExibirMoeda',
			'QRCode',
			'IndisponivelAte',
			'TipoPrimeiroDiaSemana',
			'TipoDispHoraSemana',
			'EsquemaCor',
			'TipoPerfilConta',
			'Valor',
			'Url',
			'Unidade',
			'TransfUniaoEuropeia',
			'TransfSWIFT',
			'TransfItalia',
			'TipoSegmentoInteresse',
			'TipoMoeda',
			'TipoMetodoPgto',
			'TipoMarcador',
			'TipoFaturacao',
			'TipoFacilidade',
			'TipoDominioUm',
			'TipoDominioDois',
			'TipoAreaGeoAtu',
			'TipoAmenidade',
			'SaldoMensagem',
			'Referencia',
			'RedeSocial',
			'QuadroSocio',
			'Projeto',
			'PersonificacaoDominio',
			'PagamentoOnline',
			'Outorga',
			'OrdemPagamentoBrasil',
			'Notificacao',
			'Microsite',
			'MargemLucro',
			'Integracao',
			'Imposto',
			'Identificacao',
			'HorarioFuncionamento',
			'Endereco',
			'Email',
			'DispTurnoPreferido',
			'DispDiaPreferido',
			'DadoBancario',
			'CtrlQualidade',
			'Criptomoeda',
			'Contato',
			'Comissao',
			'CodigoEndPostal',
			'Clausula',
			'CartaoCredito',
			'BancoImagem',
			'BancoArquivo'
		]
        

class SalaAulaSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalaAula
        fields = [
			'id',
			'Nome',
			'Virtual',
			'Contato',
			'Url',
			'DisponivelArCordicionado',
			'DisponivelQuadroBranco',
			'DisponivelComputador',
			'DisponivelInternet',
			'DisponivelDataShow',
			'DisponivelTelaProjecao',
			'AssentoDisponivelAluno',
			'AssentoDisponivelColaborador',
			'DisponivelTV',
			'DisponivelCaixaSom',
			'Unidade',
			'HorarioFuncionamento'
		]
        

class TipoNivelAlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoNivelAluno
        fields = [
			'id',
			'Nome',
			'Ordem',
			'CodigoIDezoitoN',
			'LanguageCode'
		]
        

class TurmaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Turma
        fields = [
			'id',
			'Nome',
			'Unidade',
			'HorarioFuncionamento',
			'SalaAula',
			'Item',
			'TipoNivelAluno'
		]
        

class TipoExtDigEditSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoExtDigEdit
        fields = [
			'id',
			'Nome',
			'Partida',
			'Chegada',
			'TipoExtensao',
			'Ordem',
			'CodigoIDezoitoN',
			'LanguageCode'
		]
        

class TipoPerifericoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoPeriferico
        fields = [
			'id',
			'Nome',
			'Unidade',
			'Ordem',
			'CodigoIDezoitoN',
			'LanguageCode'
		]
        

class TipoSistemaOperacionalSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoSistemaOperacional
        fields = [
			'id',
			'Nome',
			'Visivel',
			'Unidade',
			'Ordem',
			'CodigoIDezoitoN',
			'LanguageCode'
		]
        

class TipoSoftwareTraducaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoSoftwareTraducao
        fields = [
			'id',
			'Nome',
			'Unidade',
			'Ordem',
			'CodigoIDezoitoN',
			'LanguageCode'
		]
        

class TipoSoftwareLocalizSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoSoftwareLocaliz
        fields = [
			'id',
			'Nome',
			'Unidade',
			'Ordem',
			'CodigoIDezoitoN',
			'LanguageCode'
		]
        

class TipoSoftwareDTPSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoSoftwareDTP
        fields = [
			'id',
			'Nome',
			'Unidade',
			'Ordem',
			'CodigoIDezoitoN',
			'LanguageCode'
		]
        

class TipoSoftwarePacEscSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoSoftwarePacEsc
        fields = [
			'id',
			'Nome',
			'Unidade',
			'Ordem',
			'CodigoIDezoitoN',
			'LanguageCode'
		]
        

class TipoSoftwareModTresDSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoSoftwareModTresD
        fields = [
			'id',
			'Nome',
			'Unidade',
			'Ordem',
			'CodigoIDezoitoN',
			'LanguageCode'
		]
        

class TipoSoftwareTranscSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoSoftwareTransc
        fields = [
			'id',
			'Nome',
			'Unidade',
			'Ordem',
			'CodigoIDezoitoN',
			'LanguageCode'
		]
        

class TipoSoftwareLeitorSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoSoftwareLeitor
        fields = [
			'id',
			'Nome',
			'Unidade',
			'Ordem',
			'CodigoIDezoitoN',
			'LanguageCode'
		]
        

class TipoEngineGameSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoEngineGame
        fields = [
			'id',
			'Nome',
			'Unidade',
			'Ordem',
			'CodigoIDezoitoN',
			'LanguageCode'
		]
        

class ProtocoloAtendimentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProtocoloAtendimento
        fields = [
			'id',
			'Codigo',
			'Data',
			'Unidade'
		]
        

class TipoHardwareComputadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoHardwareComputador
        fields = [
			'id',
			'Nome',
			'Ordem',
			'CodigoIDezoitoN',
			'LanguageCode'
		]
        

class TipoBancoDadosSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoBancoDados
        fields = [
			'id',
			'Nome',
			'Visivel',
			'Unidade',
			'Ordem',
			'CodigoIDezoitoN',
			'LanguageCode'
		]
        

class TipoExtDiagramacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoExtDiagramacao
        fields = [
			'id',
			'Nome',
			'TipoExtensao',
			'Partida',
			'Chegada',
			'Ordem',
			'CodigoIDezoitoN',
			'LanguageCode'
		]
        

class TipoExtAudioSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoExtAudio
        fields = [
			'id',
			'Nome',
			'TipoExtensao',
			'Partida',
			'Chegada',
			'Ordem',
			'CodigoIDezoitoN',
			'LanguageCode'
		]
        

class TipoExtLocalizacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoExtLocalizacao
        fields = [
			'id',
			'Nome',
			'TipoExtensao',
			'Partida',
			'Chegada',
			'Ordem',
			'CodigoIDezoitoN',
			'LanguageCode'
		]
        

class TipoExtVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoExtVideo
        fields = [
			'id',
			'Nome',
			'TipoExtensao',
			'Partida',
			'Chegada',
			'Ordem',
			'CodigoIDezoitoN',
			'LanguageCode'
		]
        

class TipoIntervaloTempoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoIntervaloTempo
        fields = [
			'id',
			'HoraInicio',
			'HoraFim',
			'Ordem',
			'CodigoIDezoitoN',
			'Unidade'
		]
        

class TipoParteSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoParte
        fields = [
			'id',
			'Nome',
			'Ordem',
			'CodigoIDezoitoN',
			'Pais',
			'LanguageCode'
		]
        

class TipoInstCertificSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoInstCertific
        fields = [
			'id',
			'Abreviatura',
			'Nome',
			'Url',
			'TipoCtrlQualidade',
			'Visivel',
			'Pais',
			'Ordem',
			'CodigoIDezoitoN',
			'LanguageCode'
		]
        

class ExameProficienciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExameProficiencia
        fields = [
			'id',
			'Ponto',
			'Validade',
			'CopiaComprovante',
			'CodigoIDezoitoN',
			'TipoInstCertific',
			'LanguageCode'
		]
        

class TipoExtDigNaoEditSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoExtDigNaoEdit
        fields = [
			'id',
			'Nome',
			'TipoExtensao',
			'Partida',
			'Chegada',
			'Ordem',
			'CodigoIDezeoitoN',
			'LanguageCode'
		]
        

class TipoReligiaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoReligiao
        fields = [
			'id',
			'Nome',
			'CodigoIDezoitoN',
			'Ordem',
			'LanguageCode'
		]
        

class TipoHobbieSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoHobbie
        fields = [
			'id',
			'Nome',
			'BancoImagem',
			'Ordem',
			'CodigoIDezoitoN',
			'LanguageCode'
		]
        

class TipoAcessoInternetSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoAcessoInternet
        fields = [
			'id',
			'Nome',
			'Ordem',
			'CodigoIDezoitoN',
			'LanguageCode'
		]
        

class TipoExpLocalizaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoExpLocaliza
        fields = [
			'id',
			'Nome',
			'Ordem',
			'CodigoIDezoitoN',
			'LanguageCode'
		]
        

class ParteTraducaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParteTraducao
        fields = [
			'id',
			'Ordem',
			'ImportanciaTrabalhoEquipe',
			'Proatividade',
			'Organizacao',
			'Concentracao',
			'FocoProdutividade',
			'AlcanceObjetivo',
			'AtencaoDetalhes',
			'ProcessosMapeados',
			'ComunicacaoTrabalhoEquipe',
			'AdaptacaoCulturaEmpresa',
			'CapacidadeAprendizado',
			'Flexibilidade',
			'BagagemCultural',
			'Resumo',
			'CodigoIDezoitoN',
			'LanguageCode'
		]
        

class TipoFonteSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoFonte
        fields = [
			'id',
			'Nome',
			'Ordem',
			'CodigoIDezoitoN'
		]
        

class AssinaturaDigitalSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssinaturaDigital
        fields = [
			'id',
			'Assinatura',
			'AssinaturaUm',
			'AssinaturaUmPrincipal',
			'AssinaturaDois',
			'AssinaturaDoisPrincipal',
			'AssinaturaTres',
			'RubricaUm',
			'RubricaUmPrincipal',
			'RubricaDois',
			'SelfieIdentificacao',
			'TipoFonte'
		]
        

class DispHoraSemanaSerializer(serializers.ModelSerializer):
    class Meta:
        model = DispHoraSemana
        fields = [
			'id',
			'TipoDispHoraSemana'
		]
        

class BancoCurriculoSerializer(serializers.ModelSerializer):
    class Meta:
        model = BancoCurriculo
        fields = [
			'id',
			'Arquivo',
			'ProibirImpressao',
			'ProibirDownload',
			'CodigoIDezoitoN',
			'LanguageCode'
		]
        

class TipoRelacionamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoRelacionamento
        fields = [
			'id',
			'Nome',
			'Ordem',
			'CodigoIDezoitoN',
			'LanguageCode'
		]
        

class RelacionamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Relacionamento
        fields = [
			'id',
			'Parte',
			'TipoRelacionamento'
		]
        

class TipoUnidComprimentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoUnidComprimento
        fields = [
			'id',
			'Nome',
			'Abreviatura',
			'Ordem',
			'CodigoIDezoitoN',
			'LanguageCode'
		]
        

class TipoUnidMassaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoUnidMassa
        fields = [
			'id',
			'Nome',
			'Abreviatura',
			'Ordem',
			'CodigoIDezoitoN',
			'LanguageCode'
		]
        

class ParteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parte
        fields = [
			'id',
			'Iniciais',
			'SetorComercial',
			'User',
			'TipoParte',
			'TipoPronomeTratamento',
			'Cargo',
			'Funcao',
			'TipoRelacao',
			'VIP',
			'RegistroConselho',
			'Estrangeiro',
			'PreferenciaFiscalInformada',
			'BancoCurriculo',
			'AceitaCartao',
			'LimiteFinanceiro',
			'AssinaturaDigital',
			'ResponsavelFinanceiro',
			'RanqueamentoGeral',
			'Observacao',
			'PercentualPreenchimento',
			'NaoExibirMoeda',
			'QRCode',
			'IndisponivelAte',
			'TipoPrimeiroDiaSemana',
			'DispHoraSemana',
			'EsquemaCor',
			'DataAceiteCandidato',
			'DataAceiteColaborador',
			'DataNascimento',
			'OcultarAnoDataNascimento',
			'ParteAtualmDisp',
			'TipoPerfilConta',
			'UnidadeMassa',
			'UnidadeComprimento',
			'IMC',
			'TipoUnidMassa',
			'ParteTraducao',
			'TipoUnidComprimento',
			'Valor',
			'Url',
			'Turma',
			'TransfUniaoEuropeia',
			'TransfSWIFT',
			'TransfItalia',
			'TipoSoftwareTransc',
			'TipoSoftwareTraducao',
			'TipoSoftwarePacEsc',
			'TipoSoftwareModTresD',
			'TipoSoftwareLocaliz',
			'TipoSoftwareLeitor',
			'TipoSoftwareDTP',
			'TipoSistemaOperacional',
			'TipoSegmentoInteresse',
			'TipoReligiao',
			'TipoPeriferico',
			'TipoMoeda',
			'TipoMetodoPgto',
			'TipoMarcador',
			'TipoIntervaloTempo',
			'TipoHobbie',
			'TipoHardwareComputador',
			'TipoFaturacao',
			'TipoExtVideo',
			'TipoExtLocalizacao',
			'TipoExtDigNaoEdit',
			'TipoExtDigEdit',
			'TipoExtDiagramacao',
			'TipoExtAudio',
			'TipoExpLocaliza',
			'TipoEngineGame',
			'TipoDominioUm',
			'TipoDominioDois',
			'TipoBancoDados',
			'TipoAreaGeoAtu',
			'TipoAcessoInternet',
			'SaldoMensagem',
			'Relacionamento',
			'Referencia',
			'RedeSocial',
			'QuadroSocio',
			'ProtocoloAtendimento',
			'Projeto',
			'PersonificacaoDominio',
			'Pais',
			'PagamentoOnline',
			'PDV',
			'Outorga',
			'OrdemPagamentoBrasil',
			'Notificacao',
			'Microsite',
			'MargemLucro',
			'Integracao',
			'Imposto',
			'Identificacao',
			'ExameProficiencia',
			'Endereco',
			'Empresa',
			'Email',
			'DispTurnoPreferido',
			'DispDiaPreferido',
			'DadoBancario',
			'CtrlQualidade',
			'Criptomoeda',
			'Contato',
			'Comissao',
			'CodigoEndPostal',
			'Clausula',
			'Cidade',
			'CartaoCredito',
			'BancoImagem',
			'TipoSexo',
			'BancoArquivo'
		]
        

class SecaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Secao
        fields = [
			'id',
			'Data',
			'Ip',
			'Cidade',
			'Estado',
			'Pais',
			'TipoSistemaOperacional',
			'ProtocoloAtendimento',
			'CtrlQualidade',
			'Item'
		]
        

class TipoDescontoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoDesconto
        fields = [
			'id',
			'Nome',
			'Unidade',
			'Ordem',
			'CodigoIDezoitoN',
			'LanguageCode'
		]
        

class DescontoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Desconto
        fields = [
			'id',
			'QuantidadeMaxima',
			'Unidade',
			'Item',
			'TipoDesconto'
		]
        

class TipoComoConheceuSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoComoConheceu
        fields = [
			'id',
			'Nome',
			'Ordem',
			'CodigoIDezoitoN',
			'LanguageCode'
		]
        

class OrdemExeServicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrdemExeServico
        fields = [
			'id',
			'Codigo',
			'TipoDataMesCard',
			'TipoDataAnoCard',
			'DataCriacao'
		]
        

class ConvenioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Convenio
        fields = [
			'id',
			'ConvenioAtivo',
			'DataInicio',
			'DataFim',
			'Empresa'
		]
        

class TipoRelDiagSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoRelDiag
        fields = [
			'id',
			'Nome',
			'Ordem',
			'CodigoIDezoitoN',
			'LanguageCode'
		]
        

class TipoModoEntregaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoModoEntrega
        fields = [
			'id',
			'Nome',
			'Ordem',
			'CodigoIDezoitoN',
			'LanguageCode'
		]
        

class RelDiagSerializer(serializers.ModelSerializer):
    class Meta:
        model = RelDiag
        fields = [
			'id',
			'Codigo',
			'Secao',
			'TipoRelDiag',
			'ValidadeProposta',
			'TipoModoEntrega',
			'Desconto',
			'TipoComoConheceu',
			'DataCriacao',
			'Convenio',
			'CodigoValidacao',
			'Unidade',
			'PDV',
			'CtrlQualidade',
			'ContratoCDC',
			'CodigoIDezoitoN',
			'LanguageCode',
			'TipoDominioUm',
			'TipoDominioDois',
			'Parte',
			'OrdemExeServico',
			'Empresa'
		]
        

class ItemModeloSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemModelo
        fields = [
			'id',
			'Codigo',
			'CFOP',
			'SKU',
			'Item',
			'ItemTipoArea'
		]
        

class ItemModeloTraducaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemModeloTraducao
        fields = [
			'id',
			'Nome',
			'ItemModelo',
			'Explicacao',
			'CodigoBarra',
			'Url',
			'BancoArquivo',
			'CodigoIDezoitoN',
			'LanguageCode',
			'QRCode'
		]
        

class ItemTraducaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemTraducao
        fields = [
			'id',
			'Nome',
			'Explicacao',
			'Mensagem',
			'Observacao',
			'InfoAdicional',
			'CondicaoPagamento',
			'ListaBrinde',
			'Convenio',
			'ProgramaCurso',
			'AulaParticular',
			'InCompany',
			'CodigoIDezoitoN',
			'Item',
			'LanguageCode'
		]
        

class TipoSuporteContSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoSuporteCont
        fields = [
			'id',
			'Nome',
			'Ordem',
			'CodigoIDezoitoN',
			'LanguageCode'
		]
        

class TipoConteudoCategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoConteudoCategoria
        fields = [
			'id',
			'Nome',
			'Ordem',
			'CodigoIDezoitoN',
			'Descricao',
			'LanguageCode'
		]
        

class TipoConteudoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoConteudo
        fields = [
			'id',
			'Nome',
			'Ordem',
			'CodigoIDezoitoN',
			'TipoConteudoCategoria',
			'LanguageCode'
		]
        

class TipoSuporteContIOSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoSuporteContIO
        fields = [
			'id',
			'PartidaChegada',
			'Ordem',
			'TipoSuporteCont',
			'CodigoIDezoitoN'
		]
        

class TipoExtDigEdtIOSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoExtDigEdtIO
        fields = [
			'id',
			'PartidaChegada',
			'Ordem',
			'CodigoIDezoitoN',
			'TipoExtDigEdit'
		]
        

class RelDiagServAdSerializer(serializers.ModelSerializer):
    class Meta:
        model = RelDiagServAd
        fields = [
			'id',
			'DataEntrega',
			'RelDiag',
			'HoraEntrega',
			'UrgenciaServico',
			'DireitosAutorais',
			'TipoSuporteCont',
			'Secao',
			'Cargo',
			'Item',
			'ItemTraducao',
			'ItemModeloTraducao',
			'Quantidade',
			'Preco',
			'TipoSuporteContIO',
			'TipoExtDigEdtIO',
			'TipoConteudo',
			'BancoArquivo'
		]
        

class TipoFusoHorarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoFusoHorario
        fields = [
			'id',
			'TZdatabaseName',
			'UTCOff',
			'UTCDSToff',
			'LatitudeLongitudeDDMMDDDMM',
			'PartePaisCoberto',
			'Status',
			'Ordem',
			'Visivel',
			'Cidade',
			'Pais',
			'Continente',
			'CodigoIDezoitoN',
			'LanguageCode'
		]
        

class TipoAgendaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoAgenda
        fields = [
			'id',
			'Nome',
			'Ordem',
			'CodigoIDezoitoN',
			'LanguageCode'
		]
        

class AgendaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agenda
        fields = [
			'id',
			'Nome',
			'Descricao',
			'TipoAgenda',
			'VisivelUrl',
			'TipoFusoHorario'
		]
        

class AgendaDisponivelSerializer(serializers.ModelSerializer):
    class Meta:
        model = AgendaDisponivel
        fields = [
			'id',
			'Dia',
			'TipoIntervaloTempo',
			'Unidade'
		]
        

class TipoStatusMensagemSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoStatusMensagem
        fields = [
			'id',
			'Nome',
			'Ordem',
			'CodigoIDezoitoN',
			'LanguageCode',
			'Unidade'
		]
        

class TipoMensagemSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoMensagem
        fields = [
			'id',
			'Nome',
			'Ordem',
			'CodigoIDezoitoN',
			'LanguageCode'
		]
        

class MensagemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mensagem
        fields = [
			'id',
			'Nome',
			'Codigo',
			'Email',
			'TipoRedeSocial',
			'RedeSocial',
			'TipoContato',
			'Contato',
			'Cidade',
			'Estado',
			'Pais',
			'TipoDominioDois',
			'TipoComoConheceu',
			'Assunto',
			'Corpo',
			'HoraInicio',
			'HoraFim',
			'Agenda',
			'AgendaDisponivel',
			'Unidade',
			'CodigoIDezoitoN',
			'TipoMensagem',
			'TipoStatusMensagem',
			'Ip',
			'LanguageCode',
			'PersonificacaoDominio',
			'TipoSetor',
			'BancoArquivo'
		]
        

class TipoFormComplSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoFormCompl
        fields = [
			'id',
			'Nome',
			'TipoCtrlQualidade',
			'Unidade',
			'Ordem',
			'CodigoIDezoitoN',
			'LanguageCode'
		]
        

class TipoCertificacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoCertificacao
        fields = [
			'id',
			'Abreviatura',
			'Nome',
			'EscalaVisivel',
			'TipoFormCompl',
			'Url',
			'TipoCtrlQualidade',
			'Visivel',
			'Pais',
			'Ordem',
			'CodigoIDezoitoN',
			'LanguageCode'
		]
        

class TipoDataMesOrdnSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoDataMesOrdn
        fields = [
			'id',
			'Mes',
			'TipoDataMesCard',
			'Ordem',
			'CodigoIDezoitoN',
			'LanguageCode'
		]
        

class TipoPeriodoAnoAtualSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoPeriodoAnoAtual
        fields = [
			'id',
			'Nome',
			'Ordem',
			'CodigoIDezoitoN',
			'LanguageCode'
		]
        

class TipoStatusFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoStatusForm
        fields = [
			'id',
			'Nome',
			'Ordem',
			'CodigoIDezoitoN',
			'LanguageCode'
		]
        

class TipoDuracaoCursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoDuracaoCurso
        fields = [
			'id',
			'Nome',
			'Ordem',
			'CodigoIDezoitoN',
			'LanguageCode'
		]
        

class TipoUnidTempoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoUnidTempo
        fields = [
			'id',
			'Nome',
			'Abreviatura',
			'Quantidade',
			'Decada',
			'Ano',
			'Mes',
			'Dia',
			'Minuto',
			'MilesimoSegundo',
			'Ordem',
			'CodigoIDezoitoN',
			'LanguageCode'
		]
        

class FormComplSerializer(serializers.ModelSerializer):
    class Meta:
        model = FormCompl
        fields = [
			'id',
			'Abreviatura',
			'Nome',
			'FormacaoDesc',
			'Url',
			'Parte',
			'TipoFormCompl',
			'TipoInstCertific',
			'TipoCertificacao',
			'TipoProficienciaLingua',
			'TipoStatusForm',
			'TipoPeriodoAnoAtual',
			'TipoDuracaoCurso',
			'TipoDataDiaCard',
			'TipoDataMesOrdn',
			'TipoDataAnoCard',
			'Duracao',
			'TipoUnidTempo',
			'BancoArquivo',
			'ComprovanteVerificado',
			'TipoCtrlQualidade',
			'Visivel',
			'Lingua',
			'Pais',
			'LanguageCode'
		]
        

class TipoFormAcademSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoFormAcadem
        fields = [
			'id',
			'Nome',
			'TipoCtrlQualidade',
			'Ordem',
			'CodigoIDezoitoN',
			'LanguageCode'
		]
        

class FormAcademSerializer(serializers.ModelSerializer):
    class Meta:
        model = FormAcadem
        fields = [
			'id',
			'Abreviatura',
			'Nome',
			'FormacaoDesc',
			'Url',
			'Parte',
			'TipoFormAcadem',
			'TipoInstCertific',
			'TipoCertificacao',
			'TipoStatusForm',
			'TipoPeriodoAnoAtual',
			'TipoDuracaoCurso',
			'TipoDataDiaCard',
			'TipoDataMesOrdn',
			'TipoDataAnoCard',
			'Duracao',
			'TipoUnidTempo',
			'BancoArquivo',
			'ComprovanteVerificado',
			'TipoCtrlQualidade',
			'Visivel',
			'Lingua',
			'Pais',
			'LanguageCode'
		]
        

class TipoDiaSemTradSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoDiaSemTrad
        fields = [
			'id',
			'Nome',
			'NomeAbreviado',
			'TipoDiaSemana',
			'Ordem',
			'CodigoIDezoitoN',
			'LanguageCode'
		]
        

class TipoDataDiaOrdnSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoDataDiaOrdn
        fields = [
			'id',
			'DiaExtMasc',
			'DiaOrdinal',
			'TipoDataDiaCard',
			'Ordem',
			'CodigoIDezoitoN',
			'LanguageCode'
		]
        

class TipoDataComDetlSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoDataComDetl
        fields = [
			'id',
			'Nome',
			'Ordem',
			'CodigoIDezoitoN',
			'LanguageCode'
		]
        

class TipoDataComAssuSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoDataComAssu
        fields = [
			'id',
			'Nome',
			'Ordem',
			'CodigoDezoitoN',
			'LanguageCode'
		]
        

class TipoDataComSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoDataCom
        fields = [
			'id',
			'Nome',
			'TipoDataDiaCard',
			'TipoDataMesOrdn',
			'TipoDataComDetl',
			'TipoDataComAssu',
			'EnviarTodos',
			'AssuntoEMail',
			'MsgEMail',
			'MsgEmailAt',
			'MsgSMS',
			'MsgSMSAt',
			'MsgRedeSocLon',
			'MsgRedeSocLonAt',
			'MsgRedeSocCur',
			'MsgRedeSocCurAt',
			'Visivel',
			'AnoInicio',
			'AnoTermino',
			'Fixo',
			'Municipal',
			'Estadual',
			'Nacional',
			'Continental',
			'Continente',
			'Internacional',
			'PontoFacultativo',
			'LembrarDiasAntecedencia',
			'Movel',
			'TipoDataDiaOrdn',
			'QuantDias',
			'TipoDiaSemTrad',
			'BancoImagem',
			'Unidade',
			'Ordem',
			'CodigoIDezoitoN',
			'LanguageCode',
			'TipoReligiao',
			'TipoDominioUm',
			'TipoDominioDois',
			'Pais',
			'Estado',
			'Cidade'
		]
        

class TipoEstagioPropostaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoEstagioProposta
        fields = [
			'id',
			'Nome',
			'Ordem',
			'Codigo',
			'CodigoIDezoitoN',
			'LanguageCode'
		]
        

class PropTecComercialSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropTecComercial
        fields = [
			'id',
			'Codigo',
			'Secao',
			'TipoEstagioProposta',
			'DataEnvio',
			'UltimaAlteracao',
			'UltimaConsulta',
			'TipoRedeSocial',
			'TipoContato',
			'AgendaDisponivel',
			'Sintal',
			'ValidacaoCliente',
			'SolicitaRepresentanteComercial',
			'AgendaRepresentanteComercial',
			'Parte',
			'Empresa'
		]
        

class TipoPeriodicidadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoPeriodicidade
        fields = [
			'id',
			'Nome',
			'Ordem',
			'CodigoIDezoitoN',
			'LanguageCode'
		]
        

class LembreteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lembrete
        fields = [
			'id',
			'Mensagem',
			'TipoPeriodicidade',
			'CodigoIDezoitoN',
			'LanguageCode'
		]
        

class AgendaAtividadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AgendaAtividade
        fields = [
			'id',
			'DiaInicio',
			'HoraInicio',
			'DiaFim',
			'HoraFim',
			'Ordem',
			'PropTecComercial',
			'Mensagem',
			'Email',
			'DiaInteiro',
			'Contato',
			'Endereco',
			'RedeSocial',
			'Agenda',
			'Url',
			'Microsite',
			'Repeticao',
			'TipoDataCom',
			'HorarioFuncionamento',
			'Lembrete',
			'CodigoIDezoitoN',
			'LanguageCode',
			'Unidade',
			'Parte',
			'Empresa'
		]
        

class ComboSerializer(serializers.ModelSerializer):
    class Meta:
        model = Combo
        fields = [
			'id',
			'Nome',
			'PrecoVenda',
			'QuantidadeVenda',
			'PrecoAluguel',
			'QuantidadeAluguel',
			'DataCadastro',
			'DataVencimento'
		]
        

class ItemUnidadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemUnidade
        fields = [
			'id',
			'PrecoVenda',
			'QuantidadeVenda',
			'PrecoAluguel',
			'QuantidadeAluguel',
			'QuantidadeEmprestimo',
			'DataCadastro',
			'DataVencimento',
			'ItemModelo',
			'Unidade',
			'Combo'
		]
        

class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = [
			'id',
			'DisponivelAluguel',
			'DisponivelVenda',
			'DisponivelEmprestimo',
			'NumeroSerie',
			'NumeroPatrimonio',
			'DataVencimento',
			'ItemUnidade'
		]
        

class TipoLinguaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoLingua
        fields = [
			'id',
			'Nome',
			'Ordem',
			'CodigoIDezoitoN',
			'LanguageCode'
		]
        

class RelDiagLinguaPaisSerializer(serializers.ModelSerializer):
    class Meta:
        model = RelDiagLinguaPais
        fields = [
			'id',
			'CodigoIDezoitoN',
			'RelDiag',
			'TipoLingua',
			'LanguageCode'
		]
        

class TipoDispAmbientSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoDispAmbient
        fields = [
			'id',
			'Nome',
			'Ordem',
			'CodigoIDezoitoN',
			'BancoImagem',
			'LanguageCode'
		]
        

class TipoAutodeclaracaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoAutodeclaracao
        fields = [
			'id',
			'Nome',
			'Ordem',
			'CodigoIDezoitoN',
			'LanguageCode'
		]
        

class EventoInterpCargoSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventoInterpCargo
        fields = [
			'id',
			'CodigoIDezoitoN',
			'TipoCargo',
			'LanguageCode',
			'ProfissionaisCertificados'
		]
        

class RepeticaoInterpretacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = RepeticaoInterpretacao
        fields = [
			'id',
			'Nome',
			'CodigoIDezoitoN',
			'LanguageCode'
		]
        

class RepeticaoEventoSerializer(serializers.ModelSerializer):
    class Meta:
        model = RepeticaoEvento
        fields = [
			'id',
			'Nome',
			'CodigoIDezoitoN',
			'LanguageCode'
		]
        

class NumeroRecepAuricularesSerializer(serializers.ModelSerializer):
    class Meta:
        model = NumeroRecepAuriculares
        fields = [
			'id',
			'Numero'
		]
        

class EventoDetalheSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventoDetalhe
        fields = [
			'id',
			'BlocoPavilhao',
			'Predio',
			'Andar',
			'Sala',
			'LocalApresentaRisco',
			'TipoDispAmbient',
			'RepeticaoEvento',
			'NumeroUsuariosFinais',
			'NecessitaCabine',
			'NumeroRecepAuriculares',
			'RepeticaoInterpretacao',
			'DataInicio',
			'HoraInicio',
			'Duracao',
			'QuantidadeInterpretes',
			'ProfissionalCertificado',
			'TipoAutodeclaracao',
			'NumeroRecepcionistaEvento',
			'NecessitaGravacaoAudio',
			'NecessitaTranscricaoAudio',
			'NecessitaLegendagemAudio',
			'InterpreteCoordenadorLingua',
			'NecessitaTransmissao',
			'RecepcionistaLingua',
			'TecnicoOperadorLingua',
			'SrvTraducaoTranscricaoLingua',
			'SrvTraducaoLegendagemLingua',
			'NecessitaSrvComplementares',
			'NecessitaLocacaoEquipamentos',
			'Item',
			'ItemTraducao',
			'ItemModeloTraducao',
			'ItemModelo',
			'Produto',
			'TipoDominioDois',
			'RelDiagLinguaPais',
			'EventoInterpCargo',
			'BancoArquivo'
		]
        

class ResponsavelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Responsavel
        fields = [
			'id',
			'Parte',
			'Empresa'
		]
        

class TipoLocalPresencialSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoLocalPresencial
        fields = [
			'id',
			'Nome',
			'Ordem',
			'CodigoIDezoitoN',
			'LanguageCode',
			'Unidade'
		]
        

class TipoPreferenciaAulaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoPreferenciaAula
        fields = [
			'id',
			'Nome',
			'Ordem',
			'CodigoIDezoitoN',
			'LanguageCode',
			'Unidade'
		]
        

class TipoFaixaEtariaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoFaixaEtaria
        fields = [
			'id',
			'Nome',
			'Ordem',
			'CodigoIDezoitoN',
			'LanguageCode'
		]
        

class TipoRegimeEnsinoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoRegimeEnsino
        fields = [
			'id',
			'Nome',
			'Ordem',
			'CodigoIDezoitoN',
			'LanguageCode'
		]
        

class TipoModalidadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoModalidade
        fields = [
			'id',
			'Nome',
			'Ordem',
			'CodigoIDezoitoN',
			'LanguageCode'
		]
        

class TipoRepeticaoCursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoRepeticaoCurso
        fields = [
			'id',
			'Nome',
			'Ordem',
			'CodigoIDezoitoN',
			'LanguageCode'
		]
        

class RelDiagCursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = RelDiagCurso
        fields = [
			'id',
			'NumeroParticipante',
			'RelDiag',
			'TipoFaixaEtaria',
			'TipoNivelAluno',
			'TipoRegimeEnsino',
			'Unidade',
			'TipoModalidade',
			'TipoContato',
			'Empresa',
			'TipoPreferenciaAula',
			'DataInicioCurso',
			'HoraInicioCurso',
			'DataFimCurso',
			'DuracaoAula',
			'TipoRepeticaoCurso',
			'ProfessoresCertificados',
			'Responsavel',
			'Item',
			'ItemTraducao',
			'ItemModeloTraducao',
			'Preco',
			'TipoLocalPresencial',
			'UrgenciaServico',
			'ConfirmaTransporteEscolar',
			'ConfirmaTransporteAplicativo'
		]
        

class TipoResidenciaContratoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoResidenciaContrato
        fields = [
			'id',
			'Nome',
			'Unidade',
			'Ordem',
			'CodigoIDezoitoN',
			'LanguageCode'
		]
        

class TipoHabilitacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoHabilitacao
        fields = [
			'id',
			'Nome',
			'Pais',
			'Visivel',
			'Ordem',
			'CodigoIDezoitoN',
			'LanguageCode'
		]
        

class TipoPcDAparelhoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoPcDAparelho
        fields = [
			'id',
			'Nome',
			'Ordem',
			'CodigoIDezoitoN',
			'LanguageCode'
		]
        

class TipoEstadoCivilSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoEstadoCivil
        fields = [
			'id',
			'Nome',
			'Ordem',
			'CodigoIDezoitoN',
			'LanguageCode'
		]
        

class TipoResidenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoResidencia
        fields = [
			'id',
			'Nome',
			'Ordem',
			'CodigoIDezoitoN',
			'LanguageCode'
		]
        

class TipoTrabalhoVoluntarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoTrabalhoVoluntario
        fields = [
			'id',
			'Nome',
			'Ordem',
			'CodigoIDezoitoN',
			'LanguageCode'
		]
        

class TipoMoradorSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoMorador
        fields = [
			'id',
			'Nome',
			'Ordem',
			'CodigoIDezoitoN',
			'LanguageCode'
		]
        

class TipoRendaFamiliarSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoRendaFamiliar
        fields = [
			'id',
			'Nome',
			'Ordem',
			'CodigoIDezoitoN',
			'LanguageCode'
		]
        

class TipoFilhoQuantSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoFilhoQuant
        fields = [
			'id',
			'Nome',
			'Ordem',
			'CodigoIDezoitoN',
			'LanguageCode'
		]
        

class DadosPessoaisSerializer(serializers.ModelSerializer):
    class Meta:
        model = DadosPessoais
        fields = [
			'id',
			'NomeSocialArtistico',
			'BancoImagem',
			'Pais',
			'Estado',
			'TipoAutodeclaracao',
			'TipoPcDAparelho',
			'TipoPcDCateg',
			'TipoEstadoCivil',
			'TipoResidencia',
			'TipoResidenciaContrato',
			'TipoMorador',
			'TipoRendaFamiliar',
			'TipoFilhoQuant',
			'TipoTrabalhoVoluntario',
			'TipoHabilitacao',
			'Fumante',
			'OAB'
		]
        

class TipoImovelSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoImovel
        fields = [
			'id',
			'Nome',
			'Ordem',
			'CodigoIDezoitoN',
			'LanguageCode',
			'Unidade'
		]
        

class TipoFuncionarioQuantSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoFuncionarioQuant
        fields = [
			'id',
			'Nome',
			'Ordem',
			'CodigoIDezoitoN',
			'LanguageCode',
			'Unidade'
		]
        

class TipoLicFranquiaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoLicFranquia
        fields = [
			'id',
			'Nome',
			'Ordem',
			'CodigoIDezoitoN',
			'LanguageCode'
		]
        

class TipoInvestimentoInicialSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoInvestimentoInicial
        fields = [
			'id',
			'Nome',
			'Ordem',
			'CodigoIDezoitoN',
			'LanguageCode'
		]
        

class TipoCapitalGiroSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoCapitalGiro
        fields = [
			'id',
			'Nome',
			'Ordem',
			'CodigoIDezoitoN',
			'LanguageCode'
		]
        

class TipoAreaMinimaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoAreaMinima
        fields = [
			'id',
			'Nome',
			'Ordem',
			'CodigoIDezoitoN',
			'LanguageCode'
		]
        

class TipoCompartGeoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoCompartGeo
        fields = [
			'id',
			'Nome',
			'Ordem',
			'CodigoIDezoitoN',
			'LanguageCode'
		]
        

class RelDiagLicFranquiaSerializer(serializers.ModelSerializer):
    class Meta:
        model = RelDiagLicFranquia
        fields = [
			'id',
			'Preco',
			'RelDiag',
			'Parte',
			'TipoLicFranquia',
			'TipoInvestimentoInicial',
			'TipoCapitalGiro',
			'TipoAreaMinima',
			'TipoImovel',
			'TipoCompartGeo',
			'FigurarSiteSimoes',
			'TipoFuncionarioQuant',
			'Item',
			'ItemTraducao',
			'ItemModeloTraducao'
		]
        

class RelDiagTradSerializer(serializers.ModelSerializer):
    class Meta:
        model = RelDiagTrad
        fields = [
			'id',
			'NumeroPalavras',
			'Conteudo',
			'Url',
			'DataEntrega',
			'HoraEntrega',
			'TipoFusoHorario',
			'UrgenciaServico',
			'ProfissionalRegistrado',
			'DireitosAutorais',
			'RelDiag',
			'Secao',
			'Item',
			'ItemTraducao',
			'ItemModeloTraducao',
			'Preco',
			'TipoSuporteContIO',
			'TipoExtDigEdtIO',
			'TipoConteudo',
			'BancoArquivo'
		]
        

class EventoEnderecoSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventoEndereco
        fields = [
			'id',
			'Nome',
			'Endereco',
			'CodigoEndPostal',
			'TipoLogradouro',
			'Logradouro',
			'Numero',
			'Complemento',
			'Bairro',
			'Regiao',
			'Cidade',
			'Estado',
			'Pais',
			'PontoReferencia',
			'Latitude',
			'Longitute',
			'EventoDetalhe'
		]
        

class TipoEventoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoEvento
        fields = [
			'id',
			'Nome',
			'Unidade',
			'Ordem',
			'CodigoIDezoitoN',
			'LanguageCode'
		]
        

class EventoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evento
        fields = [
			'id',
			'Nome',
			'TemaEvento',
			'ProprietarioEvento',
			'OrganizadorEvento',
			'TipoFusoHorario',
			'TipoEvento',
			'DataInicioEvento',
			'HoraInicioEvento',
			'DataFimEvento',
			'HoraFimEvento',
			'PublicoEstimado',
			'TipoSuporteCont',
			'TipoExtDigEdit',
			'EventoEndereco'
		]
        

class TipoPretensaoBolsaEstagioSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoPretensaoBolsaEstagio
        fields = [
			'id',
			'Nome',
			'Visivel',
			'Pais',
			'Ordem',
			'CodigoIDezoitoN',
			'LanguageCode'
		]
        

class TipoProgrIcentEducacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoProgrIcentEducacao
        fields = [
			'id',
			'Nome',
			'Pais',
			'Ordem',
			'CodigoIDezoitoN',
			'LanguageCode'
		]
        

class TipoDisponibilEstagiarSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoDisponibilEstagiar
        fields = [
			'id',
			'Horario',
			'Unidade',
			'Ordem',
			'CodigoIDezoitoN',
			'LanguageCode'
		]
        

class TipoTurnoEduSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoTurnoEdu
        fields = [
			'id',
			'Nome',
			'Ordem',
			'CodigoIDezoitoN',
			'LanguageCode'
		]
        

class ItemBolsaEstagioSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemBolsaEstagio
        fields = [
			'id',
			'Matricula',
			'Parte',
			'TipoPretensaoBolsaEstagio',
			'Valor',
			'NotaEnem',
			'TipoProgrIcentEducacao',
			'CoeficienteRendimento',
			'NomeCurso',
			'TipoTurnoEdu',
			'TipoDisponibilEstagiar',
			'Item',
			'FoiJovemAprendiz',
			'AtuandoOutraEmpresa',
			'DisponibilidadeViagem',
			'DisponibilidadeTrabalhoExterno',
			'DisponibilidadeInicioImediato',
			'CodigoIDezoitoN',
			'LanguageCode'
		]
        

class LivroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Livro
        fields = [
			'id',
			'MarcII',
			'NumeroControleLCCN',
			'ISBN',
			'Produto'
		]
        

class RelDiagLivrariaSerializer(serializers.ModelSerializer):
    class Meta:
        model = RelDiagLivraria
        fields = [
			'id',
			'RelDiag',
			'Produto',
			'Livro',
			'Item',
			'ItemTraducao',
			'ItemModeloTraducao',
			'ItemTipoArea',
			'ItemModelo'
		]
        

class CabecalhoTopoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CabecalhoTopo
        fields = [
			'id',
			'Nome',
			'Conteudo',
			'CodigoIDezoitoN',
			'LanguageCode'
		]
        

class RodapeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rodape
        fields = [
			'id',
			'Nome',
			'Conteudo',
			'CodigoIDezoitoN',
			'LanguageCode'
		]
        

class RodapeMenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = RodapeMenu
        fields = [
			'id',
			'Nome'
		]
        

class RodapeBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = RodapeBase
        fields = [
			'id',
			'Nome',
			'Conteudo',
			'CodigoIDezoitoN',
			'LanguageCode'
		]
        

class CabecalhoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cabecalho
        fields = [
			'id',
			'Nome',
			'Conteudo',
			'CodigoIDezoitoN',
			'LanguageCode'
		]
        

class CabecalhoMenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = CabecalhoMenu
        fields = [
			'id',
			'Nome'
		]
        

class PrincipalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Principal
        fields = [
			'id',
			'Nome',
			'Conteudo',
			'Senha',
			'CodigoIDezoitoN',
			'LanguageCode'
		]
        

class SiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Site
        fields = [
			'id',
			'CabecalhoTopo',
			'Cabecalho',
			'CabecalhoMenu',
			'Principal',
			'Rodape',
			'RodapeMenu',
			'RodapeBase',
			'Unidade'
		]
        

class TipoPainelAtendimentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoPainelAtendimento
        fields = [
			'id',
			'Nome',
			'Ordem',
			'CodigoIDezoitoN',
			'LanguageCode',
			'Unidade'
		]
        

class TipoPosicaoAtendimentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoPosicaoAtendimento
        fields = [
			'id',
			'Nome',
			'Ordem',
			'CodigoIDezoitoN',
			'LanguageCode',
			'Unidade'
		]
        

class TipoOrientacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoOrientacao
        fields = [
			'id',
			'Nome',
			'Ordem',
			'CodigoIDezoitoN',
			'LanguageCode'
		]
        

class PainelAtendimentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PainelAtendimento
        fields = [
			'id',
			'Codigo',
			'ProtocoloAtendimento',
			'Data',
			'PDV',
			'TipoPainelAtendimento',
			'Unidade',
			'Identificacao',
			'TipoPosicaoAtendimento',
			'Mensagem',
			'TipoOrientacao',
			'BancoImagem'
		]
        

class TipoClienteAtendeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoClienteAtende
        fields = [
			'id',
			'Nome',
			'Unidade',
			'Ordem',
			'CodigoIDezoitoN',
			'LanguageCode'
		]
        

class FormatoHoraSerializer(serializers.ModelSerializer):
    class Meta:
        model = FormatoHora
        fields = [
			'id',
			'Ordem',
			'Nome',
			'CodigoIDezoitoN',
			'LanguageCode'
		]
        

class TipoSituacOcupSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoSituacOcup
        fields = [
			'id',
			'Nome',
			'Ordem',
			'CodigoIDezoitoN',
			'LanguageCode'
		]
        

class TipoFormatoDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoFormatoData
        fields = [
			'id',
			'Formato',
			'Ordem',
			'CodigoIDezoitoN',
			'LanguageCode'
		]
        

class PreferenciaAdicionalSerializer(serializers.ModelSerializer):
    class Meta:
        model = PreferenciaAdicional
        fields = [
			'id',
			'ExibirGMT',
			'UrgenciaServico',
			'Parte',
			'TipoSituacOcup',
			'TipoFusoHorario',
			'NaoExibirFusoHorario',
			'TipoFormatoData',
			'NaoExibirFormatoData',
			'FormatoHora',
			'NaoExibirFormatoHora',
			'TipoClienteAtende',
			'Pais',
			'TipoComoConheceu'
		]
        

class SoftwareSerializer(serializers.ModelSerializer):
    class Meta:
        model = Software
        fields = [
			'id',
			'Parte',
			'TipoSoftwareTraducao',
			'TipoSoftwareLocaliz',
			'TipoSoftwareDTP',
			'TipoSoftwarePacEsc',
			'TipoSoftwareModTresD',
			'TipoSoftwareTransc',
			'TipoSoftwareLeitor'
		]
        

class InstituicaoEnsinoSerializer(serializers.ModelSerializer):
    class Meta:
        model = InstituicaoEnsino
        fields = [
			'id',
			'Nome',
			'Parte',
			'Empresa',
			'Ordem',
			'Endereco',
			'Contato',
			'Email',
			'Url',
			'RedeSocial'
		]
        

class TipoServTerceiroSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoServTerceiro
        fields = [
			'id',
			'Nome',
			'Ordem',
			'CodigoIDezoitoN',
			'LanguageCode'
		]
        

class RelDiagServTerceiroSerializer(serializers.ModelSerializer):
    class Meta:
        model = RelDiagServTerceiro
        fields = [
			'id',
			'Quantidade',
			'Preco',
			'Evento',
			'DataRetirada',
			'HoraRetirada',
			'DataDevolucao',
			'HoraDevolucao',
			'RelDiag',
			'Cargo',
			'TipoServTerceiro',
			'Item',
			'ItemTraducao',
			'ItemModeloTraducao'
		]
        

class ParteLinguaPaisSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParteLinguaPais
        fields = [
			'id',
			'LinguaMaterna',
			'LinguaMaternaVerificada',
			'Parte',
			'Lingua',
			'Pais',
			'TipoProficienciaLingua',
			'Ordem',
			'TipoCargoTrad',
			'FormCompl'
		]
        

class TipoNotaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoNota
        fields = [
			'id',
			'Nome',
			'Ordem',
			'CodigoIDezoitoN',
			'LanguageCode'
		]
        

class NotaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nota
        fields = [
			'id',
			'Numero',
			'Serie',
			'ChaveAcesso',
			'TributoAproxMunicipal',
			'TributoAproxEstadual',
			'TributoAproxFederal',
			'SimplesConferencia',
			'RelDiag',
			'Unidade',
			'Parte',
			'TipoNota',
			'QRCode'
		]
        

class ListaCampanhaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ListaCampanha
        fields = [
			'id',
			'Nome',
			'Parte',
			'Descricao',
			'DataCriacao',
			'QuantContato',
			'CtrlQualidade',
			'LanguageCode'
		]
        

class EmpresaLinguaPaisSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmpresaLinguaPais
        fields = [
			'id',
			'Nativo',
			'Empresa',
			'Lingua',
			'Pais',
			'FormCompl'
		]
        

class TipoAcaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoAcao
        fields = [
			'id',
			'Nome',
			'Ordem',
			'CodigoIDezoitoN',
			'LanguageCode',
			'HoraInicio',
			'HoraFim',
			'Unidade'
		]
        

class AgendaPermissaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = AgendaPermissao
        fields = [
			'id',
			'Agenda',
			'TipoAcao',
			'Unidade',
			'Parte',
			'Empresa'
		]
        

class TipoClassListaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoClassLista
        fields = [
			'id',
			'Nome',
			'Ordem',
			'CodigoIDezoitoN',
			'LanguageCode'
		]
        

class TipoStatusListaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoStatusLista
        fields = [
			'id',
			'Nome',
			'Ordem',
			'CodigoIDezoitoN',
			'LanguageCode'
		]
        

class ListaContatoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ListaContato
        fields = [
			'id',
			'Nome',
			'DataNascimento',
			'Contato',
			'Ativo',
			'Numero',
			'Texto',
			'Cidade',
			'Bairro',
			'TipoContato',
			'TipoStatusLista',
			'TipoClassLista',
			'DataAtualizacao',
			'DataCriacao',
			'ListaCampanha'
		]
        

class ListaEmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ListaEmail
        fields = [
			'id',
			'Nome',
			'Email',
			'Ativo',
			'DataNascimento',
			'Numero',
			'Texto',
			'Cidade',
			'Bairro',
			'TipoStatusLista',
			'TipoClassLista',
			'DataAtualizacao',
			'DataCriacao',
			'TipoEmail',
			'ListaCampanha'
		]
        

class FilmeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Filme
        fields = [
			'id',
			'ClassificacaoEtaria',
			'Duracao',
			'ProporcaoTela',
			'Produto',
			'Pais',
			'Url',
			'BancoImagem'
		]
        

class RelDiagLicPlanoSerializer(serializers.ModelSerializer):
    class Meta:
        model = RelDiagLicPlano
        fields = [
			'id',
			'Preco',
			'RelDiag',
			'Parte',
			'Item',
			'ItemTraducao',
			'ItemModeloTraducao'
		]
        

class ItemLocacaoBalcaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemLocacaoBalcao
        fields = [
			'id',
			'Quantidade',
			'Item',
			'ItemTraducao',
			'ItemModeloTraducao',
			'ItemModelo',
			'Produto'
		]
        

class TipoAcaoCampanhaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoAcaoCampanha
        fields = [
			'id',
			'Nome',
			'CodigoIDezoitoN',
			'Ordem',
			'LanguageCode'
		]
        

class TipoStatusCampanhaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoStatusCampanha
        fields = [
			'id',
			'Nome',
			'CodigoIDezoitoN',
			'Ordem',
			'LanguageCode'
		]
        

class TipoCategoriaModeloCampanhaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoCategoriaModeloCampanha
        fields = [
			'id',
			'Nome',
			'CodigoIDezeoitoN',
			'Ordem',
			'LanguageCode'
		]
        

class TipoModeloCampanhaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoModeloCampanha
        fields = [
			'id',
			'Nome',
			'Ordem',
			'CorpoTextoSimples',
			'CorpoHTML',
			'CodigoIDezoitoN',
			'TipoCategoriaModeloCampanha',
			'DataCriacao',
			'DataAtualizacao',
			'Url',
			'LanguageCode'
		]
        

class ModeloCampanhaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModeloCampanha
        fields = [
			'id',
			'Nome',
			'TipoModeloCampanha',
			'ValidarAntiSpam',
			'DataCriacao',
			'DataAtualizacao'
		]
        

class CampanhaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Campanha
        fields = [
			'id',
			'NomeCampanha',
			'AssuntoEmail',
			'NomeRemetente',
			'EmailEnvio',
			'ContatoEnvio',
			'DataCriacao',
			'QuantidadeMensagem',
			'QuantContato',
			'TipoStatusCampanha',
			'ModeloCampanha',
			'TipoAcaoCampanha',
			'Mensagem',
			'ListaCampanha'
		]
        

class TipoPerfilLocutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoPerfilLocutor
        fields = [
			'id',
			'FichaTecnica',
			'RadioAtuacao',
			'Equipamentos',
			'CapacidadeProducao',
			'CaracteristicasVocais',
			'Ordem',
			'CodigoIDezoitoN',
			'LanguageCode'
		]
        

class ItemTipoPerfilLocutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemTipoPerfilLocutor
        fields = [
			'id',
			'Parte',
			'Item',
			'TipoPerfilLocutor',
			'Valor'
		]
        

class TipoCategoriaServicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoCategoriaServico
        fields = [
			'id',
			'Nome',
			'Unidade',
			'Ordem',
			'CodigoIDezoitoN',
			'LanguageCode'
		]
        

class ItemCategoriaServicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemCategoriaServico
        fields = [
			'id',
			'Parte',
			'Item',
			'TipoCategoriaServico',
			'Valor'
		]
        

class TipoTamanhoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoTamanho
        fields = [
			'id',
			'Nome',
			'Ordem',
			'CodigoIDezoitoN',
			'LanguageCode'
		]
        

class ModeloDocumentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModeloDocumento
        fields = [
			'id',
			'CodigoFonte',
			'TipoOrientacao',
			'TipoTamanho',
			'PapelTimbrado',
			'BancoArquivo',
			'BancoImagem'
		]
        

class TipoLicConvenioSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoLicConvenio
        fields = [
			'id',
			'Nome',
			'Ordem',
			'CodigoIDezoitoN',
			'LanguageCode'
		]
        

class RelDiagLicConvenioSerializer(serializers.ModelSerializer):
    class Meta:
        model = RelDiagLicConvenio
        fields = [
			'id',
			'Preco',
			'Aliquota',
			'DataInicio',
			'DataFim',
			'RelDiag',
			'Parte',
			'TipoLicConvenio',
			'ConvenioAtivo',
			'Secao'
		]
        

class MedidaNotaItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedidaNotaItem
        fields = [
			'id',
			'Nome',
			'Ordem',
			'CodigoIDezoitoN',
			'LanguageCode'
		]
        

class NotaItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = NotaItem
        fields = [
			'id',
			'Quantidade',
			'Preco',
			'Nota',
			'ItemModeloTraducao',
			'MedidaNotaItem',
			'Imposto'
		]
        

class PrestadorPreferencialSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrestadorPreferencial
        fields = [
			'id',
			'Unidade',
			'Cargo',
			'Parte',
			'Empresa'
		]
        

class ComercialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comercial
        fields = [
			'id',
			'Unidade',
			'PropTecComercial',
			'Parte',
			'Empresa'
		]
        

class OpcaoMenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = OpcaoMenu
        fields = [
			'id',
			'Nome',
			'Ordem',
			'CodigoIDezoitoN',
			'Url',
			'LanguageCode',
			'RodapeMenu',
			'CabecalhoMenu'
		]
        

class TipoPercPgtoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoPercPgto
        fields = [
			'id',
			'Nome',
			'Ordem',
			'Percentual',
			'CodigoIDezoitoN',
			'LanguageCode',
			'Unidade'
		]
        

class PgtoSinalClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = PgtoSinalCliente
        fields = [
			'id',
			'Nome',
			'TempoInicio',
			'TempoFim',
			'Outorga',
			'Item',
			'Criterio',
			'Unidade',
			'TipoPercPgto'
		]
        

class TipoPercntDesmbSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoPercntDesmb
        fields = [
			'id',
			'Nome',
			'Ordem',
			'Percentual',
			'CodigoIDezoitoN',
			'LanguageCode',
			'Unidade'
		]
        

class PgtoColabSerializer(serializers.ModelSerializer):
    class Meta:
        model = PgtoColab
        fields = [
			'id',
			'Nome',
			'TempoInicio',
			'TempoFim',
			'Outorga',
			'Item',
			'Criterio',
			'Unidade',
			'TipoPercntDesmb'
		]
        

class TipoEnderecamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoEnderecamento
        fields = [
			'id',
			'Nome',
			'Ordem',
			'CodigoIDezoitoN',
			'LanguageCode',
			'Unidade'
		]
        

class EnderecamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enderecamento
        fields = [
			'id',
			'TipoEnderecamento',
			'Mensagem',
			'Parte',
			'Empresa'
		]
        

class TipoObraLiterariaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoObraLiteraria
        fields = [
			'id',
			'Nome',
			'Ordem',
			'CodigoIDezoitoN',
			'LanguageCode'
		]
        

class ItemObraLiterariaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemObraLiteraria
        fields = [
			'id',
			'Parte',
			'Item',
			'TipoObraLiteraria',
			'Valor'
		]
        

class TipoObraCientificaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoObraCientifica
        fields = [
			'id',
			'Nome',
			'Ordem',
			'CodigoIDezoitoN',
			'LanguageCode'
		]
        

class ItemObraCientificaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemObraCientifica
        fields = [
			'id',
			'Parte',
			'Item',
			'TipoObraCientifica',
			'Valor'
		]
        

class TipoPcDSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoPcD
        fields = [
			'id',
			'Produz',
			'TipoPcDCateg',
			'Ordem',
			'CodigoIDezoitoN',
			'LanguageCode'
		]
        

class TipoItemCompEqpTempoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoItemCompEqpTempo
        fields = [
			'id',
			'Nome',
			'Ordem',
			'Percentual',
			'CodigoIDezoitoN',
			'LanguageCode'
		]
        

class ItemCompEqpSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemCompEqp
        fields = [
			'id',
			'Nome',
			'Ordem',
			'Item',
			'Descricao',
			'CodigoIDezoitoN',
			'LanguageCode',
			'TipoItemCompEqpTempo'
		]
        

class TipoAssociacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoAssociacao
        fields = [
			'id',
			'Nome',
			'Ordem',
			'CodigoIDezoitoN',
			'LanguageCode'
		]
        

class AssociadoParteSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssociadoParte
        fields = [
			'id',
			'Parte',
			'CodigoAssociado'
		]
        

class AssociadoEmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssociadoEmpresa
        fields = [
			'id',
			'Empresa',
			'CodigoAssociado'
		]
        

class AssociacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Associacao
        fields = [
			'id',
			'TipoAssociacao',
			'Outorga',
			'AssociadoParte',
			'AssociadoEmpresa'
		]
        

class TipoFluenciaVerbSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoFluenciaVerb
        fields = [
			'id',
			'Nome',
			'TipoCtrlQualidade',
			'Ordem',
			'CodigoIDezoitoN',
			'LanguageCode'
		]
        

class TipoPerfilGerentProjetoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoPerfilGerentProjeto
        fields = [
			'id',
			'OrganizaProjeto',
			'PraticaLideranca',
			'PraticaComunicacao',
			'RealizaNegociacao',
			'GerenciaCrises',
			'TomadaDecisao',
			'Ordem',
			'Persistencia',
			'CodigoIDezoitoN',
			'LanguageCode'
		]
        

class ItemTipoPerfilGerProjetoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemTipoPerfilGerProjeto
        fields = [
			'id',
			'Parte',
			'Item',
			'TipoPerfilGerentProjeto',
			'Valor'
		]
        

class ItemTipoEventoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemTipoEvento
        fields = [
			'id',
			'Parte',
			'Item',
			'TipoEvento',
			'Valor'
		]
        

class TipoSistemasInformacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoSistemasInformacao
        fields = [
			'id',
			'Nome',
			'Unidade',
			'Ordem',
			'CodigoIDezoitoN',
			'LanguageCode'
		]
        

class ItemSistemasInformacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemSistemasInformacao
        fields = [
			'id',
			'Parte',
			'Item',
			'TipoSistemasInformacao',
			'Valor'
		]
        

class ItemTipoPcDSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemTipoPcD
        fields = [
			'id',
			'Parte',
			'Item',
			'TipoPcD',
			'Valor'
		]
        

class TipoObraArtisticaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoObraArtistica
        fields = [
			'id',
			'Nome',
			'Ordem',
			'CodigoIDezoitoN',
			'LanguageCode'
		]
        

class ItemObraArtisticaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemObraArtistica
        fields = [
			'id',
			'Parte',
			'Item',
			'TipoObraArtistica',
			'Valor'
		]
        

class TipoVolumeMedioVendaSemanalSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoVolumeMedioVendaSemanal
        fields = [
			'id',
			'Nome',
			'Visivel',
			'Unidade',
			'Pais',
			'Ordem',
			'CodigoIDezoitoN',
			'LanguageCode'
		]
        

class TipoModuloSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoModulo
        fields = [
			'id',
			'Nome',
			'Ordem',
			'CodigoIDezoitoN',
			'LanguageCode'
		]
        

class PermissaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permissao
        fields = [
			'id',
			'SomenteLeitura',
			'AlterarGravar',
			'Excluir',
			'Parte',
			'Outorga',
			'TipoModulo',
			'LanguageCode'
		]
        

class TipoEstiloLocucaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoEstiloLocucao
        fields = [
			'id',
			'Nome',
			'Ordem',
			'CodigoIDezoitoN',
			'LanguageCode'
		]
        

class ItemTipoEstiloLocucaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemTipoEstiloLocucao
        fields = [
			'id',
			'Parte',
			'Item',
			'TipoEstiloLocucao',
			'Valor'
		]
        

class TipoVozGeneroSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoVozGenero
        fields = [
			'id',
			'Nome',
			'Ordem',
			'CodigoIDezoitoN',
			'LanguageCode'
		]
        

class ItemTipoVozGeneroSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemTipoVozGenero
        fields = [
			'id',
			'Parte',
			'Item',
			'TipoVozGenero',
			'Valor'
		]
        

class TipoFocoLocucaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoFocoLocucao
        fields = [
			'id',
			'Nome',
			'Unidade',
			'Ordem',
			'CodigoIDezoitoN',
			'LanguageCode'
		]
        

class ItemTipoFocoLocucaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemTipoFocoLocucao
        fields = [
			'id',
			'Parte',
			'Item',
			'TipoFocoLocucao',
			'Valor'
		]
        

class TipoVozIdadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoVozIdade
        fields = [
			'id',
			'Nome',
			'Ordem',
			'CodigoIDezoitoN',
			'LanguageCode'
		]
        

class ItemTipoVozIdadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemTipoVozIdade
        fields = [
			'id',
			'Parte',
			'Item',
			'TipoVozIdade',
			'Valor'
		]
        

class TipoVozAmostraSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoVozAmostra
        fields = [
			'id',
			'Arquivo',
			'Ordem',
			'CodigoIDezoitoN',
			'LanguageCode'
		]
        

class ItemTipoVozAmostraSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemTipoVozAmostra
        fields = [
			'id',
			'Parte',
			'Item',
			'TipoVozAmostra',
			'Valor'
		]
        

class AgendaAtividadeHistoricoSerializer(serializers.ModelSerializer):
    class Meta:
        model = AgendaAtividadeHistorico
        fields = [
			'id',
			'Concluido',
			'EComoFoi',
			'QuandoFoi',
			'Data',
			'AgendaAtividade',
			'Parte',
			'CtrlQualidade',
			'LanguageCode'
		]
        

class HardwareSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hardware
        fields = [
			'id',
			'Parte',
			'TipoHardwareComputador',
			'TipoPeriferico',
			'TipoSuporteCont'
		]
        

class TipoProficCategSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoProficCateg
        fields = [
			'id',
			'Descricao',
			'TipoCtrlQualidade',
			'Ordem',
			'CodigoIDezoitoN',
			'LanguageCode'
		]
        

class ParteLinguaPaisTipoProficCategSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParteLinguaPaisTipoProficCateg
        fields = [
			'id',
			'Ordem',
			'ParteLinguaPais',
			'TipoProficCateg',
			'TipoFluenciaVerb',
			'TipoCtrlQualidade'
		]
        

class ParEmpresaLinguaPaisSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParEmpresaLinguaPais
        fields = [
			'id',
			'Partida',
			'Chegada',
			'EmpresaLinguaPais',
			'Valor',
			'TipoCargoTrad'
		]
        

class TipoFaseLuaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoFaseLua
        fields = [
			'id',
			'Nome',
			'Abreviatura',
			'Descricao',
			'TipoHemisferio',
			'BancoImagem',
			'Ordem',
			'CodigoIDezoitoN',
			'LanguageCode'
		]
        

class TipoLingProgSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoLingProg
        fields = [
			'id',
			'Nome',
			'Visivel',
			'Unidade',
			'Ordem',
			'CodigoIDezoitoN',
			'LanguageCode'
		]
        

class ParteTipoLingProgSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParteTipoLingProg
        fields = [
			'id',
			'Parte',
			'TipoLingProg',
			'TipoEngineGame'
		]
        

class TipoLocacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoLocacao
        fields = [
			'id',
			'Nome',
			'Ordem',
			'CodigoIDezoitoN',
			'LanguageCode',
			'Unidade'
		]
        

class RelDiagLocEquipamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = RelDiagLocEquipamento
        fields = [
			'id',
			'DataRetirada',
			'HoraRetirada',
			'DataDevolucao',
			'HoraDevolucao',
			'RelDiag',
			'TipoLocacao',
			'Evento'
		]
        

class RelDiagInterpretacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = RelDiagInterpretacao
        fields = [
			'id',
			'NomeEvento',
			'RelDiag',
			'Evento',
			'TemaEvento',
			'InstituicaoEvento',
			'TituloPalestra',
			'UrgenciaServico',
			'CodigoIDezoitoN',
			'LanguageCode'
		]
        

class CertificacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificacao
        fields = [
			'id',
			'Nome',
			'Parte',
			'TipoCertificacao',
			'TipoDataAnoCard'
		]
        

class TipoRestricaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoRestricao
        fields = [
			'id',
			'Nome',
			'Ordem',
			'CodigoIDezoitoN',
			'LanguageCode',
			'Unidade'
		]
        

class TipoBiometriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoBiometria
        fields = [
			'id',
			'Nome',
			'Unidade',
			'Ordem',
			'CodigoIDezoitoN',
			'LanguageCode'
		]
        

class ListaRestricaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ListaRestricao
        fields = [
			'id',
			'Data',
			'TipoRestricao',
			'Parte',
			'Empresa'
		]
        

class BiometriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Biometria
        fields = [
			'id',
			'Codigo',
			'Parte',
			'TipoBiometria',
			'BancoImagem'
		]
        

class LinguaPaisSerializer(serializers.ModelSerializer):
    class Meta:
        model = LinguaPais
        fields = [
			'id',
			'HabilitarLinguaSite',
			'Lingua',
			'Pais',
			'Ordem',
			'CodigoIDezoitoN',
			'LanguageCode'
		]
        

class TipoLicOportunidadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoLicOportunidade
        fields = [
			'id',
			'Nome',
			'Ordem',
			'CodigoIDezoitoN',
			'LanguageCode'
		]
        

class RelDiagLicOportunidadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = RelDiagLicOportunidade
        fields = [
			'id',
			'RelDiag',
			'Parte',
			'TipoLicOportunidade'
		]
        

class InventarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventario
        fields = [
			'id',
			'DataIventario',
			'QuantidadeInventariada',
			'DataProximoIventario',
			'Observacao',
			'CodigoIDezoitoN',
			'Parte',
			'Produto',
			'LanguageCode'
		]
        

class ConvenioParteEmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConvenioParteEmpresa
        fields = [
			'id',
			'Aliquota',
			'Convenio',
			'Parte',
			'Empresa'
		]
        

class ConvenioItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConvenioItem
        fields = [
			'id',
			'Preco',
			'Item',
			'ItemTraducao',
			'ItemModeloTraducao',
			'AliquotaMax'
		]
        

class LinguaPaisEmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = LinguaPaisEmpresa
        fields = [
			'id',
			'Lingua',
			'Pais',
			'Empresa'
		]
        

class EmpresaLinguaPaisTipoProficCategSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmpresaLinguaPaisTipoProficCateg
        fields = [
			'id',
			'EmpresaLinguaPais',
			'TipoProficCateg',
			'TipoFluenciaVerb'
		]
        

class ParEmpresaLinguaInstCertificSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParEmpresaLinguaInstCertific
        fields = [
			'id',
			'Outro',
			'ParEmpresaLinguaPais',
			'TipoInstCertific',
			'Url'
		]
        

class TipoEstacAnoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoEstacAno
        fields = [
			'id',
			'Nome',
			'Ordem',
			'CodigoIDezoitoN',
			'LanguageCode'
		]
        

class TipoEstacAnoIniSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoEstacAnoIni
        fields = [
			'id',
			'Data',
			'Hora',
			'TipoHemisferio',
			'Descricao',
			'Equinocio',
			'Solsticio',
			'TipoEstacAno',
			'Ordem',
			'CodigoIDezoitoN',
			'LanguageCode'
		]
        

class TipoDataComDASerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoDataComDA
        fields = [
			'id',
			'TipoDataDiaCard',
			'TipoDataMesOrdn',
			'TipoDataCom'
		]
        

class ParteTipoSuporteContSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParteTipoSuporteCont
        fields = [
			'id',
			'Parte',
			'TipoSuporteCont',
			'Partida',
			'Chegada'
		]
        

class RelDiagServAdClosedCaptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = RelDiagServAdClosedCaption
        fields = [
			'id',
			'RelDiagServAd',
			'Evento'
		]
        

class RelDiagServAdDigitacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = RelDiagServAdDigitacao
        fields = [
			'id',
			'NumeroPagina',
			'RelDiagServAd',
			'TipoTamanho'
		]
        

class ConsignadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consignado
        fields = [
			'id',
			'Quantidade',
			'DataInicio',
			'DataFim',
			'Item',
			'Empresa'
		]
        

class ItemCompEqpCargoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemCompEqpCargo
        fields = [
			'id',
			'Quantidade',
			'Cargo',
			'ItemCompEqp',
			'QuantidadeMinRaqueamentoCargo'
		]
        

class BancoImagemTraducaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = BancoImagemTraducao
        fields = [
			'id',
			'Nome',
			'Descricao',
			'CodigoIDezoitoN',
			'BancoImagem',
			'LanguageCode'
		]
        

class AuditoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Auditoria
        fields = [
			'id',
			'NomeAuditoria',
			'User',
			'Conteudo',
			'TipoModulo',
			'Data',
			'Ip',
			'NomeDispositivo',
			'MacAddress'
		]
        

class LivroTraducaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = LivroTraducao
        fields = [
			'id',
			'Autor',
			'InformacaoTitulo',
			'Edicao',
			'InformacaoPublicacao',
			'DescricaoFisica',
			'EntradaSecundarioSerie',
			'MencaoSerie',
			'NotaResumo',
			'CabecalhoAssuntoTopico',
			'EntradaSecundariaNomePessoal',
			'Livro',
			'CodigoIDezoitoN',
			'LanguageCode'
		]
        

class ItemLinguaPaisSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemLinguaPais
        fields = [
			'id',
			'Item',
			'LanguageCode',
			'CodigoIDezoitoN'
		]
        

class ExperienciaAdminTraducaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExperienciaAdminTraducao
        fields = [
			'id',
			'AtuacaoLideranca',
			'AssumirResponsabilidades',
			'CompreensaoNovasTecnologias',
			'LiderarPeloExemplo',
			'CapacidadePedirAjuda',
			'InteligenciaColetiva',
			'TomadaDecisoes',
			'ReconhecimentoMeritos',
			'Feedback',
			'LimitesPessoais',
			'Parte',
			'CodigoIDezoitoN',
			'LanguageCode'
		]
        

class ExperienciaComercialDescritivaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExperienciaComercialDescritiva
        fields = [
			'id',
			'Motivacao',
			'Dinamismo',
			'Proatividade',
			'HabilidadeNegociacao',
			'RelacionamentoPessoal',
			'ApresentacaoCliente',
			'AssumirRiscos',
			'ValorEticoMoral',
			'ProspectarNovoCliente',
			'AssumirResponsabilidade',
			'CodigoIDezoitoN',
			'Parte',
			'LanguageCode'
		]
        

class VendaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Venda
        fields = [
			'id',
			'PercentualMinimoSobreVendas',
			'TipoVolumeMedioVendaSemanal',
			'TipoVolumeAcumuladoVenda'
		]
        

class TipoDataAnoOrdnSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoDataAnoOrdn
        fields = [
			'id',
			'AnoOrdinal',
			'AnoExtMasc',
			'TipoDataAnoCard',
			'Ordem',
			'CodigoIDezoitoN',
			'LanguageCode'
		]
        

class EventoDetalheDominioUmSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventoDetalheDominioUm
        fields = [
			'id',
			'EventoDetalhe',
			'TipoDominioUm'
		]
        

class RanqueamentoCargoSerializer(serializers.ModelSerializer):
    class Meta:
        model = RanqueamentoCargo
        fields = [
			'id',
			'TipoServicoLinguisticoPrestado',
			'MediaRecebQualidServPrestado',
			'MediaRecebPrazoServPrestado',
			'IdiomaOrigemDestinoLingaMatern',
			'NumeroParticipacaoProjeto',
			'DominioUmProxAreaConhecimento',
			'DominioDoisProxSetorEconomico',
			'FormAcadem',
			'CapacidadeDiariaTrabalho',
			'CertificacoeConquistada',
			'PrecoCadastradoCargo',
			'ProximidadeLocalServico',
			'Peso',
			'Nota',
			'Media',
			'MediaGeral',
			'Cargo'
		]
        

class FilmeTraducaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = FilmeTraducao
        fields = [
			'id',
			'Titulo',
			'Sinopse',
			'Genero',
			'Diretor',
			'Roteirista',
			'Elenco',
			'Cor',
			'Produtora',
			'Locacao',
			'Filme',
			'CodigoIDezoitoN',
			'LanguageCode'
		]
        

class AssinaturaBancoArquivoSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssinaturaBancoArquivo
        fields = [
			'id',
			'BancoArquivo',
			'Parte',
			'Data'
		]
        

class TipoPergSegurSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoPergSegur
        fields = [
			'id',
			'Pergunta',
			'Ordem',
			'CodigoIDezoitoN',
			'LanguageCode'
		]
        

class SegurancaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seguranca
        fields = [
			'id',
			'TipoPergSegur',
			'RespostaPerguntaSeguranca',
			'AceitoTermoUso',
			'Parte',
			'DeclaracaoMaiorDezesseisAnos'
		]
        

class BancoArquivoTraducaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = BancoArquivoTraducao
        fields = [
			'id',
			'Nome',
			'Descricao',
			'CodigoIDezoitoN',
			'BancoArquivo',
			'LanguageCode'
		]
        

class TipoListaContatoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoListaContato
        fields = [
			'id',
			'Nome',
			'Ordem',
			'CodigoIDezoitoN',
			'LanguageCode',
			'Unidade'
		]
        

class ItemPermissaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemPermissao
        fields = [
			'id',
			'Unidade',
			'Item',
			'NaoExibirUrl',
			'NaoExibirInstant'
		]
        

class ParParteLinguaPaisSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParParteLinguaPais
        fields = [
			'id',
			'ParteLinguaPaisPartida',
			'ParteLinguaPaisChegada',
			'Ordem',
			'FormCompl',
			'FormAcadem'
		]
        

class TipoCalendLunarSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoCalendLunar
        fields = [
			'id',
			'Data',
			'TipoFaseLua',
			'EclipseSolar',
			'EclipseLunar',
			'Ordem',
			'CodigoIDezoitoN',
			'LanguageCode'
		]
        

class RelDiagServAdLegendagemSerializer(serializers.ModelSerializer):
    class Meta:
        model = RelDiagServAdLegendagem
        fields = [
			'id',
			'QuantMinutosIniciais',
			'QuantMinutosReais',
			'RelDiagServAd'
		]
        

class RelDiagServAdRedacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = RelDiagServAdRedacao
        fields = [
			'id',
			'NumPalavrasIniciais',
			'NumPalavrasReais',
			'RelDiagServAd'
		]
        

class RelDiagServAdConsulLinguisticaSerializer(serializers.ModelSerializer):
    class Meta:
        model = RelDiagServAdConsulLinguistica
        fields = [
			'id',
			'QuantHoraInicial',
			'QuantHoraReal',
			'RelDiagServAd'
		]
        

class RelDiagServAdAuditLinguisticaSerializer(serializers.ModelSerializer):
    class Meta:
        model = RelDiagServAdAuditLinguistica
        fields = [
			'id',
			'QuantHoraInicial',
			'QuantHoraReal',
			'RelDiagServAd'
		]
        

class RelDiagServAdDublagemSerializer(serializers.ModelSerializer):
    class Meta:
        model = RelDiagServAdDublagem
        fields = [
			'id',
			'RelDiagServAd'
		]
        

class RelDiagServAdLocucaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = RelDiagServAdLocucao
        fields = [
			'id',
			'RelDiagServAd',
			'TempoDuracaoAudio'
		]
        

class CodigoPromocionalSerializer(serializers.ModelSerializer):
    class Meta:
        model = CodigoPromocional
        fields = [
			'id',
			'Codigo',
			'Desconto'
		]
        

class PlanoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plano
        fields = [
			'id',
			'PagamentoAssociado',
			'PagamentoAnual',
			'ItemUnidade',
			'PagamentoMensal',
			'ConsultaAvulsaCurriculo',
			'ModCadastramentoCurriculo',
			'ModRecrutamentoSelecao',
			'ModCadastro',
			'ModAutenticacaoDocumento',
			'ModContaReceber',
			'ModContaPagar',
			'ModCadastramentoTabelaPreco',
			'ModProjeto',
			'ModEmissaoPropostaInstantanea',
			'ModCrm',
			'ModLance',
			'ModContrato',
			'ModFinanceiro',
			'ModPedagogico',
			'ModPortalAluno',
			'ModIndicador',
			'ModAgenda',
			'ModControleFrequencia',
			'ModIntegracao',
			'ModPerfilUsuarioColaborador',
			'ModCustomizacao',
			'ModPesClimaAvaliacaoDesempenho',
			'Usuario',
			'Suporte',
			'Capacidade'
		]
        

class EtapaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Etapa
        fields = [
			'id',
			'Titulo',
			'Descricao',
			'CodigoIDezoitoN',
			'LanguageCode'
		]
        

class ExperienciaAdministratOutraSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExperienciaAdministratOutra
        fields = [
			'id',
			'ExperienciaVendas',
			'ExperienciaPreviaNegocProprio',
			'DisponibilidadeViagens',
			'ExperienciaFranquias',
			'ExperienciaCapitalInicial',
			'Parte'
		]
        

class ExperienciaComercialOutraSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExperienciaComercialOutra
        fields = [
			'id',
			'PossuiEmpresa',
			'VeiculoProprio',
			'ExperienciaVendasSegmento',
			'PossuiEstruturaPropria',
			'CarteiraClientes',
			'DisponibilidadeViagens',
			'Parte'
		]
        

class RelDiagServAdRevisaoTextoSerializer(serializers.ModelSerializer):
    class Meta:
        model = RelDiagServAdRevisaoTexto
        fields = [
			'id',
			'QuantPalavrasIniciais',
			'QuantPalavrasReais',
			'RelDiagServAd'
		]
        

class RelDiagServAdDiagramacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = RelDiagServAdDiagramacao
        fields = [
			'id',
			'QuantPaginasIniciais',
			'QuantPaginasReais',
			'RelDiagServAd'
		]
        

class RelDiagServAdTranscricaoAudioSerializer(serializers.ModelSerializer):
    class Meta:
        model = RelDiagServAdTranscricaoAudio
        fields = [
			'id',
			'RelDiagServAd'
		]
        

class RelDiagServAdAudiodescricaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = RelDiagServAdAudiodescricao
        fields = [
			'id',
			'QuantidadeImagens',
			'DuracaoVideo',
			'DuracaoDescricao',
			'RelDiagServAd'
		]
        

class DescricaoAdicionalSerializer(serializers.ModelSerializer):
    class Meta:
        model = DescricaoAdicional
        fields = [
			'id',
			'PremiosRecebidos',
			'FluxoTrabalho',
			'ProcessoQualidade',
			'LivreApresentacao',
			'CodigoIDezoitoN',
			'LanguageCode'
		]
        

class PreferenciaAdicionalEmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = PreferenciaAdicionalEmpresa
        fields = [
			'id',
			'ContratoEstagiario',
			'SubContrataOutraEmpresa',
			'OportunidadeColaborador',
			'OportunidadeFreelancer',
			'OportunidadePcD',
			'Empresa'
		]
        

class EmpresaTraducaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmpresaTraducao
        fields = [
			'id',
			'Slogan',
			'Visao',
			'ProdutosServicos',
			'Descricao',
			'Missao',
			'Valor',
			'ValorDescricao',
			'CodigoIDezoitoN',
			'Apresentacao',
			'Observacao',
			'SobreEmpresa',
			'LanguageCode'
		]
        

class CodigoEndPostDescSerializer(serializers.ModelSerializer):
    class Meta:
        model = CodigoEndPostDesc
        fields = [
			'id',
			'Population',
			'CodigoEndPostal',
			'HouseholdsPerZipcode',
			'WhitePopulation',
			'BlackPopulation',
			'HispanicPopulation',
			'AsianPopulation',
			'HawaiianPopulation',
			'IndianPopulation',
			'OtherPopulation',
			'MalePopulation',
			'FemalePopulation',
			'PersonsPerHousehold',
			'AverageHouseValue',
			'IncomePerHousehold',
			'MedianAge',
			'MedianAgeMale',
			'MedianAgeFemale',
			'Elevation',
			'State',
			'StateFullName',
			'CityType',
			'CityAliasAbbreviation',
			'AreaCode',
			'City',
			'CityAliasName',
			'County',
			'CountyFIPS',
			'StateFIPS',
			'TimeZone',
			'DayLightSaving',
			'MSA',
			'PMSA',
			'CSA',
			'CBSA',
			'CBSA_DIV',
			'CBSA_Type',
			'CBSA_Name',
			'MSA_Name',
			'PMSA_Name',
			'Region',
			'Division',
			'MailingName',
			'NumberOfBusinesses',
			'NumberOfEmployees',
			'BusinessFirstQuarterPayroll',
			'BusinessAnnualPayroll',
			'BusinessEmploymentFlag',
			'GrowthRank',
			'GrowingCountiesA',
			'GrowingCountiesB',
			'GrowthIncreaseNumber',
			'GrowthIncreasePercentage',
			'CBSAPopulation',
			'CBSADivisionPopulation',
			'CongressionalDistrict',
			'CongressionalLandArea',
			'DeliveryResidential',
			'DeliveryBusiness',
			'DeliveryTotal',
			'PreferredLastLineKey',
			'ClassificationCode',
			'MultiCounty',
			'CSAName',
			'CBSA_DIV_Name',
			'CityStateKey',
			'PopulationEstimate',
			'LandArea',
			'WaterArea',
			'CityAliasCode',
			'CityMixedCase',
			'CityAliasMixedCase',
			'BoxCount',
			'SFDU',
			'MFDU',
			'StateANSI',
			'CountyANSI',
			'ZIPIntroDate',
			'AliasIntroDate',
			'FacilityCode',
			'CityDeliveryIndicator',
			'CarrierRouteRateSortation',
			'FinanceNumber',
			'UniqueZIPName',
			'SSAStateCountyCode',
			'MedicareCBSACode',
			'MedicareCBSAName',
			'MedicareCBSAType',
			'MarketRatingAreaID',
			'STATE',
			'STATEFIPS',
			'PLACEFIPS',
			'PLACENAME',
			'PLACETYPE',
			'COUNTY',
			'FUNCSTAT',
			'FUNCSTATTEXT',
			'CLASSFP',
			'GEOID',
			'POPPT',
			'HUPT',
			'AREAPT',
			'AREALANDPT',
			'ZPOP',
			'ZHU',
			'ZAREA',
			'ZAREALAND',
			'PLPOP',
			'PLHU',
			'PLAREA',
			'PLAREALAND',
			'ZPOPPCT',
			'ZHUPCT',
			'ZAREAPCT',
			'ZAREALANDPCT',
			'PLPOPPCT',
			'PLHUPCT',
			'PLAREAPCT',
			'PLAREALANDPCT',
			'City',
			'AreaCode',
			'ProvinceName',
			'CityFlag',
			'TimeZone',
			'Elevation',
			'PrivateDwellings',
			'AreaName',
			'MunicipalityName',
			'imprecise',
			'military'
		]
        

class TipoFeriadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoFeriado
        fields = [
			'id',
			'Nome',
			'Ordem',
			'CodigoDezoitoN',
			'LanguageCode'
		]
        

