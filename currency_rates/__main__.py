import datetime
import logging
import sys

from functions import Convertor, View, create_parser

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    parser = create_parser()
    namespace = parser.parse_args(sys.argv[1:])
    if namespace.date is None:
        logging.error("Не указана дата")
        exit(code=-1)
    date = datetime.datetime.strptime(namespace.date, "%Y-%m-%d").date()
    date = date.strftime("%d/%m/%Y")
    code = namespace.code
    request = Convertor(date=date)
    view = View(request)
    view.show_valute(code=code)
