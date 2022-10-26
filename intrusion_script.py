import argparse
import joblib
from os.path import exists
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import MinMaxScaler
from sklearn.compose import make_column_transformer
from category_encoders import BinaryEncoder
import pandas as pd
import sys
def parse_args():
    parser = argparse.ArgumentParser(description='Outputs to a file and stdout type of attack')
    parser.add_argument('-t','--type',choices=['bi', 'uni', 'packet'], help='Requires type of data inputted.\n1. bi\n2. uni\n3. packet', required=True)
    parser.add_argument('-f','--file', help='Requires filename of the input data. File must be in csv format', required=True)
    return vars(parser.parse_args())
def load(typ):
    """Loads the model, columns to drop and the scaler
    Input can only be arg 'type' and outputs are
    scaler, to_drop, model"""
    scaler_file='resources/'+'scaler_'+typ+'.save'
    drop_file='resources/'+typ+'_drop'+'.save'
    model_file='resources/'+'rfc_'+typ+'.save'
    if not (exists(scaler_file) and exists(drop_file) and exists(model_file)):
        sys.exit('Resources could not be loaded')
    scaler=joblib.load(scaler_file)
    to_drop=joblib.load(drop_file)
    model=joblib.load(model_file)
    return scaler,to_drop,model
def load_data(filename):
    try:
        file=open(filename)
        file.close()
    except:
        sys.exit("File not found")  
    data=pd.read_csv(filename)
    return data


if __name__ == '__main__':
    parser=parse_args()
    print('Loading resources....')
    scaler,to_drop,model=load(parser['type'])
    print('Loading data....')
    df=load_data(parser['file'])
    print('Preprocessing data....')
    data=df.drop(to_drop,axis=1)
    data=scaler.transform(data.to_numpy())
    print('Predicting the results....')
    pred=model.predict(data)
    df['predictions']=pred
    print('Attaching predictions to the predictions.csv file....')
    df.to_csv('predictions.csv')
    print('Process Completed...')




