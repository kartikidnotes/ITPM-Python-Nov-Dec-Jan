
ch=input("Enter character :: ")

match ch.lower():
    case 'a' | 'e' | 'i' | 'o' | 'u' :
        print("Vowel ")
    case _:
        print("Consonants")