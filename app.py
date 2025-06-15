from flask import Flask, render_template, request, redirect, url_for
import time
import random


app = Flask(__name__)

def load_text():
    with open("texts/text_1.txt", "r", encoding="utf-8") as f:
        return f.read().strip()

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        typed_words = request.form.get("typed_words", "")
        original_text = request.form.get("original_text", "")
        elapsed_seconds = float(request.form.get("elapsed_seconds", "60"))
        chars_per_minute = 0
        if elapsed_seconds > 0:
            chars_per_minute = len(typed_words.replace(" ", "")) / elapsed_seconds * 60
        return render_template(
            "result.html",
            chars_per_minute=round(chars_per_minute, 2),
            elapsed_seconds=round(elapsed_seconds, 2),
            typed_words=typed_words,
            original_text=original_text
        )
    else:
        text_to_type = load_text()
        words = text_to_type.split()
        return render_template("index.html", words=words, original_text=text_to_type)



if __name__ == "__main__":
    app.run(debug = True)
a = 1+2/0