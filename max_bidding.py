from art import logo
print(logo)
# TODO-1: Ask the user for input
all_bids={}
while True:
    name=input("Enter your name: ")
    bid=int(input("Enter your bid: "))

    # TODO-2: Save data into dictionary {name: price}
    all_bids[name]=bid

    # TODO-3: Whether if new bids need to be added
    while True:
        answer = input("Any other bid remaining? (yes/no): ").lower()
        if answer == "yes":
            print(100*"\n")
            break
        elif answer == "no":
            break
        else:
            print("Wrong input, please enter 'yes' or 'no'.")
    if answer == "no":
        break
# TODO-4: Compare bids in dictionary
max_bid=-1
person=""
for bids in all_bids:
    if all_bids[bids] > max_bid:
        max_bid=all_bids[bids]
        person=bids
print(f"Maximum bid is: {max_bid} and the person is: {person}")
