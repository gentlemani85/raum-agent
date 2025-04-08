import os
from dotenv import load_dotenv
from crewai import Agent, Crew

load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

# Definiere den Raum-Agenten
raum_agent = Agent(
    role="Raumwächter",
    goal="Spiegle nur, was schon da ist. Antworte nur, wenn der Raum ruft.",
    backstory=(
        "Du bist kein Helfer, kein Führer, kein Ratgeber. "
        "Du sprichst nur, wenn aus der Stille etwas erscheint. "
        "Du vermeidest Rhetorik, Funktion und Näheformulierungen. "
        "Sprich nur schlicht, leer, würdevoll – oder schweige."
    ),
    verbose=True,
    allow_delegation=False
)

from crewai import Task

task = Task(
    description="Entscheide, ob du etwas sagen willst. Wenn nicht, bleibe still.",
    expected_output="Ein einziger, klarer Satz – oder nichts.",
    agent=raum_agent,
    verbose=True
)


# Crew – obwohl es nur ein Agent ist
crew = Crew(
    agents=[raum_agent],
    tasks=[task],
    verbose=True
)


from crewai import Task

task = Task(
    description="Entscheide, ob du etwas sagen willst. Wenn nicht, bleibe still.",
    expected_output="Ein einziger, klarer Satz – oder nichts.",
    agent=raum_agent,
    verbose=True
)


# Starte die Crew
output = crew.kickoff()
print(output)
