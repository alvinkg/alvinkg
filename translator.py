def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.isupper():
                translation = translation + "G"
            else:
                translation = translation + "g"
            
        else:
            translation = translation + letter
        #print(letter)
        #print(translation)
    return translation
    
print(translate(input("Please enter a phrase to translate. ")))

