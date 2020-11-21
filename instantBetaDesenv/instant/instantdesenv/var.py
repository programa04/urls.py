from . import models
    
def Ajuste(parametro):
	# print (parametro)
	

	# print(n)
	# print (catserv[n])
	
	# print (r)
	tc = []
	for i in parametro :
		# print (i)
		tc.append((i,i))
	tp = tuple(tc)

	return (tp)

def Conteudo():
    
    vetor = [
        'livros e outros escritos',
        'poesia',
        'romance em prosa ou em verso',	
        'conto',
        'trova',	
        'artigo',		
        'ensaio',	
        'peça de teatro',			
        'história infantil',			
        'discurso',
        'sermão',	
        'conferências',		
        'artigos de jornal ou revista',	
        'cartas missivas de valor literário', 
        'obra científica',
        'artigo científico',			
        'livro científico',	
        'monografia',
        'TCC',			
        'dissertação',	
        'tese',
        'certidões de nascimento',		
        'certidões de óbito',		
        'divórcio',
        'carteiras de identidade',	
        'carteiras de motorista',
        'carteiras de trabalho',
        'carteiras de vacinação',		
        'atestado de bons',
        'cartas de recomendação',
        'documento escolar',				
        'histórico escolar',	
        'boletins de ocorrência',	
        'diploma', 		
        'decreto',
        'texto de tratado ou convenção',
        'lei',			
        'aproveitamento industrial ou comercial das idéias',
        'decisão judicial',	
        'ato oficial',		
        'contratos em geral',			
        'manual de instruções',	
        'brochura',
        'formulário em branco',		
        'esquema',			
        'plano ou regra para realizar atos mentais',
        'negócio',				
        'calendário',			
        'agenda',
        'cadastro',				
        'procedimento normativo',	
        'regulamento',
        'escultura',			
        'pintura',		
        'arquitetura',
        'filme',			
        'composição musical',		
        'apresentação',
        'artefato decorativo',
        'roteiro',			
        'sistema',	
        'método',		
        'projeto ou conceito matemático',
        'software',	
        'jogos',
        'aplicativos',
    ]

    return Ajuste(vetor)

def SuportePartida ():
    vetor = [
        'Impressão',
        'Manuscrito',
        'Arquivo On-line',	
        'Pen-drive',
        'HD Externo',	
        'HD Sata',		
        'HD IDE',	
        'CD',			
        'DVD',			
        'Blu-ray',
        'Memory Stick Pro Duo',	
        'Memory Stick Duo',		
        'Memory Stick Micro (M2)',	
        'Memory Stick', 
        'VHS',
        'Fita K7',			
        'LP Vinil',	
        'Laserdisc',
        'Rolo de Áudio',			
        'VHS-C',	
        'Hi8',
        'Mini-DV',		
        'Fita de áudio DAT',		
        'Mini Disc MD',
        'XDcam',	
        'Betacam',
        'HDcam',
        'HDV',		
        'DVCam',
        'Umatic',
        'Slide',				
        'Foto',	
        'Negativo',	
        'Microfilme', 		
    ]

    return Ajuste(vetor)

def ArquivoPartida ():
    vetor = [
        '.celtx	',
        '.csv',
        '.doc',	
        '.docx',
        '.odf',	
        '.odg',		
        '.odp',	
        '.ods',			
        '.odt',			
        '.pps',
        '.ppsx',	
        '.ppt',		
        '.pptx',	
        '.rtf', 
        '.sub',
        '.sxc',			
        '.sxd',	
        '.sxi',
        '.sxw',			
        '.txt',	
        '.asp',
        '.aspx',		
        '.c',		
        '.css',
        '.fla',	
        '.htm',
        '.html',
        '.ini',		
        '.java',
        '.jsp',
        '.jsf',				
        '.php',	
        '.xml',	
        'manuscrito', 
        'impresso',
        'jornal',
        'revista',
        '.pdf com senha',
        '.xps',
    ]

    return Ajuste(vetor)

