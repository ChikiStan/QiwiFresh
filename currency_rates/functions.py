import argparse
import datetime
import logging

import requests
import xmltodict


class Convertor:
    def __init__(self,
                 date: str):
        try:
            xml = requests.get('http://www.cbr.ru/scripts/XML_daily.asp', params={
                'date_req': date
            })
        except Exception as e:
            logging.error('Не удалось подключится к серверу')
            logging.error(e)
            exit(code=-1)
        try:
            xml_to_dict = xmltodict.parse(xml.content)
            self.valutes = xml_to_dict['ValCurs']['Valute']
        except Exception as e:
            logging.error('Неверная дата, значения не получены')
            logging.error(e)
            exit(code=-1)


class View:
    def __init__(self,
                 valute_data: Convertor):
        self.valutes = valute_data.valutes
        pass

    def show_valute(self, code: str | None):
        if code is None:
            logging.warning('Код валюты не получен,'
                            'будут выведены все!')
            for valute in self.valutes:
                print(f'{valute["CharCode"]}({valute["Name"]}): {valute["Value"]}')
            exit(code=0)

        for valute in self.valutes:
            if valute['CharCode'] == code.upper():
                print(f'{valute["CharCode"]}({valute["Name"]}): {valute["Value"]}')
                exit(code=0)
        logging.error('Код валюты не найден')


def create_parser():
    parser = argparse.ArgumentParser(prog='currency_rates')
    parser.add_argument('--date')
    parser.add_argument('--code')
    return parser
