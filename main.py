import logging

from src.extractTransform import extrair_transformar
from src.load import salvar_csv, salvar_sqlite

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
logger = logging.getLogger(__name__)


def main():
    logger.info("Iniciando ETL da Expectativa de Inflação 24 Meses")
    try:
        df = extrair_transformar()
        salvar_csv(df)
        salvar_sqlite(df)
    except Exception:
        logger.exception("Falha na execução do ETL")
        raise
    logger.info("ETL concluído: %d registros salvos em CSV e SQLite", len(df))


if __name__ == "__main__":
    main()
