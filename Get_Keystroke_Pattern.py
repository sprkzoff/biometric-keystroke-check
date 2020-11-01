from pynput import keyboard
import time

l = []
d = {}

def on_release(key):
    if key == keyboard.Key.esc:
        # Stop listener
        return False

    print('{0} released'.format(
        key))
    t = time.time()
    l.append([key,t])
    if len(l) == 2 :
        d[str(l[0][0]).strip("'")+'-'+str(l[1][0]).strip("'")]=l[1][1]-l[0][1]
        l.pop(0)

# Collect events until released
with keyboard.Listener(
        on_release=on_release) as listener:
    listener.join()

# ...or, in a non-blocking fashion:
listener = keyboard.Listener(
    on_release=on_release)
listener.start()

f = open('key_pattern.csv','a')
for key in d:
    f.write(key+","+str(d[key])+"\n")
f.close()