def SuporteChegada ():
    vetor = [
        'On-line(preferencial, e sem custos adicionais)',	
        'Impresso A4(possui os custos de impressão e envio a serem repassados ao cliente)',		
        'Pen-drive(possui os custos da mídia e envio a serem repassados ao cliente)',
        'HD Externo(possui os custos da mídia e envio a serem repassados ao cliente)',
        'CD(possui os custos da mídia e envio a serem repassados ao cliente)	',
        'DVD 	(possui os custos da mídia e envio a serem repassados ao cliente)',	
        'Blu-ray(possui os custos da mídia e envio a serem repassados ao cliente)',
    ]

    return Ajuste(vetor)

def ArquivoChegada ():
    vetor = [
        '.celtx	',
        '.csv',
        '.doc',	
        '.docx',
        '.odf',	
        '.odg',		
        '.odp',	
        '.ods',			
        '.odt',			
        '.pps',
        '.ppsx',	
        '.ppt',		
        '.pptx',	
        '.rtf', 
        '.sub',
        '.sxc',			
        '.sxd',	
        '.sxi',
        '.sxw',			
        '.txt',	
        '.asp',
        '.aspx',		
        '.c',		
        '.css',
        '.fla',	
        '.htm',
        '.html',
        '.ini',		
        '.java',
        '.jsp',
        '.jsf',				
        '.php',	
        '.xml',	
        '.pdf',
        '.txt',
        '.xps',
    ]

    return Ajuste(vetor)

def ModoEntrega ():
    vetor = [
        'E-mail (preferencial, e sem custo)',	
        'Correio registrado(possui os custos de envio a serem repassados ao cliente)',		
    ]

    return Ajuste(vetor)

def RegimeEnsino():
    vetor = [
        'Regime presencial',	
        'Ensino à distância via internet (EaD / OnLine)',		
        'Regime semipresencial (Parte presencial e parte EaD / OnLine)',	
    ]

    return Ajuste(vetor)

def Convenio():
    vetor = [
        'Não',
        'Sim',	   		
    ]

    return Ajuste(vetor)

def NivelAluno():
    vetor = [
        'Pré Iniciante (Pré-A1)',
        'Iniciante (A1)',
        'Falante básico (A2)',
        'Intermediário (B1)',
        'Falante independente (B2)',
        'Proficiência operativa eficaz (C1)',
        'Domínio pleno (C2)',	
    ]
    return Ajuste(vetor)

def PeriodicidadeAula():
    vetor = [
        'Todos os dias da semana (segunda a sexta-feira);',	
        'Todas as segundas, terças e quartas-feiras;',
        'Todas as segundas e quartas-feiras;',	
        'Todas as terças e quintas-feiras;',
        'Todas as quartas e sextas-feiras;',	
        'Todas as quartas, quintas e sextas-feiras;',	
        'Todas as quintas, sextas esábados;',	
        'Todas as segundas, quartas e sextas-feiras; ',
        'Todas as sextas e sábados; ',	
        'Apenas no sábado;',
        'Apenas no domingo;',	
        'Apenas nos fins de semana (sábado e domingo);',		
    ]

    return Ajuste(vetor)

def RepeticaoCurso():
    vetor = [
        'sem repetição',	
        'diariamente',
        'todos os dias da semana (segunda a sexta-feira);',	
        'somente nos fins de semana (sábados e domingos); ',
        'todas as segundas, quartas e sextas-feiras; ',	
        'Todas as quartas, quintas e sextas-feiras;',	
        'Todas as quintas, sextas e sábados;',	
        'Todas as segundas, quartas e sextas-feiras; ',
        'todas as terças e quintas-feiras;',	
        'semanal',
        'mensal',	
        'bimensal',
        'trimestral',	
        'semestral',
        'anual',	
    ]

    return Ajuste(vetor)

