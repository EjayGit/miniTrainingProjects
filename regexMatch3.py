import re

def text_match(text):
    regex = re.compile(r'(L|l)ove(rs)?')
    mo = regex.findall(text)
    return len(mo)

text = """Lovers in love

Lovers in love

Love, love, love, love, love

Love, love, love, love, love

Love, love, love, love, love

Love, love, love, love, love

Lovers loving love just like these lovers are loving love in love

Lovers loving love just like these lovers are loving love in love"""
text_match(text)