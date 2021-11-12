print(dealt_cards)
        if str(dealt_cards[0]['cards'][0]['value']=="JOKER"):
            dealt_cards.remove("JOKER")
            print("Joker removed")
            dealt_cards.insert((requests.get("https://deckofcardsapi.com/api/deck/"+deck_id+"/draw/?count=1")).json(),[0]['cards'][0])
        if str(dealt_cards[0]['cards'][1]['value']=="JOKER"):
            dealt_cards.remove("JOKER")
            print("Joker removed")
            dealt_cards.insert((requests.get("https://deckofcardsapi.com/api/deck/"+deck_id+"/draw/?count=1")).json(),[0]['cards'][1])
        if str(dealt_cards[0]['cards'][2]['value']=="JOKER"):
            dealt_cards.remove("JOKER")
            print("Joker removed")
            dealt_cards.insert((requests.get("https://deckofcardsapi.com/api/deck/"+deck_id+"/draw/?count=1")).json(),[0]['cards'][2])
        if str(dealt_cards[1]['cards'][0]['value']=="JOKER"):
            dealt_cards.remove("JOKER")
            print("Joker removed")
            dealt_cards.insert((requests.get("https://deckofcardsapi.com/api/deck/"+deck_id+"/draw/?count=1")).json(),[1]['cards'][0])
        if str(dealt_cards[1]['cards'][1]['value']=="JOKER"):
            dealt_cards.remove("JOKER")
            print("Joker removed")
            dealt_cards.insert((requests.get("https://deckofcardsapi.com/api/deck/"+deck_id+"/draw/?count=1")).json(),[1]['cards'][1])
        if str(dealt_cards[1]['cards'][2]['value']=="JOKER"):
            dealt_cards.remove("JOKER")
            print("Joker removed")
            dealt_cards.insert((requests.get("https://deckofcardsapi.com/api/deck/"+deck_id+"/draw/?count=1")).json(),[1]['cards'][2])
        if(num_of_players>2):
            if str(dealt_cards[2]['cards'][0]['value']=="JOKER"):
                dealt_cards.remove("JOKER")
                print("Joker removed")
                dealt_cards.insert((requests.get("https://deckofcardsapi.com/api/deck/"+deck_id+"/draw/?count=1")).json(),[2]['cards'][0])
            if str(dealt_cards[2]['cards'][1]['value']=="JOKER"):
                dealt_cards.remove("JOKER")
                print("Joker removed")
                dealt_cards.insert((requests.get("https://deckofcardsapi.com/api/deck/"+deck_id+"/draw/?count=1")).json(),[2]['cards'][1])
            if str(dealt_cards[2]['cards'][2]['value']=="JOKER"):
                dealt_cards.remove("JOKER")
                print("Joker removed")
                dealt_cards.insert((requests.get("https://deckofcardsapi.com/api/deck/"+deck_id+"/draw/?count=1")).json(),[2]['cards'][2])
            if(num_of_players>3):
                if str(dealt_cards[3]['cards'][0]['value']=="JOKER"):
                    dealt_cards.remove("JOKER")
                    print("Joker removed")
                    dealt_cards.insert((requests.get("https://deckofcardsapi.com/api/deck/"+deck_id+"/draw/?count=1")).json(),[3]['cards'][0])
                if str(dealt_cards[3]['cards'][1]['value']=="JOKER"):
                    dealt_cards.remove("JOKER")
                    print("Joker removed")
                    dealt_cards.insert((requests.get("https://deckofcardsapi.com/api/deck/"+deck_id+"/draw/?count=1")).json(),[3]['cards'][1])
                if str(dealt_cards[3]['cards'][2]['value']=="JOKER"):
                    dealt_cards.remove("JOKER")
                    print("Joker removed")
                    dealt_cards.insert((requests.get("https://deckofcardsapi.com/api/deck/"+deck_id+"/draw/?count=3")).json(),[3]['cards'][2])
