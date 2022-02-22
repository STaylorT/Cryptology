# Vigenere Cipher Dictionary Hacker
# https://www.nostarch.com/crackingcodes/ (BSD Licensed)
# Edited by Sean Taylor Thomas

import detectEnglish, vigenereCipher
def main():
    ciphertext = """lomsmlumfwyyiztsjmexwzbvwstcyxazbnkwhmestpkpehhkvxqamfxloigtjvoeikzqiidforxktweivpnsmubtgekpbpsfaqaywzbuildmaxqtmgijwipijamfxoptyfwnqamfapvvlfarggulfpaumhtsabuikaiexlomeyfuqakkwmrhkaiexkztbadfjhxylbfjszbrvwhkuqaucgismbrvqvcuisybumkzqtrssifmfntrpswausmsloiuvucpwamqisjpgmelgbyzliexzpafsmuleieluoijaweyfpvnwlyivkzatvrwhvqvmuifpguonwhvafmtsmglwzmpsfkbvqwfwhjsptgsuvucpwamnpswjrjgymglwzwhrvfwhvllagmkvdrvlomgikaevpdimtmfvvglwdwehkaiexgugbyjtieoylbeiskgfxsyb"""
    hackedMessage = hackVigenereDictionary(ciphertext)

    if hackedMessage != None:
        print("Here is the decrypted code: " , hackedMessage)
    else:
        print('Failed to hack encryption.')


def hackVigenereDictionary(ciphertext):
    fo = open('dictionary.txt')
    words = fo.readlines()
    fo.close()

    for word in words:
        word = word.strip() # Remove the newline at the end.
        decryptedText = vigenereCipher.decryptMessage(word, ciphertext)
        print(word)
        # print(decryptedText)
        if detectEnglish.isEnglish(decryptedText, wordPercentage=60):
            # Check with user to see if the decrypted key has been found:
            print()
            print('Is this the key?. . . . .')
            print('KEY : ' + str(word) + ' | Decrypted Text From Key ==== ' + decryptedText[:100])
            print()
            print('Q for quit, or hit Enter to continue searching for the key..:')
            response = input('> ')
            if response.upper().startswith('Q'):
                return decryptedText

if __name__ == '__main__':
    main()