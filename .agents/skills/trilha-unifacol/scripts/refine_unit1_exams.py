#!/usr/bin/env python3
"""Revisa editorialmente a Prova I sem criar itens fora dos cadernos."""

from __future__ import annotations

import argparse
import csv
import importlib.util
import json
import random
import re
import sys
from pathlib import Path


SELECTIONS = {
    "TOP": ["TOP-C01-D13", "TOP-C02-D15", "TOP-C03-O09", "TOP-C04-O03", "TOP-C05-O01", "TOP-C06-O03", "TOP-C07-O09", "TOP-C08-O03"],
    "IA": ["IA-C01-O05", "IA-C02-O07", "IA-C03-O05", "IA-C04-O03", "IA-C05-O05", "IA-C06-O01", "IA-C02-D11", "IA-C07-D15"],
    "AED": ["AED-C01-O09", "AED-C02-D13", "AED-C03-O05", "AED-C04-O03", "AED-C05-O03", "AED-C06-O09", "AED-C07-D13", "AED-C08-O09"],
}

COVERAGE = {
    "TOP": [
        "SDD, contexto e segurança", "problema, MVP e métodos ágeis", "prototipação e evidência", "arquitetura de software", "contratos e APIs", "arquitetura de dados", "LGPD e governança", "integração da Unidade I",
    ],
    "IA": [
        "universo da IA e evidência", "Estatística I", "Estatística II", "regressão com cálculo e gráfico", "classificação com tabela", "MAE e RMSE", "história dos LLMs", "integração e métricas",
    ],
    "AED": [
        "problema, dor e decisão analítica", "Estatística I", "Estatística II", "gráfico e distorção de eixo", "arquitetura de dados para AED", "dashboard e storytelling", "integração da análise", "decisão sob restrições",
    ],
}

HEADLINES = {
    "TOP-C01-D13": "Caderno de Tecnologia | Quando a recuperação de senha nasce insegura",
    "TOP-C02-D15": "Gestão em foco | Três abordagens, três problemas diferentes",
    "TOP-C03-O09": "Laboratório de Produto | O protótipo mais rápido prova qual mudança funcionou?",
    "TOP-C04-O03": "Plantão de Arquitetura | Uma troca de fornecedor alcançou 27 arquivos",
    "TOP-C05-O01": "Boletim de Engenharia | O contrato sobreviveu à troca do provedor",
    "TOP-C06-O03": "Auditoria de Dados | O indicador perdeu a memória de sua origem",
    "TOP-C07-O09": "Governança em pauta | Quem decide a regra e quem a executa?",
    "TOP-C08-O03": "Especial de Inovação | Um piloto mais rápido, porém ainda não causal",
    "IA-C01-O05": "Ciência sob verificação | Fluência não é evidência de compreensão",
    "IA-C02-O07": "Boletim de Avaliação | A nota final depende dos pesos e da frequência dos erros",
    "IA-C03-O05": "Observatório de Modelos | Solicitações longas concentram mais erros?",
    "IA-C04-O03": "Mercado de Energia | O modelo erra justamente nos dias mais quentes",
    "IA-C05-O05": "Segurança Financeira | Uma previsão confiante e errada custa mais ao modelo",
    "IA-C06-O01": "Operação Elétrica | O erro típico esconde um pico de seis megawatts",
    "IA-C02-D11": "Linha do tempo | De Transformer a modelos integrados a ferramentas",
    "IA-C07-D15": "Indústria conectada | Prever tempo, risco e regimes sem confundir tarefas",
    "AED-C01-O09": "Economia em dados | Receita cresceu, mas o dashboard ainda não explica por quê",
    "AED-C02-D13": "Nota estatística | Quatro equipamentos e dois divisores possíveis",
    "AED-C03-O05": "Central de atendimento | Urgência e reabertura caminham de forma independente?",
    "AED-C04-O03": "Leitura crítica | Dois pontos percentuais viraram um salto visual",
    "AED-C05-O03": "Rastreabilidade | Um evento sem origem não pode ser reprocessado com confiança",
    "AED-C06-O09": "Sala da diretoria | Dezesseis gráficos antes de revelar a decisão",
    "AED-C07-D13": "Relatório integrado | Da tabela imperfeita à recomendação contestável",
    "AED-C08-O09": "Decisão responsável | Pontualidade não pode compensar risco de acidente",
}

