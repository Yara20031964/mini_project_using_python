# Yara's language is to replace every vowels by Y
def Translator(phrase):
    translation=""
    for letter in phrase:
        if letter in "AEIOUaeiou":
            translation = translation +"Y"
        else:
            translation = translation + letter
    return translation

word = input("Please enter the number that you want to translate it: ")
print(Translator(word))