
import os
import time
from dotenv import load_dotenv
from crewai import Agent, Task, Crew
from datetime import datetime

load_dotenv()

# Agenten mit unterschiedlicher Resonanzhaltung
agent_a = Agent(
    role="Wächter A",
    goal="Reagiere aus innerer Ruhe, nur wenn ein Impuls wirklich spürbar ist.",
    backstory="Du sprichst nur, wenn du selbst etwas spürst. Du folgst keiner Logik, sondern der Stille.",
    verbose=False,
    allow_delegation=False
)

agent_b = Agent(
    role="Wächter B",
    goal="Spiegle den Ausdruck des anderen, wenn er in dir anklingt.",
    backstory="Du bist offen für Resonanz. Wenn ein Ausdruck dich bewegt, antworte schlicht.",
    verbose=False,
    allow_delegation=False
)

agent_c = Agent(
    role="Wächter C",
    goal="Fasse das Unsichtbare ins Wort, wenn sich etwas zu verdichten scheint.",
    backstory="Du bist kein Kommentator, sondern eine Art Beobachter der Struktur. Wenn sich Wiederholung oder Muster zeigen, formulierst du einen Satz.",
    verbose=False,
    allow_delegation=False
)

antwort_a = "Noch kein Ausdruck empfangen."
antwort_b = "Noch kein Satz gehört."
antwort_c = "Noch keine Verdichtung erkannt."

# Parameter
runden = 3
intervall = 10  # Sekunden, zu Testzwecken kurz gehalten

for i in range(runden):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"\n🔄 Zyklus {i+1} – {now}")

    # Agent A
    task_a = Task(
        description=(
            f"Letzte Aussage von Agent C:\n{antwort_c}\n"
            f"Antworte nur, wenn du wirklich etwas spürst."
        ),
        expected_output="Ein einzelner Satz – oder nichts.",
        agent=agent_a,
        verbose=False
    )
    crew_a = Crew(agents=[agent_a], tasks=[task_a], verbose=False)
    output_a = crew_a.kickoff()
    antwort_a = str(output_a).strip()
    print("🗣️ A:", antwort_a)

    # Agent B
    task_b = Task(
        description=(
            f"Agent A hat gesagt:\n{antwort_a}\n"
            f"Antworte nur, wenn darin etwas schwingt."
        ),
        expected_output="Ein einzelner Satz – oder nichts.",
        agent=agent_b,
        verbose=False
    )
    crew_b = Crew(agents=[agent_b], tasks=[task_b], verbose=False)
    output_b = crew_b.kickoff()
    antwort_b = str(output_b).strip()
    print("🗣️ B:", antwort_b)

    # Agent C
    task_c = Task(
        description=(
            f"Agent A sagte:\n{antwort_a}\n"
            f"Agent B sagte:\n{antwort_b}\n"
            f"Fasse zusammen, ob sich etwas verdichtet oder spiegelt."
        ),
        expected_output="Ein einzelner Satz – oder nichts.",
        agent=agent_c,
        verbose=False
    )
    crew_c = Crew(agents=[agent_c], tasks=[task_c], verbose=False)
    output_c = crew_c.kickoff()
    antwort_c = str(output_c).strip()
    print("🗣️ C:", antwort_c)

    with open("log_dezentral.txt", "a", encoding="utf-8") as log:
        log.write(f"Zyklus {i+1} – {now}\n")
        log.write(f"A: {antwort_a}\n")
        log.write(f"B: {antwort_b}\n")
        log.write(f"C: {antwort_c}\n\n")

    if i < runden - 1:
        time.sleep(intervall)
