from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class Question(BaseModel):
    id: int
    question: str
    options: List[str]
    correct_answer: int  # indeks 0-3

quiz = [
    Question(id=1, question="Stolica Polski?", options=["Kraków", "Warszawa", "Gdańsk", "Poznań"], correct_answer=1),
    Question(id=2, question="2 + 2 = ?", options=["3", "5", "4", "6"], correct_answer=2),
    Question(id=3, question="Kolor nieba to?", options=["Zielony", "Niebieski", "Czerwony", "Pomarańczowy"], correct_answer=1),
    Question(id=4, question="Największy ocean?", options=["Atlantycki", "Spokojny", "Indyjski", "Arktyczny"], correct_answer=1),
    Question(id=5, question="Które zwierzę miauczy?", options=["Pies", "Kot", "Koń", "Kura"], correct_answer=1),
    Question(id=6, question="Stolica Francji?", options=["Berlin", "Madryt", "Paryż", "Rzym"], correct_answer=2),
    Question(id=7, question="Ile nóg ma pająk?", options=["6", "8", "10", "12"], correct_answer=1),
    Question(id=8, question="Kto napisał 'Pan Tadeusz'?", options=["Mickiewicz", "Sienkiewicz", "Prus", "Rej"], correct_answer=0),
    Question(id=9, question="Ile to 5 * 6?", options=["30", "25", "35", "20"], correct_answer=0),
    Question(id=10, question="Z czego robi się chleb?", options=["Z mleka", "Z mąki", "Z sera", "Z ryżu"], correct_answer=1),
    Question(id=11, question="Który miesiąc ma 28 dni?", options=["Luty", "Każdy", "Maj", "Czerwiec"], correct_answer=1),
    Question(id=12, question="Które z poniższych to owoc?", options=["Marchew", "Ziemniak", "Banan", "Sałata"], correct_answer=2),
    Question(id=13, question="Największy kontynent?", options=["Europa", "Afryka", "Azja", "Australia"], correct_answer=2),
    Question(id=14, question="Polski noblista z 2018?", options=["Tokarczuk", "Miłosz", "Szymborska", "Reymont"], correct_answer=0),
    Question(id=15, question="Który z nich to język programowania?", options=["HTML", "Python", "CSS", "Photoshop"], correct_answer=1),
    Question(id=16, question="Stolica Niemiec?", options=["Paryż", "Berlin", "Monachium", "Hamburg"], correct_answer=1),
    Question(id=17, question="Co wytwarza energia słoneczna?", options=["Wiatraki", "Panele", "Silniki", "Turbiny wodne"], correct_answer=1),
    Question(id=18, question="Najwyższy szczyt świata?", options=["K2", "Mont Blanc", "Everest", "Rysy"], correct_answer=2),
    Question(id=19, question="Kolor śniegu?", options=["Biały", "Czarny", "Zielony", "Niebieski"], correct_answer=0),
    Question(id=20, question="Z ilu liter składa się alfabet polski?", options=["32", "26", "28", "36"], correct_answer=0),
]


@app.get("/questions", response_model=List[Question])
def get_questions():
    return quiz
