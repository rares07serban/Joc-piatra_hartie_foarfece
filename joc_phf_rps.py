import random

print("--- GAME START >:) ---")

optiuni = ["piatra", "hartie", "foarfeca"]

alegere_jucator = input("Alege (piatra, hartie sau foarfeca): ").lower()

if alegere_jucator not in optiuni:
    print("Alegere invalidă! Te rog să scrii unul dintre cele trei cuvinte.")
else:
    alegere_calculator = random.choice(optiuni)
    print("Eu am ales :" + alegere_calculator)

    if alegere_jucator == alegere_calculator:
        print("Este egalitate!")

    elif (alegere_jucator == "piatra" and alegere_calculator == "foarfeca") or \
            (alegere_jucator == "hartie" and alegere_calculator == "piatra") or \
            (alegere_jucator == "foarfeca" and alegere_calculator == "hartie"):
        print("Felicitări, ai câștigat!")

    else:
        print("Haha!!! Ai pierdut! Am câștigat.")