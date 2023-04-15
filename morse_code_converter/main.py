MORSE_CODE = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "0": "-----"
}


def convert_to_morse_code(text: str) -> str:
    result = ""
    for letter in text:
        result += MORSE_CODE[letter.upper()]
    return result


while True:
    user_input = input("Please input your text to convert to MORSE code (type .exit to exit converter): ")
    if user_input == ".exit":
        break

    try:
        print(f"\"{user_input}\" in MORSE code: {convert_to_morse_code(user_input)}")
    except KeyError:
        print("Sorry, your text cannot be converted to MORSE code")