def TipoCurso():

    vetor =[
        "Aulas em Turma Regular",
        "Aulas Particulares",
		"In Company",
	]

    return Ajuste(vetor)

def Investimento():
    
    vetor =[
        'A partir de R$ 5.000,00, com pagamento à vista;',
        'A partir de R$ 17.000,00, com pagamento à vista;',
        'De R$ 97.000,00 a R$ 273.000,00 (total estimado), com pagamento à vista.',
	]

    return Ajuste(vetor)

def Capital():
    
    vetor =[
        'Ao menos R$ 2.000,00;' ,
        'Ao menos R$ 10.000,00;' ,
        'De R$ 20.000,00 a R$ 28.000,00.',
	]

    return Ajuste(vetor)

def Area():
    
    vetor =[
		'Apenas o espaço disponível em minha residência;',
        'Entre 30 e 149 m²;',
        'Acima de 150 m²',

	]

    return Ajuste(vetor)

def Imovel():
    
    vetor =[
		'Sim;',
        'Não, o imóvel é alugado;',
        'Não possui nenhum imóvel.',
        'Há sublocação de imóvel?',
	]

    return Ajuste(vetor)

def Zona():
    
    vetor =[
	    'Não. Podem existir ilimitados franqueados por bairro;',
        'Sim, com limite de até três unidades desse tipo de franquia por bairro — equidistantes ao menos 1 km;',
        'Sim, exclusividade de uma unidade desse tipo de franquia por bairro.',
	]

    return Ajuste(vetor)

def Func():
    
    vetor =[
		'Nenhum, pretendo gerir sozinho minha franquia;',
        'Pretendo administrar e dar as aulas ou ter até 1 funcionário(a);',
        'Necessito possuir a partir de 4 funcionários(as).',
	]

    return Ajuste(vetor)

def UTC():
    
    vetor =[]
    for i in range(1,13):
        vetor.append('UTC+' +  str(i))
        vetor.append('UTC-' +  str(i))

    return Ajuste(vetor)

def TipoEvento():
    vetor = [
        'Acadêmico', 
        'Aniversário',
        'Aniversário com Banda',
        'Aula',
        'Banda',
        'Boate',
        'Casamento',
        'Casamento com Banda', 
        'Cerimônia',
        'Congresso',
        'Comitê',
        'Convenção', 
        'Coquetel',
        'Desfile',
        'Encontro',
        'Feira', 
        'Festa',
        'Formatura',
        'Fórum', 
        'Gincana',
        'Grupo',
        'Internet', 
        'Palestra',
        'Rádio', 
        'Religioso',
        'Reunião',
        'Seminário', 
        'Show',
        'Teatro',
        'Treinamento',
        'Turismo', 
        'TV',
        'Outro.',
    ]

    return Ajuste(vetor)

def Ambiente():
    vetor = [
        'reunião',		
        'espinha de peixe', 		
        'círculo aberto',			
        'conferência',	
        'blocos,' 		
        'restaurante',			
        'retângulo aberto - formato em “U”',
    ]

    return Ajuste(vetor)

def Mesa():
    vetor = [
        'Não',	
        'Mesa de som com até 9 canais',
        'Mesa de som entre 10 e 15 canais', 
        'Mesa de som entre 16 e 23 canais',
        'Mesa de som entre 24 e 31 canais',
        'Mesa de som entre 32 e 63 canais',
        'Mesa de som acima de 64 canais',
    ]

    return Ajuste(vetor)

def Retorno():
    vetor = [
        'Não', 	
        '1 retorno', 		
        '2 retornos',		
        '4 retornos',		
        '6 retornos',	
    ]

    return Ajuste(vetor)

def SideFill():
    vetor = [
        'Não',	
        'Side-Fill para DJ',
        'Side-Fill para banda',  
    ]

    return Ajuste(vetor)

