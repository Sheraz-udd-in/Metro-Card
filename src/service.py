from .repository import *
from .model import MetroCard

def balance(mid, balance):
    metroCard[mid] = MetroCard(mid, int(balance))

def rechargeCard(card, amount, src):
    card.add_balance(amount)
    station = stations[src]
    x = int(amount * 2 / 100)
    station.add_amount(x)

def check_in(mid, type, src):
    card = metroCard[mid]
    fare = rates[type]
    station = stations[src]

    if (card.src == "AIRPORT" and src == "CENTRAL") or (card.src == "CENTRAL" and src == "AIRPORT"):
        fare = fare / 2
        station.add_discount(fare)

    if card.balance < fare:
        rechargeCard(card, fare - card.balance, src)

    card.add_balance(-fare)
    card.update_src(src)
    station.add_amount(fare)
    station.add_passenger(type)

def summary():
    central = stations['CENTRAL']
    print(f"TOTAL_COLLECTION CENTRAL {int(central.total_amount)} {int(central.discount)}")
    print("PASSENGER_TYPE_SUMMARY")
    for ptype in sorted(central.passengerHistory):
        print(f"{ptype} {central.passengerHistory[ptype]}")
    airport = stations['AIRPORT']
    print(f"TOTAL_COLLECTION AIRPORT {int(airport.total_amount)} {int(airport.discount)}")
    print("PASSENGER_TYPE_SUMMARY")
    for ptype in sorted(airport.passengerHistory):
        print(f"{ptype} {airport.passengerHistory[ptype]}")
