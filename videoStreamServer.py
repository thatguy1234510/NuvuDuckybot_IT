import socket
import cv2
import camera
import io
import numpy as np
from tempfile import TemporaryFile
import zstandard

s = socket.socket()
s.bind(('', 444))

s.listen(10)

while True:
    conn, addr = s.accept()
    print('Connected with ' + addr[0] + ':' + str(addr[1]))
    break

cam = camera.Camera()

while True:
    b = io.BytesIO()
    img=cam.image
    #not sure if np.save compression is worth io overhead...
    Tfile=TemporaryFile()
    #use numpys built in save function to convert image to bytes
    np.save(Tfile,img)
    #compress it into even less bytes
    b.write(zstandard.ZstdCompressor.compress(bytearray(Tfile.read(Tfile.tell()))))
    conn.send(b.getvalue())

s.close()
