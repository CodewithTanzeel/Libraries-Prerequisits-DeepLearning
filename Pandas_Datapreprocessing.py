# pandas_dl.py
import pandas as pd
from sklearn.model_selection import train_test_split

def load_and_clean():
    # Load Titanic dataset
    url = "https://web.stanford.edu/class/archive/cs/cs109/cs109.1166/stuff/titanic.csv"
    data = pd.read_csv(url)
    
    # Drop missing values
    data = data.dropna(subset=['Age', 'Fare'])
    
    # Encode categorical data (Sex: male=0, female=1)
    data['Sex'] = data['Sex'].map({'male': 0, 'female': 1})
    
    # Normalize numerical features
    data['Age'] = (data['Age'] - data['Age'].mean()) / data['Age'].std()
    return data

def train_test(data):
    # Split into features (X) and target (y)
    X = data[['Pclass', 'Sex', 'Age', 'Fare']]
    y = data['Survived']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
    print(f"Training data shape: {X_train.shape}")

if __name__ == "__main__":
    print("=== Pandas for Deep Learning ===")
    df = load_and_clean()
    train_test(df)