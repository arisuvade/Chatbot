import random
from responses_list import quotes, jokes, rockpaperscissor


def responses_handler(msg: str) -> str | None:
    msg = msg.lower()

    # Help.
    if msg == "!help":
        return '`You can type some greetings: like hello, hi, and hey. \
Also, "quote" or "quotes" to get quotes, "joke" or "jokes" to get jokes, \
"flip" or "coin" to flip a coin, "roll" or "dice" to roll a dice, and \
"rock", "paper", or "scissor" to play rock, paper, and scissors. \
Type "?" at the start of the command to get direct message by DigiBot.`'

    # Greetings.
    if msg in ("hi", "hello", "hey"):
        return "Hello, human!"

    # Sentences.
    match msg:
        case "quote" | "quotes":
            return random.choice(quotes)
        case "joke" | "jokes":
            return random.choice(jokes)

    # Games.
    match msg:
        case "flip" | "coin":
            return random.choice(("Heads", "Tails"))
        case "roll" | "dice":
            return f"{random.randint(1, 6)}"
        case "rock" | "paper" | "scissor":
            com = random.choice(rockpaperscissor)
            if msg == "rock":
                match com:
                    case "Rock":
                        return "Draw!"
                    case "Paper":
                        return "You loss!"
                    case "Scissor":
                        return "You won!"
            elif msg == "paper":
                match com:
                    case "Rock":
                        return "You won!"
                    case "Paper":
                        return "Draw!"
                    case "Scissor":
                        return "You loss!"
            else:
                match com:
                    case "Rock":
                        return "You loss!"
                    case "Paper":
                        return "You won!"
                    case "Scissor":
                        return "Draw!"
