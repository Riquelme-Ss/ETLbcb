# ETL Expectativas de Inflação (BCB)

Pipeline ETL em Python que consome a API de dados abertos do Banco Central do Brasil,
trata as expectativas de mercado para a inflação acumulada em 24 meses e disponibiliza
os dados em CSV e SQLite para análise.

## Problema

O Banco Central publica diariamente as expectativas de mercado para a inflação, mas os
dados chegam em JSON paginado pela API. Este projeto automatiza a coleta, padroniza os
tipos e entrega uma base pronta para análise estatística e modelagem.

## Fluxo

```
API do BCB (OData) → extração → transformação → carga (CSV / SQLite) → notebooks de análise
```

## Fonte dos dados

- API de Expectativas de Mercado do Banco Central do Brasil (Olinda)
- Endpoint: `ExpectativasMercadoInflacao24Meses`
- Variável: expectativa de inflação acumulada em 24 meses

## Estrutura do projeto

```
ETLbcb/
├── main.py                  # orquestra o pipeline
├── src/
│   ├── extractTransform.py  # extração via API e tratamento dos dados
│   └── load.py              # salvamento em CSV e SQLite
├── datasets/                # saída dos dados (CSV e banco SQLite)
├── Relatorio.ipynb          # análise estatística
├── MachineLearning.ipynb    # modelagem
├── analise_cartoes.ipynb    # análise complementar
└── requirements.txt
```

## Como rodar

```bash
git clone https://github.com/Riquelme-Ss/ETLbcb.git
cd ETLbcb
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python main.py
```

Os arquivos gerados ficam em `datasets/`.

## Principais resultados

Valores obtidos na análise do `Relatorio.ipynb`:

- Média estimada de inflação: ~4,30%
- Desvio padrão: ~0,25%
- Tendência de queda nas projeções ao longo do período analisado



## Decisões técnicas

- Extração, transformação e carga separadas em módulos distintos
- Saída em dois formatos: CSV para uso rápido e SQLite para consultas com SQL
- Ponto de entrada único (`main.py`), fácil de agendar com cron ou Airflow

## Stack

Python · Pandas · Requests · SQLite · Jupyter Notebook

## Próximos passos

- [ ] Paginação completa da API
- [ ] Testes automatizados com pytest
- [ ] Execução agendada (GitHub Actions ou Airflow)
- [ ] Dashboard em Power BI ou Streamlit

## Autor

**Pablo Riquelme** · [LinkedIn](https://www.linkedin.com/in/pablo-riquelme-santana-de-souza-226671225) · riquelmessdev@gmail.com
