import numpy as np 
import pandas as pd 
from sklearn.preprocessing import MinMaxScaler


class DataTransformer:
    def __init__(self, data_file, df=None, output=None):
        self.data_file = data_file
        self.output = output
        self.output_col = "Survived"
        
        self.df = df
    
    def create_df(self):
        self.df = pd.read_csv(self.data_file)
        
    def set_passengerid_as_index(self):
        self.df.set_index("PassengerId", inplace=True)
    
    def seperate_output(self):
        self.output = self.df[self.output_col]
        
        self.df.drop(columns=self.output_col, inplace=True)
    
    def remove_unneeded_cols(self):
        remove_cols = ["Name", "Ticket", "Cabin"]
        self.df.drop(columns=remove_cols, inplace=True)
    
    def handle_missing_age_values(self):
        self.df["Age"] = self.df.groupby(["Sex", "Pclass"])["Age"].transform(lambda x: x.fillna(x.median()))

    def categorise_age_into_bins(self):
        bins = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
        labels = ['0-9', '10-19', '20-29', '30-39', '40-49', '50-59', '60-69', '70-79', '80-89', '90+']
        self.df["AgeCat"] = pd.cut(self.df["Age"], bins=bins, labels=labels)

        self.df.drop(columns="Age", inplace=True)

    def update_missing_embarked_values(self):
        mode_func = self.df.groupby(['Pclass'])["Embarked"].agg(pd.Series.mode)
        self.df["Embarked"] = self.df.apply(
            lambda row: mode_func[row["Pclass"]] if pd.isna(row['Embarked']) else row["Embarked"],
            axis=1
        )
    
    def handle_missing_fare_values(self):
        self.df["Fare"] = self.df.groupby(["Sex", "Pclass"])["Fare"].transform(lambda x: x.fillna(x.mean()))
    
    def handle_categorical_cols(self):
        one_hot_encoding_cols = ["Pclass", "Sex", "Embarked", "AgeCat"]
        self.df = pd.get_dummies(self.df, columns=one_hot_encoding_cols, dtype=float)
        
    def normalise_fare(self):
        min_max_scaler = MinMaxScaler()
        self.df["Fare"] = min_max_scaler.fit_transform(np.array(self.df["Fare"]).reshape(-1,1))
        
    