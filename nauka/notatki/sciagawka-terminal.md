# Ściągawka — Terminal

## 1. Nawigacja

```bash
pwd                   # gdzie jestem? (print working directory)
ls                    # co jest w tym folderze?
ls -la                # szczegółowy widok (ukryte pliki, uprawnienia)
cd nazwa-folderu      # wejdź do folderu
cd ..                 # wyjdź poziom wyżej
cd ~                  # wróć do katalogu domowego
```

## 2. Tworzenie

```bash
mkdir nazwa-folderu           # utwórz folder
mkdir -p folder/podfolder     # utwórz folder wraz z podfolderami
git init                      # zainicjuj repo Git w bieżącym folderze
git add .                     # dodaj wszystkie zmiany do staging
git add plik.md               # dodaj konkretny plik
git commit -m "opis zmiany"   # zapisz snapshot ze opisem
git status                    # co się zmieniło?
git log --oneline             # historia commitów (skrócona)
```

## 3. Odpalanie Claude Code

```bash
cd ~/ai-lab       # przejdź do folderu projektu
claude            # uruchom Claude Code w tym folderze
```

Drugi terminal (podgląd plików w Finderze):
```bash
open .            # otwórz bieżący folder w Finderze
```

## 4. Schemat nowego projektu — krok po kroku

```bash
# 1. Utwórz folder projektu
mkdir ~/projekty/nowy-projekt

# 2. Wejdź do niego
cd ~/projekty/nowy-projekt

# 3. Zainicjuj Git
git init

# 4. Utwórz pierwszy plik
touch README.md

# 5. Dodaj i commituj
git add README.md
git commit -m "Inicjalizacja projektu"

# 6. Uruchom Claude Code
claude
```

> Zasada: Claude działa na folderze, w którym go uruchamiasz. Zawsze najpierw `cd`, potem `claude`.
