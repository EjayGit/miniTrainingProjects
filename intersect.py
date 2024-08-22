def find_prep(quote):
    prep = {"as", "but", "by", "for", "in", "of", "on", "to", "with"}
    set1 = set(list(quote.split()))
    set2 = set()
    set2 = set1.intersection(prep)
    return set2

quote = """Success is no accident. It is hard work, perseverance, learning, studying, sacrifice and most of all, love of what you are doing or learning to do."""
prep = {"as", "but", "by", "for", "in", "of", "on", "to", "with"}
 
find_prep(quote)