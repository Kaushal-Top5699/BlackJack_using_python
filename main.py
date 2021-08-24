import random

""" This function adds up the given tow cards """
def add(card_one, card_two):
    return card_one + card_two


""" This function deals cards accordingly """
def deal_card(hit):
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    if not hit:
        cardOne = random.choice(cards)
        cardTwo = random.choice(cards)
        return cardOne, cardTwo
    else:
        card = random.choice(cards)
        return card


""" This function directly check whether we have a blackjack at beginning of the game """
def is_blackjack(card_one, card_two):
    blackjack = True
    if card_one == 10:
        if card_two == 11:
            return blackjack
        else:
            return not blackjack
    elif card_two == 10:
        if card_one == 11:
            return blackjack
        else:
            return not blackjack


""" This function is called when user opts for stand and then computer begans to play """
def cpu_score_lower(cpu_total, user_total):
  if cpu_total < 17:
    hit = True
    card = deal_card(hit)
    cpu_total += card
    cpu_score_lower(cpu_total, user_total)
  elif cpu_total > 21:
    print("You Win!, Computer Lose...")
    print(f"Your total: {user_total}\nComputer's total: {cpu_total}")
  elif user_total == cpu_total:
    print("Game Draw!!")
    print(f"Your total: {user_total}\nComputer's total: {cpu_total}")
  elif user_total > cpu_total:
    print("You Win!, Computer Lose...")
    print(f"Your total: {user_total}\nComputer's total: {cpu_total}")
  else:
    print("Computer Wins! You Lose...")
    print(f"Your total: {user_total}\nComputer's total: {cpu_total}")


""" This function is called when user wnats to "hit" or 'stand' """
def hit_or_stand(choice, user_total, cpu_total):
  if choice == "hit":
    hit = True
    card = deal_card(hit)
    sum = user_total + card
    return sum
  else:
    cpu_score_lower(cpu_total, user_total)


""" This function evaluates the scores and tries to find the winner. If not it calls cpu_score_lower() function """
def evaluate_scores(user_total, cpu_total, user_one, user_two, cpu_one, cpu_two):
  if user_total > 21:
    if user_one == 11:
      user_one -= 10
      user_total = user_one + user_two
      if user_total > 21:
        print("Computer Wins!, You Lose...")
        print(f"Computer's cards: [{cpu_one}, {cpu_two}]")
      else:
        choice = input("Would you like to 'hit' or 'stand', type in your choice.\n")
        total = hit_or_stand(choice, user_total, cpu_total)
        evaluate_scores(total, cpu_total, user_one, user_two, cpu_one, cpu_two)
    elif user_two == 11:
      user_two -= 10
      user_total = user_one + user_two
      if user_total > 21:
        print("Computer Wins!, You Lose...")
        print(f"Computer's cards: [{cpu_one}, {cpu_two}]")
      else:
        choice = input("Would you like to 'hit' or 'stand', type in your choice.\n")
        total = hit_or_stand(choice, user_total, cpu_total)
        evaluate_scores(total, cpu_total, user_one, user_two, cpu_one, cpu_two)
    else:
      print("Computer Wins!, You Lose...")
      print(f"Your total: {user_total}\nComputer Total: {cpu_total}")

  else:
    choice = input("Would you like to 'hit' or 'stand', type in your choice.\n")
    total = hit_or_stand(choice, user_total, cpu_total)
    if total == None:
      print("Game End")
    else:
      print(f"Your total: {total}")
      evaluate_scores(total, cpu_total, user_one, user_two, cpu_one, cpu_two)


""" This function adds up the total user and computer score and calls is_blackjack() """
def play_blackjack(choice):
  if choice == "yes":
    hit = False
    user_one, user_two = deal_card(hit)
    cpu_one, cpu_two = deal_card(hit)

    user_total = add(user_one, user_two)
    cpu_total = add(cpu_one, cpu_two)

    all_user_cards = f"[{user_one}, {user_two}]"
    print(f"Your cards: {all_user_cards}")
    print(f"Your total: {user_total}")
    print(f"Computer's one card: {cpu_one}")

    user_blackjack = is_blackjack(user_one, user_two)
    cpu_blackjack = is_blackjack(cpu_one, cpu_two)

    if user_blackjack:
      print("You Win!!")
    elif cpu_blackjack:
      print("Computer Wins!, You Lose..")
      print(f"Computer's cards: [{cpu_one}, {cpu_two}]")
    else:
      evaluate_scores(user_total, cpu_total, user_one, user_two, cpu_one, cpu_two)
  else:
    print("The game has been terminated!")


""" This is the main function. """
while True:
  choice = input("Welcome to BlackJack!!. Type 'yes' to play or 'no' to quit.\n")
  if choice == "yes":
    play_blackjack(choice)
  else:
    print("The game has been terminated!")
    break
