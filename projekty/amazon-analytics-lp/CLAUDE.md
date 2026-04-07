# Projekt: Landing Page — Narzędzie analityki Amazon

## Produkt
SaaS do raportowania i analityki wyników sprzedaży na Amazon.
Model: subskrypcja miesięczna. Sprzedaż bezpośrednia (CTA: "Kup teraz").
Nazwa robocza: SellerIQ (do zmiany).

## Co robi narzędzie (funkcje BI)
- Sprzedaż dzienna / tygodniowa / miesięczna
- Analiza marży i rentowności (realne koszty, fulfilment, koszty reklamy)
- Ranking produktów: bestsellery i słabe pozycje
- Porównanie do poprzednich okresów (trendy)
- Ruch organiczny vs płatny (podział kosztów)
- Predykcje sprzedaży
- Podpowiada budżet reklamowy
- Wyniki w rozbiciu na poszczególne rynki Amazon (multi-marketplace)
- Kalkulacja fulfilment (FBA/FBM)

## Klient docelowy
Sprzedawcy Amazon różnej wielkości — od małych (50-500 SKU) po średnich (500+ SKU).
Amazon jako główne lub istotne źródło dochodu. Potrzebują jasnych danych, nie surowych raportów Sellera.

## Ból klienta (problem który rozwiązujemy)
Panel Amazon daje dane surowe — trzeba je ręcznie łączyć w Excelu.
Nie widać realnej marży po wszystkich kosztach.
Nie wiadomo które produkty naprawdę zarabiają.
Brak predykcji = brak planowania budżetu i stocku.
Sprzedaż na wielu rynkach = chaos w raportowaniu.

## Propozycja wartości (USP)
Jeden dashboard — wszystkie liczby które mają znaczenie.
Nie dane dla danych — decyzje biznesowe poparte liczbami.
Realna marża, nie obrotowa iluzja.

## Styl wizualny LP
- Nowoczesny, minimalistyczny, analityczny
- Ciemne tło (dark mode) z akcentami w kolorze danych: niebieski #0ea5e9 lub zielony #10b981
- Typografia: Inter lub DM Sans (Google Fonts)
- Elementy: wykresy/dashboard jako grafika hero, liczby w dużej skali, ikony danych
- UX sprzedażowy: jasna hierarchia, CTA widoczny 2x (hero + koniec strony)
- Zero clipartów. Zero stockowych zdjęć ludzi przy laptopie.

## Struktura LP (sekcje)
1. HERO — mocny claim + sub-claim + CTA "Zacznij teraz — 14 dni za darmo"
2. PROBLEM — 3 bolączki sprzedawcy (bez narzędzia)
3. ROZWIĄZANIE — co robi produkt (6-8 funkcji z ikonami)
4. SOCIAL PROOF — placeholder: "Zaufało nam X sprzedawców"
5. CENNIK — 2-3 plany subskrypcji (placeholder kwoty)
6. FAQ — 3-4 pytania
7. CTA końcowe — "Zacznij dziś"

## Stack techniczny
- Dwa pliki: index.html + style.css
- Czysty HTML5 + CSS3, zero frameworków
- Responsywny (mobile-first)
- Google Fonts przez CDN
- SVG inline dla ikon (nie zewnętrzne biblioteki)

## Zasady CC
- Pokazuj diff przed każdą zmianą
- Commituj po każdej sekcji
- Komentuj kod po polsku
