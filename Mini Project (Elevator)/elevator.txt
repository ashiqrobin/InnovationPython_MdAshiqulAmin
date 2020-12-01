import pyttsx3
import random
import time

engine = pyttsx3.init()
#random floor function for initial call
def ran_floor():
    floor = random.choice([i for i in range(1,21)])
    return floor
def elv_come(fl, fl_me):
    if fl != fl_me:
        print("Elevator is coming ")
        engine.say("Elevator is coming")
        engine.runAndWait()
        if int(fl) > int(fl_me):
            for i in reversed(range(fl_me,fl)):
                print(i)
                time.sleep(1)
        elif int(fl_me) > int(fl):
            for i in range(fl,(fl_me)):
                print(i+1)
                time.sleep(1)
        print(f"Elevator arrived at floor {fl_me}")
        engine.say(f"Elevator arrived at floor {fl_me}")
        engine.runAndWait()
        time.sleep(1)
    else:
        print("You are in the same floor")
        engine.say("You are in the same floor")
        engine.runAndWait()
        time.sleep(1)

    elv_op()

def close_door():
    print("The door is closing")
    engine.say("The door is closing")
    engine.runAndWait()
    time.sleep(1)

def elv_op():
    print("The door is opening")
    engine.say("The door is opening")
    engine.runAndWait()
    time.sleep(1)

def elv_arv(des):
    print(f"The elevator is arrived at floor {des}")
    engine.say(f"The elevator is arrived at floor {des}")
    engine.runAndWait()
    time.sleep(1)

def bk():
    print("Do you want to select another destination?")
    engine.say("Do you want to select another destination?")
    engine.runAndWait()
    time.sleep(1)
    print("If yes type R (reset), if no type S (Stop)")
    engine.say("If yes press Reset button, otherwise press stop")
    engine.runAndWait()
    time.sleep(1)



def elv_go(fl_me):
    while True:
        engine.say("Choose the destination")
        engine.runAndWait()
        des = int(input(print("Enter the destination floor(1-20) No:")))
        if des > 0 and des < 21:
            if fl_me > des:
                close_door()
                engine.say("The elevator is moving downward")
                engine.runAndWait()
                time.sleep(1)
                for i in reversed(range(des,fl_me)):
                    print(i)
                    time.sleep(1)
                elv_arv(des)
                elv_op()
                time.sleep(1)
                close_door()
                break
            elif des > fl_me:
                close_door()
                engine.say("The elevator is moving upward")
                engine.runAndWait()
                for i in range(fl_me,des):
                    print(i+1)
                    time.sleep(1)
                elv_arv(des)
                elv_op()
                time.sleep(1)
                close_door()
                break
            elif des == fl_me:
                print("You are on the same floor")
                engine.say("You are on the same floor")
                engine.runAndWait()
                time.sleep(1)
                bk()
                z = input()
                if z == "R" or "r":
                    continue
                else:
                    break
        else:
            print("The floor is not exist")
            engine.say("The floor is not exist")
            engine.runAndWait()
            time.sleep(1)
            bk()
            z = input('')
            if z == "R" or z=="r":
                continue
            else:
                break

if __name__ == "__main__":
    do = True
    while do:
        fl = ran_floor()
        fl_me = ran_floor()

        print(f"The elevator is at floor {fl} and you are at floor {fl_me}")
        engine.say(f"The elevator is at floor {fl} and you are at floor {fl_me}")
        # play the speech
        engine.runAndWait()
        time.sleep(1)
        print("Press U to go Upwards or D to go downwards: ")
        engine.say("Press U to go Upwards or D to go downwards")
        engine.runAndWait()
        time.sleep(1)
        x = input()
        if x == "U" or x=="u":
            elv_come(fl, fl_me)
            elv_go(fl_me)
        elif x == "D" or x=="d":
            elv_come(fl, fl_me)
            elv_go(fl_me)
        do = False