from app.readers.pdf_reader import PDFReader
from app.readers.text_reader import TextReader

from app.services.resume_service import ResumeService
from app.services.job_service import JobService
from app.services.ats_service import ATSService


class JobPilot:

    def __init__(self):
        self.pdf_reader = PDFReader()
        self.text_reader = TextReader()

        self.resume_service = ResumeService()
        self.job_service = JobService()
        self.ats_service = ATSService()

    def analyze_resume(self, resume_path: str):

        resume = self.pdf_reader.read(resume_path)

        return self.resume_service.analyze(resume)

    def analyze_job(self, jd_path: str):

        jd = self.text_reader.read(jd_path)

        return self.job_service.analyze(jd)

    def match_resume(self, resume_path: str, jd_path: str):

        resume = self.pdf_reader.read(resume_path)

        jd = self.text_reader.read(jd_path)

        return self.ats_service.compare(
            resume,
            jd
        )