phrase1 = "Giraffe\nAcademy"
phrase2 = "Giraffe\\Academy"
phrase3 = "Giraffe\"Academy"
phrase = "Giraffe Academy"
print(phrase + " is cool")
print(phrase.lower())
print(phrase.upper())
print(phrase.isupper())
print(phrase.upper().isupper())

print(len(phrase))
print(phrase[3])

# passing a parameter
print(phrase.index('a'))
print(phrase.index('Acad'))
# print(phrase.index('z'))

print(phrase.replace("Giraffe", "Elephant"))
