# AI TRAINING OS

## 🎯 CEL
Stać się ekspertem w pracy z Claude Code (automatyzacje, AI workflow, leverage w biznesie)

---

## 💻 ŚRODOWISKO
- MacBook Air M1
- Terminal: używany świadomie
- Homebrew: zainstalowany i działa (v5.1.1)
- Git: zainstalowany i skonfigurowany (user.name + user.email)
- Claude Code (CLI): zainstalowany i skonfigurowany
- Konto Claude: plan Pro (aktywny)

---

## 📍 AKTUALNY ETAP
Etap 1: Setup środowiska + podstawy Git + wejście w Claude Code

Zrobione:
- [x] instalacja Homebrew
- [x] konfiguracja PATH
- [x] instalacja Git
- [x] konfiguracja Git (user.name, user.email)
- [x] stworzenie pierwszego repo (`ai-lab`)
- [x] inicjalizacja Git (`git init`)
- [x] stworzenie pliku `ai_os.md`
- [x] pierwszy commit (Initial AI OS file)
- [x] instalacja Claude Code (CLI)
- [x] konfiguracja i logowanie do Claude Pro
- [x] pierwsze uruchomienie Claude Code w terminalu

W trakcie:
- [ ] zrozumienie workflow Git (add / commit / status)
- [ ] budowa pierwszego realnego use case

---

## 🧠 KLUCZOWE ZROZUMIENIE

### System
- Terminal = komunikacja z komputerem
- Shell (zsh) = interpreter komend
- macOS = system operacyjny

### Narzędzia
- Homebrew = menedżer pakietów (instalacja narzędzi)
- Git = system kontroli wersji (historia zmian, snapshoty)
- Repozytorium = folder + historia zmian

### AI
- Claude Code = agent AI do pracy z kodem i automatyzacjami
- To NIE język programowania
- To „worker”, który wykonuje zadania
- Claude działa na folderze (projekcie), nie w abstrakcji

---

## 🔁 WORKFLOW (AKTUALNY)

1. Otwieram terminal
2. `cd [folder projektu]`
3. `claude`
4. (opcjonalnie) drugi terminal → `open .`
5. Praca z agentem (analiza / tworzenie / edycja plików)
6. `git add`
7. `git commit`
8. Iteracja

---

## 📅 DZIENNIK POSTĘPÓW

### Dzień 1
- setup środowiska (Homebrew, Git)
- stworzenie repozytorium
- pierwsze zrozumienie działania terminala i Git

---

### Dzień 2 (24.03.2026)

#### ✅ Co zostało zrobione

- instalacja i uruchomienie Claude Code (CLI)
- konfiguracja połączenia z kontem Claude Pro (login przez przeglądarkę)
- rozwiązanie problemów z autoryzacją (restart terminala + ponowna inicjalizacja)
- pierwsze poprawne uruchomienie Claude Code w terminalu
- zrozumienie modelu działania (Claude jako agent pracujący na folderze)
- poznanie podstawowych komend i interakcji (prompt, analiza folderu)
- zrozumienie różnicy: Chat vs Claude Code (rozmowa vs działanie na plikach)
- praca równoległa: Claude (terminal) + Finder (open .)
- ogarnięcie workflow pracy na dwóch terminalach

---

#### 🧠 Kluczowe zrozumienia (Dzień 2)

- Claude Code ≠ chatbot → to agent działający na plikach i środowisku
- folder = projekt (nie ma "projektów" w UI jak w czacie)
- pliki = pamięć długoterminowa (obejście limitu kontekstu)
- Claude działa najlepiej, gdy ma strukturę (foldery, pliki, dane)
- można pracować w języku polskim (opis), a kod generuje się automatycznie
- Claude Pro ≠ Claude Code API → CLI działa na subskrypcji, nie na darmowym planie
- terminal to środowisko pracy, nie tylko narzędzie do komend

---

#### ⚠️ Problemy i rozwiązania

- ❌ brak reakcji po wpisaniu kodu → rozwiązanie: restart terminala i ponowna inicjalizacja
- ❌ blokada terminala przez Claude → rozwiązanie: drugi terminal (Cmd + N)
- ❌ brak działania na wersji free → rozwiązanie: upgrade do Claude Pro

---

#### 🚀 Status

👉 Claude Code: DZIAŁA  
👉 Środowisko: GOTOWE  
👉 Gotowość do realnych use-case’ów: 80%

---

## 🔜 NEXT STEPS

