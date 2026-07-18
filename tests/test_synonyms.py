from app.ats.extractor import SkillExtractor

text = """
Senior RN Developer

React-Native
RTK
RESTful API
Amazon Web Services
"""

extractor = SkillExtractor()

print(extractor.extract(text))