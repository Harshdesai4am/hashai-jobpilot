from app.ats.calculator import ATSCalculator

resume_skills = [
    "react native",
    "firebase",
    "redux toolkit",
    "typescript",
    "git"
]

jd_skills = [
    "react native",
    "typescript",
    "graphql",
    "firebase",
    "aws"
]

calculator = ATSCalculator()

result = calculator.calculate(
    resume_skills,
    jd_skills
)

print(result)