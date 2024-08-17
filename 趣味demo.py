import streamlit as st
import random

# 设置页面标题
st.title("趣味小程序 - 给你带来快乐！")

# 鼓励语句列表
encouragements = [
    "你今天已经很努力了，继续加油！",
    "生活就像一盒巧克力，你永远不知道你会得到什么。",
    "笑一笑，烦恼跑掉！",
    "你是独一无二的，世界因为有你而更美好。",
    "今天的困难，明天会成为你的动力。",
]

# 笑话列表
jokes = [
    "为什么书本很害怕？因为它们有很多封面！",
    "为什么青蛙总是很快乐？因为它吃什么都喜欢“嘎嘎”！",
    "我昨晚做了个梦，梦见我变成了一块蛋糕！醒来后发现自己太甜了！",
    "两颗橘子在路上走，突然一辆车开过来，其中一颗橘子就变成了果汁。",
    "有一天，一只小熊说：今天不吃蜂蜜，明天再吃，结果它一天没吃。"
]

# 用户选项
option = st.selectbox("你想听什么？", ("鼓励语", "笑话"))

# 显示结果
if option == "鼓励语":
    st.write(random.choice(encouragements))
else:
    st.write(random.choice(jokes))

# 额外功能：让用户点击按钮生成新的语句或笑话
if st.button('再来一次'):
    if option == "鼓励语":
        st.write(random.choice(encouragements))
    else:
        st.write(random.choice(jokes))

st.write("希望这个小程序能让你微笑 😊")