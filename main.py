import joke as joke_self
import t2s as t2s_self


if __name__ == "__main__":
    for i in range(int(input("How many Vids do you want?\n$"))):
        
        joke = joke_self.run()
        t2s_self.create_voice(joke,int(str(i)))
        print(f"Audio createt with Joke:{joke[0]}{joke[1]}")
    