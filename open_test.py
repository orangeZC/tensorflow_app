import os
import re
import random


def divide_data():

    """
    划分训练集，交叉测试集以及测试集交叉测试集和测试集各200条，其他为训练集，同时对文本进行基本的预处理，去掉换行符。
    """

    file_list = os.listdir('trainingdataset')
    total_vec = []

    for file_dir in file_list[1:]:
        file_list = os.listdir('trainingdataset/%s' % file_dir)
        for file in file_list:
            word_vec = [file_dir]
            with open('trainingdataset/%s/%s' % (file_dir, file), 'r') as f:
                content = re.sub(r'\n.*?', "", f.read())
                word_vec.append(content)
            total_vec.append(word_vec)

    random.shuffle(total_vec)
    test_data = total_vec[:200]

    with open('ex_test.txt', 'w') as f:
        for test in test_data:
            f.write(test[0])
            f.write('\t')
            f.write(test[1])
            f.write('\n')
    val_data = total_vec[200:400]

    with open('ex_val.txt', 'w') as f:
        for val in val_data:
            f.write(val[0])
            f.write('\t')
            f.write(val[1])
            f.write('\n')
    train_data = total_vec[400:]

    with open('ex_train.txt', 'w') as f:
        for train in train_data:
            f.write(train[0])
            f.write('\t')
            f.write(train[1])
            f.write('\n')

    predict_file_list = os.listdir('experimentdataset')

    for predict_file in predict_file_list:
        with open('experimentdataset/%s' % predict_file, 'r') as f:
            content = re.sub(r'\n.*?', '', f.read())
        with open('experimentdataset/%s' % predict_file, 'w') as f:
            f.write(content)


if __name__ == '__main__':
    divide_data()