def Televisor():
    vetor = [
        'Não',	
        '1 televisor LED 42"',	
        '2 televisores LED 42"',	
        '4 televisores LED 42"', 
    ]

    return Ajuste(vetor)

def Projetor():
    vetor = [
        'Não',	
        '1 projetor com tela', 	
        '1 projetor sem tela',
        '2 projetores com tela', 	
        '2 projetores sem tela',
    ]

    return Ajuste(vetor)

def ArquivoPartida2():
    vetor = [
        '.celtx	',
        '.csv',
        '.doc',	
        '.docx',
        '.odf',	
        '.odg',		
        '.odp',	
        '.ods',			
        '.odt',			
        '.pps',
        '.ppsx',	
        '.ppt',		
        '.pptx',	
        '.rtf', 
        '.sub',
        '.sxc',			
        '.sxd',	
        '.sxi',
        '.sxw',			
        '.txt',	
        '.asp',
        '.aspx',		
        '.c',		
        '.css',
        '.fla',	
        '.htm',
        '.html',
        '.ini',		
        '.java',
        '.jsp',
        '.jsf',				
        '.php',	
        '.xml',	
        '.xls',
        '.xlsx',
        '.2bp',	
        '.2bpp',
        '.ai',	
        '.ani',	
        '.aup',	
        '.cdr',	
        '.ccx',	
        '.cdt',	
        '.cmx',	
        '.cur',
        '.dds',	
        '.dib',	
        '.dng',	
        '.emf',	
        '.emz',	
        '.epdf',	
        '.epub',
        '.fh4',	
        '.fh5',	
        '.fh7',
		'.fh8',	
        '.fhc',	
        '.fh',	
        '.gfa',	
        '.hdp',	
        '.ico',	
        '.jxr',	
        '.key',	
        '.msp',	
        '.pdb',
		'.pdd',	
        '.ps',
        '.psb',	
        '.psd',	
        '.rle',	
        '.spl',	
        '.wdp',
		'.wmz',	
        '.xaml',
        'manuscrito', 
        'impresso',
        'jornal',
        'revista',
        '.pdf com senha',
        '.xps',
    ]

    return Ajuste(vetor)

def ArquivoChegada2():
    vetor = [
        '.celtx',
        '.csv',
        '.doc',	
        '.docx',
        '.odf',	
        '.odg',		
        '.odp',	
        '.ods',			
        '.odt',			
        '.pps',
        '.ppsx',	
        '.ppt',		
        '.pptx',	
        '.rtf', 
        '.sub',
        '.sxc',			
        '.sxd',	
        '.sxi',
        '.sxw',			
        '.txt',	
        '.asp',
        '.aspx',		
        '.c',		
        '.css',
        '.fla',	
        '.htm',
        '.html',
        '.ini',		
        '.java',
        '.jsp',
        '.jsf',				
        '.php',	
        '.xml',	
        '.xls',
        '.xlsx',
        '.2bp',	
        '.2bpp',
        '.ai',	
        '.ani',	
        '.aup',	
        '.cdr',	
        '.ccx',	
        '.cdt',	
        '.cmx',	
        '.cur',
        '.dds',	
        '.dib',	
        '.dng',	
        '.emf',	
        '.emz',	
        '.epdf',	
        '.epub',
        '.fh4',	
        '.fh5',	
        '.fh7',
		'.fh8',	
        '.fhc',	
        '.fh',	
        '.gfa',	
        '.hdp',	
        '.ico',	
        '.jxr',	
        '.key',	
        '.msp',	
        '.pdb',
		'.pdd',	
        '.ps',
        '.psb',	
        '.psd',	
        '.rle',	
        '.spl',	
        '.wdp',
		'.wmz',	
        '.xaml',
        '.xps',
    ]

    return Ajuste(vetor)

def Profossionais():
    vetor = [
        'negros',	
        'pardos',
        'indígenas', 
        'asiáticos',
    ]
    return Ajuste(vetor)

