txt = "lorem ipsum tartarto max m "

def max_lword(txt):
    words =  []
    lenght = []
    for word in txt.split():
        words.append(word)
        lenght.append(len(word))
    x = lenght.index(max(lenght))
    return words[x]
    

print(max_lword(txt))