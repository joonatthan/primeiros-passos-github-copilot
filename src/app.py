"""
High School Management System API

A super simple FastAPI application that allows students to view and sign up
for extracurricular activities at Mergington High School.
"""

from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
import os
from pathlib import Path

app = FastAPI(title="Mergington High School API",
              description="API for viewing and signing up for extracurricular activities")

# Mount the static files directory
current_dir = Path(__file__).parent
app.mount("/static", StaticFiles(directory=os.path.join(Path(__file__).parent,
          "static")), name="static")

# In-memory activity database
activities = {
   "Clube de Xadrez": {
      "description": "Aprenda estratégias e participe de torneios de xadrez",
      "schedule": "Sextas, 15h30 - 17h",
      "max_participants": 12,
      "participants": ["michael@mergington.edu", "daniel@mergington.edu"]
   },
   "Basquetebol": {
      "description": "Treinamento e competição de basquetebol",
      "schedule": "Terças e quintas, 16h30 - 18h",
      "max_participants": 15,
      "participants": ["lucas@mergington.edu"]
      },
   "Voleibol": {
      "description": "Treinamento técnico e jogos amistosos de voleibol",
      "schedule": "Segundas e quartas, 16h - 17h30",
      "max_participants": 18,
      "participants": ["ana@mergington.edu", "bruno@mergington.edu"]
      },
   "Clube de Teatro": {
      "description": "Desenvolvimento de habilidades teatrais e apresentações",
      "schedule": "Quartas, 14h30 - 16h",
      "max_participants": 25,
      "participants": ["julia@mergington.edu"]
      },
   "Aula de Dança": {
      "description": "Aprenda diferentes estilos de dança",
      "schedule": "Sextas, 16h - 17h",
      "max_participants": 20,
      "participants": ["maria@mergington.edu", "carlos@mergington.edu"]
      },
   "Clube de Debate": {
      "description": "Desenvolva habilidades de argumentação e pensamento crítico",
      "schedule": "Terças, 15h - 16h30",
      "max_participants": 16,
      "participants": ["pedro@mergington.edu"]
      },
   "Clube de Robótica": {
      "description": "Construa e programe robôs para competições",
      "schedule": "Quartas e sextas, 15h - 16h30",
      "max_participants": 14,
      "participants": ["antonio@mergington.edu", "patricia@mergington.edu"]
      },
   "Aula de Programação": {
      "description": "Aprenda fundamentos de programação e desenvolva projetos de software",
      "schedule": "Terças e quintas, 15h30 - 16h30",
      "max_participants": 20,
      "participants": ["emma@mergington.edu", "sophia@mergington.edu"]
   },
   "Educação Física": {
      "description": "Educação física e atividades esportivas",
      "schedule": "Segundas, quartas e sextas, 14h - 15h",
      "max_participants": 30,
      "participants": ["john@mergington.edu", "olivia@mergington.edu"]
   }
}


@app.get("/")
def root():
    return RedirectResponse(url="/static/index.html")


@app.get("/activities")
def get_activities():
    return activities


@app.post("/activities/{activity_name}/signup")
def signup_for_activity(activity_name: str, email: str):
    """Sign up a student for an activity"""
    # Validate activity exists
    if activity_name not in activities:
        raise HTTPException(status_code=404, detail="Atividade não encontrada")

    # Get the specificy activity
    activity = activities[activity_name]

   # Validar se o estudante já está inscrito
    if email in activity["participants"]:
        raise HTTPException(status_code=400, detail="Estudante já está inscrito na atividade")

    # Add student
    activity["participants"].append(email)
    return {"message": f"{email} inscrito(a) em {activity_name} com sucesso"}
