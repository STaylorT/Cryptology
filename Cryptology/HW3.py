from numpy import *
# Sean Taylor Thomas
def question_1_brute(str = "lomsmlumfwyyiztsjmexwzbvwstcyxazbnkwhmestpkpehhkvxqamfxloigtjvoeikzqiidforxktweivpnsmubtgekpbpsfaqaywzbuildmaxqtmgijwipijamfxoptyfwnqamfapvvlfarggulfpaumhtsabuikaiexlomeyfuqakkwmrhkaiexkztbadfjhxylbfjszbrvwhkuqaucgismbrvqvcuisybumkzqtrssifmfntrpswausmsloiuvucpwamqisjpgmelgbyzliexzpafsmuleieluoijaweyfpvnwlyivkzatvrwhvqvmuifpguonwhvafmtsmglwzmpsfkbvqwfwhjsptgsuvucpwamnpswjrjgymglwzwhrvfwhvllagmkvdrvlomgikaevpdimtmfvvglwdwehkaiexgugbyjtieoylbeiskgfxsyb"):
    alphabet = {
        "a": 0,
        "b": 1,
        "c": 2,
        "d": 3,
        "e": 4,
        "f":5,
        "g":6,
        "h":7,
        "i":8,
        "j":9,
        "k":10,
        "l":11,
        "m":12,
        "n":13,
        "o":14,
        "p":15,
        "q":16,
        "r":17,
        "s":18,
        "t":19,
        "u":20,
        "v":21,
        "w":22,
        "x":23,
        "y":24,
        "z":25
    }  # dictionary to convert letter into number
    str_encoded = []  # array representing the string in number form
    key = [0]  # representing the key of this cigenere cipher
    blank_str = ""

    for letter in str:  # converting string cipher into corresponding number cipher
        str_encoded.append(alphabet[letter])

    # print("This is input: ", str)

    def get_key(val):  # method for converting back into alphabet from numbers text
        for key, value in alphabet.items():
            if val == value:
                return key
        return "There is no such Key"

    inc_index = 0
    length_key = 1
    while (inc_index <= 5):
        str2 = str_encoded.copy()

        decoded_plaintext = blank_str[:]

        for i in range(len(str2)):
            str2[i] = (str2[i] - key[i%length_key]) % 26
            # convert str2 into plaintext
            decoded_plaintext += get_key(str2[i])

        print(": ", key)
        print("converted plaintext: ", decoded_plaintext)
        print("converted key: ")
        for i in key:
            print(get_key(i), end =" ")
        print("---------------------------------------------------/n")

        if (len(key) == length_key):
            if (key[inc_index] == 25):
                if (inc_index == len(key)-1):
                    inc_index = 0
                    key.append(0)
                    length_key += 1
                    for i in range(len(key)):
                        key[i] = 0
                else:
                    inc_index += 1
            else:
                # update key
                key[inc_index] += 1

def question_2(): # not correct implementation here. just an experiment
    for i in range(0,2):
        isPrime = True

        if (i*i % 97 == 1):
            print(i)

def question_3():
    for i in range(255):
        if(i % 15 == 5 and i % 17 == 2):
            print(i)
def question_4():
    for i in range(1161):
        if(i % 43 == 7 and i % 27 == 2):
            print(i)

def question_5():
    for i in range(221):
        if (i*i % 221 == 97):
            print(i)

def question_6():
    for i in range(221):
        if (i*i % 221 == 179):
            print(i)

def question_7():
    for i in range(10000):
        if (i % 5 == 1 and i % 6 == 2 and i % 7 == 4):
            print(i)

# question_1_brute() # not working
# question_4()
# question_3()
# question_5()
question_2()