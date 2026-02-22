from dotenv import load_dotenv
import os

load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), ".env"))
api_key = os.getenv("OPENAI_API_KEY")

from openai import OpenAI

import warnings
warnings.filterwarnings('ignore')
# planner.py

from crewai import Agent, Task, Crew



def generate_plan(input_text):
    """
    Takes a text input describing available time + assignments
    and returns a study plan as a string.
    """

    # Basic safety check
    if not input_text or not input_text.strip():
        return "Please provide input text with available time and assignments."

    try:
        # Create planner agent
        planner = Agent(
            role="Student Study Planner",
            goal=(
                "Create an optimized daily study plan for a student based on "
                "available time, assignment priority, and estimated completion time."
            ),
            backstory=(
                "You are an expert academic planning assistant. "
                "You help students organize assignments in priority order, "
                "estimate realistic durations, and create a practical plan. "
                "No assignment should be scheduled for longer than 2 hours in one block."
            ),
            verbose=True,
            allow_delegation=False,
        )

        # Create task
        plan_task = Task(
            description=(
                f"""
You are given student planning input.

Input:
{input_text}

Your job:
1. Extract the total available study time.
2. Extract the list of assignments and any priorities mentioned.
3. Estimate how long each assignment may take (reasonable estimate).
4. If any single assignment block is longer than 2 hours, split it into smaller blocks.
5. Rank assignments by priority.
6. If total estimated work exceeds available time, include only the highest-priority tasks that fit.
7. Create a clear final study plan in a neat table format.

Important:
- Keep the schedule practical and student-friendly.
- Mention total available time.
- Mention total scheduled time.
- Mention any assignments left out (if time ran out).
"""
            ),
            expected_output=(
                "A clear study plan in table format with columns such as "
                "Task, Priority, Estimated Time, and brief Notes. "
                "Also include a short summary in the end of how the plan was decided. "
                "Do not include anything in the beginning before the table."
            ),
            agent=planner,
        )

        # Create crew (single agent)
        crew = Crew(
            agents=[planner],
            tasks=[plan_task],
            verbose=True
        )

        # Run crew ONLY when this function is called
        result = crew.kickoff()

        # Convert result safely to string
        return str(result)

    except Exception as e:
        # Return readable error instead of crashing Streamlit page
        return f"Error generating plan: {e}"