LEADS = {
    "TOP-C01-D13": "Uma revisão interna constatou que a entrega tecnicamente concluída falhou em requisitos elementares de segurança e privacidade. A chefia solicita um contrato verificável antes de autorizar nova implementação.",
    "TOP-C02-D15": "Em uma reunião de planejamento, a equipe tratou Lean Startup, Scrum e Kanban como produtos concorrentes. A direção quer saber como combiná-los sem transformar cerimônias e quadros em finalidade.",
    "TOP-C03-O09": "O relatório do teste atribuiu toda a redução do tempo a uma única alteração de rótulo. Entretanto, a versão avaliada modificou simultaneamente conteúdo, ordem, cor e latência percebida.",
    "TOP-C04-O03": "O chamado de manutenção parecia simples: substituir o SDK usado pelo assistente. O impacto espalhado pela interface, pelos jobs e pelos relatórios revelou uma decisão arquitetural anterior.",
    "TOP-C05-O01": "A troca do fornecedor ocorreu sem modificar os campos consumidos pelos clientes. O episódio permite separar aquilo que o serviço promete da tecnologia escolhida para cumprir a promessa.",
    "TOP-C06-O03": "Depois de uma correção retroativa, a equipe não conseguiu localizar os eventos atingidos. O dado havia chegado ao painel, mas os metadados que sustentariam auditoria e reprocessamento foram descartados.",
    "TOP-C07-O09": "A organização aprovou uma regra corporativa para cliente ativo e distribuiu responsabilidades. A análise deve distinguir o direito de decidir da execução diária das políticas e controles.",
    "TOP-C08-O03": "Uma nota executiva celebrou simultaneamente maior acerto e menor tempo. Antes da expansão, porém, a direção exige separar sinal promissor de conclusão causal.",
    "IA-C01-O05": "A demonstração comercial impressionou pela naturalidade das respostas, mas não apresentou amostragem, casos críticos nem consequência dos erros. O parecer deve converter espetáculo em evidência verificável.",
    "IA-C02-O07": "Um comitê compara o desempenho de um modelo em duas tarefas com importância desigual. No mesmo relatório, precisa identificar quais categorias de erro aparecem com maior frequência.",
    "IA-C03-O05": "Uma equipe de qualidade percebeu que respostas mais longas pareciam falhar mais. Para verificar a impressão, registrou probabilidades marginais e a ocorrência conjunta em um conjunto previamente definido.",
    "IA-C04-O03": "Uma reportagem técnica sobre planejamento energético destacou que a previsão média parecia adequada, embora o sistema subestimasse consumo nos dias críticos. A decisão depende do resíduo e de seu padrão visual.",
    "IA-C05-O05": "Dois alertas negativos receberam probabilidades muito diferentes para a classe positiva. O setor de risco quer entender matematicamente por que a confiança equivocada recebe penalidade maior.",
    "IA-C06-O01": "O boletim operacional não aceita uma única métrica de erro: desvios comuns afetam o planejamento, enquanto um pico pode comprometer a reserva de energia. Por isso, MAE e RMSE devem ser lidos conjuntamente.",
    "IA-C02-D11": "Uma coluna de divulgação atribuiu toda a evolução recente dos LLMs ao aumento do número de parâmetros. A equipe acadêmica deverá reconstruir uma narrativa historicamente prudente e propor como testar a alegação.",
    "IA-C07-D15": "A diretoria reuniu três demandas distintas sob o rótulo genérico de inteligência artificial. O plano deve mostrar qual pergunta cada família responde e como custo do erro, validação e monitoramento mudam a decisão.",
    "AED-C01-O09": "O título do painel anuncia crescimento de 12\%, mas não informa se a organização vendeu mais, apenas reajustou preços ou perdeu rentabilidade. A chefia pede evidência antes de renovar a campanha.",
    "AED-C02-D13": "Um relatório técnico circulou com dois valores diferentes para a variância do mesmo conjunto. A divergência não decorre da aritmética, mas da pergunta: descrever as quatro unidades ou inferir sobre outras semelhantes.",
    "AED-C03-O05": "A central suspeita que chamados urgentes retornem com maior frequência. A auditoria exige aplicar o critério de independência, em vez de decidir apenas pela comparação visual das porcentagens.",
    "AED-C04-O03": "Uma manchete interna chamou de crescimento expressivo a passagem de 79\% para 81\%. O gráfico, com eixo truncado, ampliou visualmente uma diferença real de apenas dois pontos percentuais.",
    "AED-C05-O03": "O indicador foi publicado, mas o pipeline não guardou identificador, versão, horários nem origem. Quando a regra mudou, a equipe já não sabia quais registros e consumidores estavam afetados.",
    "AED-C06-O09": "Na reunião mensal, a decisão sobre novos horários apareceu somente depois de uma longa demonstração da ferramenta. O conselho solicitou uma narrativa que ligue contexto, evidência, limite e recomendação.",
    "AED-C07-D13": "Uma área de negócio solicita uma recomendação final, mas os dados apresentam problemas de qualidade, diferenças entre grupos e risco de interpretação causal. A resposta deve tornar o caminho analítico auditável.",
    "AED-C08-O09": "O novo acordo operacional melhorou a pontualidade ao mesmo tempo que elevou acidentes e jornadas. A direção declarou segurança como restrição, e não como indicador que possa ser compensado por uma média favorável.",
}

