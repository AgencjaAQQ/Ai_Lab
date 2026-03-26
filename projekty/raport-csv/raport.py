import csv
from collections import defaultdict

def wczytaj_csv(sciezka):
    produkty = []
    with open(sciezka, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if not row['nazwa'].strip():
                continue
            produkty.append({
                'nazwa': row['nazwa'].strip(),
                'kategoria': row['kategoria'].strip(),
                'cena': float(row['cena']),
                'stan_magazynowy': int(row['stan_magazynowy']),
                'sprzedaz_miesiac': int(row['sprzedaz_miesiac']),
            })
    return produkty

def generuj_raport(produkty):
    linie = []
    linie.append("=" * 50)
    linie.append("        RAPORT SPRZEDAŻY PRODUKTÓW")
    linie.append("=" * 50)

    # Liczba produktów
    linie.append(f"\nLiczba produktów: {len(produkty)}")

    # Średnia cena
    srednia_cena = sum(p['cena'] for p in produkty) / len(produkty)
    linie.append(f"Średnia cena: {srednia_cena:.2f} zł")

    # Top 3 najlepiej sprzedające się
    top3 = sorted(produkty, key=lambda p: p['sprzedaz_miesiac'], reverse=True)[:3]
    linie.append("\nTop 3 najlepiej sprzedające się produkty:")
    for i, p in enumerate(top3, 1):
        linie.append(f"  {i}. {p['nazwa']} — {p['sprzedaz_miesiac']} szt. ({p['kategoria']})")

    # Kategoria z najwyższą sprzedażą
    sprzedaz_kategorii = defaultdict(int)
    for p in produkty:
        sprzedaz_kategorii[p['kategoria']] += p['sprzedaz_miesiac']

    top_kategoria = max(sprzedaz_kategorii, key=sprzedaz_kategorii.get)
    linie.append(f"\nKategoria z najwyższą sprzedażą: {top_kategoria} ({sprzedaz_kategorii[top_kategoria]} szt.)")

    linie.append("\nSprzedaż wg kategorii:")
    for kat, sprzedaz in sorted(sprzedaz_kategorii.items(), key=lambda x: x[1], reverse=True):
        linie.append(f"  {kat}: {sprzedaz} szt.")

    # Produkty z niskim stanem magazynowym
    niski_stan = [p for p in produkty if p['stan_magazynowy'] < 100]
    niski_stan.sort(key=lambda p: p['stan_magazynowy'])
    linie.append("\nPRODUKTY Z NISKIM STANEM (poniżej 100 szt.):")
    if niski_stan:
        for p in niski_stan:
            linie.append(f"  {p['nazwa']} — {p['stan_magazynowy']} szt. (kategoria: {p['kategoria']})")
    else:
        linie.append("  Brak produktów z niskim stanem magazynowym.")

    linie.append("\n" + "=" * 50)
    return "\n".join(linie)

def main():
    produkty = wczytaj_csv('produkty.csv')
    raport = generuj_raport(produkty)
    print(raport)
    with open('raport.txt', 'w', encoding='utf-8') as f:
        f.write(raport + "\n")
    print("\nRaport zapisany do raport.txt")

if __name__ == '__main__':
    main()
