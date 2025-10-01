import random
from words import ORD

MAX_FEL = 6 

def maska(ordet, gissningar):
    return " ".join([b if b in gissningar else "_" for b in ordet])

def main():
    hemligt = random.choice(ORD).lower()
    gissade = set()
    fel = set()

    print("Välkommen till Hangman!")
    print(f"Ordet har {len(hemligt)} bokstäver.")
    print(maska(hemligt, gissade))

    while True:
        # Vinst
        if all(b in gissade for b in hemligt):
            print(f"\nRätt! Ordet var: {hemligt}")
            break

        # Förlust
        if len(fel) >= MAX_FEL:
            print(f"\nDu förlorade. Ordet var: {hemligt}")
            break

        gissning = input("Gissa en bokstav: ").strip().lower()

        
        if len(gissning) != 1 or not gissning.isalpha():
            continue

        if gissning in hemligt:
            if gissning not in gissade:
                gissade.add(gissning)
                print("Rätt!")
        else:
            if gissning not in fel:
                fel.add(gissning)
                print("Fel.")

        print(maska(hemligt, gissade))
        print(f"Felgissningar: {len(fel)}/{MAX_FEL}")

if __name__ == "__main__":
    main()