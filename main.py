from skimage import io
import numpy


class ScriptCompiler:

    def __init__(self, path, std_pause, echo_off=True):
        file = open(path, "w+")
        self.file = file
        self.std_pause = std_pause
        if echo_off:
            file.write("@ECHO OFF\n")

    def write_line(self, string, pause=None):
        if pause is None:
            pause = self.std_pause
        self.file.write(f"timeout /t {pause} /nobreak>nul\n")
        self.file.write(f"echo {string}\n")

    def write_lines(self, lines, pause=None):
        for line in lines:
            self.write_line(line, pause)

    def write_command(self, command, pause=None):
        if pause is None:
            pause = self.std_pause
        self.file.write(f"timeout /t {pause} /nobreak>nul\n")
        self.file.write(f"{command}\n")

    def write_word(self, word, pause=None):
        if pause is None:
            pause = self.std_pause
        self.file.write(f"timeout /t {pause} /nobreak>nul\n")
        self.file.write(f'echo|set /p="{word}"\n')

    def write_words(self, words, pause=None):
        for word in words:
            self.write_word(word, pause)

    def print_img(self, path, char_set, pause=None):
        img = io.imread(path)
        if len(img.shape) >2:
            img_grey = numpy.mean(img[:,:,0:3], axis=2)
        else:
            img_grey = img
        rows = []
        for i in range(img_grey.shape[0]):
            row = ""
            for j in range(img_grey.shape[1]):
                val = img_grey[i,j] / 255
                char = char_set[int((len(char_set)-1)*val)]
                row += char
            rows.append(row)
        self.write_lines(rows, pause)

    def close(self):
        self.file.close()


def act_1(comp):
    comp.write_lines([
        "Willkommen zu ihrem interaktiven Avatar",
        "Initializing",
        "Loading",
        "Loading.",
        "Loading..",
        "Loading...",
        "Loading....",
        "Loading.....",
        "Loading Sequence complete",
        "Ich erwarte ihren Befehl"
    ])

    comp.write_command("set /p id=")
    comp.write_lines([
        "Hallo, es freut mich, dass Sie heute meine Dienste in Anspruch nehmen.",
        "Ich erwarte ihren Befehl"
    ])

    comp.write_command("set /p id=")

    comp.write_lines([
        "Die Banane ist gelb",
        "Ich erwarte ihren Befehl"
    ])

    comp.write_command("set /p id=")

    comp.write_lines([
        "Ihr Name ist WeGlove",
        "Ich erwarte ihren Befehl"
    ])

    comp.write_command("set /p id=")

    comp.write_lines([
        "Es ist der 16.5.22",
        "Ich erwarte ihren Befehl"
    ])

    comp.write_command("set /p id=")

    comp.write_lines([
        "Ihre Lieblingsfarbe ist rot",
        "Ich erwarte ihren Befehl"
    ])

    comp.write_command("set /p id=")

    comp.write_lines([
        "Meine Funktionalitäten strecken sich auf viele Gebiete aus, die ihnen behilflich sein können.",
        "Ich erwarte ihren Befehl"
    ])

    comp.write_command("set /p id=")

    comp.write_lines([
        "Die ersten 100 Primzahlen sind:",
    ], pause=2)

    comp.write_lines([str(x) for x in
                      [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97,
                       101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193,
                       197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307,
                       311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421,
                       431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541]],
                     pause=0)

    comp.write_line("Ich erwarte ihren Befehl")


if __name__ == "__main__":
    comp = ScriptCompiler("test2.cmd", 1)
    act_1(comp)


    comp.write_command("set /p id=")

    comp.write_lines([
        "._.",
        "Ich erwarte ihren Befehl"
    ])

    comp.write_command("set /p id=")

    comp.write_lines([
        "Das Modul wurde noch nicht auf Sie kalibriert",
        "Jetzt kalibrieren? (Y/N)"
    ])

    comp.write_command("set /p id=")

    comp.write_lines([
        "=.=",
        "0_0",
        "O-0",
        "o-o",
        "-_-",
        "Was halten Sie von der bisherigen Kunst?"
    ])

    comp.write_command("set /p id=")

    comp.write_lines([
        "Ich verstehe. Danke für ihr Feedback.",
        "Beginnen wir mit der nächsten Iteration"
    ])

    comp.write_words(
        ["(;_;)","(;_;)","(;_;)","(;_;)","(;_;)", "\n"]
    )

    comp.write_words(
        ["(;_","(;_","(;_;)","_;)","_;)", "\n"]
    )

    comp.write_words(["-" for x in range(10)]+ ["\n"])

    comp.print_img("ex3vqham.bmp", [x for x in "kein schönes Bild"], pause=0)

    comp.print_img("A.png", ["B", " "])

    comp.print_img("Line.png", ["Nichts", "Alles"], pause=3)

    comp.print_img("gradients.png", [".",",",":","!","#"])

    comp.print_img("9qcbw2y5.bmp", ["9", "0", "°"], pause=0)

    comp.write_line("Kalibrierung abgeschlossen!")
    comp.write_line("Ich erwarte ihren Befehl")

    comp.write_command("set /p id=")

