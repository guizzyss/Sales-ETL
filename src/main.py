#Script principal que executa o pipeline ETL
#Main script that runs the ETL pipeline

import logging
from src import extract, transform, load

# Configuração do logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

if __name__ == "__main__":
    logging()
    logger = logging.getLogger(__name__)

    logger.info("Iniciando pipeline ETL...")

    data = extract.run()
    transformed = transform.run(data)
    load.run(transformed)

    logger.info("Pipeline ETL concluído com sucesso!")