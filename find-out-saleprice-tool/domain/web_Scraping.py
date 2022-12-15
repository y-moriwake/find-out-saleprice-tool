import numpy # 計算など

# 中央値などの計算処理
def yahoo_calculation_f(Yahoo_scraping_list):
    """
    画面のラベル　総数・金額平均・金額中央値を計算する処理
    """

    # リストから金額だけを取得したリストを作成し、平均、中央値をそれぞれのラベルに入れる
    price_list = [Yahoo_scraping_list[x][1] for x in range(len(Yahoo_scraping_list))]
    price_numpylist = numpy.array(price_list)

    Yahoo_mean = round(numpy.mean(price_numpylist), 1) # 小数点以下２まで切り捨て、金額の平均を入れる
    Yahoo_Median = round(numpy.median(price_numpylist), 1) # 小数点以下２まで切り捨て、金額の中央値を入れる

    goods_count = str(len(Yahoo_scraping_list)) # 総数

    return goods_count, Yahoo_mean, Yahoo_Median














