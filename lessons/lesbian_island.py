"""EX06 - Create your own adventure!"""

__author__ = "730557757"


from random import randint


SMILE: str = "\U0001F603"
FROWN: str = "\U0001F928"
PEACH: str = "\U0001F351"
CAT: str = "\U0001F639"
FINGER: str = "\U0001F91F"
HAND: str = "\U0001F590"
points: int
player: str


def main() -> None:
    """Places the user in a simulated middle school environment, where the goal is to make friends."""
    global points
    points = 0
    global player
    greet()
    running: bool = True
    while running is True:
        options: str = input(f"Hi {player}! You currently have a total of {points} points. What would you like to do next? make a friend, play dodgeball, or end game: ")
        if options == "play dodgeball":
            points = dodgeball(points)
            continue
        elif options == "make a friend":
            friend()
            continue
        else:
            end_game: str = (f"Aw, okay {FROWN}. Thanks for playing Middle School Simulator {SMILE}! You earned a total of {points} points. We'll see you next time, {player}!")
            print(end_game)
            running = False
    return


def greet() -> None:
    """Greets player and asks their name."""
    global player
    player = input("Heyy there! I love your look. What's your name? name: ")
    print("Here, you'll be able to meet hot chicks who dig other hot chicks and/or play dodgeball. Hint: the best way to win a girl and money is to be aggressive and have spirit!")


def friend() -> None:
    """User should try to make a friend by being petty to others but nice to the character with whom player is conversing."""
    global points
    global player
    small_talk: str = input(f"Hey, carpet-muncher? Are you good at sex? great or terrible: ")
    if small_talk == "great":
        points += 1
        gossip: str = input(f"{SMILE} I rate you a {randint(5, 10)} out of 10. Can I get yodffu a drink? yes or no: ")
        if gossip == "yes":
            points += 1
            plans: str = input(f"{SMILE} Tea. Do you want to listen to my amazing sex playlist? yes or no: ")
            if plans == "yes":
                points += 1
                friend_made: str = input(f"{SMILE} Sick, sounds like a plan, {player}! Can I get your digits ? yes or no: ")
                if friend_made == "yes":
                    points += 1
                    do_it_fart: str = input(f"Do that ass be fartin'? {PEACH} yes or no: ")
                    if do_it_fart == "yes":
                        points += 1
                        go_upstairs: str = input(f"Hot. Let's go upstairs! Are you coming? yes or no: ")
                        if go_upstairs == "yes":
                            points += 1
                            return
                    print(f"{SMILE} Congrats, {player}, you made a friend!")
                    return
                else:
                    points -= 1
                    print(f"{FROWN} Well, {player}, I ALMOST let you tickle my pickle. Maybe next time.")
                    return
            else:
                points -= 1
                no_plans: str = input(f"{FROWN} Oh, well that's too bad, can I at least get your Instagram? yes or no: ")
                if no_plans == "yes":
                    points += 1
                    print(f"{SMILE} Congrats, {player}, you made an online friend!")
                    return
                else: 
                    points -= 1
                    print(f"{FROWN} Well, you didn't make a friend, so maybe say yes next time, {player}!")
                    return
        else:
            points -= 1
            print(f"{FROWN} Oh okay, so you're too nice to tell the truth. Maybe go be boring somewhere else, {player}.")
            return
    else:
        points -= 1
        print(f"{FROWN} Oh wow, that sucks. Maybe go be boring somewhere else, {player}.")
        return


def dodgeball(points: int) -> int:
    """User should try their best at gym dodgeball."""
    global player
    if points >= 4:
        red_team: str = input(f"Alright, {player}, prepare yourself for gym dodgeball. You've been selected for the red team, so you better be ready to go crazy on that court. Are you ready? yes or no: ")
        if red_team == "yes":
            points += 1
            play_ball: str = input(f"{SMILE} Glad to hear it! Now go kick some butt! kick butt or don't kick butt: ")
            if play_ball == "kick butt":
                points += 1
                print(f"{SMILE} Thanks for supporting red team, {player}, we'd love to have you back some time!")
                return points
            else:
                points -= 1
                print(f"{FROWN} You didn't really show up like you said you would, {player}. Maybe work on your skills or play for blue team instead.")
                return points
        else:
            points -= 1
            print(f"{FROWN} You seem pretty lame, {player}. You should go play for blue team instead.")
            return points 
    else:
        blue_team: str = input(f"Okay, {player}, we don't have much faith in you, but you must participate in this game of gym dodgeball. You've been put on the blue team. Are you ready? yes or no: ")
        if blue_team == "yes":
            points += 1
            print(f"{SMILE} Glad to hear it, {player}. Thanks for playing with blue team.")
            return points
        else:
            points -= 1
            print(f"{FROWN} We didn't have much faith in you in the first place, yet you still failed us, {player}. Go get a more competitive spirit perhaps.")
            return points 


if __name__ == "__main__":
    main()