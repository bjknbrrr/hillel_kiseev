d = {
    'apple': ['malum', 'pomum', 'popula', 'bacca'],
    'fruit': ['baca', 'bacca', 'popum', 'pomum'],
    'punishment': ['malum', 'multa', 'pomum']
}

d1 = {}
for key, value in d.items():
    for word in value:
        if word not in d1:
            d1[word] = []
        d1[word].append(key)

print(d1)
