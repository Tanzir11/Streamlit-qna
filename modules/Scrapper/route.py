from .service import Scrapper_obj

def upload_resume(file):
    return Scrapper_obj.embedding_generator_pdf(file)