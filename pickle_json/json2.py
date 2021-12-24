import json

blackjack_hand = (8, "Q")

encoded_hand = json.dumps(blackjack_hand)


decoded_hand = json.loads(encoded_hand)

print(encoded_hand) # list
print(decoded_hand) # list