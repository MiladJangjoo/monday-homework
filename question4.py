# Let’s create an exciting monster battle game! You’ll face off against a formidable monster and aim to defeat it. Here’s an outline to guide you:

# Set initial health values for yourself (the player) and the monster.
# Use a while loop to run the game until either you or the monster has no health left.
# Inside the loop:
# Prompt the player to enter an attack value.
# Subtract the attack value from the monster’s health.
# Check if the monster’s health is 0 or less. If so, exit the loop.
# Generate a random attack value for the monster.
# Subtract the monster’s attack value from the player’s health.
# Check if the player’s health is 0 or less. If so, exit the loop.
# After the loop ends, print the result of the battle (e.g., victory or defeat).
player = 100
monster = 100

while True:
    player_attack=int(input("player please enter attack value"))
    monster -= player_attack
    if monster <= 0 :
        print("player won")
        break
    monster_attack=int(input("monster please enter attack value"))
    player -= monster_attack
    if player <= 0:
        print("monster won")
        break

