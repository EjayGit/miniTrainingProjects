import re

text = """What’s New In Python 3.10

Release 3.10.1

Date January 10, 2022

Editor

Pablo Galindo Salgado

This article explains the new features in Python 3.10, compared to 3.9."""

regex = re.compile(r'3\S+')
mo = regex.findall(text)
print(mo)