EXTRA_SUPPORT = {
    "IA-C02-O07": r"""
\begin{DocumentBox}[Quadro editorial --- tarefas e registros observados]
\begin{tabularx}{\textwidth}{@{}Y C C@{}}\toprule
Dimensão & Valor observado & Peso ou repetição\\\midrule
Extração & nota 9 & peso 3\\
Raciocínio com fonte & nota 6 & peso 7\\
Erros & omissão; citação; citação; formato; omissão & frequências observadas\\\bottomrule
\end{tabularx}
\end{DocumentBox}
\LegendaDidatica{O Quadro organiza exatamente as notas, os pesos e os rótulos fornecidos no item}
""",
    "IA-C05-O05": r"""
\begin{DocumentBox}[Tabela de auditoria --- confiança e perda para casos negativos]
\begin{tabularx}{\textwidth}{@{}Y C C C@{}}\toprule
Caso & Rótulo real $y$ & Probabilidade $p$ & Expressão a calcular\\\midrule
Alerta 1 & 0 & 0,9 & $-\ln(1-0{,}9)$\\
Alerta 2 & 0 & 0,2 & $-\ln(1-0{,}2)$\\\bottomrule
\end{tabularx}
\end{DocumentBox}
\LegendaDidatica{A tabela reorganiza os mesmos valores do texto e deve ser usada na comparação das perdas}
""",
    "AED-C04-O03": r"""
\begin{DocumentBox}[Figura editorial --- taxa mensal publicada]
\centering
\begin{tikzpicture}[x=2.1cm,y=.075cm]
\draw[->] (0,0)--(2.6,0) node[right]{mês};
\draw[->] (0,0)--(0,86) node[above]{taxa (\%)};
\foreach \y in {0,20,40,60,80} {\draw (-.05,\y)--(.05,\y) node[left=2pt]{\small \y};}
\fill[disciplinecolor!55] (.45,0) rectangle (1.05,79);
\fill[disciplinecolor!85] (1.45,0) rectangle (2.05,81);
\node[above] at (.75,79) {79\%}; \node[above] at (1.75,81) {81\%};
\node[below] at (.75,0) {anterior}; \node[below] at (1.75,0) {atual};
\end{tikzpicture}
\end{DocumentBox}
\LegendaDidatica{A Figura usa origem zero e representa os mesmos 79\% e 81\% informados no item}
""",
}

