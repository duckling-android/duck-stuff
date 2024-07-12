import os
import string
import random

chars = string.ascii_lowercase[13:]

parent = "/home/workshop/escaperoom/keys"

for i in chars:
    for j in chars:
        for k in chars:
            for l in chars:
                for m in chars:
                    for n in chars:
                        folder = i+j+k+l+m+n
                        path = os.path.join(parent, folder)
                        os.mkdir(path)