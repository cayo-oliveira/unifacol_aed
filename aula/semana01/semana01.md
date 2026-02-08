Roteiro de Aula (3 Horas) – Semana 1: Do Caos à Clareza
1.0 Abertura e O Gancho (19:00 – 19:20)
1.1 Boas-vindas e a Grande Ideia
Boa noite a todos! Sei que vocês tiveram um dia longo de trabalho, mas as próximas três horas serão o divisor de águas na carreira de vocês como profissionais de Sistemas de Informação.Eu serei o mentor de vocês nesta jornada. O nosso semestre será guiado por uma única e poderosa ideia central, a nossa  "Big Idea" :  "Dados brutos são apenas ruído; o seu valor no mercado será medido pela sua capacidade de extrair deles uma história que force uma decisão" . O objetivo deste curso é exatamente este: mover vocês do "apenas código" para o "insight visual".Para começar, deixo uma provocação:  "Por que algumas empresas sobrevivem a crises e outras não?" . A resposta raramente está na quantidade de dados que elas possuem, mas sim na habilidade de interrogá-los corretamente, de fazer as perguntas certas e entender as respostas que eles oferecem.
1.2 A Diferença Crucial: Análise Exploratória vs. Análise Explanativa
Antes de construirmos qualquer visualização, precisamos entender o material com que estamos trabalhando. Este é o domínio da Análise Exploratória de Dados (AED), um passo preliminar essencial, como nos ensina  Peter Bruce . Nosso foco será em  dados retangulares  — o formato que vocês encontram em planilhas e tabelas SQL, onde cada linha representa um registro e cada coluna, uma variável.Mas o que isso significa na prática? Pensem da seguinte forma: para dominar os dados, precisamos dominar dois modos de pensamento distintos. A especialista Cole Nussbaumer nos ajuda a entender essa diferença fundamental com uma analogia perfeita: a Análise Exploratória é o trabalho na cozinha, e a Análise Explanativa é o jantar que servimos aos convidados.| Conceito | Análise Exploratória (A Cozinha) | Análise Explanativa (O Jantar) || ------ | ------ | ------ || Metáfora | "Virar 100 pedras para encontrar 1 ou 2 pedras preciosas." | "Mostrar essas joias para o seu chefe." || Objetivo | Entender os dados, encontrar padrões, anomalias e insights escondidos. | Comunicar os insights encontrados de forma clara e persuasiva para uma audiência. || Quem Faz | O analista, o cientista de dados. | O analista apresentando para gestores, diretores, clientes. || Ferramenta Principal | Python (Jupyter, Pandas) | Tableau, Power BI, Apresentações || Referência | Cole Nussbaumer | Cole Nussbaumer |
Agora que entendemos a diferença entre encontrar e apresentar uma joia, vamos ver como nosso semestre está estruturado para dominar ambas as artes.
2.0 O Mapa da Jornada: Apresentação do Plano de Ensino (19:20 – 19:45)
2.1 Visão Geral do Semestre
Toda jornada bem-sucedida começa com um mapa claro. Nosso curso foi desenhado para ser uma experiência prática e intuitiva, dividida em duas grandes unidades complementares que construirão progressivamente suas competências.A estrutura geral é a seguinte:| Unidade | Período | Foco Principal | Referência Base || ------ | ------ | ------ | ------ || I | Semanas 1-8 | Estatística Prática, AED e Python | Peter Bruce || II | Semanas 9-16 | Storytelling, Tableau e Visualização Interativa | Nancy Duarte e Artigos Tableau |
Para garantir que o aprendizado seja contínuo e aplicado, nossa avaliação será composta por:
Projetos Quinzenais (40%):  Aplicações práticas dos conceitos vistos em aula.
Avaliação Final (60%):  Composta por uma prova e um projeto prático final, unindo todas as habilidades que vocês desenvolverão.
2.2 Cronograma Detalhado
Este é o nosso caminho, semana a semana:
Semana 1:  O "Gosto" dos Dados e a Exploração
Semana 2:  Pesquisa e Aplicação Prática (Pré-Carnaval)
Semana 3:  Elementos de dados estruturados e Estimativas de Localização
Semana 4:  Estimativas de Variabilidade e  Projeto 1
Semana 5:  Explorando a Distribuição dos Dados
Semana 6:  Correlação e Variáveis Categóricas +  Projeto 2
Semana 7:  Distribuições de Amostragem e Viés
Semana 8:  Experimentos Estatísticos e Testes de Significância (A/B Testing)
Semana 9:  Introdução ao Storytelling: Análise Exploratória vs. Explanativa
Semana 10:  O Mapa de Empatia da Audiência e a "Big Idea" +  Projeto 3
Semana 11:  Estruturando o Conteúdo: O "Gancho" e o Contraste
Semana 12:  Princípios de Design Visual (Simplicidade e Teste do Relance) +  Projeto 4
Semana 13:  Tableau Avançado: Filtros, Parâmetros e Interatividade
Semana 14:  Construindo Dashboards que contam histórias +  Projeto 5
Semana 15:  Entrega Final: Preparação e Postura de Apresentação
Semana 16:   Apresentação dos Projetos FinaisCom nosso mapa em mãos, é hora de sujar as mãos e entrar na "cozinha" dos dados com nossa primeira ferramenta: Python.
3.0 Mão na Massa: O Processo ETL com Python (19:45 – 20:45)
3.1 A "Cozinha" dos Dados: Por que Python e Jupyter?
Agora entramos na fase do 'caos' controlado, o ponto de partida da nossa jornada rumo à clareza. Bem-vindos à 'cozinha', o coração da nossa operação. Lembrem-se desta estatística de mercado crucial: um cientista de dados gasta 80% do tempo aqui. Se a 'cozinha' está suja, o prato final (o gráfico) será intragável.O processo que vamos executar é conhecido como ETL (Extract, Transform, Load), ou Extrair, Transformar e Carregar. Nosso fluxo de trabalho hoje será este:Dado Bruto (Netflix Dataset) -> Passo 1: Extrair com Pandas -> Passo 2: Transformar/Limpar -> Passo 3: Carregar como CSV limpo -> Dado Pronto para Visualização
3.2 Demonstração Prática: Limpando o Dataset da Netflix
Abram seus laptops e vamos trabalhar juntos. Nosso cenário de hoje é um dataset popular da Netflix.
Passo 1: Leitura e Interrogatório (Extract)  Vamos usar a biblioteca pandas para ler o arquivo CSV e dar uma primeira olhada na estrutura dos dados, entendendo as colunas, os tipos de dados e os valores ausentes.
Passo 2: Limpeza (Transform)  Esta é a etapa crítica. Precisamos tratar os dados para que ferramentas de visualização como o Tableau não "engasguem". Hoje, faremos duas ações de limpeza essenciais:
A coluna de data de lançamento está formatada como texto. Vamos transformá-la em um objeto datetime para que possamos analisar tendências ao longo do tempo.
Vamos remover colunas que não agregam valor ao nosso storytelling inicial, como IDs complexos ou notas internas que não dizem nada à nossa audiência.
Passo 3: Exportação (Load)  Com os dados limpos e estruturados, vamos exportar o resultado para um novo arquivo, que chamaremos de netflix_limpo.csv. Este é o nosso ingrediente preparado, pronto para a próxima etapa.Agora que nosso ingrediente principal está limpo e preparado, vamos sair da cozinha e montar o prato final com o Tableau.
Intervalo para Café e Networking (20:45 – 21:00)
4.0 Da Clareza à Persuasão: Visualização com Tableau (21:00 – 21:45)
4.1 Apresentando o Prato Final: O Poder do Tableau
Se a etapa anterior foi sobre sair do caos, esta é sobre fabricar a clareza. Agora que preparamos nossos ingredientes na 'cozinha' do Python, é hora de ir para a 'sala de jantar'. O Tableau é a nossa louça fina, a ferramenta que usamos para apresentar o prato final de forma irresistível. Abram o Tableau e vamos conectar nosso arquivo netflix_limpo.csv.Observem a agilidade: simplesmente arrastem a coluna "País" para o centro da tela. O Tableau interpreta automaticamente que se trata de dados geográficos e, em um instante, gera um mapa. Isso demonstra o poder da ferramenta para "sentir" os dados e nos dar respostas visuais rápidas, sem a necessidade de escrever uma única linha de código.
4.2 O Teste dos Três Segundos: Design e Simplicidade
Agora, uma das lições mais importantes que vocês levarão deste curso, e que fará toda a diferença na carreira de vocês. Quero que internalizem esta regra de ouro do design de informação, criada pela mestre Nancy Duarte: o  The Glance Test™  (ou Teste do Relance).A regra é simples:  se o seu usuário não entender a mensagem principal do seu gráfico em três segundos, o seu visual falhou .Para passar neste teste, precisamos adotar o princípio de que "menos é mais". Vamos remover todo o "lixo visual" — grades desnecessárias, cores conflitantes, eixos sobrecarregados. Ao simplificar o visual, permitimos que o insight "respire" e que a audiência foque imediatamente no que é mais importante.Dominar esta técnica de clareza visual é o que separa um analista comum de um profissional que realmente influencia decisões. Vamos ver como isso se traduz em sua carreira.
5.0 O Futuro e a Próxima Etapa (21:45 – 22:00)
5.1 O "New Bliss": O Poder de Dominar os Dados
Mas qual é o objetivo final de tudo isso? Onde essa habilidade realmente nos leva? Quero que vocês visualizem um cenário futuro. Imaginem-se em uma reunião de diretoria. Enquanto todos discutem com base em opiniões e achismos, você abre um dashboard interativo e mostra, com base em evidências, exatamente onde a empresa está perdendo dinheiro. A sala fica em silêncio. A decisão é tomada com base na sua análise.Esse é o  "New Bliss"  (a Nova Felicidade) que esta disciplina oferece: a segurança, a credibilidade e o poder de quem domina os dados.
5.2 Chamada para Ação e Tarefa da Próxima Semana
O conhecimento que adquirimos hoje é volátil se não for praticado. Portanto, não esperem a próxima aula para abrir o Jupyter ou o Tableau novamente. A prática contínua é o que transformará a informação em habilidade.Para a próxima semana, vocês farão uma  Apresentação Relâmpago  de 2 minutos, valendo 0.5 ponto. A tarefa é a seguinte:
Escolha um Tema:  Utilizem um dos 20 links de datasets do Kaggle que foram fornecidos (Vendas de Videogames, Spotify, Airbnb, etc.).
Faça o ETL:  No Jupyter, limpem pelo menos uma coluna e filtrem os dados para um recorte específico (ex: apenas artistas brasileiros no dataset do Spotify).
Crie um Infográfico:  No Tableau, gerem  três visuais  que respondam a uma pergunta de negócio clara (ex: "Qual o gênero de filme mais lucrativo?").
Critério de Sucesso:  O visual final deve passar no  Teste do Relance . Usem cores de forma consistente e garantam que cada gráfico tenha uma "Big Idea" evidente.Lembrem-se: a apresentação de vocês deve ter um  gancho  forte no início e terminar com uma  chamada para ação  clara no final.
5.3 Dica Final e Encerramento
Aqui vai uma dica prática para maximizar o engajamento e o impacto: ao escolher seu tema no Kaggle, pense em um desafio ou problema do seu trabalho atual. Como você poderia aplicar essa mesma lógica de limpeza e visualização para analisar dados da sua empresa e, quem sabe, impressionar seu gestor já amanhã?Nos vemos na semana que vem para transformar esses dados em histórias!

