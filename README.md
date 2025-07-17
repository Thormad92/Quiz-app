# Quiz App – Projekt semestralny

Aplikacja chmurowa zbudowana w FastAPI + HTML + Tailwind CSS, uruchomiona w Railway.

## Autor

**Jacek Gruca – 7520**

---

## Funkcjonalności

- 20 pytań z wiedzy ogólnej
- 4 odpowiedzi do wyboru
- Informacja czy odpowiedź była poprawna
- Licznik poprawnych i błędnych odpowiedzi
- Podpis autora na stronie
- Hosting w Railway
- Docker + FastAPI + Tailwind

---

## Zrzuty ekranu

### Ekran startowy quizu/przykład pytania z odpowiedziami
![APP1](screenshots/APP1.png)

### Informacja o poprawnej odpowiedzi
![APP2](screenshots/APP2.png)

### Informacja o niepoprawnej odpowiedzi
![APP3](screenshots/APP3.png)

### Koniec quizu – wynik końcowy
![APP4](screenshots/APP4.png)

![VS1](screenshots/VS1.png)

![VS2](screenshots/VS2.png)

![VS3](screenshots/VS3.png)

![VS4](screenshots/VS4.png)

---

## Jak uruchomić lokalnie?

git clone https://github.com/Thormad92/quiz-app.git
cd quiz-app
docker build -t quiz-app .
docker run -d -p 8000:8000 quiz-app

Potem otwórz:
http://localhost:8000