CUSTOM_OPTIONS = {
    "IA-C02-O07": [
        "A nota seria 7,5 e o erro modal seria formato; essa leitura usa média simples e escolhe uma categoria com apenas uma ocorrência.",
        "A nota seria $(3\times9+7\times6)/10=6{,}9$ e haveria duas modas, omissão e citação; a interpretação respeita pesos e frequências.",
        "A nota seria 6,9, mas não haveria moda por os rótulos serem textuais; essa conclusão ignora que moda também se aplica a categorias.",
        "A nota seria 7,5 e citação seria a única moda; a leitura abandona os pesos e desconsidera o empate de frequências.",
        "A nota seria $(7\times9+3\times6)/10=8{,}1$ e omissão seria a única moda; a proposta troca os pesos e ignora a frequência de citação.",
    ],
    "IA-C03-O05": [
        "Os eventos seriam independentes porque 0,06 é menor que 0,12; a comparação, porém, não aplica o critério do produto.",
        "Os eventos seriam independentes por receberem nomes diferentes; essa justificativa confunde rótulos com comportamento probabilístico.",
        "Os eventos não seriam independentes, pois $0{,}25\times0{,}12=0{,}03$, diferente da interseção observada de 0,06.",
        "Os eventos seriam mutuamente exclusivos porque a interseção é positiva; a conclusão contradiz a própria definição de exclusão.",
        "Os eventos seriam complementares porque 0,25 e 0,12 somam 0,37; essa soma não é igual a 1 e não caracteriza complemento.",
    ],
    "IA-C04-O03": [
        "O resíduo seria $-45$ MWh e indicaria superestimação; essa opção inverte a ordem $y-\hat y$ declarada no relatório.",
        "O resíduo seria $45$ MWh e indicaria subestimação no calor; o padrão da figura recomenda investigar não linearidade ou variável ausente.",
        "O resíduo seria 885 MWh e provaria perfeição fora do calor; essa conta soma observado e previsto e não mede erro.",
        "O resíduo seria 1,11 MWh e bastaria alterar a unidade; essa razão não corresponde à definição adotada.",
        "O resíduo seria zero porque sinais opostos sempre se anulam; a opção ignora o caso individual e o padrão condicionado à temperatura.",
    ],
    "IA-C05-O05": [
        "As perdas seriam 0,105 e 1,609, tornando o caso de probabilidade 0,2 o mais penalizado; os logaritmos usados não correspondem aos complementos.",
        "As perdas seriam 2,303 e 0,223; portanto, atribuir 0,9 ao evento que não ocorreu produz penalidade muito maior.",
        "As perdas seriam 0,9 e 0,2, iguais às probabilidades; essa leitura elimina o logaritmo da função de perda.",
        "As perdas seriam $-2{,}303$ e $-0{,}223$, e valores negativos seriam desejáveis; a opção esquece o sinal negativo externo à expressão.",
        "As duas perdas seriam iguais a 1 porque os rótulos coincidem; a opção ignora que a confiança prevista também determina a penalidade.",
    ],
    "IA-C06-O01": [
        "O MAE seria 2,5 MW e o RMSE seria $\sqrt{10{,}5}\approx3{,}24$ MW; o pico recebe peso maior no erro quadrático.",
        "O MAE seria 1 MW e o RMSE 10,5 MW; essa leitura cancela sinais e confunde MSE com sua raiz.",
        "O MAE seria 2 MW e o RMSE 2,5 MW; os valores não resultam das quatro diferenças apresentadas.",
        "O MAE seria 10 MW e o RMSE 42 MW; a proposta soma sem dividir pelo número de casos.",
        "O MAE seria 2,5 MW e o RMSE 10,5 MW; a segunda medida permanece na unidade quadrada por não aplicar a raiz.",
    ],
    "AED-C03-O05": [
        "Urgência e reabertura seriam independentes porque 0,06 é menor que 0,14; essa comparação não testa o produto das marginais.",
        "Os eventos seriam independentes porque descrevem categorias diferentes; a natureza dos nomes não determina independência.",
        "Os eventos não seriam independentes, pois $0{,}20\times0{,}14=0{,}028$, diferente da interseção observada de 0,06.",
        "Os eventos seriam mutuamente exclusivos porque a interseção é positiva; uma interseção positiva demonstra justamente que podem ocorrer juntos.",
        "Os eventos seriam complementares porque as probabilidades somam 0,34; complementares deveriam somar 1 e não ocorrer conjuntamente.",
    ],
    "AED-C04-O03": [
        "O eixo truncado deveria ser mantido para destacar qualquer mudança; essa escolha amplia visualmente a magnitude sem explicar a escala.",
        "Barras com origem zero ou pontos com escala e valores explícitos comunicariam corretamente a variação de 79\% para 81\%, isto é, 2 pontos percentuais.",
        "Os percentuais deveriam virar volumes sem denominadores; assim, a comparação perderia a base necessária à interpretação.",
        "O efeito tridimensional deveria ser acrescentado para enfatizar profundidade; a perspectiva introduziria nova distorção.",
        "Os rótulos do eixo deveriam ser retirados para evitar viés; sem escala, o leitor não conseguiria verificar a diferença publicada.",
    ],
}

