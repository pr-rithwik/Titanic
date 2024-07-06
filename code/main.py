from pathlib import Path
from code.data_transformer import DataTransformer
from code.logistic_regr_model import \
    simple_logistic_model_fit, simple_logistic_model_predict


BASE_DIR = Path("/")


def transform_data(file_path, train_data=True):
    data_transformer = DataTransformer(file_path)
    data_transformer.create_df()
    
    if train_data:
        data_transformer.seperate_output()
    
    data_transformer.set_passengerid_as_index()
    data_transformer.remove_unneeded_cols()
    data_transformer.handle_missing_age_values()
    data_transformer.categorise_age_into_bins()
    data_transformer.update_missing_embarked_values()
    data_transformer.handle_missing_fare_values()
    data_transformer.handle_categorical_cols()
    data_transformer.normalise_fare()

    return data_transformer

def simple_logistic_model():
    train_data_path = BASE_DIR / "code/train.csv"
    test_data_path = BASE_DIR / "code/test.csv"

    train_data_transformer = transform_data(train_data_path)
    clf = simple_logistic_model_fit(
        train_data_transformer.df, train_data_transformer.output
    )
    
    test_data_transformer = transform_data(test_data_path, train_data=False)
    df_out = simple_logistic_model_predict(
        test_data_transformer.df, clf
    )
    return df_out