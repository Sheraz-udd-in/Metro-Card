from  .repository import *
from  .model import MetroCard

def balance(mid  ,  balance ):
    metroCard[mid] = MetroCard(mid  ,int(balance) )



def rechargeCard(card  , ammount , src) :
    card.add_balance(ammount)
    station  = stations[src]
    x =  ammount*2/100
    station.add_ammount(x)


def check_in(mid  ,  type  ,  src) :
    card = metroCard[mid]
    fare =  rates[type]
    station = stations[src]

    if (card.src == "AIRPORT" and src == "CENTRAL") or (card.src == "CENTRAL" and src == "AIRPORT") :
        fare =  fare/2
        station.add_discount(fare)

    if card.balance <  fare  :
        rechargeCard(card , fare - card.balance , src)

    card.add_balance(-1*fare)
    card.update_src(src)


    station.add_ammount(fare)
    station.add_passenger(type)


def summary() :
    central  =  stations['CENTRAL']
    print("Total Collection")
    print(central.total_ammount)
    print(central.discount)
    print(central.passengerHistory)
    airport  =  stations['AIRPORT']
    print("Total Collection")
    print(airport.total_ammount)
    print(airport.discount)
    print(airport.passengerHistory)


