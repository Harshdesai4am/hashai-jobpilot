import re


class SkillMatcher:

    def extract_skills(self, text: str):

        words = re.findall(r"[A-Za-z0-9.+#-]+", text.lower())

        return set(words)

    def calculate_score(self, resume: str, jd: str):

        resume_skills = self.extract_skills(resume)

        jd_skills = self.extract_skills(jd)

        matched = resume_skills.intersection(jd_skills)

        missing = jd_skills - resume_skills

        score = 0

        if len(jd_skills) > 0:
            score = round(
                len(matched) / len(jd_skills) * 100
            )

        return {
            "score": score,
            "matched": sorted(matched),
            "missing": sorted(missing)
        }