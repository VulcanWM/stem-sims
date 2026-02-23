import random
import re
import os
import sys

word_pattern = re.compile(r"[^\W\d_]+(?:['’][^\W\d_]+)*", re.UNICODE)

def read_novel(filename):
    if hasattr(sys, "_MEIPASS"):
        base_path = sys._MEIPASS
    else:
        base_path = os.path.dirname(__file__)

    # try same folder first
    novel_path = os.path.join(base_path, filename)

    # fallback: try inside text_prediction folder
    if not os.path.exists(novel_path):
        novel_path = os.path.join(base_path, "text_prediction", filename)

    with open(novel_path, "r", encoding="utf-8") as f:
        lines = []
        for line in f:
            line = line.strip()

            if line == "----------":
                break

            if line and not line.lower().startswith("chapter"):
                line = line.lower().replace("’", "'")
                lines.append(line)

    return lines


def tokenize(lines):
    words = []

    for line in lines:
        words.extend(word_pattern.findall(line))

    return words

def create_model(cleaned_text, n_grams=3):
    model = {}
    words = cleaned_text
    for i in range(len(words) - n_grams):
        curr_token = " ".join(words[i:i+n_grams])
        next_token = words[i+n_grams]
        if curr_token in model:
            if next_token in list(model[curr_token].keys()):
                model[curr_token][next_token] += 1
            else:
                model[curr_token][next_token] = 1
        else:
            model[curr_token] = {next_token: 1}
    return model


def predict_text(model, starting_token, n_grams=3):
    text = starting_token
    last_token = starting_token
    for i in range(500):
        if last_token not in model:
            break

        next_words = list(model[last_token].keys())
        weights = list(model[last_token].values())

        next_token = random.choices(next_words, weights=weights, k=1)[0]

        text += " " + next_token
        words_in_text = text.split()
        last_token = " ".join(words_in_text[n_grams * -1:])
    return text

def example():
    novel_lines = read_novel("jane-eyre.txt")

    cleaned_text = tokenize(novel_lines)

    model = create_model(cleaned_text, 3)

    starting_token = 'mr rochester and'
    text = predict_text(model, starting_token, 3)
    print(text)

if __name__ == "__main__":
    example()
