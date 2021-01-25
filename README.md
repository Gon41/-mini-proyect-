# -minigame-     Guess a number game


The game consists in guessing the number randomly proposed by the computer between 0 and 20.

(using the random.randit function)

I have chosen a random number with random.randit with a range from 0 to 20.

For the player I have made a loop with a counter that goes up to 5 (which are the attempts that the player has to guess the number). If the player has not managed to guess the number in 5 attempts the game ends by printing an end message.

Each number chosen by the player is stored in a sorted list so that the player always knows the numbers chosen.

The machine game works in the same way, but I have not been able to get it to choose the number "rationally" to win.

At the end of the file there is a comparison (between the counters of the player and the machine) to see who has taken longer to choose the number.


