import os
import PyPDF2
import nltk
import json
from pathlib import Path
from constants import TEMP, DATA

nltk.download('punkt')

TEMP_TXTS = TEMP + '/txts'
TEMP_JSONS = TEMP + '/jsons'

def text_from_pdf(file_path: str):
    base_name = os.path.splitext(os.path.basename(file_path))[0]
    text_file_path = os.path.join(TEMP_TXTS, f"{base_name}.txt")

    with open(file_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        number_of_pages = len(reader.pages)
        all_text = ""
        for page_number in range(number_of_pages):
            page = reader.pages[page_number]
            text = page.extract_text()
            all_text += text + "\n"

    with open(text_file_path, 'w', encoding='utf-8') as text_file:
        text_file.write(all_text)

    return text_file_path


def split_into_sentences(text_file_path: Path):
    with open(text_file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    sentences = nltk.sent_tokenize(text)
    return sentences


def save_sentences_to_json(sentences, json_file_path):
    with open(json_file_path, 'w', encoding='utf-8') as file:
        json.dump(sentences, file, ensure_ascii=False, indent=4)


if __name__ == '__main__':
    pdf_file_path = DATA + '/GPT_Story.pdf'
    text_file_path = text_from_pdf(pdf_file_path)

    sentences = split_into_sentences(text_file_path)

    json_file_path = os.path.join(TEMP_JSONS, os.path.splitext(os.path.basename(pdf_file_path))[0] + '.json')
    save_sentences_to_json(sentences, json_file_path)