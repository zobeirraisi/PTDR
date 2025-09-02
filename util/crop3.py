from PIL import Image
import os
import glob

os.makedirs('cropped', exist_ok=True)

path = f'*.txt'
Textfiles = glob.glob(path)
print(len(Textfiles))

cnt = 11132
with open('gt.csv', 'w') as g:
    for txtfile in Textfiles:
        print(txtfile)
        imgfile = txtfile.split('.')[0] + '.jpg'

        im = Image.open(imgfile)
    # with open('../gt.txt', 'w') as g:
        with open(txtfile) as f:
            lines = [line for line in f.readlines() if line.strip()]
            for line in lines:
                line = line.split(',')
                print(line)
                if len(line) < 9 :
                    continue
                elif len(line) > 9 :
                    # continue
                    p1, p2, p3, p4, p5, p6, p7, p8, word1,word2 = line
                    word = word1+word2
                else:
                    p1, p2, p3, p4, p5, p6, p7, p8, word = line

                xmin = min(int(p1), int(p3), int(p5), int(p7))
                ymin = min(int(p2), int(p4), int(p6), int(p8))

                xmax = max(int(p1), int(p3), int(p5), int(p7))
                ymax = max(int(p2), int(p4), int(p6), int(p8))

                im1 = im.crop((xmin, ymin, xmax, ymax))

                # im1.save()
                # print(word)
                g.write(f'img_{cnt}.jpg,{word}')
                im1.save(f'cropped/img_{cnt}.jpg')
                cnt += 1

print(cnt)
