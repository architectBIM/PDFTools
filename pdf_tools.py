import os
import logging
from PyPDF2 import PdfMerger


logger = logging.getLogger(__name__)


def merge_pdfs_from_folder(folder_path, output_path, file_count=2):
    merger = PdfMerger()
    pdf_files = [f for f in os.listdir(folder_path) if f.lower().endswith('.pdf')]
    pdf_files = sorted(pdf_files)

    if len(pdf_files) < file_count:
        logger.warning(f"Only {len(pdf_files)} PDF-file(s) found. At least {file_count} needed.")
        return

    for pdf in pdf_files:
        full_path = os.path.join(folder_path, pdf)
        merger.append(full_path)

    merger.write(output_path)
    merger.close()
    logger.info(f"File saved as {output_path}")
