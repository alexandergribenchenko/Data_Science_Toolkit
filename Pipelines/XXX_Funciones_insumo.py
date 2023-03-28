import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, recall_score, f1_score
import pickle

def split_data(df):

    X = df.iloc[:,1:]
    y = df.iloc[:,0]
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
    data = {'train': {'X': X_train, 'y': y_train},
            'test': {'X': X_test, 'y': y_test}}
    return data

def train_model(data, model):
    model.fit(data["train"]["X"], data["train"]["y"])
    return model

def get_model_metrics(model, data):
    preds = model.predict(data["test"]["X"])
    accuracy = accuracy_score(data["test"]["y"], preds)
    recall = recall_score(data["test"]["y"], preds)
    f1 = f1_score(data["test"]["y"], preds)

    metrics = {"accuracy": accuracy,
               "recall": recall,
               "f1": f1 
    }
    return metrics

if __name__ == "__main__":
    
    df = pd.read_csv('data/BPT_POC_Data.csv')
    data = split_data(df)
    
    pipeline_full = pickle.load(open('pipelines/model.pkl', 'rb'))

    metrics = get_model_metrics(pipeline_full, data)

    print(metrics)
