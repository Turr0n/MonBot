#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from dateutil.relativedelta import relativedelta
from tqdm import tqdm
import scrapper
import datetime
import argparse

def args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-s', dest='start', action='store', required=True, type=str)
    parser.add_argument(
        '-e', dest='end', action='store', required=False, type=str, default='')
    
    args = parser.parse_args()
    args.end = args.start if args.end == '' else args.end
    return args

def dates(start, end):
    '''Crear el intervalo de fechas según la fecha inicial y final especificada'''

    start = datetime.datetime.strptime(start, '%Y%m')
    end = datetime.datetime.strptime(end, '%Y%m')

    while start <= end:
        yield start.date()
        start += relativedelta(months=+1)

args = args()
for date in dates(args.start, args.end):
    print('Descargando textos de: {}-{}'.format(date.year, date.month))
    bot = scrapper.pepe(date)
    bot.process()
    [bot.get_docs(entry) for entry in tqdm(bot.entries)]

