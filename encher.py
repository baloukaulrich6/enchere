# TODO 1 PRAGRAMME
# from replit import clear
# valeur_encher ={}
# continu_shoul = False
#
# def find_highes_bidder(bidding_record):
#     highest_bid = 0
#     winner = ""
#     for bidder in bidding_record:
#         bid_amount = bidding_record[bidder]
#         if bid_amount > highest_bid:
#             highest_bid = bid_amount
#             winner = bidder
#     print(f"the winner is {winner} with a bid of ${highest_bid}")
#
# while not continu_shoul:
#     name = input("entre votre nom: \n")
#     prix = int(input('entrer la valeur de votre encher: \n $'))
#     valeur_encher[name] = prix
#     result = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
#     if result == 'no':
#         continu_shoul = True
#         find_highes_bidder(valeur_encher)
    # elif result =='yes':
# clear()

entre_les_enchar = {}
continuer = False
def entre_les_valeur(plus_haute_encher):
    haut_prix = 0
    winner = ""
    for participent in entre_les_enchar:
        valeur_entre =entre_les_enchar[participent]
        if valeur_entre > haut_prix:
            haut_prix = valeur_entre
            winner = participent
    print(f"the winner is {winner} with bid of ${haut_prix}")
while not continuer :
    name = input("entre votre nom: \n")
    prix = int(input('entrer la valeur de votre encher: \n $'))
    entre_les_enchar[name] = prix
    result = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if result == 'no':
        continuer = True
        entre_les_valeur(plus_haute_encher=entre_les_enchar)

