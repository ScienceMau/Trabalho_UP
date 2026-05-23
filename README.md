# Análise Histórica e Estatística da Taxa de Câmbio USD/BRL (2010–2019)

Este repositório contém o projeto de análise exploratória, tratamento de séries temporais e modelagem estatística descritiva da taxa de câmbio entre o Dólar Americano (USD) e o Real Brasileiro (BRL) cobrindo uma década histórica (janeiro de 2010 a dezembro de 2019).

O objetivo principal do projeto é aplicar pipelines de dados em Python para transformar registros brutos em visualizações analíticas de alta fidelidade, baseando-se em três unidades de medida e abordagens matemáticas distintas.

---

## 📌 Links Obrigatórios do Projeto

* **Dataset Real Utilizado:** [Repositório Histórico USD/BRL](https://github.com/datasets/usd-brl-historical-data)
* **Apresentação Técnica no Loom:** [Assista ao Vídeo Explicativo (Máx. 5 min)](https://www.loom.com/share/placeholder-da-sua-gravacao-de-tela)

---

## 🛠️ Arquitetura do Código (`analise_cambio.py`)

O script foi desenvolvido como um arquivo único estruturado de forma linear e modular, garantindo legibilidade e reprodutibilidade:

1.  **Ingestão e Parsing Temporal:** Leitura dos dados brutos em formato `.csv`. Como as datas originais encontram-se no padrão string brasileiro (`DD.MM.YYYY`), o pipeline realiza o parsing nativo para objetos `datetime64[ns]` do Pandas.
2.  **Ordenação Cronológica:** Ordenação indexada em ordem crescente (`sort_values`), premissa matemática obrigatória para evitar distorções ou linhas entrelaçadas em plotagens de séries temporais.
3.  **Cálculo Algorítmico de Retornos:** Aplicação da função de variação percentual discreta de primeira ordem ($r_t$) para converter valores nominais em flutuações de volatilidade.
4.  **Exportação Vetorial:** Salvamento dos plots com resolução de 300 DPI, prontos para integração em relatórios de alta qualidade (como documentos em $\LaTeX$).

---

## 📊 Visualizações de Dados e Fundamentação Teórica

O projeto adota três naturezas físicas e unidades de medidas diferentes para o mesmo conjunto de dados, mapeando perspectivas temporais, econômicas e de distribuição de frequência.

### 1. Evolução Temporal Diária (Série Temporal contínua)
* **Unidade de Medida:** Valor Nominal da Moeda em Reais ($R\$$)
* **Arquivo Gerado:** `grafico1_evolucao_temporal.png`
* **Justificativa:** O gráfico de linha contínua é a ferramenta clássica e matematicamente correta para variáveis que flutuam em alta frequência temporal. Ele preserva a dependência estocástica e a sequência cronológica dos eventos, permitindo identificar ciclicidades, tendências de longo prazo e quebras estruturais sem fragmentar o fluxo histórico.

### 2. Média Anual da Taxa de Câmbio (Análise Macroeconômica Discreta)
* **Unidade de Medida:** Média por Janela Temporal Anual ($R\$/\text{Ano}$)
* **Arquivo Gerado:** `grafico2_media_anual.png`
* **Justificativa:** Ao agrupar os dados microscópicos diários em médias aritméticas anuais, eliminamos o ruído estocástico do mercado de balcão (*day-to-day noise*). O gráfico de barras verticais atua como uma excelente ferramenta de comparação discreta, tornando evidente a transição de patamar econômico e a desvalorização cambial acentuada observada no Brasil a partir do ano fiscal de 2015.

### 3. Distribuição das Variações Percentuais Diárias (Estatística Descritiva e Volatilidade)
* **Unidade de Medida:** Taxa de Retorno Diário em Percentual ($\%$)
* **Arquivo Gerado:** `grafico3_distribuicao_retornos.png`
* **Justificativa:** Ao transformar o preço nominal em retorno pela equação:
    $$r_t = \left(\frac{P_t - P_{t-1}}{P_{t-1}}\right) \times 100$$
    alteramos a dimensão do problema para uma taxa adimensional. O histograma com 100 *bins* permite mapear a função de densidade de probabilidade empírica do ativo. O resultado revela uma distribuição simétrica, com alta curtose (pico centrado próximo a $0\%$) e a presença de caudas longas (*heavy tails*), um comportamento característico de sistemas dinâmicos complexos e não-lineares encontrados no mercado financeiro.

---

## 🚀 Como Executar o Projeto

### Pré-requisitos
Certifique-se de possuir o Python 3.8+ instalado junto às dependências listadas no ecossistema de computação científica:
```bash
pip install pandas matplotlib numpy
