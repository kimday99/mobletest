class MorseCodeTranslator:
    def __init__(self):
        self.morse_dict = {
            ".-": "A",
            "-...": "B",
            "-.-.": "C",
            "-..": "D",
            ".": "E",
            "..-.": "F",
            "--.": "G",
            "....": "H",
            "..": "I",
            ".---": "J",
            "-.-": "K",
            ".-..": "L",
            "--": "M",
            "-.": "N",
            "---": "O",
            ".--.": "P",
            "--.-": "Q",
            ".-.": "R",
            "...": "S",
            "-": "T",
            "..-": "U",
            "...-": "V",
            ".--": "W",
            "-..-": "X",
            "-.--": "Y",
            "--..": "Z",
            " ": " ",
        }
        self.english_dict = {value: key for key, value in self.morse_dict.items()}
        self.english_dict[" "] = ""

    def english_to_morse(self, english_text):
        self.morse_t = ""
        for self.morse_char in english_text:
            if self.morse_char.upper() in self.english_dict:
                self.morse_t += self.english_dict[self.morse_char.upper()] + " "
            else:
                pass
        return self.morse_t

    def morse_to_english(self, morse_text):
        self.english_t = ""
        self.morse_words = morse_text.strip().split("  ")
        for self.morse_word in self.morse_words:
            self.english_chars = self.morse_word.split(" ")
            for self.english_char in self.english_chars:
                if self.english_char in self.morse_dict:
                    self.english_t += self.morse_dict[self.english_char]
                else:
                    pass
            self.english_t += " "
        return self.english_t
