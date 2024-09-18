# Author: <Förnamn Efternamn>
# Date: 2023-10-12

def main():
    print("Ei23 - genrep praktiskt prov ht24")
    resistors_input = input("Ange resistorer: ")
    
    if resistors_input.strip() == "":
        series_resistance = 0
        parallel_resistance = 0
    else:
        resistors = list(map(float, resistors_input.split()))
        series_resistance = sum(resistors)
        parallel_resistance = 1 / sum(1 / r for r in resistors)
    
    print(f"Serieresistans: {series_resistance}")
    print(f"Parallellresistans: {parallel_resistance}")

if __name__ == "__main__":
    main()
