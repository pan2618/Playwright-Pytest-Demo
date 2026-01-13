import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    BASE_URL = os.getenv("BASE_URL", "https://staging.example-shop.com")
    USERNAME = os.getenv("TEST_USER_EMAIL")
    PASSWORD = os.getenv("TEST_USER_PWD")
    HEADLESS = os.getenv("HEADLESS", "true").lower() == "true"
    
    # 設定全域顯式等待時間 (取代 hard code sleep)
    DEFAULT_TIMEOUT = 10000
