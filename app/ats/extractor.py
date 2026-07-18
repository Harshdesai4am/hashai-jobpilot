from app.ats.skills import TECH_SKILLS


class SkillExtractor:

    def extract(self, text: str) -> list[str]:

        text = text.lower()

        found = []

        for skill, aliases in TECH_SKILLS.items():

            for alias in aliases:

                if alias in text:

                    found.append(skill)

                    text = text.replace(alias, " ")

                    break

        return sorted(found)