def Validade():
    vetor = [
        '7 dias',	
        '30 dias',
        '45 dias', 
        '60 dias',
    ]
    return Ajuste(vetor)

def Auricular():
    vetor = [
        '16',
        '32',
        '34',
        '48',
        '55',
        '64',
        '68',
        '80',
        '96',
        '102',
        '110',
        '112',
        '128',
        '136',
        '144',
        '160',
        '165',
        '170',
        '176',
        '192',
        '204',
        '208',
        '220',
        '224',
        '238',
        '240',
        '256',
        '272',
        '272',
        '275',
        '288',
        '304',
        '306',
        '320',
        '330',
        '336',
        '340',
        '352',
        '368',
        '374',
        '384',
        '385',
        '400',
        '408',
        '416',
        '432',
        '440',
        '442',
        '448',
        '464',
        '476',
        '480',
        '495',
        '496',
        '510',
        '512',
        '528',
        '544',
        '544',
        '550',
        '560',
        '576',
        '578',
        '592',
        '605',
        '608',
        '612',
        '624',
        '640',
        '646',
        '656',
        '660',
        '672',
        '680',
        '688',
        '704',
        '714',
        '715',
        '720',
        '736',
        '748',
        '752',
        '768',
        '770',
        '782',
        '784',
        '800',
        '816',
        '816',
        '825',
        '832',
        '848',
        '850',
        '864',
        '880',
        '880',
        '884',
        '896',
        '912',
        '918',
        '928',
        '935',
        '944',
        '952',
        '960',
        '976',
        '986',
        '990',
        '992',
        '1008',
        '1020',
        '1045',
    ]
    return Ajuste(vetor)

def Faixaetaria():
    vetor = [
        'Adolescentes 15+ (entre 15 e 17 anos)',
        'Adultos 18+ (a partir dos 18 anos)',
        'Pré-adolescentes 11+ (entre 11 e 14 anos)',
        'Crianças 6+ (entre 6 e 10 anos)',
        'Crianças 3+ (entre 3 e 5 anos)',
        'Terceira idade 60+ (a partir dos 60)',
    ]
    return Ajuste(vetor)

def Unidade():
    vetor = [
        'Unidade Vilar dos Teles',
    ]
    return Ajuste(vetor)

def ComoConheceu():
    vetor = [
        'Associações ou rede de profissionais de serviços linguísticos',
        'E-mail marketing',
        'Redes sociais (Facebook, Instagram, Twitter, Linkedin, ...)',
        'Marketing digital (buscadores, telelistas.net, banner em sites)',
        'Cadastros governamentais (Cadastur, UN, JUCERJA)', 
        'Grupos e fóruns de discussão',
        'Material de divulgação (cartaz A3, propaganda impressa, folder, envelope, CD, brinde, cartão de visita)',
        'Veículos de comunicação - Midia impressa (jornais; revistas, ...)',
        'Veículos de comunicação - Mídia sonora (rádios; podcasts, ...)',
        'Veículos de comunicação - Mídia audiovisual (TV; YouTube, ...)',
        'Carro adesivado ou carro de som',
        'Midiaexterior (outdoor, busdoor, relógio de rua)',
        'Distribuição de panfletos',
        'Empresa parceira',
        'Cartão pré-pago',
        'Evento (feira, congresso)',
        'Indicação de amigo(a)',
    ]
    return Ajuste(vetor)

def Linguas():
    linguas = list(models.Linguas.objects.all())
    return Ajuste(linguas)

def TipoClausula():
    vetor = [
        'Qualificação das partes',
        'Considerações iniciais',
        'Objeto do contrato',
        'Forma e condições de remuneração',
        'Prazo de duração',
        'Cláusula resolutiva',
        'Acordo de confidencialidade',
        'Propriedade intelectual',
        'Direitos e deveres',
        'Condições gerais',
        'Formas de extinção e rescisão contratual',
        'Forma de solução de conflitos',
        'Foro',
        'Assinaturas'
    ]
    return Ajuste(vetor)

