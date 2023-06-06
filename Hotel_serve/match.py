from multiprocessing.spawn import import_main_path
import re


import re

str = r"(?P<first>abc)(?:def)(ghi)"

match = re.match(str,"abcdefghi")
print(match.group("first"))
print(match.groups())
