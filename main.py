from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

questions = [
    {"id": 1, "question": "Jaka jest stolica Polski?", "options": ["Kraków", "Warszawa", "Gdańsk", "Poznań"], "correct": 1},
    {"id": 2, "question": "Ile to 2 + 2?", "options": ["3", "4", "5", "6"], "correct": 1},
    {"id": 3, "question": "Jaki język programowania używa FastAPI?", "options": ["Java", "C++", "Python", "JavaScript"], "correct": 2},
    {"id": 4, "question": "Które zwierzę miauczy?", "options": ["Pies", "Kot", "Krowa", "Koń"], "correct": 1},
    {"id": 5, "question": "Który ocean jest największy?", "options": ["Atlantycki", "Spokojny", "Indyjski", "Arktyczny"], "correct": 1},
    {"id": 6, "question": "Kto napisał 'Pan Tadeusz'?", "options": ["Mickiewicz", "Słowacki", "Prus", "Sienkiewicz"], "correct": 0},
    {"id": 7, "question": "Ile kontynentów jest na Ziemi?", "options": ["5", "6", "7", "8"], "correct": 2},
    {"id": 8, "question": "Który kolor powstaje z połączenia czerwonego i niebieskiego?", "options": ["Zielony", "Pomarańczowy", "Fioletowy", "Brązowy"], "correct": 2},
    {"id": 9, "question": "Jaki jest symbol chemiczny tlenu?", "options": ["T", "O", "Ox", "H"], "correct": 1},
    {"id": 10, "question": "Kto był pierwszym człowiekiem w kosmosie?", "options": ["Neil Armstrong", "Jurij Gagarin", "Buzz Aldrin", "Chris Hadfield"], "correct": 1},
    {"id": 11, "question": "Ile nóg ma pająk?", "options": ["6", "8", "10", "12"], "correct": 1},
    {"id": 12, "question": "Jak nazywa się najmniejsza planeta Układu Słonecznego?", "options": ["Mars", "Merkury", "Pluton", "Wenus"], "correct": 1},
    {"id": 13, "question": "Który kraj ma najwięcej ludności?", "options": ["USA", "Chiny", "Indie", "Brazylia"], "correct": 1},
    {"id": 14, "question": "Jak nazywa się największy ssak na Ziemi?", "options": ["Słoń", "Wieloryb", "Żyrafa", "Hipopotam"], "correct": 1},
    {"id": 15, "question": "Co oznacza skrót CPU?", "options": ["Central Processing Unit", "Computer Power Unit", "Central Program Unit", "Control Panel Unit"], "correct": 0},
    {"id": 16, "question": "Który pierwiastek chemiczny ma symbol H?", "options": ["Hel", "Wodór", "Rtęć", "Tlen"], "correct": 1},
    {"id": 17, "question": "Ile dni ma rok przestępny?", "options": ["365", "366", "364", "360"], "correct": 1},
    {"id": 18, "question": "Która planeta nazywana jest Czerwoną Planetą?", "options": ["Wenus", "Mars", "Merkury", "Neptun"], "correct": 1},
    {"id": 19, "question": "Jakiego koloru jest chlorofil?", "options": ["Zielony", "Niebieski", "Brązowy", "Czerwony"], "correct": 0},
    {"id": 20, "question": "W którym roku rozpoczęła się II wojna światowa?", "options": ["1939", "1945", "1914", "1920"], "correct": 0}
]

@app.get("/")
def serve_frontend():
    return FileResponse("static/index.html")

@app.get("/questions")
def get_questions():
    return [{"id": q["id"], "question": q["question"], "options": q["options"]} for q in questions]

@app.post("/answer")
def check_answer(data: dict):
    q_id = data.get("id")
    user_answer = data.get("answer")

    question = next((q for q in questions if q["id"] == q_id), None)
    if question is None:
        raise HTTPException(status_code=404, detail="Pytanie nie istnieje")

    is_correct = (question["correct"] == user_answer)
    return {"correct": is_correct}
