import gkeepapi
import numpy as np
import requests
from PIL import Image

keep = gkeepapi.Keep()
keep.login('yoruijob@gmail.com', 'hntrse421')
keep.sync()
# メモの取得
gnotes = keep.all()
for gnote in gnotes:
    if gnote.title == 'aaa':
        blob = gnote.drawings[0]
        url = keep.getMediaLink(blob)

        filename='blob.png'

        urlData = requests.get(url).content # バイト型
        with open(filename ,mode='wb') as f: # wb でバイト型を書き込める
            f.write(urlData)


        im = np.array(Image.open(filename))
        print(im)
        print(np.shape(im))


    