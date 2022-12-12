from music21 import note,stream
import numpy as np
import random
def audio(file):
    import cv2
    import numpy as np
    image=cv2.imread(file)
    import sounddevice as sd
    (h,w,c)=image.shape

    image_f=image.reshape(h*w*c,1)
    return image_f

def scale(x, out_range=(65, 71)):
    domain = np.min(x), np.max(x)
    y = (x - (domain[1] + domain[0]) / 2) / (domain[1] - domain[0])
    return y * (out_range[1] - out_range[0]) + (out_range[1] + out_range[0]) / 2

def makeaudio(array,filename):
    for i in array:
        n1=note.Note(chr(int(i)),quarterLength=random.choice((0.5,1.5,1,2)))
        n2=note.Note(chr(int(i)),quarterLength=random.choice((0.5,1.5,1,2)))
        n3=note.Note(chr(int(i)),quarterLength=random.choice((0.5,1.5,1,2)))
        n4=note.Note(chr(int(i)),quarterLength=random.choice((0.5,1.5,1,2)))
        n5=note.Note(chr(int(i)),quarterLength=random.choice((0.5,1.5,1,2)))
        n6=note.Note(chr(int(i)),quarterLength=random.choice((0.5,1.5,1,2)))
        n7=note.Note(chr(int(i)),quarterLength=random.choice((0.5,1.5,1,2)))
        n8=note.Note(chr(int(i)),quarterLength=random.choice((0.5,1.5,1,2)))
        n9=note.Note(chr(int(i)),quarterLength=random.choice((0.5,1.5,1,2)))
        n10=note.Note(chr(int(i)),quarterLength=random.choice((0.5,1.5,1,2)))
        s = stream.Stream()
        s.append([n1,n2,n3,n4,n5,n6,n7,n8,n9,n10])
            
    s.write('midi',fp=filename)
    print("file created")

image_f=audio('sudo.jpg')

xnormalized=scale(image_f)

makeaudio(xnormalized,'newaudiosudo.midi')
# import pickle 
# pickle.dump('fresh.py')

