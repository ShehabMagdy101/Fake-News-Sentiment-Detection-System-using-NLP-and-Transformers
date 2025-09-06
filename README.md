# 📰 Fake News Classification using Classical, Sequential & Transfomer Based Models

<br>

This project utilizes classical models such as **SVM**, **Naïve Bayes**, and **Logistic Regression**. also we used some sequential models such as **RNN**, **GRU**, and **LSTM**. moreover we Fine-tuned **DistilBERT** (`distilbert-base-uncased`) model to classify news text articles into (**Fake** or **True**) 

## 📂 Dataset
- **Source:** [fake and real news dataset](https://www.kaggle.com/datasets/clmentbisaillon/fake-and-real-news-dataset)  
- **Features:**
  - `title`: title of news article
  - `text`: body text of news article
  - `subject`: subject of news article
  - `date`: publish date of news article
- **Size:** 
  - Fake: 23481 samples  
  - true: 21417 samples 
---

## Project Structure

```
├── LICENSE            <- Open-source license if one is chosen
├── Makefile           <- Makefile with convenience commands like `make data` or `make train`
├── README.md          <- The top-level README for developers using this project.
├── data
│   ├── external       <- Data from third party sources.
│   ├── interim        <- Intermediate data that has been transformed.
│   ├── processed      <- The final, canonical data sets for modeling.
│   └── raw            <- The original, immutable data dump.
│
├── docs               <- A default mkdocs project; see www.mkdocs.org for details
│
├── models             <- Trained and serialized models, model predictions, or model summaries
│
├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
│                         the creator's initials, and a short `-` delimited description, e.g.
│                         `1.0-jqp-initial-data-exploration`.
│
├── pyproject.toml     <- Project configuration file with package metadata for 
│                         {{ cookiecutter.module_name }} and configuration for tools like black
│
├── references         <- Data dictionaries, manuals, and all other explanatory materials.
│
├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
│   └── figures        <- Generated graphics and figures to be used in reporting
│
├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
│                         generated with `pip freeze > requirements.txt`
│
├── setup.cfg          <- Configuration file for flake8
│
└── {{ cookiecutter.module_name }}   <- Source code for use in this project.
    │
    ├── __init__.py             <- Makes {{ cookiecutter.module_name }} a Python module
    │
    ├── config.py               <- Store useful variables and configuration
    │
    ├── dataset.py              <- Scripts to download or generate data
    │
    ├── features.py             <- Code to create features for modeling
    │
    ├── modeling                
    │   ├── __init__.py 
    │   ├── predict.py          <- Code to run model inference with trained models          
    │   └── train.py            <- Code to train models
    │
    └── plots.py                <- Code to create visualizations   
```

## 🚀 Setup Instructions
1. Clone this repository:
   ```
   git clone https://github.com/your-username/fake-news-sentiment.git
   cd fake-news-sentiment
   ```
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Go to `fake-news-sentiment/src`
   ```
   cd src
   ```
4. Run the Streamlit app:
   ```
   streamlit run app.py
   ```
##  📊 Results
---

| Model                     |  Accuracy | 
| ------------------------ | -------- |
| Linear SVC (SVM)     | 0.99      |
| Linear Regression |  0.98      |
| Naïve Bayes |  0.93      |
| GRU |  0.98      |
| RNN  |   0.98      |
| LSTM |   0.98      |
| distilbert-base-uncased |   0.99      |



## 🌍 Deployment

<img width="1082" height="454" alt="image" src="https://github.com/user-attachments/assets/0d3cf7cd-5868-4fec-a825-d8852d779bfd" />

### Example 1
---
<img width="1067" height="511" alt="image" src="https://github.com/user-attachments/assets/2b5058c3-bd6f-4e68-b177-52e48993d3d9" />

### Example 2
---
<img width="1140" height="484" alt="image" src="https://github.com/user-attachments/assets/b6efb9b9-de32-4e95-8771-c997d3b21592" />

