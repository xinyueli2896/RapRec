# Towards Accurate Lyrics Recognition For Rap Songs
Transcibe rap lyrics using wav2vec2.0 with CTC loss by transfer learning

# Dataset
We download audio and lyrics files of 187 English rap songs from a playlist on [QQMusic](https://c6.y.qq.com/base/fcgi-bin/u?__=AdOgRqZ)) featuring different rap artists. 

## [Prepare Audiofolder for loading later](https://github.com/xinyueli2896/raptranscription/blob/main/loader_prepare.ipynb)
Segment the each audio file into several chunks with sample rate 44000Hz in alignment with the timestamps in the .flac files containing the lyrics. Then we store the path to our audio files and their "labels" (lyrics) in a .csv file to be used for loading as an audiofolder later.
Store mp3 files into train and test subfolders under the main audiofolder and upload metadata.csv under the main directory as well.
The dataset directory should look like this:
dataset/
├── train/
├── test/
└── metadata.csv

## [Clean up my Audiofolder](https://github.com/xinyueli2896/raptranscription/blob/main/loader_clean.ipynb)
1. Filter out replicated and corrupted audio files
2. Unmask explicit vocabulary

## [Usage of the Audiofolder](https://github.com/xinyueli2896/raptranscription/blob/main/dataloader.ipynb)
Load data with load_dataset from huggingface, specifying 'audiofolder' and path to the dataset in the argument. More information see [documentation](https://huggingface.co/docs/datasets/audio_dataset#audiofolder).