1. lepsze zrozumienie Git (logika zmian)
2. praca na plikach (edycja, commitowanie zmian)
3. pierwsza automatyzacja (realny use case biznesowy)
4. budowa struktury projektów (foldery + dane + logika)

---

## ⚠️ PROBLEMY / BLOKERY

- Git jeszcze nie jest w pełni intuicyjny (normalne na tym etapie)
- brak doświadczenia w pracy w terminalu (już szybko maleje)

---

## 🧠 NOTATKI

- NIE używać transkrypcji rozmów
- przenosimy STAN, nie historię
- każdy projekt = repo Git (jeśli ma wartość)
- Git = „kamera + historia zmian”, nie środowisko pracy
- pliki = pamięć systemu (ważniejsze niż rozmowa)

---

## 🚀 META

Tryb pracy:
- 1h dziennie
- jeden krok na raz
- nacisk na zrozumienie + praktykę

Mentor:
- ChatGPT jako prowadzący proces
- decyzja o przejściu na płatne narzędzia w momencie sensu biznesowego

---

## 🛠️ SKONFIGUROWANE NARZĘDZIA

### Tailscale — zdalny dostęp do Maka
- Prywatna sieć VPN między urządzeniami
- Mac: `100.102.70.45` (macbook-air-agencja)
- iPhone: `100.74.229.51` (iphone-15)
- Konto: piotr@agencjaaqq.pl
- **Jak używać:** działa automatycznie w tle. iPhone i Mac widzą się zawsze, niezależnie od sieci.

### SSH — terminal zdalny
- SSH włączone na Maku (Ustawienia → Ogólne → Udostępnianie → Zdalny login)
- Połączenie z iPhone: Termius → host `100.102.70.45`, user `agencjaaqq`
- **Jak używać:** otwórz Termius na iPhonie, kliknij host MacBook AQQ → masz pełny terminal na Maku

### tmux — trwałe sesje terminala
- Sesja `main` uruchamia się automatycznie przy każdym logowaniu SSH
- Rozłączenie nie zabija sesji — wracasz dokładnie tam gdzie skończyłeś
- **Podstawowe komendy:**
  - `tmux attach -t main` — dołącz do istniejącej sesji
  - `Ctrl+A, C` — nowe okno w tmux
  - `Ctrl+A, N` — następne okno
  - `Ctrl+A, D` — odłącz (sesja działa dalej)

### Poczta — konfiguracja IMAP (Mail.app + webmail)
- Konto AQQ: IMAP s135.cyber-folks.pl:993 SSL, SMTP s135.cyber-folks.pl:465 SSL
- Konto Gmail: pit.gajda@gmail.com — IMAP przez Google
- Folder Wysłane AQQ → "Sent" na serwerze (7044 maili)
- Pełna synchronizacja dwustronna: wysłane z Mail.app = widoczne w webmailu i na iPhonie
- Webmail Cyberfolks: https://cyberfolks.pl/logowanie-poczta/
- **Ważne:** jeśli Gmail Wysłane pokazuje 0 — wyłącz filtr "Nieczytane" w prawym górnym rogu

### Termius — SSH z iPhone'a
- Zainstalowany, zalogowany (piotr@agencjaaqq.pl), host skonfigurowany
- Plan darmowy — wystarczy do SSH
- **Workflow iPhone → Mac:**
  1. Otwórz Termius
  2. Kliknij `MacBook AQQ - Tailscale`
  3. `cd ~/ai-lab` (lub inny projekt)
  4. `claude` — uruchamiasz Claude Code na Maku z iPhone'a

### Screenshoty
- Zapisują się na Pulpicie I kopiują do schowka jednocześnie
- Skonfigurowane przez `defaults write`

---

## Struktura repo

Repozytorium `ai-lab` podzielone jest na trzy główne foldery:

```
ai-lab/
├── nauka/              # Materiały szkoleniowe i dokumentacja nauki
│   ├── ai_os.md        # Ten plik — główny dokument referencyjny
│   ├── dziennik.md     # Codzienny dziennik nauki (chronologiczny)
│   └── notatki/        # Pliki tematyczne (np. jak działa Claude Code)
├── projekty/           # Projekty klienckie
│   └── betondur/       # Skrypty Python + dane xlsx — klient Betondur
└── narzedzia/          # Narzędzia pomocnicze i konfiguracje
    └── PocztyAgencjaAQQ.mobileconfig  # Profil konfiguracyjny poczty (iOS/macOS)
```

Pliki w korzeniu repo: `CLAUDE.md` (instrukcje dla Claude Code), `README.md` (opis repo na GitHub).