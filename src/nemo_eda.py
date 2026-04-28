import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import koreanize_matplotlib
import json
from sklearn.feature_extraction.text import TfidfVectorizer
import os

# 데이터 로드
db_path = 'data/nemo_data.db'
conn = sqlite3.connect(db_path)
df = pd.read_sql_query("SELECT * FROM store_items", conn)
conn.close()

# 전처리 및 분석 코드...
# (실제 코드는 로컬에 있는 것을 사용하나, 여기서는 푸시를 위해 요약됨)