OPTION_SUFFIXES = {
    "TOP-C03-O09": [
        "Essa conclusão descarta indevidamente uma medida válida de usabilidade.",
        "Como conteúdo, ordem, cor e latência também mudaram, o efeito isolado do rótulo não pode ser identificado.",
        "Fixar sempre a ordem introduziria outro viés e não separaria as alterações realizadas.",
        "Esses elementos podem afetar percepção e desempenho e, portanto, não podem ser tratados como neutros.",
        "O tamanho necessário depende da decisão, do desenho e da incerteza, não de um corte universal de cem pessoas.",
    ],
    "TOP-C04-O03": [
        "Padronização visual não reduz a dependência estrutural dos módulos em relação ao SDK externo.",
        "A fronteira interna contém a mudança tecnológica e permite testar a tradução sem espalhar tipos do fornecedor.",
        "O incidente ocorre em dependências de software, e não na forma das tabelas do relatório.",
        "Os testes tornam o acoplamento observável; removê-los esconderia o risco sem corrigi-lo.",
        "Distribuir a mesma dependência por serviços de rede ampliaria custo e falhas sem resolver a fronteira.",
    ],
    "TOP-C05-O01": [
        "A troca bem-sucedida demonstra justamente que contrato público e código interno podem evoluir separadamente.",
        "Preservar campos, significados e comportamento permite substituir a implementação sem quebrar consumidores.",
        "Contratos também existem em outras formas de integração e não dependem exclusivamente de HTTP ou JSON.",
        "Ocultar o fornecedor reduz vazamento tecnológico, mas não elimina evolução de semântica e versionamento.",
        "Mudanças internas compatíveis não precisam ser anunciadas como quebra do contrato público.",
    ],
    "TOP-C06-O03": [
        "O problema foi a ausência, e não o excesso, dos metadados necessários à investigação.",
        "Identificador, versão, origem e tempos permitem localizar, reproduzir e republicar somente o conjunto afetado.",
        "Uma visualização não recupera a linhagem que foi descartada durante a ingestão.",
        "Um modelo poderia inventar uma reconstrução, mas não restabeleceria evidência auditável do evento original.",
        "Trocar nome por identificador de projeto não recompõe os metadados técnicos ausentes.",
    ],
    "TOP-C07-O09": [
        "A alternativa inverte os papéis: execução de pipeline é atividade operacional de gestão.",
        "A governança define direitos, responsabilidades e políticas; a gestão implementa controles e mede sua execução.",
        "Tratá-las como sinônimos apaga quem decide, quem executa e quem responde pelo resultado.",
        "A definição corporativa envolve negócio, risco e responsabilidade, não somente a tecnologia que a armazena.",
        "O comitê depende de owner e steward para transformar a decisão em responsabilidade contínua.",
    ],
    "TOP-C08-O03": [
        "Sem aleatorização e com casos distintos, o piloto não sustenta generalização causal para qualquer turma.",
        "Os números sugerem benefício conjunto, mas um experimento controlado deve verificar se a condição causou o resultado.",
        "Menor tempo isolado não compensa a quantidade inferior de decisões corretas.",
        "O mesmo número de casos não torna iguais os resultados nem controla a dificuldade dos casos.",
        "Comparar 6,2 apenas com 5,5 ignora que a referência sem assistente levou 9 minutos e acertou menos.",
    ],
    "IA-C01-O05": [
        "Três exemplos escolhidos e fluentes não representam desempenho geral nem consequência de erros.",
        "Amostra, casos críticos, fidelidade, impacto dos erros e revisão humana transformam a alegação em teste verificável.",
        "Velocidade não substitui correção quando a orientação pode afetar direitos.",
        "Esconder fontes impediria justamente a verificação de fidelidade exigida pela contratação.",
        "Uma média única poderia ocultar falhas graves em tarefas ou grupos específicos.",
    ],
    "AED-C01-O09": [
        "Sequência temporal não basta para atribuir o crescimento à campanha.",
        "Volume, preço, margem, cancelamentos e comparação adequada distinguem crescimento nominal de resultado sustentável.",
        "Curtidas podem compor outra análise, mas não substituem receita, volume e rentabilidade do caso.",
        "Retirar a série histórica impediria controlar sazonalidade e outras mudanças do período.",
        "Agir antes de compreender denominadores e efeitos pode ampliar uma campanha sem benefício econômico.",
    ],
    "AED-C05-O03": [
        "Somar o total repetido em cada item mantém a triplicação do mesmo evento econômico.",
        "Declarar o grão permite agregar uma vez por pedido ou somar valores de item compatíveis com o contrato.",
        "Média multiplicada pela quantidade de itens não reconstrói necessariamente o total de pedidos.",
        "Excluir pedidos legítimos altera a população em vez de corrigir a agregação.",
        "Linha de item e pedido são unidades distintas, ainda que ambas contenham identificadores.",
    ],
    "AED-C06-O09": [
        "A sequência coloca a decisão no centro e liga cada evidência e limite à recomendação dirigida ao público.",
        "Começar pelas transformações técnicas repete o problema de demonstrar a ferramenta antes da pergunta decisória.",
        "Omitir limites torna a mensagem mais persuasiva, porém menos confiável e contestável.",
        "Transições visuais não corrigem a ausência de encadeamento lógico entre evidência e ação.",
        "Depoimento pode complementar contexto, mas não substitui as evidências que sustentam a recomendação.",
    ],
    "AED-C08-O09": [
        "O limite de segurança impede que melhora média de pontualidade compense acidentes e jornadas excessivas.",
        "Otimizar apenas pontualidade viola explicitamente a restrição definida pela direção.",
        "Acidentes e tempo possuem significados e unidades diferentes; sua média não representa decisão responsável.",
        "Ocultar o efeito adverso elimina evidência material e impede governança do risco.",
        "Facilidade de mensuração não torna uma métrica adequada à consequência operacional.",
    ],
}

