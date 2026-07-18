from app.ats.extractor import SkillExtractor


sample_resume = """
Senior React Native Developer

Skills:
React Native
Redux Toolkit
Firebase
TypeScript
Git
GitHub
REST API
"""

extractor = SkillExtractor()

skills = extractor.extract(sample_resume)

print(skills)