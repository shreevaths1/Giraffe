phrase1 = "Giraffe\nAcademy"
phrase2 = "Giraffe\\Academy"
phrase3 = "Giraffe\"Academy"
phrase = "Giraffe Academy"

print(len(phrase))

print(phrase.replace("Giraffe", "Elephant"))
print("--- --- --- --- --- ---")

# string methods
st = "hello"
print(st.upper())
print(st.lower())
print(st.capitalize())
print(st.replace('h','g'))
print(st.find('e'))
print(st.encode())
print(st.casefold())
print(st.center(20)+"shree")
print(st.count('l'))

print(st.endswith('o'))
print(st.endswith('j'))

print("\t" + st.expandtabs(10) + "shree")
print("Hello! My name is {}. I am {} years old.".format("shree",22))
print(st.index('h'))
print("#".join(['a','b','c','d','e']))
print("TEST".join({"name": "John", "country": "Norway"}))
print(st.ljust(20)+"shree")
print(st.rjust(20)+"shree")
