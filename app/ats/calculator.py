class ATSCalculator:

    def calculate(self, resume_skills: list[str], jd_skills: list[str]):

        resume_set = set(skill.lower() for skill in resume_skills)
        jd_set = set(skill.lower() for skill in jd_skills)

        matched = sorted(list(resume_set & jd_set))
        missing = sorted(list(jd_set - resume_set))

        if len(jd_set) == 0:
            score = 0
        else:
            score = round((len(matched) / len(jd_set)) * 100)

        return {
            "score": score,
            "matched": matched,
            "missing": missing
        }