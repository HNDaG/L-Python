from PyDictionary import PyDictionary

dictionary = PyDictionary()

while True:
    word = input("Word:")
    print(dictionary.meaning(word))
    print(dictionary.translate(word, "es"))
