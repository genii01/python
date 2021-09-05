'''
hyperparameter set up 
'''
import argparse
import json
def parse_args():
    with open('./conf.json') as f:
        conf = json.load(f)
    parser = argparse.ArgumentParser(description="Run sentiment analysis model.")
    parser.add_argument('--model_name', nargs='?', default=conf["model_name"], help='set up model name')
    parser.add_argument('--epoch', type=int, default= conf["epoch"],  help='set up num of epochs')
    parser.add_argument('--predict', type=bool, default=bool(conf["predict"]), help='set up predict mode')
    parser.add_argument('--stopwords', nargs='?', default=conf["stopwords"], help='set up stopwords')
    parser.add_argument('--learner', nargs='?', default=conf["learner"], help='set up learner')
    parser.add_argument('--kor_tokenizer', nargs='?', default=conf["kor_tokenizer"], help='set up korean-tokenizer from konlpy')
    parser.add_argument('--learning_rate', type=float, default= conf["learning_rate"],  help='set up learning_rate')
    parser.add_argument('--dropout', type=float, default= conf["dropout"],  help='set up dropout')
    parser.add_argument('--data_split', type=float, default= conf["data_split"],  help='set up train / test dataset split ratio')
    parser.add_argument('--validation_split', type=float, default= conf["validation_split"],  help='set up train / validation dataset split ratio')
    parser.add_argument('--activation', nargs='?', default=conf["activation"], help='set up activation function')
    parser.add_argument('--max_length', type=float, default= conf["max_length"],  help='set up sentence max length')
    parser.add_argument('--train_batch_size', type=int, default= conf["train_batch_size"],  help='set up num of train batch size')
    parser.add_argument('--test_batch_size', type=int, default= conf["test_batch_size"],  help='set up num of test batch size')
    parser.add_argument('--predict_batch_size', type=int, default= conf["predict_batch_size"],  help='set up num of predict batch size')
    parser.add_argument('--path', nargs='?', default=conf["path"], help='Input data path.')
    parser.add_argument('--dataset', nargs='?', default=conf["dataset"], help='Choose a dataset.')
    parser.add_argument('--embedding_matrix', nargs='?', default= conf["embedding_matrix"],  help='set up embedding matrix application')
    parser.add_argument('--verbose', type=int, default=conf["verbose"], help='progress visualization.')
    return parser.parse_args()
