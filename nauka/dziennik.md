# CLAUDE CODE MASTER PLAN — DZIENNIK POSTĘPÓW
## Piotr Gajda | Start: 25.03.2026

---

## JAK UŻYWAĆ TEGO PLIKU

### Przed każdą sesją:
1. Otwórz nową konwersację w tym samym projekcie Claude
2. Wklej na start wiadomość według szablonu poniżej (sekcja SZABLON STARTU DNIA)
3. Czekaj na instrukcje od mentora

### Po każdej sesji:
1. Zaktualizuj status dnia poniżej (zmień [ ] na [x], dopisz notatki)
2. Zapisz plik

---

## SZABLON STARTU DNIA

Skopiuj i wklej to na początek każdej nowej konwersacji:

```
Jesteś moim mentorem Claude Code. Prowadzisz mnie przez 30-dniowy kurs.
Moje materiały i plan kursu masz w plikach projektu.

DZIEŃ: [wpisz numer]
DATA: [wpisz datę]

CO ZROBIŁEM WCZORAJ:
[krótko opisz co zrobiłeś — 2-3 zdania]

PROBLEMY / PYTANIA:
[jeśli coś nie działa lub masz pytania — wpisz tutaj]

STATUS ŚRODOWISKA:
- Terminal: działa / nie działa
- Claude Code CLI: działa / nie działa
- Git repo (ai-lab): istnieje / nie istnieje
- Ostatni commit: [wpisz wiadomość ostatniego commita lub "brak"]

GOTOWY. Prowadź mnie przez Dzień [numer].
```

---

## POSTĘPY — FAZA 1: FUNDAMENTY

### Dzień 1 (25.03.2026) — Git podstawy
- Status: [x] ZROBIONY
- Zadania:
  - [x] git status — rozumiem co pokazuje
  - [x] git add — rozumiem staging area
  - [x] git commit — zrobiłem min. 3 commity
  - [x] git log — umiem przejrzeć historię
- Notatki: Analogia przeprowadzkowa: add = pakowanie kartonu, commit = wywiezienie kartonu. Zrobione 6 commitów (w tym aktualizacja ai_os.md, nowy dziennik.md). 5 commitów w historii repo na koniec dnia. Stworzony plik dziennik.md.
- Problemy: brak
- Czas: ~20 min

### Dzień 2 (25.03.2026) — Git branche + GitHub
- Status: [x] ZROBIONY
- Zadania:
  - [x] Git branche: branch, checkout, merge — opanowane
  - [x] Branch test stworzony, plik dodany, zmergowany do main, branch usunięty
  - [x] GitHub: konto sparowane, repo wypchnięte, pliki widoczne online
  - [x] Nowe komendy: git branch, git checkout, git merge, git push
  - [x] Analogia: branch = kopia mieszkania w równoległym wszechświecie
- Notatki: coraz lepiej to kumam
- Problemy: brak drugiego monitora, który usprawniłby pracę ;)
- Czas: ~30 min

### Dzień 3 (25.03.2026) — Claude Code anatomia
- Status: [x] ZROBIONY
- Zadania:
  - [x] /help — znam dostępne komendy
  - [x] /status — rozumiem co CC widzi
  - [x] /clear, /compact — umiem zarządzać kontekstem
  - [x] Notatka: jak CC działa (zapisana w pliku notatki/jak-dziala-cc.md)
- Notatki: CC widzi tylko folder w którym go odpaliłeś. CC widzi pliki w folderze, czyta je na żądanie. Kontekst = pamięć robocza, /compact kompresuje. Ty mówisz CO, CC decyduje JAK. Pierwszy plik stworzony i edytowany przez CC. Commit + push po polsku jednym zdaniem.
- Problemy: brak
- Czas: ~30 min

### Dzień 4 (25.03.2026) — CLAUDE.md
- Status: [x] ZROBIONY
- Zadania:
  - [x] CLAUDE.md stworzony w ai-lab (przez /init)
  - [x] CC rozpoznaje i stosuje instrukcje z CLAUDE.md
  - [x] Rozumiem: po co CLAUDE.md, co w nim pisać
- Notatki: Komenda /init skanuje lokalne repo i generuje CLAUDE.md automatycznie. CC czyta CLAUDE.md przy każdym starcie — to jego brief. Dodane zasady: komunikacja po polsku, potwierdzanie usunięć, git diff przed commitem. CC stosuje zasady w czasie rzeczywistym — sam pytał o potwierdzenie i pokazywał diff. Usunięto test-plik.txt (porządki). CLAUDE.md = brief dla pracownika, każdy projekt powinien mieć swój.
- Problemy: brak
- Czas: ~30 min

### Dzień 5 (26.03.2026) — CC + pliki
- Status: [x] ZROBIONY
- Zadania:
  - [x] CC stworzył strukturę folderów (nauka/, projekty/betondur/, narzedzia/)
  - [x] CC przeniósł pliki używając git mv (zachowana historia)
  - [x] CC wygenerował README.md (opis repo na GitHub)
  - [x] CC edytował ai_os.md — dodał sekcję "Struktura repo"
  - [x] CC stworzył ściągawkę terminala (nauka/notatki/sciagawka-terminal.md)
  - [x] Wszystko commitnięte i spushowane
- Notatki: CC zaproponował strukturę repo jako drzewko → zaakceptowałem → wykonał bez pytania o każdy krok. Wzorzec pracy: propozycja → akceptacja → wykonanie. Pliki śledzone przez Git przenoszone przez git mv (zachowana historia), pliki nieśledzone przez mv + git add. Nowy projekt = folder + git init + claude + CLAUDE.md.
- Problemy: brak
- Czas: ~40 min

