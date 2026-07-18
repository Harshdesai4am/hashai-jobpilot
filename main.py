from app.readers.text_reader import TextReader
from app.services.job_service import JobService

reader = TextReader()
job_service = JobService()

job_description = reader.read(
    "data/jobs/react_native_jd.txt"
)

result = job_service.analyze(job_description)

print(result)