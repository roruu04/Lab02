import translator as tr

t = tr.Translator()


while(True):

    t.printMenu()

    t.loadDictionary("c:/Users/auror/Desktop/tdp/Lab02/dictionary.txt")

    txtIn = input()

    # Add input control here!

    if int(txtIn) == 1:
        txtIn = input("Ok, quale parola devo aggiungere?\n")
        alien = txtIn.split(" ")[0]
        italian = txtIn.split(" ")[1]
        t.addWord(alien, italian)
        print(f"['{alien}', '{italian}']\nAggiunta!")
        pass

    if int(txtIn) == 2:
        txtIn = input("Ok, quale parola devo tradurre?")
        print(txtIn.handleTranslate())
        pass
    if int(txtIn) == 3:
        txtIn = input("Ok, quale parola devo cercare?")
        print(txtIn.handleWildCard())
        pass
    if int(txtIn) == 4:
        break
    else:
        print("Scelta non valida, riprova!")