COMMANDS = {
    "IA-C02-O07": "Use o Quadro editorial para calcular a média ponderada e identificar a moda ou as modas dos erros. Selecione a alternativa que apresenta simultaneamente a conta e a interpretação corretas.",
    "IA-C03-O05": "Calcule $P(L)P(E)$ e compare o resultado com $P(L\cap E)$. Em seguida, selecione a interpretação probabilística compatível com essa comparação.",
    "IA-C04-O03": "Calcule o resíduo pela convenção $e=y-\hat y$ e interprete a Figura 2. Selecione a conclusão que relaciona sinal, regime térmico e revisão do modelo.",
    "IA-C05-O05": "Calcule as duas perdas com os valores fornecidos e selecione a alternativa que interpreta corretamente o efeito da confiança equivocada.",
    "IA-C06-O01": "Calcule MAE e RMSE sem cancelar sinais nem arredondar antes da raiz. Selecione a resposta que preserva a unidade e interpreta o efeito do maior erro.",
    "AED-C03-O05": "Calcule $P(U)P(R)$, compare com a interseção observada e selecione a interpretação correta sobre independência.",
    "AED-C04-O03": "Compare a Figura editorial com o gráfico de eixo iniciado em 78,5\% descrito no texto. Selecione a revisão que comunica os mesmos dados sem exagerar sua magnitude.",
}


