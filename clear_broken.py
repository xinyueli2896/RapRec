import librosa
import os
from tqdm import tqdm

os.chdir('dataset_cleaned/test')
all_paths = os.listdir()
brokens = []
for x in tqdm(all_paths):
    try:
        y, sr = librosa.load(x)
    except:
        brokens.append(x)
        
print(brokens)