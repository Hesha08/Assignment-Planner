Inspiration: 
Time management is a recurring challenge among college students. Through personal experience and conversations with peers, we oberserved how many students struggle not with 
completing assignments, but with deciding where to start when multiple tasks are on line within a limited time. 
What It Does? 
Assignment Planner is a Streamlit-based web application that generates a structured daily study schedule.
Users need to provide: 
- Total time available to study for the day
- A list of assignments to complete
- A priority level (1-5) for each task.
Based on this input the system:
- Ranks tasks by priority
- Estimates realistic completion times.
- Produces a constraint-aware study plan in a clear table format.
That is if the total work exceeds available time, only the highest-priority tasks are scheduled.
How We Built It? 
The frontend was develpoed using Streamlit to collect structures user inputs and display dynamic results.
The logic is powered by CrewAI-based LLM planning agent. We defined the agent with a clear role, goal and constraints. The agent analyzes the user's avaiable time and assignments
applies priority ranking and time-block rules( no single task longer than 2 hours), and generates a practical dialy schedule.

Environment variables were securely managed using dotenv to handle API keys.

