# -*- coding: utf-8 -*-
"""
Projeto de Análise Econômica - Taxa de Câmbio USD/BRL (2010-2019)
Arquivo único contendo o pipeline de tratamento de dados e geração de gráficos.
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def carregar_e_limpar_dados(caminho_arquivo):
    # Carrega o dataset enviado
    df = pd.read_csv(caminho_arquivo)
    
    # Converte a coluna de Data para o tipo datetime (padrão DD.MM.YYYY)
    df['Data'] = pd.to_datetime(df['Data'], format='%d.%m.%Y')
    
    # Ordena os dados por data de forma crescente (essencial para séries temporais)
    df = df.sort_values('Data').reset_index(drop=True)
    return df

def gerar_metricas_e_graficos(df):
    # Configuração de estilo limpo para os gráficos
    plt.style.use('seaborn-v0_8-whitegrid' if 'seaborn-v0_8-whitegrid' in plt.style.available else 'default')
    
    # -------------------------------------------------------------
    # Gráfico 1: Evolução Temporal Diária (Série Temporal)
    # Unidade de Medida: Valor Nominal da Moeda em Reais (R$)
    # -------------------------------------------------------------
    fig1, ax1 = plt.subplots(figsize=(10, 5))
    ax1.plot(df['Data'], df['USD_BRL'], color='#1f77b4', linewidth=1.5, label='USD/BRL')
    ax1.set_title('Gráfico 1: Evolução Diária da Taxa de Câmbio USD/BRL (2010-2019)', fontsize=14, fontweight='bold', pad=15)
    ax1.set_xlabel('Ano', fontsize=12)
    ax1.set_ylabel('Taxa de Câmbio (R$)', fontsize=12)
    ax1.grid(True, linestyle='--', alpha=0.6)
    ax1.legend(loc='upper left')
    plt.tight_layout()
    plt.savefig('grafico1_evolucao_temporal.png', dpi=300)
    plt.close()
    print("-> Gráfico 1 gerado com sucesso ('grafico1_evolucao_temporal.png').")

    # -------------------------------------------------------------
    # Gráfico 2: Média Anual da Cotação (Gráfico de Barras)
    # Unidade de Medida: Média por Período Anual em Reais (R$/Ano)
    # -------------------------------------------------------------
    df['Ano'] = df['Data'].dt.year
    media_anual = df.groupby('Ano')['USD_BRL'].mean().reset_index()

    fig2, ax2 = plt.subplots(figsize=(10, 5))
    bars = ax2.bar(media_anual['Ano'].astype(str), media_anual['USD_BRL'], color='#2ca02c', alpha=0.8, edgecolor='black')
    ax2.set_title('Gráfico 2: Média Anual da Taxa de Câmbio USD/BRL (2010-2019)', fontsize=14, fontweight='bold', pad=15)
    ax2.set_xlabel('Ano', fontsize=12)
    ax2.set_ylabel('Média da Taxa de Câmbio (R$)', fontsize=12)
    ax2.grid(True, axis='y', linestyle='--', alpha=0.6)

    # Adicionar os valores exatos acima de cada barra para melhor legibilidade
    for bar in bars:
        yval = bar.get_height()
        ax2.text(bar.get_x() + bar.get_width()/2.0, yval + 0.05, f'R$ {yval:.2f}', ha='center', va='bottom', fontsize=9, fontweight='bold')

    plt.tight_layout()
    plt.savefig('grafico2_media_anual.png', dpi=300)
    plt.close()
    print("-> Gráfico 2 gerado com sucesso ('grafico2_media_anual.png').")

    # -------------------------------------------------------------
    # Gráfico 3: Distribuição dos Retornos Diários (Histograma)
    # Unidade de Medida: Frequência Absoluta (Dias) por Faixa de Variação Percentual (%)
    # -------------------------------------------------------------
    df['Retorno_Percentual'] = df['USD_BRL'].pct_change() * 100

    fig3, ax3 = plt.subplots(figsize=(10, 5))
    ax3.hist(df['Retorno_Percentual'].dropna(), bins=100, color='#9467bd', alpha=0.8, edgecolor='black', range=(-4, 4))
    ax3.set_title('Gráfico 3: Distribuição das Variações Percentuais Diárias do USD/BRL (2010-2019)', fontsize=14, fontweight='bold', pad=15)
    ax3.set_xlabel('Variação Percentual Diária (%)', fontsize=12)
    ax3.set_ylabel('Frequência (Quantidade de Dias)', fontsize=12)
    ax3.grid(True, linestyle='--', alpha=0.6)
    
    # Linha vertical indicando a média de retorno diário
    media_retorno = df['Retorno_Percentual'].mean()
    ax3.axvline(media_retorno, color='red', linestyle='dashed', linewidth=1.5, label=f'Média: {media_retorno:.4f}%')
    ax3.legend()

    plt.tight_layout()
    plt.savefig('grafico3_distribuicao_retornos.png', dpi=300)
    plt.close()
    print("-> Gráfico 3 gerado com sucesso ('grafico3_distribuicao_retornos.png').")

if __name__ == '__main__':
    caminho_dados = 'USD_BRL_hist.csv'
    print("Iniciando a análise dos dados do câmbio USD/BRL...")
    dados = carregar_e_limpar_dados(caminho_dados)
    gerar_metricas_e_graficos(dados)
    print("Processo concluído com sucesso!")
