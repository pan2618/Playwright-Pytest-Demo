import csv
import os
from typing import List, Dict

def get_csv_data(filename: str) -> List[Dict]:
    """
    讀取 test_data 資料夾下的 CSV 檔案
    回傳格式: [{'sku': 'A01', 'qty': '1'}, ...]
    """
    # 動態取得專案根目錄路徑
    base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    file_path = os.path.join(base_path, "test_data", filename)
    
    data = []
    try:
        with open(file_path, mode='r', encoding='utf-8-sig') as f:
            reader = csv.DictReader(f)
            for row in reader:
                data.append(row)
        return data
    except FileNotFoundError:
        print(f"❌ Error: 找不到測試資料檔案: {file_path}")
        return []
