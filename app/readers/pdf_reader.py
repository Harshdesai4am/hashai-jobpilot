try:
    from pypdf import PdfReader
except ImportError:  # pragma: no cover - runtime fallback
    try:
        from PyPDF2 import PdfReader  # type: ignore
    except ImportError:  # pragma: no cover - runtime fallback
        PdfReader = None


class PDFReader:

    def read(self, file_path: str) -> str:
        if PdfReader is None:
            raise RuntimeError(
                "PDF reading requires 'pypdf' or 'PyPDF2'. Install one of them and try again."
            )

        reader = PdfReader(file_path)

        text = ""

        for page in reader.pages:
            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

        return text