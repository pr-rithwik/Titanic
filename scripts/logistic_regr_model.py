import pandas as pd
from sklearn.linear_model import LogisticRegression


def simple_logistic_model_fit(df, output):
    clf = LogisticRegression(random_state=0).fit(df, output)
    print(f"Simple Logistic Model Train Data: {clf.score(df, output)}")

    return clf

def simple_logistic_model_predict(df, clf):
    output = clf.predict(df)

    df_out = pd.DataFrame({
        "PassengerId": df.index,
        "Survived": output
    })

    return df_out