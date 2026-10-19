# ETL Expectativas de Inflação (BCB)

Pipeline ETL em Python que consome a API de dados abertos do Banco Central do Brasil,
trata as expectativas de mercado para a inflação acumulada em 24 meses e disponibiliza
os dados em CSV e SQLite para análise.

## Fluxo

API do BCB → extração e transformação → carga (CSV / SQLite) → análise em notebooks

## Estrutura

- `main.py`: orquestra o pipeline
- `src/extractTransform.py`: extração via API e tratamento dos dados
- `src/load.py`: salvamento em CSV e SQLite
- `conjuntos de dados/`: saída dos dados
- `Relatório.ipynb`: análise estatística
- `analise_cartoes.ipynb`: análise complementar
- `MachineLearning.ipynb`: modelagem

## Como rodar

pip install -r requisitos.txt
python main.py

## Principais resultados

- Média estimada de inflação: ~4,30%
- Desvio padrão: ~0,25%
- Tendência de queda nas projeções ao longo do período analisado

## Stack

Python, Pandas, SQLite, Jupyter Notebook
