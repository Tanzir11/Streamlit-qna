from .utils import create_embeddings, extract_text_from_pdf
import re


class Scrapper:
    @staticmethod
    def embedding_generator_pdf(file):
        pdf_bytes = file.read()
        data = extract_text_from_pdf(pdf_bytes)
        data_push = create_embeddings(data)
        return data_push



Scrapper_obj = Scrapper()
