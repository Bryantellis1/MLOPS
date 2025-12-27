# Import libraries

import argparse
import glob
import os

import pandas as pd

from sklearn.linear_model import LogisticRegression


# define functions
def main(args):
    # TO DO: enable autologging


    # read data
    df = get_csvs_df(args.training_data)

    # split data
    X_train, X_test, y_train, y_test = split_data(df)

    # train model and capture the result
    model = train_model(args.reg_rate, X_train, X_test, y_train, y_test)
    
    return model


def get_csvs_df(path):
    if not os.path.exists(path):
        raise RuntimeError(f"Cannot use non-existent path provided: {path}")
    csv_files = glob.glob(f"{path}/*.csv")
    if not csv_files:
        raise RuntimeError(f"No CSV files found in provided data path: {path}")
    
    # Read CSV files with error handling and optimized settings
    # Using explicit loop for better error handling per file
    dataframes = []
    for csv_file in csv_files:
        try:
            # Use low_memory=False to avoid dtype guessing which can be slow
            df = pd.read_csv(csv_file, low_memory=False)
            dataframes.append(df)
        except Exception as e:
            raise RuntimeError(f"Error reading CSV file {csv_file}: {str(e)}")
    
    return pd.concat(dataframes, ignore_index=True, copy=False)


# TO DO: add function to split data


def train_model(reg_rate, X_train, X_test, y_train, y_test):
    # train model with optimized parameters
    # max_iter increased from default 100 to ensure convergence
    model = LogisticRegression(
        C=1/reg_rate, 
        solver="liblinear",
        max_iter=1000  # Prevent convergence warnings and potential slowdowns
    ).fit(X_train, y_train)
    return model


def parse_args():
    # setup arg parser
    parser = argparse.ArgumentParser()

    # add arguments
    parser.add_argument("--training_data", dest='training_data',
                        type=str)
    parser.add_argument("--reg_rate", dest='reg_rate',
                        type=float, default=0.01)

    # parse args
    args = parser.parse_args()

    # return args
    return args

# run script
if __name__ == "__main__":
    # add space in logs
    print("\n\n")
    print("*" * 60)

    # parse args
    args = parse_args()

    # run main function
    main(args)

    # add space in logs
    print("*" * 60)
    print("\n\n")
