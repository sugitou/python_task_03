import pandas as pd
import eel
import os

### デスクトップアプリ作成課題
def kimetsu_search(word, csv_file):
    # 検索対象取得
    # Mac環境のため今回はフルパスを指定
    df=pd.read_csv(f"/Users/right/python課題/project03/{csv_file}")
    # Windows環境なら以下
    # df=pd.read_csv(f"./{csv_file}")
    source=list(df["name"])

    textlog = ''

    # 検索
    if word in source:
        log_y = "『{}』はあります".format(word)
        print(log_y)
        textlog = log_y

    else:
        log_n = "『{}』はありません".format(word) + "\n" + "『{}』を追加します".format(word)
        print(log_n)
        textlog = log_n
        # 追加
        #add_flg=input("追加登録しますか？(0:しない 1:する)　＞＞　")
        #if add_flg=="1":
        source.append(word)
    
    # CSV書き込み
    df=pd.DataFrame(source,columns=["name"])
    # Mac環境のため今回はフルパスを指定
    df.to_csv(f"/Users/right/python課題/project03/{csv_file}",encoding="utf_8-sig")
    # Windows環境なら以下
    # df.to_csv(f"./{csv_file}",encoding="utf_8-sig")
    print(source)
    return textlog