def PosicaoClausula():
    vetor = [
        'No início (O Instant posicionará esta cláusula no início de um contrato)',
        'Após o título (O Instant posicionará esta cláusula após o texto do cabeçalho no registro do contrato)', 
        'Após o corpo (O Instant posicionará esta cláusula após o corpo no registro do contrato)',
        'Após as especificações (O Instant posicionará esta cláusula após as especificações do contrato)',
        'No fim (O Instant posicionará esta cláusula no final, após o texto do rodapé no registro do contrato)',
    ]
    return Ajuste(vetor)

def TipoContrato():
    vetor = [
        'Contrato',
        'Aditamento',
        'Anexo',
        'Ata',
        'Atestado',
        'Arras',
        'Autorização',
        'Auto',
        'Aviso',
        'Carta',
        'Comprovante',
        'Comunicado',
        'Comodato',
        'Convênio',
        'Convite',
        'Corretagem',
        'Declaração',
        'Distrato',
        'Edital',
        'Estatuto',
        'Franqueamento',
        'Justificativa',
        'Memorando',
        'Nota',
        'Notificação',
        'Ofício',
        'Parecer',
        'Plano',
        'Politica',
        'Procuração',
        'Profissional',
        'Proposta',
        'Recibo',
        'Recurso',
        'Requerimento',
        'Solicitação',
        'Sorteio',
        'Tabela',
        'Termo',
    ]
    return Ajuste(vetor)

def TituloContrato():
    vetor = [  
        'Prestação de Serviços', 
        'Locação de Imóvel', 
        'Social', 
        'Franqueado - Home-Based', 
        'Franqueado - Escritório de Tradução e Interpretação', 
        'Franqueado - Escola de Idiomas', 
        'Licenciado - Plano Intro', 
        'Licenciado - Plano Liberal', 
        'Licenciado - Plano Serviço',
        'Licenciado - Plano Curso', 
        'Licenciado - Plano Completo',  
        'Profissional - Candidato', 
        'Profissional - Colaborador', 
        'Técnico-Comercial',
        'Autorização', 
        'Experiência',
        'Vistoria',
        'Locação de Equipamentos',
    ]
    return Ajuste(vetor)

