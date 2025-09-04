import os

ROOT='.'

gt=os.path.join(ROOT,'gt_15')
out=os.path.join(ROOT,'out')
# print(os.listdir(gt))

for txt in os.listdir(gt):
    basename= os.path.splitext(txt)[0]
    print(basename)
    with open(out+'/'+txt,'w') as f_o:
        with open(gt+'/'+txt) as f:
            lines = [line for line in f.readlines() if line.strip()]
            for line in lines:
                line=line.split(',')
                # print(line)
                p1, p2, p3, p4,p5,p6,p7,p8,word =line
                xmin=min(int(p1),int(p3),int(p5),int(p7))
                ymin=min(int(p2),int(p4),int(p6),int(p8))

                xmax=max(int(p1),int(p3),int(p5),int(p7))
                ymax= max(int(p2),int(p4),int(p6),int(p8))

                f_o.write(f'{xmin},{ymin},{xmax},{ymin},{xmax},{ymax},{xmin},{ymax},{word}')


        # break




