# -*- coding: utf-8 -*-
# vim: set bg=dark noet ts=4 sw=4 fdm=indent :

""" DESCRIPTION OF WORK"""
__author__ = "morosm"

import logging
import argparse
import pandas as pd

def main():
    logging.basicConfig(
        level=logging.DEBUG,
        format='[%(filename)s:%(lineno)s - %(funcName)s %(asctime)s;%(levelname)s] %(message)s',
        datefmt='%a, %d %b %Y %H:%M:%S'
    )
    logger = logging.getLogger(__file__)

    example_word = """
        DESCRIBE ARGUMENT USAGE HERE
        python main.py --help
    """

    parser = argparse.ArgumentParser(prog=__file__, description='code description', epilog=example_word,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    # add parameter if needed
    parser.add_argument('-v', '--version', help='version of code', action='version', version='%(prog)s 1.0')
    parser.add_argument('--file_name', help='file to parse', type=str, default='all')
    parser.add_argument('--unit_price', help='max unit price', type=str, default='65000')
    parser.add_argument('--total_price', help='max total price', type=str, default='200')

    args = parser.parse_args()
    clean_data(args.file_name, args.unit_price, args.total_price)
    
    
def clean_data(file_name, unit_price, total_price):
    df = pd.read_csv(file_name, encoding='utf-8-sig')
    selected_data = df[(df['unit_price'] < int(unit_price)) & (df['total_price'] < int(total_price))]
    new_file_name = get_file_name(file_name)
    selected_data.to_csv(new_file_name, encoding='utf-8-sig')
    
def get_file_name(file_name):
    # 分割文件名和扩展名
    base_name, extension = file_name.rsplit('.', 1)

    # 拼接新的文件名
    new_file_name = f"{base_name}_cleaned.{extension}"
    return new_file_name

if __name__ == '__main__':
    main()