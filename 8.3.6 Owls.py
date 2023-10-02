# this function should return the number of words that contain "owl"!
text ="I really like owls. Did you know that an owl's eyes are more than twice as big as the eyes of other birds of comparable weight? And that when an owl partially closes its eyes during the day, it is just blocking out light? Sometimes I wish I could be an owl."

word ="owl"
def owl_count(text):
    text=text.lower()
    owlist=list(text.split())
    count=text.count(word)
    return count

print (owl_count(text))
