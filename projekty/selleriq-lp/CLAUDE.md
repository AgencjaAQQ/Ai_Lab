# Projekt: SellerIQ — Landing Page

## Produkt
SellerIQ — SaaS do analityki i raportowania sprzedaży na Amazon.
Model: subskrypcja miesięczna. CTA: sprzedaż bezpośrednia + 14 dni trial.

## Dwa segmenty klientów
SEGMENT A — Seller: sprzedaje sam na Amazon (50-500+ SKU), Amazon = główne źródło dochodu.
SEGMENT B — Agency/Freelancer: obsługuje klientów marketplace, potrzebuje raportowania white-label lub multi-konto.

## Funkcje BI (co robi produkt)
- Sprzedaż dzienna / tygodniowa / miesięczna
- Realna analiza marży: po kosztach FBA, reklamy, zwrotów, fulfilmentu
- Ranking produktów: bestsellery i "pożeracze budżetu"
- Porównanie okresów: tydzień do tygodnia, miesiąc do miesiąca, YoY
- Ruch organiczny vs płatny — podział kosztów i efektywności
- Predykcje sprzedaży oparte na trendach
- Sugestie budżetu reklamowego
- Kalkulacja fulfilment FBA i FBM
- Wyniki w rozbiciu na rynki: .de .fr .it .es .pl i inne

## Ból klienta — Seller
Panel Amazon = surowe dane. Excel = godziny pracy.
Nie widać realnej marży po wszystkich kosztach.
Nie wiadomo które produkty naprawdę zarabiają a które tylko generują obrót.
Brak predykcji = brak planowania budżetu i stocku.
Wiele rynków = chaos, brak jednego widoku.

## Ból klienta — Agency/Freelancer
Ręczne raportowanie dla każdego klienta = dziesiątki godzin miesięcznie.
Profesjonalne raporty = przewaga konkurencyjna i uzasadnienie fee.
Klienci pytają "co z moją marżą?" — trudno odpowiedzieć bez danych.

## USP (propozycja wartości)
"Jeden dashboard. Wszystkie liczby które mają znaczenie."
Nie dane dla danych — decyzje poparte liczbami.
Realna marża, nie obrotowa iluzja.
Dla sellerów: oszczędzasz 10h/mies. na raportowaniu.
Dla agencji: profesjonalne raporty dla klientów w minutach, nie dniach.

## Cennik — 3 plany
STARTER: dla małego sellera (1 konto, do 500 SKU) — placeholder 99 zł/mies.
PRO: dla średniego sellera (3 konta, unlimited SKU, predykcje) — placeholder 249 zł/mies.
AGENCY: dla agencji/freelancera (10 kont, white-label raporty, priorytetowy support) — placeholder 599 zł/mies.

## Styl wizualny
- Dark mode: tło #0f172a (głęboka noc), powierzchnie #1e293b
- Akcent główny: niebieski #0ea5e9
cat > CLAUDE.md << 'EOF'
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
