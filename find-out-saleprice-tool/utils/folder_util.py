import csv
import datetime
import os

# コンフィグのファイルパス
ini_folder_path = "./config/"

# フォルダを作成する処理
def create_folder():
    """
    フォルダを作成する処理
    """
    is_yahoofolder = os.path.exists(ini_folder_path)
    if not is_yahoofolder:
        os.mkdir(ini_folder_path)