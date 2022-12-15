import csv
import datetime

ini_folder_path = "./output/"

# webスクレイピングの結果をCSVとして保存する処理
def write_csv(godos_list, goodsName):
    """
    webスクレイピングの結果をCSVとして保存する処理
    """
    # 現在の年月日_時間
    date_nowtime = datetime.datetime.now()
    now = date_nowtime.strftime('%Y-%m-%d_%H-%M-%S')
    global ini_folder_path
    data_csv_path = ini_folder_path + now + "_" + goodsName  + ".csv"

    print("CSV出力")
    with open(data_csv_path, 'w') as f:
        header = ["title", "price", "when"]
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(godos_list)
    print("CSV完了")