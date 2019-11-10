import os
import pandas as pd

if __name__ == '__main__':
    base_dir = os.path.join('data', 'kaggle', 'input', 'data-science-bowl-2019')
    train_path = os.path.join(base_dir, 'train.csv')
    test_path = os.path.join(base_dir, 'test.csv')
    train_data = pd.read_csv(test_path)
    print(train_data['installation_id'])
    print(len(set(train_data['installation_id'])))
