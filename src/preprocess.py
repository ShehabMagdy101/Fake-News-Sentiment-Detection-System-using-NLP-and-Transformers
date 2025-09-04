import os
import pandas as pd

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
data_path = os.path.join(BASE_DIR, "data")
raw_data_path = os.path.join(data_path, "raw")
interim_data_path = os.path.join(data_path, "interim", "dataset.csv")
fake = pd.read_csv(os.path.join(raw_data_path, 'Fake.csv'))
true = pd.read_csv(os.path.join(raw_data_path, 'True.csv'))

# adding an encoded label column
true['label'] = 0
fake['label'] = 1 

# concating into one dataset
data = pd.concat([fake, true], ignore_index=True)

# drop unwanted columns
data = data.drop(columns=['subject','date'])

# save dataset into '../data/interim'
data.to_csv(interim_data_path, index=False, encoding='utf-8')

# save splits
from sklearn.model_selection import train_test_split

X = data[['title', 'text']]
y = data[['label']]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, stratify=y, random_state= 2003)

x_train_path = os.path.join(data_path, 'processed', 'splits', 'X_train.csv')
x_test_path = os.path.join(data_path, 'processed', 'splits', 'X_test.csv')
y_train_path = os.path.join(data_path, 'processed', 'splits', 'y_train.csv')
y_test_path = os.path.join(data_path, 'processed', 'splits', 'y_test.csv')

X_train.to_csv(x_train_path, index=False, encoding='utf-8')
y_train.to_csv(y_train_path, index=False, encoding='utf-8')
X_test.to_csv(x_test_path, index=False, encoding='utf-8')
y_test.to_csv(y_test_path, index=False, encoding='utf-8')