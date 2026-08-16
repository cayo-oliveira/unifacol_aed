# Perguntas para Análise no Tableau

Use estas perguntas para guiar a criação de visualizações e dashboards no Tableau com o dataset de desempenho acadêmico. Foque em insights acionáveis para educadores e pais.

## Perguntas Estratégicas
1. **Quais são os fatores mais influentes no desempenho acadêmico?**
   - Correlacionar `Nota_Exame` com variáveis como `Frequencia`, `Horas_Estudadas`, `Envolvimento_Parental`.
   - Visualização: Heatmap de correlações ou scatter plots.

2. **Como o ambiente familiar afeta as notas?**
   - Analisar `Renda_Familiar`, `Educacao_Parental`, `Envolvimento_Parental`.
   - Visualização: Bar charts ou box plots por categoria.

3. **Há diferenças significativas por gênero ou tipo de escola?**
   - Comparar médias de `Nota_Exame` por `Genero` e `Tipo_Escola`.
   - Visualização: Violin plots ou stacked bars.

4. **Quais comportamentos impactam mais as notas?**
   - Explorar `Sono_Horas`, `Atividade_Fisica`, `Motivacao`.
   - Visualização: Scatter plots com linhas de tendência.

5. **Podemos identificar alunos em risco?**
   - Usar `Categoria_Desempenho` (nova coluna) para filtrar baixos.
   - Visualização: Tabela dinâmica com filtros.

## Atividades Práticas
- Crie um dashboard com KPIs (média de notas, taxa de aprovação).
- Adicione filtros interativos (ex.: por renda ou gênero).
- Construa uma narrativa: "Da frequência à excelência acadêmica".

## Dicas
- Use o dataset transformado (`StudentPerformanceFactors_transformado.csv`) com labels em português.
- Referência: `context.md` para protótipo e metadados.