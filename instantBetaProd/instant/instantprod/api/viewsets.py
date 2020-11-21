from django.contrib.auth.models import User
from instantprod.models import *
from django.shortcuts import get_object_or_404
from .serializers import *
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import permissions 

class LanguageCodeViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing LanguageCode instances.
    serializer_class = LanguageCodeSerializer
    queryset = LanguageCode.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class PalavraChaveViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing PalavraChave instances.
    serializer_class = PalavraChaveSerializer
    queryset = PalavraChave.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class TipoBancoImagemViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing TipoBancoImagem instances.
    serializer_class = TipoBancoImagemSerializer
    queryset = TipoBancoImagem.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class BancoImagemViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing BancoImagem instances.
    serializer_class = BancoImagemSerializer
    queryset = BancoImagem.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class ContinenteViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing Continente instances.
    serializer_class = ContinenteSerializer
    queryset = Continente.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class TipoHemisferioViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing TipoHemisferio instances.
    serializer_class = TipoHemisferioSerializer
    queryset = TipoHemisferio.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class AreaGeograficaViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing AreaGeografica instances.
    serializer_class = AreaGeograficaSerializer
    queryset = AreaGeografica.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class PaisViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing Pais instances.
    serializer_class = PaisSerializer
    queryset = Pais.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class RegiaoViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing Regiao instances.
    serializer_class = RegiaoSerializer
    queryset = Regiao.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class TipoOrgaoEmissViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing TipoOrgaoEmiss instances.
    serializer_class = TipoOrgaoEmissSerializer
    queryset = TipoOrgaoEmiss.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class EstadoViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing Estado instances.
    serializer_class = EstadoSerializer
    queryset = Estado.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class CidadeViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing Cidade instances.
    serializer_class = CidadeSerializer
    queryset = Cidade.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class TipoLogradouroViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing TipoLogradouro instances.
    serializer_class = TipoLogradouroSerializer
    queryset = TipoLogradouro.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class CodigoEndPostalViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing CodigoEndPostal instances.
    serializer_class = CodigoEndPostalSerializer
    queryset = CodigoEndPostal.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class TipoComplementoViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing TipoComplemento instances.
    serializer_class = TipoComplementoSerializer
    queryset = TipoComplemento.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class TipoEnderecoViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing TipoEndereco instances.
    serializer_class = TipoEnderecoSerializer
    queryset = TipoEndereco.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class EnderecoViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing Endereco instances.
    serializer_class = EnderecoSerializer
    queryset = Endereco.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class TipoContatoTecnViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing TipoContatoTecn instances.
    serializer_class = TipoContatoTecnSerializer
    queryset = TipoContatoTecn.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class TipoContatoViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing TipoContato instances.
    serializer_class = TipoContatoSerializer
    queryset = TipoContato.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class TipoOpTelefoniaViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing TipoOpTelefonia instances.
    serializer_class = TipoOpTelefoniaSerializer
    queryset = TipoOpTelefonia.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class ContatoViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing Contato instances.
    serializer_class = ContatoSerializer
    queryset = Contato.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class TipoPcDCategViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing TipoPcDCateg instances.
    serializer_class = TipoPcDCategSerializer
    queryset = TipoPcDCateg.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class TipoDiaSemanaViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing TipoDiaSemana instances.
    serializer_class = TipoDiaSemanaSerializer
    queryset = TipoDiaSemana.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class TipoHorarioFuncionamentoViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing TipoHorarioFuncionamento instances.
    serializer_class = TipoHorarioFuncionamentoSerializer
    queryset = TipoHorarioFuncionamento.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class HorarioFuncionamentoViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing HorarioFuncionamento instances.
    serializer_class = HorarioFuncionamentoSerializer
    queryset = HorarioFuncionamento.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class TipoUrlViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing TipoUrl instances.
    serializer_class = TipoUrlSerializer
    queryset = TipoUrl.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class UrlViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing Url instances.
    serializer_class = UrlSerializer
    queryset = Url.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class TipoPDVViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing TipoPDV instances.
    serializer_class = TipoPDVSerializer
    queryset = TipoPDV.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class PDVViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing PDV instances.
    serializer_class = PDVSerializer
    queryset = PDV.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class ItemTipoAreaViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing ItemTipoArea instances.
    serializer_class = ItemTipoAreaSerializer
    queryset = ItemTipoArea.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class MicrositeViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing Microsite instances.
    serializer_class = MicrositeSerializer
    queryset = Microsite.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class UnidadeViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing Unidade instances.
    serializer_class = UnidadeSerializer
    queryset = Unidade.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class TipoPromocaoViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing TipoPromocao instances.
    serializer_class = TipoPromocaoSerializer
    queryset = TipoPromocao.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class TipoProgressaoViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing TipoProgressao instances.
    serializer_class = TipoProgressaoSerializer
    queryset = TipoProgressao.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class TipoCargoViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing TipoCargo instances.
    serializer_class = TipoCargoSerializer
    queryset = TipoCargo.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class TipoDocumentoViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing TipoDocumento instances.
    serializer_class = TipoDocumentoSerializer
    queryset = TipoDocumento.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class TipoSetorViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing TipoSetor instances.
    serializer_class = TipoSetorSerializer
    queryset = TipoSetor.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class TipoFuncioTurnoViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing TipoFuncioTurno instances.
    serializer_class = TipoFuncioTurnoSerializer
    queryset = TipoFuncioTurno.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class TipoRelacaoViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing TipoRelacao instances.
    serializer_class = TipoRelacaoSerializer
    queryset = TipoRelacao.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class CargoViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing Cargo instances.
    serializer_class = CargoSerializer
    queryset = Cargo.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class TipoCargoTradViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing TipoCargoTrad instances.
    serializer_class = TipoCargoTradSerializer
    queryset = TipoCargoTrad.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class TipoCtrlQualidadeViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing TipoCtrlQualidade instances.
    serializer_class = TipoCtrlQualidadeSerializer
    queryset = TipoCtrlQualidade.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class TipoProficienciaLinguaViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing TipoProficienciaLingua instances.
    serializer_class = TipoProficienciaLinguaSerializer
    queryset = TipoProficienciaLingua.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class TipoMoedaViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing TipoMoeda instances.
    serializer_class = TipoMoedaSerializer
    queryset = TipoMoeda.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class TipoVolumeAcumuladoVendaViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing TipoVolumeAcumuladoVenda instances.
    serializer_class = TipoVolumeAcumuladoVendaSerializer
    queryset = TipoVolumeAcumuladoVenda.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class TipoDomUmGdArCoViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing TipoDomUmGdArCo instances.
    serializer_class = TipoDomUmGdArCoSerializer
    queryset = TipoDomUmGdArCo.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class TipoDomUmSbArCoViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing TipoDomUmSbArCo instances.
    serializer_class = TipoDomUmSbArCoSerializer
    queryset = TipoDomUmSbArCo.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class TipoDominioUmViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing TipoDominioUm instances.
    serializer_class = TipoDominioUmSerializer
    queryset = TipoDominioUm.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class TipoLinguaClasfViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing TipoLinguaClasf instances.
    serializer_class = TipoLinguaClasfSerializer
    queryset = TipoLinguaClasf.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class LinguaViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing Lingua instances.
    serializer_class = LinguaSerializer
    queryset = Lingua.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class TipoImpostoViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing TipoImposto instances.
    serializer_class = TipoImpostoSerializer
    queryset = TipoImposto.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class TipoNotaComunicacaoViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing TipoNotaComunicacao instances.
    serializer_class = TipoNotaComunicacaoSerializer
    queryset = TipoNotaComunicacao.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class TipoNotaQualidadeViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing TipoNotaQualidade instances.
    serializer_class = TipoNotaQualidadeSerializer
    queryset = TipoNotaQualidade.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class TipoNotaGeralViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing TipoNotaGeral instances.
    serializer_class = TipoNotaGeralSerializer
    queryset = TipoNotaGeral.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class CtrlQualidadeViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing CtrlQualidade instances.
    serializer_class = CtrlQualidadeSerializer
    queryset = CtrlQualidade.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class TipoMargemLucroViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing TipoMargemLucro instances.
    serializer_class = TipoMargemLucroSerializer
    queryset = TipoMargemLucro.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class MargemLucroViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing MargemLucro instances.
    serializer_class = MargemLucroSerializer
    queryset = MargemLucro.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class TituloViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing Titulo instances.
    serializer_class = TituloSerializer
    queryset = Titulo.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class SubTituloServicoViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing SubTituloServico instances.
    serializer_class = SubTituloServicoSerializer
    queryset = SubTituloServico.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class SubTipoDocumentoViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing SubTipoDocumento instances.
    serializer_class = SubTipoDocumentoSerializer
    queryset = SubTipoDocumento.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class ItemCategoriaViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing ItemCategoria instances.
    serializer_class = ItemCategoriaSerializer
    queryset = ItemCategoria.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class TipoDomDoisSecViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing TipoDomDoisSec instances.
    serializer_class = TipoDomDoisSecSerializer
    queryset = TipoDomDoisSec.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class TipoDomDoisDivViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing TipoDomDoisDiv instances.
    serializer_class = TipoDomDoisDivSerializer
    queryset = TipoDomDoisDiv.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class TipoDomDoisGrupViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing TipoDomDoisGrup instances.
    serializer_class = TipoDomDoisGrupSerializer
    queryset = TipoDomDoisGrup.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class TipoDomDoisClasViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing TipoDomDoisClas instances.
    serializer_class = TipoDomDoisClasSerializer
    queryset = TipoDomDoisClas.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class TipoDominioDoisViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing TipoDominioDois instances.
    serializer_class = TipoDominioDoisSerializer
    queryset = TipoDominioDois.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class FuncaoViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing Funcao instances.
    serializer_class = FuncaoSerializer
    queryset = Funcao.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class TipoExtCategoriaViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing TipoExtCategoria instances.
    serializer_class = TipoExtCategoriaSerializer
    queryset = TipoExtCategoria.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class TipoExtensaoViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing TipoExtensao instances.
    serializer_class = TipoExtensaoSerializer
    queryset = TipoExtensao.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class CodigoValidacaoViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing CodigoValidacao instances.
    serializer_class = CodigoValidacaoSerializer
    queryset = CodigoValidacao.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class ImpostoViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing Imposto instances.
    serializer_class = ImpostoSerializer
    queryset = Imposto.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class PadraoDocumentoViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing PadraoDocumento instances.
    serializer_class = PadraoDocumentoSerializer
    queryset = PadraoDocumento.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class BancoArquivoViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing BancoArquivo instances.
    serializer_class = BancoArquivoSerializer
    queryset = BancoArquivo.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class ItemViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing Item instances.
    serializer_class = ItemSerializer
    queryset = Item.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class CapacidadeDiariaViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing CapacidadeDiaria instances.
    serializer_class = CapacidadeDiariaSerializer
    queryset = CapacidadeDiaria.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class TipoMedidaServViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing TipoMedidaServ instances.
    serializer_class = TipoMedidaServSerializer
    queryset = TipoMedidaServ.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class TipoMedidaViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing TipoMedida instances.
    serializer_class = TipoMedidaSerializer
    queryset = TipoMedida.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class TipoCompLinguaViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing TipoCompLingua instances.
    serializer_class = TipoCompLinguaSerializer
    queryset = TipoCompLingua.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class TipoAnoInicioAtuacaoViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing TipoAnoInicioAtuacao instances.
    serializer_class = TipoAnoInicioAtuacaoSerializer
    queryset = TipoAnoInicioAtuacao.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class ValorViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing Valor instances.
    serializer_class = ValorSerializer
    queryset = Valor.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class TipoFuncaoTradViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing TipoFuncaoTrad instances.
    serializer_class = TipoFuncaoTradSerializer
    queryset = TipoFuncaoTrad.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class PosicaoClausulaDocumentoViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing PosicaoClausulaDocumento instances.
    serializer_class = PosicaoClausulaDocumentoSerializer
    queryset = PosicaoClausulaDocumento.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class TipoClausulaViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing TipoClausula instances.
    serializer_class = TipoClausulaSerializer
    queryset = TipoClausula.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class ClausulaViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing Clausula instances.
    serializer_class = ClausulaSerializer
    queryset = Clausula.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class TipoIdentificacaoViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing TipoIdentificacao instances.
    serializer_class = TipoIdentificacaoSerializer
    queryset = TipoIdentificacao.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class IdentificacaoViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing Identificacao instances.
    serializer_class = IdentificacaoSerializer
    queryset = Identificacao.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class TipoSituacaoViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing TipoSituacao instances.
    serializer_class = TipoSituacaoSerializer
    queryset = TipoSituacao.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class TipoCargoProjetoViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing TipoCargoProjeto instances.
    serializer_class = TipoCargoProjetoSerializer
    queryset = TipoCargoProjeto.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class TipoVinculoViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing TipoVinculo instances.
    serializer_class = TipoVinculoSerializer
    queryset = TipoVinculo.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class TipoCtrlPrazoViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing TipoCtrlPrazo instances.
    serializer_class = TipoCtrlPrazoSerializer
    queryset = TipoCtrlPrazo.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class CtrlPrazoViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing CtrlPrazo instances.
    serializer_class = CtrlPrazoSerializer
    queryset = CtrlPrazo.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class ProjetoViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing Projeto instances.
    serializer_class = ProjetoSerializer
    queryset = Projeto.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class OutorgaViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing Outorga instances.
    serializer_class = OutorgaSerializer
    queryset = Outorga.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class TipoEmailViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing TipoEmail instances.
    serializer_class = TipoEmailSerializer
    queryset = TipoEmail.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class EmailViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing Email instances.
    serializer_class = EmailSerializer
    queryset = Email.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class TipoDataDiaCardViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing TipoDataDiaCard instances.
    serializer_class = TipoDataDiaCardSerializer
    queryset = TipoDataDiaCard.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class TipoDataAnoCardViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing TipoDataAnoCard instances.
    serializer_class = TipoDataAnoCardSerializer
    queryset = TipoDataAnoCard.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class TipoRedeSocialViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing TipoRedeSocial instances.
    serializer_class = TipoRedeSocialSerializer
    queryset = TipoRedeSocial.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class RedeSocialViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing RedeSocial instances.
    serializer_class = RedeSocialSerializer
    queryset = RedeSocial.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class TipoPronomeTratamentoViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing TipoPronomeTratamento instances.
    serializer_class = TipoPronomeTratamentoSerializer
    queryset = TipoPronomeTratamento.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class ReferenciaViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing Referencia instances.
    serializer_class = ReferenciaSerializer
    queryset = Referencia.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class TipoAreaGeoAtuViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing TipoAreaGeoAtu instances.
    serializer_class = TipoAreaGeoAtuSerializer
    queryset = TipoAreaGeoAtu.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class UserViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing User instances.
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class TipoFiliacaoViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing TipoFiliacao instances.
    serializer_class = TipoFiliacaoSerializer
    queryset = TipoFiliacao.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class OrdemPagamentoBrasilViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing OrdemPagamentoBrasil instances.
    serializer_class = OrdemPagamentoBrasilSerializer
    queryset = OrdemPagamentoBrasil.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class QRCodeViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing QRCode instances.
    serializer_class = QRCodeSerializer
    queryset = QRCode.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class TipoMetodoPgtoViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing TipoMetodoPgto instances.
    serializer_class = TipoMetodoPgtoSerializer
    queryset = TipoMetodoPgto.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class TipoBancoViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing TipoBanco instances.
    serializer_class = TipoBancoSerializer
    queryset = TipoBanco.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class TipoContaViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing TipoConta instances.
    serializer_class = TipoContaSerializer
    queryset = TipoConta.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class DadoBancarioViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing DadoBancario instances.
    serializer_class = DadoBancarioSerializer
    queryset = DadoBancario.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class TipoFaturacaoViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing TipoFaturacao instances.
    serializer_class = TipoFaturacaoSerializer
    queryset = TipoFaturacao.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class TipoCriptomoedaViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing TipoCriptomoeda instances.
    serializer_class = TipoCriptomoedaSerializer
    queryset = TipoCriptomoeda.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class CriptomoedaViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing Criptomoeda instances.
    serializer_class = CriptomoedaSerializer
    queryset = Criptomoeda.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class TipoPrimeiroDiaSemanaViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing TipoPrimeiroDiaSemana instances.
    serializer_class = TipoPrimeiroDiaSemanaSerializer
    queryset = TipoPrimeiroDiaSemana.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class TipoDispHoraSemanaViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing TipoDispHoraSemana instances.
    serializer_class = TipoDispHoraSemanaSerializer
    queryset = TipoDispHoraSemana.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class TipoFacilidadeViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing TipoFacilidade instances.
    serializer_class = TipoFacilidadeSerializer
    queryset = TipoFacilidade.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class TipoSegmentoInteresseViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing TipoSegmentoInteresse instances.
    serializer_class = TipoSegmentoInteresseSerializer
    queryset = TipoSegmentoInteresse.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class TipoDataMesCardViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing TipoDataMesCard instances.
    serializer_class = TipoDataMesCardSerializer
    queryset = TipoDataMesCard.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class TipoTurnoTrabViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing TipoTurnoTrab instances.
    serializer_class = TipoTurnoTrabSerializer
    queryset = TipoTurnoTrab.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class DispTurnoPreferidoViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing DispTurnoPreferido instances.
    serializer_class = DispTurnoPreferidoSerializer
    queryset = DispTurnoPreferido.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class TipoAmenidadeViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing TipoAmenidade instances.
    serializer_class = TipoAmenidadeSerializer
    queryset = TipoAmenidade.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class TipoPagamentoOnlineViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing TipoPagamentoOnline instances.
    serializer_class = TipoPagamentoOnlineSerializer
    queryset = TipoPagamentoOnline.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class PagamentoOnlineViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing PagamentoOnline instances.
    serializer_class = PagamentoOnlineSerializer
    queryset = PagamentoOnline.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class TipoMarcadorViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing TipoMarcador instances.
    serializer_class = TipoMarcadorSerializer
    queryset = TipoMarcador.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class DispDiaPreferidoViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing DispDiaPreferido instances.
    serializer_class = DispDiaPreferidoSerializer
    queryset = DispDiaPreferido.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class TipoPerfilContaViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing TipoPerfilConta instances.
    serializer_class = TipoPerfilContaSerializer
    queryset = TipoPerfilConta.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class TipoEmpresaViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing TipoEmpresa instances.
    serializer_class = TipoEmpresaSerializer
    queryset = TipoEmpresa.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class TipoBandeiraCartaoViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing TipoBandeiraCartao instances.
    serializer_class = TipoBandeiraCartaoSerializer
    queryset = TipoBandeiraCartao.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class CartaoCreditoViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing CartaoCredito instances.
    serializer_class = CartaoCreditoSerializer
    queryset = CartaoCredito.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class PersonificacaoDominioViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing PersonificacaoDominio instances.
    serializer_class = PersonificacaoDominioSerializer
    queryset = PersonificacaoDominio.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class TipoSocioViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing TipoSocio instances.
    serializer_class = TipoSocioSerializer
    queryset = TipoSocio.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class QuadroSocioViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing QuadroSocio instances.
    serializer_class = QuadroSocioSerializer
    queryset = QuadroSocio.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class TipoFerramentaIntegracaoViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing TipoFerramentaIntegracao instances.
    serializer_class = TipoFerramentaIntegracaoSerializer
    queryset = TipoFerramentaIntegracao.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class IntegracaoViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing Integracao instances.
    serializer_class = IntegracaoSerializer
    queryset = Integracao.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class TransfSWIFTViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing TransfSWIFT instances.
    serializer_class = TransfSWIFTSerializer
    queryset = TransfSWIFT.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class TransfItaliaViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing TransfItalia instances.
    serializer_class = TransfItaliaSerializer
    queryset = TransfItalia.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class TransfUniaoEuropeiaViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing TransfUniaoEuropeia instances.
    serializer_class = TransfUniaoEuropeiaSerializer
    queryset = TransfUniaoEuropeia.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class EsquemaCorViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing EsquemaCor instances.
    serializer_class = EsquemaCorSerializer
    queryset = EsquemaCor.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class SaldoMensagemViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing SaldoMensagem instances.
    serializer_class = SaldoMensagemSerializer
    queryset = SaldoMensagem.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class RanqueamentoGeralViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing RanqueamentoGeral instances.
    serializer_class = RanqueamentoGeralSerializer
    queryset = RanqueamentoGeral.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class NotificacaoViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing Notificacao instances.
    serializer_class = NotificacaoSerializer
    queryset = Notificacao.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class ComissaoViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing Comissao instances.
    serializer_class = ComissaoSerializer
    queryset = Comissao.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class TipoRegimTributViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing TipoRegimTribut instances.
    serializer_class = TipoRegimTributSerializer
    queryset = TipoRegimTribut.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class TipoEmpresaTamanhoViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing TipoEmpresaTamanho instances.
    serializer_class = TipoEmpresaTamanhoSerializer
    queryset = TipoEmpresaTamanho.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class TipoContribViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing TipoContrib instances.
    serializer_class = TipoContribSerializer
    queryset = TipoContrib.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class EmpresaViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing Empresa instances.
    serializer_class = EmpresaSerializer
    queryset = Empresa.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class SalaAulaViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing SalaAula instances.
    serializer_class = SalaAulaSerializer
    queryset = SalaAula.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class TipoNivelAlunoViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing TipoNivelAluno instances.
    serializer_class = TipoNivelAlunoSerializer
    queryset = TipoNivelAluno.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class TurmaViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing Turma instances.
    serializer_class = TurmaSerializer
    queryset = Turma.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class TipoExtDigEditViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing TipoExtDigEdit instances.
    serializer_class = TipoExtDigEditSerializer
    queryset = TipoExtDigEdit.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class TipoPerifericoViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing TipoPeriferico instances.
    serializer_class = TipoPerifericoSerializer
    queryset = TipoPeriferico.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class TipoSistemaOperacionalViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing TipoSistemaOperacional instances.
    serializer_class = TipoSistemaOperacionalSerializer
    queryset = TipoSistemaOperacional.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class TipoSoftwareTraducaoViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing TipoSoftwareTraducao instances.
    serializer_class = TipoSoftwareTraducaoSerializer
    queryset = TipoSoftwareTraducao.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class TipoSoftwareLocalizViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing TipoSoftwareLocaliz instances.
    serializer_class = TipoSoftwareLocalizSerializer
    queryset = TipoSoftwareLocaliz.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class TipoSoftwareDTPViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing TipoSoftwareDTP instances.
    serializer_class = TipoSoftwareDTPSerializer
    queryset = TipoSoftwareDTP.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class TipoSoftwarePacEscViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing TipoSoftwarePacEsc instances.
    serializer_class = TipoSoftwarePacEscSerializer
    queryset = TipoSoftwarePacEsc.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class TipoSoftwareModTresDViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing TipoSoftwareModTresD instances.
    serializer_class = TipoSoftwareModTresDSerializer
    queryset = TipoSoftwareModTresD.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class TipoSoftwareTranscViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing TipoSoftwareTransc instances.
    serializer_class = TipoSoftwareTranscSerializer
    queryset = TipoSoftwareTransc.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class TipoSoftwareLeitorViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing TipoSoftwareLeitor instances.
    serializer_class = TipoSoftwareLeitorSerializer
    queryset = TipoSoftwareLeitor.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class TipoEngineGameViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing TipoEngineGame instances.
    serializer_class = TipoEngineGameSerializer
    queryset = TipoEngineGame.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class ProtocoloAtendimentoViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing ProtocoloAtendimento instances.
    serializer_class = ProtocoloAtendimentoSerializer
    queryset = ProtocoloAtendimento.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class TipoHardwareComputadorViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing TipoHardwareComputador instances.
    serializer_class = TipoHardwareComputadorSerializer
    queryset = TipoHardwareComputador.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class TipoBancoDadosViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing TipoBancoDados instances.
    serializer_class = TipoBancoDadosSerializer
    queryset = TipoBancoDados.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class TipoExtDiagramacaoViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing TipoExtDiagramacao instances.
    serializer_class = TipoExtDiagramacaoSerializer
    queryset = TipoExtDiagramacao.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class TipoExtAudioViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing TipoExtAudio instances.
    serializer_class = TipoExtAudioSerializer
    queryset = TipoExtAudio.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class TipoExtLocalizacaoViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing TipoExtLocalizacao instances.
    serializer_class = TipoExtLocalizacaoSerializer
    queryset = TipoExtLocalizacao.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class TipoExtVideoViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing TipoExtVideo instances.
    serializer_class = TipoExtVideoSerializer
    queryset = TipoExtVideo.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class TipoIntervaloTempoViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing TipoIntervaloTempo instances.
    serializer_class = TipoIntervaloTempoSerializer
    queryset = TipoIntervaloTempo.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class TipoParteViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing TipoParte instances.
    serializer_class = TipoParteSerializer
    queryset = TipoParte.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class TipoInstCertificViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing TipoInstCertific instances.
    serializer_class = TipoInstCertificSerializer
    queryset = TipoInstCertific.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class ExameProficienciaViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing ExameProficiencia instances.
    serializer_class = ExameProficienciaSerializer
    queryset = ExameProficiencia.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class TipoExtDigNaoEditViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing TipoExtDigNaoEdit instances.
    serializer_class = TipoExtDigNaoEditSerializer
    queryset = TipoExtDigNaoEdit.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class TipoReligiaoViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing TipoReligiao instances.
    serializer_class = TipoReligiaoSerializer
    queryset = TipoReligiao.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class TipoHobbieViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing TipoHobbie instances.
    serializer_class = TipoHobbieSerializer
    queryset = TipoHobbie.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class TipoAcessoInternetViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing TipoAcessoInternet instances.
    serializer_class = TipoAcessoInternetSerializer
    queryset = TipoAcessoInternet.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class TipoExpLocalizaViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing TipoExpLocaliza instances.
    serializer_class = TipoExpLocalizaSerializer
    queryset = TipoExpLocaliza.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class ParteTraducaoViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing ParteTraducao instances.
    serializer_class = ParteTraducaoSerializer
    queryset = ParteTraducao.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class TipoFonteViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing TipoFonte instances.
    serializer_class = TipoFonteSerializer
    queryset = TipoFonte.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class AssinaturaDigitalViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing AssinaturaDigital instances.
    serializer_class = AssinaturaDigitalSerializer
    queryset = AssinaturaDigital.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class DispHoraSemanaViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing DispHoraSemana instances.
    serializer_class = DispHoraSemanaSerializer
    queryset = DispHoraSemana.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class BancoCurriculoViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing BancoCurriculo instances.
    serializer_class = BancoCurriculoSerializer
    queryset = BancoCurriculo.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class TipoRelacionamentoViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing TipoRelacionamento instances.
    serializer_class = TipoRelacionamentoSerializer
    queryset = TipoRelacionamento.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class RelacionamentoViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing Relacionamento instances.
    serializer_class = RelacionamentoSerializer
    queryset = Relacionamento.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class TipoUnidComprimentoViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing TipoUnidComprimento instances.
    serializer_class = TipoUnidComprimentoSerializer
    queryset = TipoUnidComprimento.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class TipoUnidMassaViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing TipoUnidMassa instances.
    serializer_class = TipoUnidMassaSerializer
    queryset = TipoUnidMassa.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class ParteViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing Parte instances.
    serializer_class = ParteSerializer
    queryset = Parte.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class SecaoViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing Secao instances.
    serializer_class = SecaoSerializer
    queryset = Secao.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class TipoDescontoViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing TipoDesconto instances.
    serializer_class = TipoDescontoSerializer
    queryset = TipoDesconto.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class DescontoViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing Desconto instances.
    serializer_class = DescontoSerializer
    queryset = Desconto.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class TipoComoConheceuViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing TipoComoConheceu instances.
    serializer_class = TipoComoConheceuSerializer
    queryset = TipoComoConheceu.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class OrdemExeServicoViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing OrdemExeServico instances.
    serializer_class = OrdemExeServicoSerializer
    queryset = OrdemExeServico.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class ConvenioViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing Convenio instances.
    serializer_class = ConvenioSerializer
    queryset = Convenio.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class TipoRelDiagViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing TipoRelDiag instances.
    serializer_class = TipoRelDiagSerializer
    queryset = TipoRelDiag.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class TipoModoEntregaViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing TipoModoEntrega instances.
    serializer_class = TipoModoEntregaSerializer
    queryset = TipoModoEntrega.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class RelDiagViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing RelDiag instances.
    serializer_class = RelDiagSerializer
    queryset = RelDiag.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class ItemModeloViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing ItemModelo instances.
    serializer_class = ItemModeloSerializer
    queryset = ItemModelo.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class ItemModeloTraducaoViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing ItemModeloTraducao instances.
    serializer_class = ItemModeloTraducaoSerializer
    queryset = ItemModeloTraducao.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class ItemTraducaoViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing ItemTraducao instances.
    serializer_class = ItemTraducaoSerializer
    queryset = ItemTraducao.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class TipoSuporteContViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing TipoSuporteCont instances.
    serializer_class = TipoSuporteContSerializer
    queryset = TipoSuporteCont.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class TipoConteudoCategoriaViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing TipoConteudoCategoria instances.
    serializer_class = TipoConteudoCategoriaSerializer
    queryset = TipoConteudoCategoria.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class TipoConteudoViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing TipoConteudo instances.
    serializer_class = TipoConteudoSerializer
    queryset = TipoConteudo.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class TipoSuporteContIOViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing TipoSuporteContIO instances.
    serializer_class = TipoSuporteContIOSerializer
    queryset = TipoSuporteContIO.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class TipoExtDigEdtIOViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing TipoExtDigEdtIO instances.
    serializer_class = TipoExtDigEdtIOSerializer
    queryset = TipoExtDigEdtIO.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class RelDiagServAdViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing RelDiagServAd instances.
    serializer_class = RelDiagServAdSerializer
    queryset = RelDiagServAd.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class TipoFusoHorarioViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing TipoFusoHorario instances.
    serializer_class = TipoFusoHorarioSerializer
    queryset = TipoFusoHorario.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class TipoAgendaViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing TipoAgenda instances.
    serializer_class = TipoAgendaSerializer
    queryset = TipoAgenda.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class AgendaViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing Agenda instances.
    serializer_class = AgendaSerializer
    queryset = Agenda.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class AgendaDisponivelViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing AgendaDisponivel instances.
    serializer_class = AgendaDisponivelSerializer
    queryset = AgendaDisponivel.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class TipoStatusMensagemViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing TipoStatusMensagem instances.
    serializer_class = TipoStatusMensagemSerializer
    queryset = TipoStatusMensagem.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class TipoMensagemViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing TipoMensagem instances.
    serializer_class = TipoMensagemSerializer
    queryset = TipoMensagem.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class MensagemViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing Mensagem instances.
    serializer_class = MensagemSerializer
    queryset = Mensagem.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class TipoFormComplViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing TipoFormCompl instances.
    serializer_class = TipoFormComplSerializer
    queryset = TipoFormCompl.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class TipoCertificacaoViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing TipoCertificacao instances.
    serializer_class = TipoCertificacaoSerializer
    queryset = TipoCertificacao.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class TipoDataMesOrdnViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing TipoDataMesOrdn instances.
    serializer_class = TipoDataMesOrdnSerializer
    queryset = TipoDataMesOrdn.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class TipoPeriodoAnoAtualViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing TipoPeriodoAnoAtual instances.
    serializer_class = TipoPeriodoAnoAtualSerializer
    queryset = TipoPeriodoAnoAtual.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class TipoStatusFormViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing TipoStatusForm instances.
    serializer_class = TipoStatusFormSerializer
    queryset = TipoStatusForm.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class TipoDuracaoCursoViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing TipoDuracaoCurso instances.
    serializer_class = TipoDuracaoCursoSerializer
    queryset = TipoDuracaoCurso.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class TipoUnidTempoViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing TipoUnidTempo instances.
    serializer_class = TipoUnidTempoSerializer
    queryset = TipoUnidTempo.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class FormComplViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing FormCompl instances.
    serializer_class = FormComplSerializer
    queryset = FormCompl.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class TipoFormAcademViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing TipoFormAcadem instances.
    serializer_class = TipoFormAcademSerializer
    queryset = TipoFormAcadem.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class FormAcademViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing FormAcadem instances.
    serializer_class = FormAcademSerializer
    queryset = FormAcadem.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class TipoDiaSemTradViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing TipoDiaSemTrad instances.
    serializer_class = TipoDiaSemTradSerializer
    queryset = TipoDiaSemTrad.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class TipoDataDiaOrdnViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing TipoDataDiaOrdn instances.
    serializer_class = TipoDataDiaOrdnSerializer
    queryset = TipoDataDiaOrdn.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class TipoDataComDetlViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing TipoDataComDetl instances.
    serializer_class = TipoDataComDetlSerializer
    queryset = TipoDataComDetl.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class TipoDataComAssuViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing TipoDataComAssu instances.
    serializer_class = TipoDataComAssuSerializer
    queryset = TipoDataComAssu.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class TipoDataComViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing TipoDataCom instances.
    serializer_class = TipoDataComSerializer
    queryset = TipoDataCom.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class TipoEstagioPropostaViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing TipoEstagioProposta instances.
    serializer_class = TipoEstagioPropostaSerializer
    queryset = TipoEstagioProposta.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class PropTecComercialViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing PropTecComercial instances.
    serializer_class = PropTecComercialSerializer
    queryset = PropTecComercial.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class TipoPeriodicidadeViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing TipoPeriodicidade instances.
    serializer_class = TipoPeriodicidadeSerializer
    queryset = TipoPeriodicidade.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class LembreteViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing Lembrete instances.
    serializer_class = LembreteSerializer
    queryset = Lembrete.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class AgendaAtividadeViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing AgendaAtividade instances.
    serializer_class = AgendaAtividadeSerializer
    queryset = AgendaAtividade.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class ComboViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing Combo instances.
    serializer_class = ComboSerializer
    queryset = Combo.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class ItemUnidadeViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing ItemUnidade instances.
    serializer_class = ItemUnidadeSerializer
    queryset = ItemUnidade.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class ProdutoViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing Produto instances.
    serializer_class = ProdutoSerializer
    queryset = Produto.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class TipoLinguaViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing TipoLingua instances.
    serializer_class = TipoLinguaSerializer
    queryset = TipoLingua.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class RelDiagLinguaPaisViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing RelDiagLinguaPais instances.
    serializer_class = RelDiagLinguaPaisSerializer
    queryset = RelDiagLinguaPais.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class TipoDispAmbientViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing TipoDispAmbient instances.
    serializer_class = TipoDispAmbientSerializer
    queryset = TipoDispAmbient.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class TipoAutodeclaracaoViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing TipoAutodeclaracao instances.
    serializer_class = TipoAutodeclaracaoSerializer
    queryset = TipoAutodeclaracao.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class EventoInterpCargoViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing EventoInterpCargo instances.
    serializer_class = EventoInterpCargoSerializer
    queryset = EventoInterpCargo.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class RepeticaoInterpretacaoViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing RepeticaoInterpretacao instances.
    serializer_class = RepeticaoInterpretacaoSerializer
    queryset = RepeticaoInterpretacao.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class RepeticaoEventoViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing RepeticaoEvento instances.
    serializer_class = RepeticaoEventoSerializer
    queryset = RepeticaoEvento.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class NumeroRecepAuricularesViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing NumeroRecepAuriculares instances.
    serializer_class = NumeroRecepAuricularesSerializer
    queryset = NumeroRecepAuriculares.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class EventoDetalheViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing EventoDetalhe instances.
    serializer_class = EventoDetalheSerializer
    queryset = EventoDetalhe.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class ResponsavelViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing Responsavel instances.
    serializer_class = ResponsavelSerializer
    queryset = Responsavel.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class TipoLocalPresencialViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing TipoLocalPresencial instances.
    serializer_class = TipoLocalPresencialSerializer
    queryset = TipoLocalPresencial.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class TipoPreferenciaAulaViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing TipoPreferenciaAula instances.
    serializer_class = TipoPreferenciaAulaSerializer
    queryset = TipoPreferenciaAula.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class TipoFaixaEtariaViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing TipoFaixaEtaria instances.
    serializer_class = TipoFaixaEtariaSerializer
    queryset = TipoFaixaEtaria.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class TipoRegimeEnsinoViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing TipoRegimeEnsino instances.
    serializer_class = TipoRegimeEnsinoSerializer
    queryset = TipoRegimeEnsino.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class TipoModalidadeViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing TipoModalidade instances.
    serializer_class = TipoModalidadeSerializer
    queryset = TipoModalidade.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class TipoRepeticaoCursoViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing TipoRepeticaoCurso instances.
    serializer_class = TipoRepeticaoCursoSerializer
    queryset = TipoRepeticaoCurso.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class RelDiagCursoViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing RelDiagCurso instances.
    serializer_class = RelDiagCursoSerializer
    queryset = RelDiagCurso.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class TipoResidenciaContratoViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing TipoResidenciaContrato instances.
    serializer_class = TipoResidenciaContratoSerializer
    queryset = TipoResidenciaContrato.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class TipoHabilitacaoViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing TipoHabilitacao instances.
    serializer_class = TipoHabilitacaoSerializer
    queryset = TipoHabilitacao.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class TipoPcDAparelhoViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing TipoPcDAparelho instances.
    serializer_class = TipoPcDAparelhoSerializer
    queryset = TipoPcDAparelho.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class TipoEstadoCivilViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing TipoEstadoCivil instances.
    serializer_class = TipoEstadoCivilSerializer
    queryset = TipoEstadoCivil.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class TipoResidenciaViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing TipoResidencia instances.
    serializer_class = TipoResidenciaSerializer
    queryset = TipoResidencia.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class TipoTrabalhoVoluntarioViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing TipoTrabalhoVoluntario instances.
    serializer_class = TipoTrabalhoVoluntarioSerializer
    queryset = TipoTrabalhoVoluntario.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class TipoMoradorViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing TipoMorador instances.
    serializer_class = TipoMoradorSerializer
    queryset = TipoMorador.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class TipoRendaFamiliarViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing TipoRendaFamiliar instances.
    serializer_class = TipoRendaFamiliarSerializer
    queryset = TipoRendaFamiliar.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class TipoFilhoQuantViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing TipoFilhoQuant instances.
    serializer_class = TipoFilhoQuantSerializer
    queryset = TipoFilhoQuant.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class DadosPessoaisViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing DadosPessoais instances.
    serializer_class = DadosPessoaisSerializer
    queryset = DadosPessoais.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class TipoImovelViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing TipoImovel instances.
    serializer_class = TipoImovelSerializer
    queryset = TipoImovel.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class TipoFuncionarioQuantViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing TipoFuncionarioQuant instances.
    serializer_class = TipoFuncionarioQuantSerializer
    queryset = TipoFuncionarioQuant.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class TipoLicFranquiaViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing TipoLicFranquia instances.
    serializer_class = TipoLicFranquiaSerializer
    queryset = TipoLicFranquia.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class TipoInvestimentoInicialViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing TipoInvestimentoInicial instances.
    serializer_class = TipoInvestimentoInicialSerializer
    queryset = TipoInvestimentoInicial.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class TipoCapitalGiroViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing TipoCapitalGiro instances.
    serializer_class = TipoCapitalGiroSerializer
    queryset = TipoCapitalGiro.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class TipoAreaMinimaViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing TipoAreaMinima instances.
    serializer_class = TipoAreaMinimaSerializer
    queryset = TipoAreaMinima.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class TipoCompartGeoViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing TipoCompartGeo instances.
    serializer_class = TipoCompartGeoSerializer
    queryset = TipoCompartGeo.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class RelDiagLicFranquiaViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing RelDiagLicFranquia instances.
    serializer_class = RelDiagLicFranquiaSerializer
    queryset = RelDiagLicFranquia.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class RelDiagTradViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing RelDiagTrad instances.
    serializer_class = RelDiagTradSerializer
    queryset = RelDiagTrad.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class EventoEnderecoViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing EventoEndereco instances.
    serializer_class = EventoEnderecoSerializer
    queryset = EventoEndereco.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class TipoEventoViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing TipoEvento instances.
    serializer_class = TipoEventoSerializer
    queryset = TipoEvento.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class EventoViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing Evento instances.
    serializer_class = EventoSerializer
    queryset = Evento.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class TipoPretensaoBolsaEstagioViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing TipoPretensaoBolsaEstagio instances.
    serializer_class = TipoPretensaoBolsaEstagioSerializer
    queryset = TipoPretensaoBolsaEstagio.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class TipoProgrIcentEducacaoViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing TipoProgrIcentEducacao instances.
    serializer_class = TipoProgrIcentEducacaoSerializer
    queryset = TipoProgrIcentEducacao.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class TipoDisponibilEstagiarViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing TipoDisponibilEstagiar instances.
    serializer_class = TipoDisponibilEstagiarSerializer
    queryset = TipoDisponibilEstagiar.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class TipoTurnoEduViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing TipoTurnoEdu instances.
    serializer_class = TipoTurnoEduSerializer
    queryset = TipoTurnoEdu.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class ItemBolsaEstagioViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing ItemBolsaEstagio instances.
    serializer_class = ItemBolsaEstagioSerializer
    queryset = ItemBolsaEstagio.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class LivroViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing Livro instances.
    serializer_class = LivroSerializer
    queryset = Livro.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class RelDiagLivrariaViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing RelDiagLivraria instances.
    serializer_class = RelDiagLivrariaSerializer
    queryset = RelDiagLivraria.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class CabecalhoTopoViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing CabecalhoTopo instances.
    serializer_class = CabecalhoTopoSerializer
    queryset = CabecalhoTopo.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class RodapeViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing Rodape instances.
    serializer_class = RodapeSerializer
    queryset = Rodape.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class RodapeMenuViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing RodapeMenu instances.
    serializer_class = RodapeMenuSerializer
    queryset = RodapeMenu.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class RodapeBaseViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing RodapeBase instances.
    serializer_class = RodapeBaseSerializer
    queryset = RodapeBase.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class CabecalhoViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing Cabecalho instances.
    serializer_class = CabecalhoSerializer
    queryset = Cabecalho.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class CabecalhoMenuViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing CabecalhoMenu instances.
    serializer_class = CabecalhoMenuSerializer
    queryset = CabecalhoMenu.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class PrincipalViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing Principal instances.
    serializer_class = PrincipalSerializer
    queryset = Principal.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class SiteViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing Site instances.
    serializer_class = SiteSerializer
    queryset = Site.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class TipoPainelAtendimentoViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing TipoPainelAtendimento instances.
    serializer_class = TipoPainelAtendimentoSerializer
    queryset = TipoPainelAtendimento.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class TipoPosicaoAtendimentoViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing TipoPosicaoAtendimento instances.
    serializer_class = TipoPosicaoAtendimentoSerializer
    queryset = TipoPosicaoAtendimento.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class TipoOrientacaoViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing TipoOrientacao instances.
    serializer_class = TipoOrientacaoSerializer
    queryset = TipoOrientacao.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class PainelAtendimentoViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing PainelAtendimento instances.
    serializer_class = PainelAtendimentoSerializer
    queryset = PainelAtendimento.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class TipoClienteAtendeViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing TipoClienteAtende instances.
    serializer_class = TipoClienteAtendeSerializer
    queryset = TipoClienteAtende.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class FormatoHoraViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing FormatoHora instances.
    serializer_class = FormatoHoraSerializer
    queryset = FormatoHora.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class TipoSituacOcupViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing TipoSituacOcup instances.
    serializer_class = TipoSituacOcupSerializer
    queryset = TipoSituacOcup.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class TipoFormatoDataViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing TipoFormatoData instances.
    serializer_class = TipoFormatoDataSerializer
    queryset = TipoFormatoData.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class PreferenciaAdicionalViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing PreferenciaAdicional instances.
    serializer_class = PreferenciaAdicionalSerializer
    queryset = PreferenciaAdicional.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class SoftwareViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing Software instances.
    serializer_class = SoftwareSerializer
    queryset = Software.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class InstituicaoEnsinoViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing InstituicaoEnsino instances.
    serializer_class = InstituicaoEnsinoSerializer
    queryset = InstituicaoEnsino.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class TipoServTerceiroViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing TipoServTerceiro instances.
    serializer_class = TipoServTerceiroSerializer
    queryset = TipoServTerceiro.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class RelDiagServTerceiroViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing RelDiagServTerceiro instances.
    serializer_class = RelDiagServTerceiroSerializer
    queryset = RelDiagServTerceiro.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class ParteLinguaPaisViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing ParteLinguaPais instances.
    serializer_class = ParteLinguaPaisSerializer
    queryset = ParteLinguaPais.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class TipoNotaViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing TipoNota instances.
    serializer_class = TipoNotaSerializer
    queryset = TipoNota.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class NotaViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing Nota instances.
    serializer_class = NotaSerializer
    queryset = Nota.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class ListaCampanhaViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing ListaCampanha instances.
    serializer_class = ListaCampanhaSerializer
    queryset = ListaCampanha.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class EmpresaLinguaPaisViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing EmpresaLinguaPais instances.
    serializer_class = EmpresaLinguaPaisSerializer
    queryset = EmpresaLinguaPais.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class TipoAcaoViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing TipoAcao instances.
    serializer_class = TipoAcaoSerializer
    queryset = TipoAcao.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class AgendaPermissaoViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing AgendaPermissao instances.
    serializer_class = AgendaPermissaoSerializer
    queryset = AgendaPermissao.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class TipoClassListaViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing TipoClassLista instances.
    serializer_class = TipoClassListaSerializer
    queryset = TipoClassLista.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class TipoStatusListaViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing TipoStatusLista instances.
    serializer_class = TipoStatusListaSerializer
    queryset = TipoStatusLista.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class ListaContatoViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing ListaContato instances.
    serializer_class = ListaContatoSerializer
    queryset = ListaContato.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class ListaEmailViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing ListaEmail instances.
    serializer_class = ListaEmailSerializer
    queryset = ListaEmail.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class FilmeViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing Filme instances.
    serializer_class = FilmeSerializer
    queryset = Filme.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class RelDiagLicPlanoViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing RelDiagLicPlano instances.
    serializer_class = RelDiagLicPlanoSerializer
    queryset = RelDiagLicPlano.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class ItemLocacaoBalcaoViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing ItemLocacaoBalcao instances.
    serializer_class = ItemLocacaoBalcaoSerializer
    queryset = ItemLocacaoBalcao.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class TipoAcaoCampanhaViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing TipoAcaoCampanha instances.
    serializer_class = TipoAcaoCampanhaSerializer
    queryset = TipoAcaoCampanha.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class TipoStatusCampanhaViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing TipoStatusCampanha instances.
    serializer_class = TipoStatusCampanhaSerializer
    queryset = TipoStatusCampanha.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class TipoCategoriaModeloCampanhaViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing TipoCategoriaModeloCampanha instances.
    serializer_class = TipoCategoriaModeloCampanhaSerializer
    queryset = TipoCategoriaModeloCampanha.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class TipoModeloCampanhaViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing TipoModeloCampanha instances.
    serializer_class = TipoModeloCampanhaSerializer
    queryset = TipoModeloCampanha.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class ModeloCampanhaViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing ModeloCampanha instances.
    serializer_class = ModeloCampanhaSerializer
    queryset = ModeloCampanha.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class CampanhaViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing Campanha instances.
    serializer_class = CampanhaSerializer
    queryset = Campanha.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class TipoPerfilLocutorViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing TipoPerfilLocutor instances.
    serializer_class = TipoPerfilLocutorSerializer
    queryset = TipoPerfilLocutor.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class ItemTipoPerfilLocutorViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing ItemTipoPerfilLocutor instances.
    serializer_class = ItemTipoPerfilLocutorSerializer
    queryset = ItemTipoPerfilLocutor.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class TipoCategoriaServicoViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing TipoCategoriaServico instances.
    serializer_class = TipoCategoriaServicoSerializer
    queryset = TipoCategoriaServico.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class ItemCategoriaServicoViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing ItemCategoriaServico instances.
    serializer_class = ItemCategoriaServicoSerializer
    queryset = ItemCategoriaServico.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class TipoTamanhoViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing TipoTamanho instances.
    serializer_class = TipoTamanhoSerializer
    queryset = TipoTamanho.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class ModeloDocumentoViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing ModeloDocumento instances.
    serializer_class = ModeloDocumentoSerializer
    queryset = ModeloDocumento.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class TipoLicConvenioViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing TipoLicConvenio instances.
    serializer_class = TipoLicConvenioSerializer
    queryset = TipoLicConvenio.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class RelDiagLicConvenioViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing RelDiagLicConvenio instances.
    serializer_class = RelDiagLicConvenioSerializer
    queryset = RelDiagLicConvenio.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class MedidaNotaItemViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing MedidaNotaItem instances.
    serializer_class = MedidaNotaItemSerializer
    queryset = MedidaNotaItem.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class NotaItemViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing NotaItem instances.
    serializer_class = NotaItemSerializer
    queryset = NotaItem.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class PrestadorPreferencialViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing PrestadorPreferencial instances.
    serializer_class = PrestadorPreferencialSerializer
    queryset = PrestadorPreferencial.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class ComercialViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing Comercial instances.
    serializer_class = ComercialSerializer
    queryset = Comercial.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class OpcaoMenuViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing OpcaoMenu instances.
    serializer_class = OpcaoMenuSerializer
    queryset = OpcaoMenu.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class TipoPercPgtoViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing TipoPercPgto instances.
    serializer_class = TipoPercPgtoSerializer
    queryset = TipoPercPgto.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class PgtoSinalClienteViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing PgtoSinalCliente instances.
    serializer_class = PgtoSinalClienteSerializer
    queryset = PgtoSinalCliente.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class TipoPercntDesmbViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing TipoPercntDesmb instances.
    serializer_class = TipoPercntDesmbSerializer
    queryset = TipoPercntDesmb.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class PgtoColabViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing PgtoColab instances.
    serializer_class = PgtoColabSerializer
    queryset = PgtoColab.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class TipoEnderecamentoViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing TipoEnderecamento instances.
    serializer_class = TipoEnderecamentoSerializer
    queryset = TipoEnderecamento.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class EnderecamentoViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing Enderecamento instances.
    serializer_class = EnderecamentoSerializer
    queryset = Enderecamento.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class TipoObraLiterariaViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing TipoObraLiteraria instances.
    serializer_class = TipoObraLiterariaSerializer
    queryset = TipoObraLiteraria.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class ItemObraLiterariaViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing ItemObraLiteraria instances.
    serializer_class = ItemObraLiterariaSerializer
    queryset = ItemObraLiteraria.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class TipoObraCientificaViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing TipoObraCientifica instances.
    serializer_class = TipoObraCientificaSerializer
    queryset = TipoObraCientifica.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class ItemObraCientificaViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing ItemObraCientifica instances.
    serializer_class = ItemObraCientificaSerializer
    queryset = ItemObraCientifica.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class TipoPcDViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing TipoPcD instances.
    serializer_class = TipoPcDSerializer
    queryset = TipoPcD.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class TipoItemCompEqpTempoViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing TipoItemCompEqpTempo instances.
    serializer_class = TipoItemCompEqpTempoSerializer
    queryset = TipoItemCompEqpTempo.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class ItemCompEqpViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing ItemCompEqp instances.
    serializer_class = ItemCompEqpSerializer
    queryset = ItemCompEqp.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class TipoAssociacaoViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing TipoAssociacao instances.
    serializer_class = TipoAssociacaoSerializer
    queryset = TipoAssociacao.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class AssociadoParteViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing AssociadoParte instances.
    serializer_class = AssociadoParteSerializer
    queryset = AssociadoParte.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class AssociadoEmpresaViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing AssociadoEmpresa instances.
    serializer_class = AssociadoEmpresaSerializer
    queryset = AssociadoEmpresa.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class AssociacaoViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing Associacao instances.
    serializer_class = AssociacaoSerializer
    queryset = Associacao.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class TipoFluenciaVerbViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing TipoFluenciaVerb instances.
    serializer_class = TipoFluenciaVerbSerializer
    queryset = TipoFluenciaVerb.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class TipoPerfilGerentProjetoViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing TipoPerfilGerentProjeto instances.
    serializer_class = TipoPerfilGerentProjetoSerializer
    queryset = TipoPerfilGerentProjeto.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class ItemTipoPerfilGerProjetoViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing ItemTipoPerfilGerProjeto instances.
    serializer_class = ItemTipoPerfilGerProjetoSerializer
    queryset = ItemTipoPerfilGerProjeto.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class ItemTipoEventoViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing ItemTipoEvento instances.
    serializer_class = ItemTipoEventoSerializer
    queryset = ItemTipoEvento.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class TipoSistemasInformacaoViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing TipoSistemasInformacao instances.
    serializer_class = TipoSistemasInformacaoSerializer
    queryset = TipoSistemasInformacao.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class ItemSistemasInformacaoViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing ItemSistemasInformacao instances.
    serializer_class = ItemSistemasInformacaoSerializer
    queryset = ItemSistemasInformacao.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class ItemTipoPcDViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing ItemTipoPcD instances.
    serializer_class = ItemTipoPcDSerializer
    queryset = ItemTipoPcD.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class TipoObraArtisticaViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing TipoObraArtistica instances.
    serializer_class = TipoObraArtisticaSerializer
    queryset = TipoObraArtistica.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class ItemObraArtisticaViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing ItemObraArtistica instances.
    serializer_class = ItemObraArtisticaSerializer
    queryset = ItemObraArtistica.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class TipoVolumeMedioVendaSemanalViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing TipoVolumeMedioVendaSemanal instances.
    serializer_class = TipoVolumeMedioVendaSemanalSerializer
    queryset = TipoVolumeMedioVendaSemanal.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class TipoModuloViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing TipoModulo instances.
    serializer_class = TipoModuloSerializer
    queryset = TipoModulo.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class PermissaoViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing Permissao instances.
    serializer_class = PermissaoSerializer
    queryset = Permissao.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class TipoEstiloLocucaoViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing TipoEstiloLocucao instances.
    serializer_class = TipoEstiloLocucaoSerializer
    queryset = TipoEstiloLocucao.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class ItemTipoEstiloLocucaoViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing ItemTipoEstiloLocucao instances.
    serializer_class = ItemTipoEstiloLocucaoSerializer
    queryset = ItemTipoEstiloLocucao.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class TipoVozGeneroViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing TipoVozGenero instances.
    serializer_class = TipoVozGeneroSerializer
    queryset = TipoVozGenero.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class ItemTipoVozGeneroViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing ItemTipoVozGenero instances.
    serializer_class = ItemTipoVozGeneroSerializer
    queryset = ItemTipoVozGenero.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class TipoFocoLocucaoViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing TipoFocoLocucao instances.
    serializer_class = TipoFocoLocucaoSerializer
    queryset = TipoFocoLocucao.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class ItemTipoFocoLocucaoViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing ItemTipoFocoLocucao instances.
    serializer_class = ItemTipoFocoLocucaoSerializer
    queryset = ItemTipoFocoLocucao.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class TipoVozIdadeViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing TipoVozIdade instances.
    serializer_class = TipoVozIdadeSerializer
    queryset = TipoVozIdade.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class ItemTipoVozIdadeViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing ItemTipoVozIdade instances.
    serializer_class = ItemTipoVozIdadeSerializer
    queryset = ItemTipoVozIdade.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class TipoVozAmostraViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing TipoVozAmostra instances.
    serializer_class = TipoVozAmostraSerializer
    queryset = TipoVozAmostra.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class ItemTipoVozAmostraViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing ItemTipoVozAmostra instances.
    serializer_class = ItemTipoVozAmostraSerializer
    queryset = ItemTipoVozAmostra.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class AgendaAtividadeHistoricoViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing AgendaAtividadeHistorico instances.
    serializer_class = AgendaAtividadeHistoricoSerializer
    queryset = AgendaAtividadeHistorico.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class HardwareViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing Hardware instances.
    serializer_class = HardwareSerializer
    queryset = Hardware.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class TipoProficCategViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing TipoProficCateg instances.
    serializer_class = TipoProficCategSerializer
    queryset = TipoProficCateg.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class ParteLinguaPaisTipoProficCategViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing ParteLinguaPaisTipoProficCateg instances.
    serializer_class = ParteLinguaPaisTipoProficCategSerializer
    queryset = ParteLinguaPaisTipoProficCateg.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class ParEmpresaLinguaPaisViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing ParEmpresaLinguaPais instances.
    serializer_class = ParEmpresaLinguaPaisSerializer
    queryset = ParEmpresaLinguaPais.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class TipoFaseLuaViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing TipoFaseLua instances.
    serializer_class = TipoFaseLuaSerializer
    queryset = TipoFaseLua.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class TipoLingProgViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing TipoLingProg instances.
    serializer_class = TipoLingProgSerializer
    queryset = TipoLingProg.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class ParteTipoLingProgViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing ParteTipoLingProg instances.
    serializer_class = ParteTipoLingProgSerializer
    queryset = ParteTipoLingProg.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class TipoLocacaoViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing TipoLocacao instances.
    serializer_class = TipoLocacaoSerializer
    queryset = TipoLocacao.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class RelDiagLocEquipamentoViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing RelDiagLocEquipamento instances.
    serializer_class = RelDiagLocEquipamentoSerializer
    queryset = RelDiagLocEquipamento.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class RelDiagInterpretacaoViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing RelDiagInterpretacao instances.
    serializer_class = RelDiagInterpretacaoSerializer
    queryset = RelDiagInterpretacao.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class CertificacaoViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing Certificacao instances.
    serializer_class = CertificacaoSerializer
    queryset = Certificacao.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class TipoRestricaoViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing TipoRestricao instances.
    serializer_class = TipoRestricaoSerializer
    queryset = TipoRestricao.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class TipoBiometriaViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing TipoBiometria instances.
    serializer_class = TipoBiometriaSerializer
    queryset = TipoBiometria.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class ListaRestricaoViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing ListaRestricao instances.
    serializer_class = ListaRestricaoSerializer
    queryset = ListaRestricao.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class BiometriaViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing Biometria instances.
    serializer_class = BiometriaSerializer
    queryset = Biometria.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class LinguaPaisViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing LinguaPais instances.
    serializer_class = LinguaPaisSerializer
    queryset = LinguaPais.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class TipoLicOportunidadeViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing TipoLicOportunidade instances.
    serializer_class = TipoLicOportunidadeSerializer
    queryset = TipoLicOportunidade.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class RelDiagLicOportunidadeViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing RelDiagLicOportunidade instances.
    serializer_class = RelDiagLicOportunidadeSerializer
    queryset = RelDiagLicOportunidade.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class InventarioViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing Inventario instances.
    serializer_class = InventarioSerializer
    queryset = Inventario.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class ConvenioParteEmpresaViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing ConvenioParteEmpresa instances.
    serializer_class = ConvenioParteEmpresaSerializer
    queryset = ConvenioParteEmpresa.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class ConvenioItemViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing ConvenioItem instances.
    serializer_class = ConvenioItemSerializer
    queryset = ConvenioItem.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class LinguaPaisEmpresaViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing LinguaPaisEmpresa instances.
    serializer_class = LinguaPaisEmpresaSerializer
    queryset = LinguaPaisEmpresa.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class EmpresaLinguaPaisTipoProficCategViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing EmpresaLinguaPaisTipoProficCateg instances.
    serializer_class = EmpresaLinguaPaisTipoProficCategSerializer
    queryset = EmpresaLinguaPaisTipoProficCateg.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class ParEmpresaLinguaInstCertificViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing ParEmpresaLinguaInstCertific instances.
    serializer_class = ParEmpresaLinguaInstCertificSerializer
    queryset = ParEmpresaLinguaInstCertific.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class TipoEstacAnoViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing TipoEstacAno instances.
    serializer_class = TipoEstacAnoSerializer
    queryset = TipoEstacAno.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class TipoEstacAnoIniViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing TipoEstacAnoIni instances.
    serializer_class = TipoEstacAnoIniSerializer
    queryset = TipoEstacAnoIni.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class TipoDataComDAViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing TipoDataComDA instances.
    serializer_class = TipoDataComDASerializer
    queryset = TipoDataComDA.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class ParteTipoSuporteContViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing ParteTipoSuporteCont instances.
    serializer_class = ParteTipoSuporteContSerializer
    queryset = ParteTipoSuporteCont.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class RelDiagServAdClosedCaptionViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing RelDiagServAdClosedCaption instances.
    serializer_class = RelDiagServAdClosedCaptionSerializer
    queryset = RelDiagServAdClosedCaption.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class RelDiagServAdDigitacaoViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing RelDiagServAdDigitacao instances.
    serializer_class = RelDiagServAdDigitacaoSerializer
    queryset = RelDiagServAdDigitacao.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class ConsignadoViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing Consignado instances.
    serializer_class = ConsignadoSerializer
    queryset = Consignado.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class ItemCompEqpCargoViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing ItemCompEqpCargo instances.
    serializer_class = ItemCompEqpCargoSerializer
    queryset = ItemCompEqpCargo.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class BancoImagemTraducaoViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing BancoImagemTraducao instances.
    serializer_class = BancoImagemTraducaoSerializer
    queryset = BancoImagemTraducao.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class AuditoriaViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing Auditoria instances.
    serializer_class = AuditoriaSerializer
    queryset = Auditoria.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class LivroTraducaoViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing LivroTraducao instances.
    serializer_class = LivroTraducaoSerializer
    queryset = LivroTraducao.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class ItemLinguaPaisViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing ItemLinguaPais instances.
    serializer_class = ItemLinguaPaisSerializer
    queryset = ItemLinguaPais.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class ExperienciaAdminTraducaoViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing ExperienciaAdminTraducao instances.
    serializer_class = ExperienciaAdminTraducaoSerializer
    queryset = ExperienciaAdminTraducao.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class ExperienciaComercialDescritivaViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing ExperienciaComercialDescritiva instances.
    serializer_class = ExperienciaComercialDescritivaSerializer
    queryset = ExperienciaComercialDescritiva.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class VendaViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing Venda instances.
    serializer_class = VendaSerializer
    queryset = Venda.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class TipoDataAnoOrdnViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing TipoDataAnoOrdn instances.
    serializer_class = TipoDataAnoOrdnSerializer
    queryset = TipoDataAnoOrdn.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class EventoDetalheDominioUmViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing EventoDetalheDominioUm instances.
    serializer_class = EventoDetalheDominioUmSerializer
    queryset = EventoDetalheDominioUm.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class RanqueamentoCargoViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing RanqueamentoCargo instances.
    serializer_class = RanqueamentoCargoSerializer
    queryset = RanqueamentoCargo.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class FilmeTraducaoViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing FilmeTraducao instances.
    serializer_class = FilmeTraducaoSerializer
    queryset = FilmeTraducao.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class AssinaturaBancoArquivoViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing AssinaturaBancoArquivo instances.
    serializer_class = AssinaturaBancoArquivoSerializer
    queryset = AssinaturaBancoArquivo.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class TipoPergSegurViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing TipoPergSegur instances.
    serializer_class = TipoPergSegurSerializer
    queryset = TipoPergSegur.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class SegurancaViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing Seguranca instances.
    serializer_class = SegurancaSerializer
    queryset = Seguranca.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class BancoArquivoTraducaoViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing BancoArquivoTraducao instances.
    serializer_class = BancoArquivoTraducaoSerializer
    queryset = BancoArquivoTraducao.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class TipoListaContatoViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing TipoListaContato instances.
    serializer_class = TipoListaContatoSerializer
    queryset = TipoListaContato.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class ItemPermissaoViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing ItemPermissao instances.
    serializer_class = ItemPermissaoSerializer
    queryset = ItemPermissao.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class ParParteLinguaPaisViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing ParParteLinguaPais instances.
    serializer_class = ParParteLinguaPaisSerializer
    queryset = ParParteLinguaPais.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class TipoCalendLunarViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing TipoCalendLunar instances.
    serializer_class = TipoCalendLunarSerializer
    queryset = TipoCalendLunar.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class RelDiagServAdLegendagemViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing RelDiagServAdLegendagem instances.
    serializer_class = RelDiagServAdLegendagemSerializer
    queryset = RelDiagServAdLegendagem.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class RelDiagServAdRedacaoViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing RelDiagServAdRedacao instances.
    serializer_class = RelDiagServAdRedacaoSerializer
    queryset = RelDiagServAdRedacao.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class RelDiagServAdConsulLinguisticaViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing RelDiagServAdConsulLinguistica instances.
    serializer_class = RelDiagServAdConsulLinguisticaSerializer
    queryset = RelDiagServAdConsulLinguistica.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class RelDiagServAdAuditLinguisticaViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing RelDiagServAdAuditLinguistica instances.
    serializer_class = RelDiagServAdAuditLinguisticaSerializer
    queryset = RelDiagServAdAuditLinguistica.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class RelDiagServAdDublagemViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing RelDiagServAdDublagem instances.
    serializer_class = RelDiagServAdDublagemSerializer
    queryset = RelDiagServAdDublagem.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class RelDiagServAdLocucaoViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing RelDiagServAdLocucao instances.
    serializer_class = RelDiagServAdLocucaoSerializer
    queryset = RelDiagServAdLocucao.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class CodigoPromocionalViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing CodigoPromocional instances.
    serializer_class = CodigoPromocionalSerializer
    queryset = CodigoPromocional.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class PlanoViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing Plano instances.
    serializer_class = PlanoSerializer
    queryset = Plano.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class EtapaViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing Etapa instances.
    serializer_class = EtapaSerializer
    queryset = Etapa.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class ExperienciaAdministratOutraViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing ExperienciaAdministratOutra instances.
    serializer_class = ExperienciaAdministratOutraSerializer
    queryset = ExperienciaAdministratOutra.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class ExperienciaComercialOutraViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing ExperienciaComercialOutra instances.
    serializer_class = ExperienciaComercialOutraSerializer
    queryset = ExperienciaComercialOutra.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class RelDiagServAdRevisaoTextoViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing RelDiagServAdRevisaoTexto instances.
    serializer_class = RelDiagServAdRevisaoTextoSerializer
    queryset = RelDiagServAdRevisaoTexto.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class RelDiagServAdDiagramacaoViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing RelDiagServAdDiagramacao instances.
    serializer_class = RelDiagServAdDiagramacaoSerializer
    queryset = RelDiagServAdDiagramacao.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class RelDiagServAdTranscricaoAudioViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing RelDiagServAdTranscricaoAudio instances.
    serializer_class = RelDiagServAdTranscricaoAudioSerializer
    queryset = RelDiagServAdTranscricaoAudio.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class RelDiagServAdAudiodescricaoViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing RelDiagServAdAudiodescricao instances.
    serializer_class = RelDiagServAdAudiodescricaoSerializer
    queryset = RelDiagServAdAudiodescricao.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class DescricaoAdicionalViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing DescricaoAdicional instances.
    serializer_class = DescricaoAdicionalSerializer
    queryset = DescricaoAdicional.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class PreferenciaAdicionalEmpresaViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing PreferenciaAdicionalEmpresa instances.
    serializer_class = PreferenciaAdicionalEmpresaSerializer
    queryset = PreferenciaAdicionalEmpresa.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class EmpresaTraducaoViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing EmpresaTraducao instances.
    serializer_class = EmpresaTraducaoSerializer
    queryset = EmpresaTraducao.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class CodigoEndPostDescViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing CodigoEndPostDesc instances.
    serializer_class = CodigoEndPostDescSerializer
    queryset = CodigoEndPostDesc.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class TipoFeriadoViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing TipoFeriado instances.
    serializer_class = TipoFeriadoSerializer
    queryset = TipoFeriado.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
