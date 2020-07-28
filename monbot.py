from dateutil.relativedelta import relativedelta
from typing import Generator

import scrapper
from datetime import datetime
import argparse


def get_arguments():
    parser = argparse.ArgumentParser()
    
    parser.add_argument(
        '-s', dest = 'start', action = 'store', required = True, type = str
    )
    
    parser.add_argument(
        '-e', dest = 'end', action = 'store', required = False, type = str, default = ''
    )
    
    parser.add_argument(
        '-fn', dest = 'fn', action = 'store', required = False, type = str, default = 'info.json'
    )
    
    args = parser.parse_args()
    args.end = args.start if (args.end == '') else args.end
    
    return args


def dates(start: str, end: str) -> Generator[str, None, None]:
    '''Crear el intervalo de fechas según la fecha inicial y final especificada'''

    current = datetime.strptime(start, '%Y%m')
    final = datetime.strptime(end, '%Y%m')

    while current <= final:
        tmp = current.date()
        
        yield f"{ tmp.year }{ tmp.month }" if (tmp.month >= 10) else f"{ tmp.year }0{ tmp.month }"
        current += relativedelta(months = 1)


args = get_arguments()
bot = scrapper.pepe()

for date in dates(args.start, args.end):
    print(f'Descargando textos de: {date}')

    bot.process(date)

bot.dump(args.fn)
