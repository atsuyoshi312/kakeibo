import streamlit as st
import pandas as pd
from datetime import datetime

# データフレームを初期化
data = pd.DataFrame(columns=["日付", "カテゴリ", "金額"])

# Streamlitアプリのタイトルと説明
st.title("家計簿アプリ")
st.write("このアプリで簡単に家計を管理しましょう。")

# カテゴリの選択肢を定義
categories = ["食費", "日用品","住居費", "交通費", "娯楽", "その他"]

# 入力フォームを作成
st.header("新しいトランザクションの追加")
date = st.date_input("日付を選択してください", datetime.today())
category = st.selectbox("カテゴリを選択してください", categories)
amount = st.number_input("金額を入力してください", min_value=1)

# 日付をdatetime形式に変換
date = pd.to_datetime(date)

# トランザクションをデータフレームに追加
if st.button("追加"):
    new_entry = {"日付": date, "カテゴリ": category, "金額": amount}
    data = data.append(new_entry, ignore_index=True)
    st.success("トランザクションが追加されました。")

# データを表示
st.header("家計簿の一覧")
st.write(data)

# グラフを表示
st.header("カテゴリ別支出の合計")
category_total = data.groupby("カテゴリ")["金額"].sum()
st.bar_chart(category_total)

# 月ごとの支出合計を表示
data["年月"] = data["日付"].dt.strftime("%Y-%m")
monthly_total = data.groupby("年月")["金額"].sum()
st.header("月ごとの支出合計")
st.line_chart(monthly_total)

# CSVファイルにデータを保存
if st.button("データを保存"):
    data.to_csv("household_budget.csv", index=False)
    st.success("データが保存されました。")
