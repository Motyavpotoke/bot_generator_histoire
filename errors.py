import logging


error666 = 'Произошла неизвестная ошибка!'

logging.basicConfig(filename='errors.cod.log', level=logging.ERROR, filemode='a',
                    format='%(asctime)s - %(levelname)s - %(message)s')
