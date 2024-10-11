#6.Écrivez un algorithme qui convertisse un nombre de la base 10 vers la base 2 (en binaire).  Le principe utilisé est celui de la division entière.
# Prenons le chiffre 19 pour le convertir en base 2.
# La division entière de 19 par 2 donne un quotient de 9 et un reste de 1.
# La division entière de 9 par 2 donne un quotient de 4 et un reste de 1.
# Plaçons les restes dans l’ordre inverse de leur apparition, nous obtenons « 11 ».  La division de 4 par 2 donne un quotient de 2 et un reste de 0.
# L’accumulation des restes donne « 011 ».
# La division de 2 par 2 donne un quotient de 1 et un reste de 0.
# L’accumulation des restes donne « 0011 ».
# La division de 1 par 2 donne un quotient de 0 et un reste de 1.
# L’accumulation des restes donne « 10011 ».
# La conversion s’arrête là et le chiffre 19 converti en base 2 est « 10011 »

nbConvert=int(input("Veuillez entrer un nombre à convertir : "))
decimal=nbConvert
bin=""

if nbConvert ==0:
    bin="0"
else:
    while decimal > 0:
        reste= decimal % 2
        bin=str(reste)+bin
        decimal//=2

print(f"{nbConvert} en binaire est {bin}")