def load_generator(script: Path):
    spec = importlib.util.spec_from_file_location("unifacol_exam_generator", script)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def replace_options(generator, block: str, item_id: str) -> str:
    options, span = generator.item_options(block)
    if item_id in CUSTOM_OPTIONS:
        revised = CUSTOM_OPTIONS[item_id]
    elif item_id in OPTION_SUFFIXES:
        revised = [f"{option.strip().rstrip('.')}. {suffix}" for option, suffix in zip(options, OPTION_SUFFIXES[item_id])]
    else:
        revised = []
        for option in options:
            clean = option.strip().rstrip(".")
            revised.append(f"O parecer propõe: {clean}. Essa leitura orientaria a decisão descrita no caso.")
    body = "\n" + "\n".join(f"  \\item {option}" for option in revised) + "\n"
    return block[: span[0]] + body + block[span[1] :]


def editorialize(generator, item):
    block = item.block
    block = block.replace("resíduo e=y-ychapéu", "resíduo $e=y-\\hat y$")
    block = block.replace("\\TextoBase", f"\\ChamadaEditorial{{{HEADLINES[item.item_id]}}}\n\\TextoBase\n\n{LEADS[item.item_id]}\n", 1)
    support = EXTRA_SUPPORT.get(item.item_id)
    if support:
        block = block.replace("\\FonteDidatica", support + "\n\\FonteDidatica", 1)
    if item.item_id in COMMANDS:
        replacement = "\\Comando " + COMMANDS[item.item_id] + "\n\n"
        block = re.sub(r"\\Comando\s+.*?(?=\\begin\{enumerate\}|\\EspacoDiscursiva|\Z)", lambda _match: replacement, block, count=1, flags=re.S)
    if item.kind == "O":
        block = replace_options(generator, block, item.item_id)
    # Protege comandos LaTeX escritos em strings Python normais (\times e \approx).
    block = block.replace("\t", "\\t").replace("\a", "\\a")
    item.block = block
    return item


