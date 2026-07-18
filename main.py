from app.readers.pdf_reader import PDFReader
from app.readers.text_reader import TextReader
from app.utils.skill_matcher import SkillMatcher

pdf = PDFReader()
text = TextReader()

resume = pdf.read("data/resumes/resume.pdf")

jd = text.read("data/jobs/react_native_jd.txt")

matcher = SkillMatcher()

result = matcher.calculate_score(
    resume,
    jd
)

print(result)