def SubTituloServico():
    vetor = [
        'Tradução com Revisão de Texto',
        'Tradução Automática com Revisão de Texto',
        'Tradução Juramentada',
        'Localização de Software, Aplicativo ou Site',
        'Interpretação Simultânea',
        'Interpretação Consecutiva',
        'Interpretação em Acompanhamento',
        'Interpretação Sussurrada',
        'Interpretação Remota',
        'Dupla Interpretação',
        'Interpretação em Língua Brasileira de Sinais (Libras)',
        'Curso de Inglês',
        'Curso de Espanhol',
        'Curso de Francês',
        'Curso de Alemão',
        'Curso de Italiano',
        'Curso de Japonês',
        'Curso de Holandês',
        'Curso de Chinês',
        'Curso de Árabe',
        'Curso de Coreano',
        'Curso de Português',
        'Curso de Português para Estrangeiros',
        'Curso de Redação de Documentos Oficiais',
        'Curso de Língua Brasileira de Sinais (Libras)',
        'Curso de Inglês para Concursos, Enem e Vestibulares',
        'Curso de Espanhol para Concursos, Enem e Vestibulares',
        'Curso de Português para Concursos, Enem e Vestibulares',
        'Curso de Redação para Concursos, Enem e Vestibulares'
        'Curso de Inglês para Advogados',
        'Curso de Inglês para Forças Armadas',
        'Curso de Inglês para Lojistas, Comerciantes e MEI',
        'Curso de Inglês para Pedreiros',
        'Curso de Inglês para Profissionais de Enfermagem',
        'Curso de Inglês para Recepcionistas e Garçons',
        'Curso de Inglês para Transportadoras e Logística',
        'Curso de Inglês para Turismo e Hotelaria',
        'Curso de Espanhol para Advogados',
        'Curso de Espanhol para Lojistas, Comerciantes e MEI',
        'Curso de Espanhol para Turismo e Hotelaria',
        'Conversação em Inglês',
        'Conversação em Espanhol',
        'Intercâmbio na Argentina',
        'Intercâmbio nos Estados Unidos',
        'Inglês - Cambridge English Proficiency - CPE',
        'Inglês - Graduate Management Admission Test - GMAT',
        'Inglês - International English Language Testing System - IELTS',
        'Inglês - Test of English as a Foreign Language - TOEFL',
        'Inglês - Test of English for International Communication - TOEIC',
        'Espanhol - Diploma de Español como Lengua Extranjera - DELE',
        'Curso de Audiodescrição',
        'Curso de Auditoria Linguística',
        'Curso de Closed Caption',
        'Curso de Consultoria Linguística',
        'Curso de Diagramação',
        'Curso de Digitação',
        'Curso de Dublagem para Atores',
        'Curso de Edição de Áudio Digital',
        'Curso de Estenotipia',
        'Curso de Ferramentas de Apoio a Tradução',
        'Curso de Legendagem',
        'Curso de Locução',
        'Curso de Oratória',
        'Curso de Transcrição de Áudio',
        'Transmissor',
        'Cabine acústica',
        'Central de intérprete',
        'Estojo carregador com até 34 receptores',
        'Estojo carregador com até 55 receptores',
        'Rádio receptor com até 3 canais',
        'Microfone para presidente tipo gooseneck',
        'Microfone para participante tipo gooseneck',
        'Processador para até 100 microfones',
        'Microfone de punho para visitação',
        'Microfone headset para visitação',
        'Rádio receptor de 3 canais para visitação',
        'Estojo carregador com até 16 receptores',
        'Fone auricular',
        'Caixa acústica',
        'Microfone de punho sem fio',
        'Pedestal de caixa e emissor de infravermelho',
        'Mixer Amplificado de até 8 canais',
        'Mesa de som com até 9 canais',
        'Mesa de som entre 10 e 15 canais',
        'Mesa de som entre 16 e 23 canais',
        'Mesa de som entre 24 e 31 canais',
        'Mesa de som entre 32 e 63 canais',
        'Mesa de som acima de 64 canais',
        'Acesso a internet (Por Hora)',
        'Backup em DVD (Até 100 Fotos)',
        'Conversão de Imagem e PDF para DOC',
        'Cópia Colorida (Por Unidade)',
        'Cópia Preto e Branco (Por Unidade)',
        'Copiar arquivos para celular, pendrive, MP3 e etc. (Por Dispositivo)',
        'Criação de contas de E-mail, Facebook, Twitter e etc. (Por Domínio)',
        'Envio de fax 0800 ou ligação a cobrar (Por Página)',
        'Envio de fax DDD 21 RJ (Por Página)',
        'Envio de fax demais regiões (Por Página)',
        'Gravação de CD/DVD (Documentos, fotos, áudios e vídeos)',
        'Impressão Colorida de Documentos por Página (Sem imagens)',
        'Impressão Colorida de Imagens e/ou Fotos (A4 Fotográfico) por Página',
        'Impressão Colorida de Imagens e/ou Fotos (A4 Normal) por Página',
        'Impressão de Boleto Atualizado e/ou Emissão de Fatura e/ou Duplicata.',
        'Impressão de Certidão Nada Consta',
        'Impressão de Declarações e/ou Ofícios e/ou Cartas',
        'Impressão Preto e Branco - 01 à 05 Páginas',
        'Impressão Preto e Branco - 06 à 20 Páginas',
        'Impressão Preto e Branco - 21 à 30 Páginas',
        'Impressão Preto e Branco - 31 à 50 Páginas',
        'Impressão Preto e Branco - 51 Páginas acima',
        'Recebimento de Fax (Por Página)',
        'Uso do Scanner (Por Página)',
    ]
    return Ajuste(vetor)

