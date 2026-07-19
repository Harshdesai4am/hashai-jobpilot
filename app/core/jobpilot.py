from app.readers.pdf_reader import PDFReader
from app.readers.text_reader import TextReader

from app.services.resume_service import ResumeService
from app.services.job_service import JobService
from app.services.ats_service import ATSService
from app.services.cover_letter_service import CoverLetterService
from app.services.email_service import EmailService


class JobPilot:
    def __init__(self):
        self.pdf_reader = PDFReader()
        self.text_reader = TextReader()

        self.resume_service = ResumeService()
        self.job_service = JobService()
        self.ats_service = ATSService()
        self.cover_letter_service = CoverLetterService()
        self.email_service = EmailService()

    def _read_resume(self, resume_path: str) -> str:
        return self.pdf_reader.read(resume_path)

    def _read_job_description(self, jd_path: str) -> str:
        return self.text_reader.read(jd_path)

    def analyze_resume(self, resume_path: str):
        resume = self._read_resume(resume_path)
        return self.resume_service.analyze(resume)

    def analyze_job(self, jd_path: str):
        job_description = self._read_job_description(jd_path)
        return self.job_service.analyze(job_description)

    def match_resume(self, resume_path: str, jd_path: str):
        resume = self._read_resume(resume_path)
        job_description = self._read_job_description(jd_path)

        return self.ats_service.compare(
            resume,
            job_description,
        )

    def generate_cover_letter(self, resume_path: str, jd_path: str):
        resume = self._read_resume(resume_path)
        job_description = self._read_job_description(jd_path)

        return self.cover_letter_service.generate(
            resume,
            job_description,
        )

    def generate_email(self, resume_path: str, jd_path: str):
        resume = self._read_resume(resume_path)
        job_description = self._read_job_description(jd_path)

        return self.email_service.generate(
            resume,
            job_description,
        )