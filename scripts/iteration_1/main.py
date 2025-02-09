from scripts.iteration_1 import DataTransformer
from scripts.iteration_1 import \
    simple_logistic_model_fit, simple_logistic_model_predict
from scripts.utils import get_project_root, get_config_details
import hydra


BASE_DIR = get_project_root()
CONFIG_PATH = get_config_details()
CONFIG_NAME = "config"


def transform_data(file_path, train_data=True):
    data_transformer = DataTransformer(file_path)
    data_transformer.create_df()
    
    if train_data:
        data_transformer.seperate_output()
    
    data_transformer.set_passenger_id_as_index()
    data_transformer.remove_unneeded_cols()
    data_transformer.handle_missing_age_values()
    data_transformer.categorise_age_into_bins()
    data_transformer.update_missing_embarked_values()
    data_transformer.handle_missing_fare_values()
    data_transformer.handle_categorical_cols()
    data_transformer.normalise_fare()

    return data_transformer

@hydra.main(version_base=None, config_path=CONFIG_PATH, config_name=CONFIG_NAME)
def simple_logistic_model(cfg):
    train_data_path = BASE_DIR / cfg.data.train_raw
    test_data_path = BASE_DIR / cfg.data.test_raw

    train_data_transformer = transform_data(train_data_path)
    clf = simple_logistic_model_fit(
        train_data_transformer.df, train_data_transformer.output
    )
    
    test_data_transformer = transform_data(test_data_path, train_data=False)
    df_out = simple_logistic_model_predict(
        test_data_transformer.df, clf
    )
    output_file = BASE_DIR / cfg.results.simple_logistic_regr_1
    df_out.to_csv(output_file, index=False)

# if __name__ == "__main__":
#     simple_logistic_model()