def SubTituloCargo():
    vetor = [
        'Coordenador de Serviços de Tradução',
        'Gerente de Projetos de Tradução',
        'Tradutor',
        'Tradutor Juramentado',
        'Revisor de Texto',
        'Programador',
        'Coordenador de Serviços de Interpretação',
        'Gerente de Projetos de Interpretação',
        'Intérprete-Coordenador',
        'Intérprete',
        'Intérprete de Língua de Sinais',
        'Recepcionista',
        'Assistente de Som',
        'Montador',
        'Motorista',
        'Coordenador de Serviços Adicionais',
        'Gerente de Projetos de Serviços Adicionais',
        'Audiodescritor',
        'Transcritor de Áudio',
        'Redator',
        'Legendador',
        'Revisor de Texto',
        'Editor de Vídeo',
        'Digitador',
        'Taquígrafo',
        'Estenotipista',
        'Diagramador',
        'Consultor Linguístico',
        'Auditor Linguístico',
        'Linguista',
        'Locutor',
        'Dublador',
        'Filólogo',
        'Monitor de Braille',
        'Revisor de Texto em Braille',
        'Transcritor de Texto em Braille',
        'Coordenador Administrativo',
        'Administrador',
        'Auxiliar Financeiro',
        'Auxiliar de Recursos Humanos',
        'Auxiliar de Assistência Técnica',
        'Ouvidor',
        'Coordenador de Cursos',
        'Secretário Acadêmico',
        'Professor de Língua Estrangeira',
        'Professor de Língua Portuguesa',
        'Professor de Tradução',
        'Professor de Revisão de Texto',
        'Professor de Interpretação',
        'Professor de Programação',
        'Professor de Redação',
        'Professor de Edição de Áudio Digital',
        'Professor de Redação de Documentos Oficiais',
        'Professor de Estenotipia',
        'Professor de Ferramentas de Apoio a Tradução',
        'Professor de Auditoria Linguística',
        'Professor de Língua Portuguesa para Estrangeiros',
        'Professor de Consultoria Linguística',
        'Professor de Digitação',
        'Professor de Closed Caption',
        'Professor de Audiodescrição',
        'Professor de Legendagem',
        'Professor de Transcrição de Áudio',
        'Professor de Diagramação',
        'Professor de Oratória',
        'Professor de Dublagem para Atores',
        'Professor de Locução',
        'Professor de Língua de Sinais',
        'Professor de Braille',
        'Professor de Curso Preparatório para Exame de Proficiência em Línguas',
    ]
    return Ajuste(vetor)

def Subtipo():
    vetor = [  
        'de Autônomo - Não Residente na Localidade da Prestação do Serviço',
        'de Autônomo - Residente na Localidade da Prestação do Serviço',
        'de Estágio',
        'Baseado no Código Civil - CC',
        'Baseado no Código de Defesa do Consumidor - CDC',
        'Baseado na Consolidação das Leis do Trabalho - CLT',
    ]
    return Ajuste(vetor)

def Outorga():
    vetor = [  
        'Profissional - Candidato',
        'Profissional - Colaborador',
        'Licenciado - Plano Intro',
        'Licenciado - Plano Liberal',
        'Licenciado - Plano Serviço',
        'Licenciado - Plano Curso',
        'Licenciado - Plano Completo',
        'Franqueado - Home-Based',
        'Franqueado - Escritório de Tradução e Interpretação',
        'Franqueado - Escola de Idiomas',
        'Cliente',
        'Afiliado',
        'Associação',
        'Administrador',
        'Super Administrador',
    ]
    return Ajuste(vetor)

