import logging

# Logging Configuration
logging.basicConfig(
    filename="interview_agent.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Step 1: Job Description API
def get_job_description(role):

    jobs = {
        "Python Developer":
            "Python REST API JSON SQL Git",

        "Data Analyst":
            "Python SQL Excel Power BI"
    }

    return jobs.get(role, "No Description Found")


# Step 2: Skill Extraction
def extract_skills(job_description):

    skills = job_description.split()

    return skills


# Step 3: Question Generator Agent
def generate_questions(skills):

    questions = []

    for skill in skills:
        questions.append(
            f"Explain {skill}?"
        )

    return questions


# Step 4: Answer Evaluation Agent
def evaluate_answer(answer):

    if len(answer) > 20:
        return "Good Answer", 8

    else:
        return "Needs Improvement", 4


# Main Program
role = input("Enter Job Role: ")

logging.info(f"Role Entered: {role}")

job_description = get_job_description(role)

print("\nJob Description:")
print(job_description)

skills = extract_skills(job_description)

print("\nSkills:")
print(skills)

questions = generate_questions(skills)

print("\nInterview Questions:")

for q in questions:
    print(q)

answer = input("\nEnter Your Answer: ")

feedback, score = evaluate_answer(answer)

print("\nFeedback Report")
print("Feedback:", feedback)
print("Score:", score, "/10")

logging.info("Interview Process Completed")