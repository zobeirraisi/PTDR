import numpy as np
import os


root = '/media/karim/Data/Me/Text/Detection/Test-Data/2/1'
os.chdir(root)

for files in os.listdir():
    if not files.startswith('.') and os.path.isfile(os.path.join(root, files)):
        file_name,file_ext = os.path.splitext(files)
        # print('{}{}'.format(file_name, file_ext))
        # os.makedirs(file_name, exist_ok=file_ext)
        # img_f = '{}{}'.format(file_name, '.bmp')
        txt_f = '{}{}'.format(file_name, '.txt')
        # print(txt_f)
        # img=Image.open(img_f)
        # img.show()
        s='###'+'\n'
        m=''+'\n'
        with open(root+'/../'+txt_f,'w') as g:
            with open(txt_f,'r') as f:
                # f.readline()
                # cnt = 0
                for line in f:
                    T = line.split(',')
                    if str(T[8]) !=s and str(T[8]) != m:
                        g.write(line)
                        # print('yes')



                # print('no')