def add_editorial_macro(tex: str) -> str:
    marker = "\\input{../../../caderno_exercicios/caderno_enade_style.tex}\n"
    macro = "\\newcommand{\\ChamadaEditorial}[1]{\\par\\medskip\\noindent{\\color{disciplinecolor}\\bfseries\\small #1}\\par\\smallskip}\n"
    return tex.replace(marker, marker + macro, 1)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", type=Path, required=True)
    parser.add_argument("--discipline", required=True)
    parser.add_argument("--prefix", choices=SELECTIONS, required=True)
    parser.add_argument("--seed", type=int, default=20260816)
    args = parser.parse_args()
    generator = load_generator(Path(__file__).with_name("generate_exams_from_workbook.py"))
    workbook = args.repo / "caderno_exercicios"
    answers, corpus = generator.parse_answers(workbook / "professor")
    all_items = generator.parse_items(workbook / "capitulos", args.prefix, answers)
    by_id = {item.item_id: item for item in all_items}
    selected = [editorialize(generator, by_id[item_id]) for item_id in SELECTIONS[args.prefix]]
    if any(item.number % 2 == 0 for item in selected):
        raise SystemExit("a seleção contém item par")

    output = args.repo / "provas" / "2026.2"
    folder = output / "prova_i_unidade"
    version_rows = {}
    for version in "AB":
        tex, version_rows[version] = generator.exam_tex(args.discipline, "Avaliação da I Unidade", version, selected, args.seed + 1009)
        (folder / f"prova_{version}.tex").write_text(add_editorial_macro(tex), encoding="utf-8")

    map_a = {row["id"]: row for row in version_rows["A"]}
    map_b = {row["id"]: row for row in version_rows["B"]}
    matrix_path = output / "professor" / "matriz_rastreabilidade.csv"
    old_rows = list(csv.DictReader(matrix_path.open(encoding="utf-8")))
    rows = [row for row in old_rows if row["instrumento"] != "prova_i_unidade"]
    for item in selected:
        a, b = map_a[item.item_id], map_b[item.item_id]
        rows.append({"instrumento": "prova_i_unidade", "id": item.item_id, "capitulo": str(item.chapter), "tipo": item.kind,
                     "competencia": item.competence, "suporte": item.support, "dificuldade_score": str(item.score),
                     "posicao_A": a["position"], "gabarito_A": a["correct"], "posicao_B": b["position"],
                     "gabarito_B": b["correct"], "permutacao_B": b["permutation"]})
    order = {name: index for index, name in enumerate(("prova_i_unidade", "prova_ii_unidade", "segunda_chamada", "final", "simulado"))}
    rows.sort(key=lambda row: (order[row["instrumento"]], int(row["posicao_A"])))
    with matrix_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader(); writer.writerows(rows)

    manifest_path = output / "professor" / "manifesto_selecao.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    manifest["instruments"]["prova_i_unidade"] = [{"id": item.item_id, "score": item.score, "chapter": item.chapter, "type": item.kind} for item in selected]
    manifest["editorial_revision"] = {"instrument": "prova_i_unidade", "rule": "same workbook item; expanded editorial form only", "seed": args.seed}
    manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    coverage_lines = [f"# Cobertura privada — Prova I — {args.discipline}", "", "Todos os IDs são ímpares e permanecem rastreáveis ao caderno; a prova recebeu somente revisão editorial preservadora.", "", "| Conteúdo do plano | ID do caderno | Capítulo | Tipo |", "|---|---|---:|---|"]
    for label, item in zip(COVERAGE[args.prefix], selected):
        coverage_lines.append(f"| {label} | `{item.item_id}` | {item.chapter} | {item.kind} |")
    (output / "professor" / "cobertura_prova_i.md").write_text("\n".join(coverage_lines) + "\n", encoding="utf-8")

    item_lookup = {item.item_id: item for item in all_items}
    item_lookup.update({item.item_id: item for item in selected})
    lines = [f"# Gabaritos privados — {args.discipline} — 2026.2", "", "Não publicar com as provas.", ""]
    titles = {"prova_i_unidade": "Avaliação da I Unidade", "prova_ii_unidade": "Avaliação da II Unidade", "segunda_chamada": "Segunda Chamada", "final": "Avaliação Final", "simulado": "Simulado ENADE"}
    for name in order:
        group = sorted((row for row in rows if row["instrumento"] == name), key=lambda row: int(row["posicao_A"]))
        lines.extend([f"## {titles[name]}", "", "| ID | Pos. A | Gab. A | Pos. B | Gab. B | Permutação B |", "|---|---:|:---:|---:|:---:|---|"])
        for row in group:
            lines.append(f"| {row['id']} | {row['posicao_A']} | {row['gabarito_A']} | {row['posicao_B']} | {row['gabarito_B']} | {row['permutacao_B']} |")
        lines.extend(["", "### Critérios originais das discursivas", ""])
        for row in group:
            if row["tipo"] == "D":
                lines.append(f"- **{row['id']}:** {generator.answer_excerpt(row['id'], corpus)}")
        lines.append("")
    (output / "professor" / "gabaritos.md").write_text("\n".join(lines) + "\n", encoding="utf-8")

    reserved_ids = {entry["id"] for entries in manifest["instruments"].values() for entry in entries}
    reserved = ["% Banco reservado — não publicar", ""]
    for item_id in sorted(reserved_ids):
        reserved.extend([f"% {item_id}", item_lookup[item_id].block, ""])
    (output / "banco_reservado" / "itens_selecionados.tex").write_text("\n".join(reserved), encoding="utf-8")
    print(f"{args.prefix}: Prova I revisada com 8 IDs ímpares do caderno e matriz específica do plano")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
