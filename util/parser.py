import sys
import re

cnt = 0
with open(sys.argv[1], 'r') as dataset, open(f'filtered_{sys.argv[1]}', 'w') as filtered_gt:
    samples = dataset.readlines()
    for sample in samples:
        image_path, label = sample.strip().split('\t')
        label = label.strip('"')
        if not re.search('[^a-zA-Z0-9]', label) and len(list(label)) >= 3:
            cnt += 1
            filtered_gt.write('par/' + image_path + '\t' + label + '\n')

    print('number of samples :', cnt)
