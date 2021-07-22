import os
import csv
import datetime

# csvファイルの保存
def save_csv(save_dir, filename):
    # カレントディレクトリの取得
    base_dir = os.path.dirname(os.path.abspath(__file__))
    new_dir = base_dir + '/' + save_dir
    # 指定ディレクトリ作成
    if new_dir:
        pass
    else:
        os.mkdir(new_dir)
    
    # サーチ後のcsvファイル読み込み
    with open(filename, 'r', encoding='utf_8-sig') as rf:
        h = next(csv.reader(rf))
        read_data = rf.readlines()
    
    # 現在時刻取得
    now = datetime.datetime.now().strftime('%Y-%m-%d_%H:%M:%S')
    new_file = now + '_' +filename
    output = new_dir + '/' + new_file

    # データの書き込み
    with open(output, 'w', encoding='utf_8-sig') as wf:
        for line in read_data:
            wf.write(line)