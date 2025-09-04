import kagglehub
import os
import shutil

# Download the dataset
path = kagglehub.dataset_download("clmentbisaillon/fake-and-real-news-dataset")

# project base directory  '../Fake News & Sentiment Detection System'
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

target_dir = os.path.join(BASE_DIR, "data", "raw")
os.makedirs(target_dir, exist_ok=True)

source_file1 = os.path.join(path, "Fake.csv")   
source_file2 = os.path.join(path, "True.csv")   

fake = os.path.join(target_dir, 'Fake.csv')
true = os.path.join(target_dir, 'True.csv')

shutil.copy(source_file1, fake)
shutil.copy(source_file2, true)