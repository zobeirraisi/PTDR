import os

ROOT='.'

gt=os.path.join(ROOT,'gt')
out=os.path.join(ROOT,'out')
# print(os.listdir(gt))

for txt in os.listdir(gt):
    basename= os.path.splitext(txt)[0]
    # print(basename)
    with open(out+'/'+txt,'w') as f_o:
        with open(gt+'/'+txt) as f:
            lines = [line for line in f.readlines() if line.strip()]
            for line in lines:
                line=line.split(' ')
                print(line)
                xmin, ymin, xmax, ymax,word =line
                f_o.write(f'{xmin},{ymin},{xmax},{ymin},{xmax},{ymax},{xmin},{ymax},{word}')


        # break