### Dzień 6 (26.03.2026) — CC + skrypty
- Status: [x] ZROBIONY
- Zadania:
  - [x] CC napisał skrypt Python analizujący plik CSV (produkty.csv — 15 produktów)
  - [x] Skrypt generuje raport: liczba produktów, średnia cena, top 3 sprzedaży, ranking kategorii
  - [x] Dodana sekcja alertu niskiego stanu magazynowego (poniżej 100 szt.)
  - [x] Raport zapisywany do pliku raport.txt
  - [x] Rozumiem logikę skryptu: wczytanie CSV → obliczenia → zapis raportu
  - [x] Wszystko commitnięte i spushowane
- Notatki: CC napisał skrypt w czystym Pythonie (bez zewnętrznych bibliotek). Wzorzec: jedna funkcja = jedno zadanie (wczytaj_csv / generuj_raport / main). Skrypt modyfikowany na bieżąco — dodano sekcję alertów bez przepisywania całości. Nowe pojęcia: csv.DictReader, defaultdict, lambda, sorted z key=. CC tłumaczy kod logicznie (blokami), nie linię po linii — to wystarczy.
- Problemy: brak
- Czas: ~30 min

### Dzień 7 (27.03.2026) — CC + HTML
- Status: [x] ZROBIONY
- Zadania:
  - [x] Node.js v25.8.1 — zainstalowany i zweryfikowany
  - [x] CC stworzył stronę HTML dla agencji AQQ
  - [x] Strona wyświetla się w przeglądarce (file://)
  - [x] CC edytował stronę na polecenie (granatowy nagłówek, pomarańczowy przycisk)
  - [x] Wszystko commitnięte i spushowane (commit a07fa85)
- Notatki: Wzorzec identyczny jak przy CSV — polecenie po polsku → CC pisze kod → odświeżasz przeglądarkę → widzisz efekt. HTML + CSS generowany przez CC w jednym pliku index.html. CLAUDE.md zadziałał — CC sam pokazał diff i zapytał o potwierdzenie przed commitem. Iteracja działa natychmiast: mówisz co zmienić → CC zmienia → Cmd+R → gotowe.
- Problemy: brak
- Czas: ~30 min

### Dzień 8 — Powtórka + mini-projekt
- Status: [ ] ZROBIONY
- Zadania:
  - [ ] Nowe repo stworzone od zera
  - [ ] CLAUDE.md skonfigurowany
  - [ ] CC wygenerował landing page
  - [ ] Wszystko commitnięte i czyste
- Notatki:
- Problemy:

---

## POSTĘPY — FAZA 2: REALNE PROJEKTY

### Dzień 9 — Landing page #1
- Status: [ ] ZROBIONY
- Notatki:
- Problemy:

### Dzień 10 — Landing page #2
- Status: [ ] ZROBIONY
- Notatki:
- Problemy:

### Dzień 11 — Tailwind CSS
- Status: [ ] ZROBIONY
- Notatki:
- Problemy:

### Dzień 12 — React start
- Status: [ ] ZROBIONY
- Notatki:
- Problemy:

### Dzień 13 — React aplikacja
- Status: [ ] ZROBIONY
- Notatki:
- Problemy:

### Dzień 14 — Porównywarka v1
- Status: [ ] ZROBIONY
- Notatki:
- Problemy:

### Dzień 15 — Porównywarka v2
- Status: [ ] ZROBIONY
- Notatki:
- Problemy:

### Dzień 16 — API + dane
- Status: [ ] ZROBIONY
- Notatki:
- Problemy:

### Dzień 17 — Deploy #1
- Status: [ ] ZROBIONY
- Notatki:
- Problemy:

### Dzień 18 — Deploy #2 + domena
- Status: [ ] ZROBIONY
- Notatki:
- Problemy:

---

## POSTĘPY — FAZA 3: ZAAWANSOWANE WORKFLOW

### Dzień 19 — MCP co to jest
- Status: [ ] ZROBIONY
- Notatki:
- Problemy:

### Dzień 20 — MCP praktyka
- Status: [ ] ZROBIONY
- Notatki:
- Problemy:

### Dzień 21 — Automatyzacja #1
- Status: [ ] ZROBIONY
- Notatki:
- Problemy:

### Dzień 22 — Automatyzacja #2
- Status: [ ] ZROBIONY
- Notatki:
- Problemy:

### Dzień 23 — E-commerce tools
- Status: [ ] ZROBIONY
- Notatki:
- Problemy:

### Dzień 24 — Full-stack projekt
- Status: [ ] ZROBIONY
- Notatki:
- Problemy:

### Dzień 25 — Testowanie + debug
- Status: [ ] ZROBIONY
- Notatki:
- Problemy:

---

## POSTĘPY — FAZA 4: MONETYZACJA

### Dzień 26 — Portfolio setup
- Status: [ ] ZROBIONY
- Notatki:
- Problemy:

### Dzień 27 — Portfolio deploy
- Status: [ ] ZROBIONY
- Notatki:
- Problemy:

### Dzień 28 — Oferta usługowa
- Status: [ ] ZROBIONY
- Notatki:
- Problemy:

### Dzień 29 — Pitch + outreach
- Status: [ ] ZROBIONY
- Notatki:
- Problemy:

### Dzień 30 — Podsumowanie
- Status: [ ] ZROBIONY
- Notatki:
- Problemy:
