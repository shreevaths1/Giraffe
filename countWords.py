def freq(string):
    words = []
    words = string.split()
    dt = {}

    for key in words:
        dt[key] = words.count(key)

    print(dt)


freq("Mary had a little lamb Little lamb, little lamb Mary had a little lamb. \
     Its fleece was white as snow And everywhere that Mary went Mary went, Mary went \
     Everywhere that Mary went The lamb was sure to go")
