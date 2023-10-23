from flask import Flask, request
from flask import render_template
from morse import MorseCodeTranslator


app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/morse_decoding", methods=["POST", "GET"])
def morse_decoding():
    if request.method == "POST":
        inputMorse = request.form.get("inputMorse")
        morse = MorseCodeTranslator()
        inputMorsespace = inputMorse.replace(" ", "")
        change_text = set(inputMorse)

        # 1. 모스부호인지 확인
        if change_text.issubset([" ", ".", "-"]):
            result_text = morse.morse_to_english(inputMorse)

        # 2. 알파벳인지 확인
        elif inputMorsespace.isalpha():
            result_text = morse.english_to_morse(inputMorse)
            print(result_text)
        # 3. else일 때 에러출력
        else:
            result_text = "에러"

        # english_text = inputMorse

    return render_template("index.html", result=result_text)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5100)
