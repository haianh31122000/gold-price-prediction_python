﻿from __future__ import division, print_function, unicode_literals
import streamlit as st
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.title('Mô hình dự đoán giá vàng ')

X = np.array([[82.739998, 82.830002, 81.980003, 82.459999, 3815600], [82.739998, 82.830002, 81.980003, 82.459999, 3815600], [82.739998, 82.830002, 81.980003, 82.459999, 3815600], [82.739998, 82.830002, 81.980003, 82.459999, 3815600], [82.739998, 82.830002, 81.980003, 82.459999, 3815600], [82.739998, 82.830002, 81.980003, 82.459999, 3815600], [82.739998, 82.830002, 81.980003, 82.459999, 3815600], [82.739998, 82.830002, 81.980003, 82.459999, 3815600], [82.739998, 82.830002, 81.980003, 82.459999, 3815600], [82.739998, 82.830002, 81.980003, 82.459999, 3815600], [82.739998, 82.830002, 81.980003, 82.459999, 3815600], [82.739998, 82.830002, 81.980003, 82.459999, 3815600], [82.739998, 82.830002, 81.980003, 82.459999, 3815600], [82.739998, 82.830002, 81.980003, 82.459999, 3815600], [82.739998, 82.830002, 81.980003, 82.459999, 3815600], [82.739998, 82.830002, 81.980003, 82.459999, 3815600], [82.739998, 82.830002, 81.980003, 82.459999, 3815600], [82.739998, 82.830002, 81.980003, 82.459999, 3815600], [82.739998, 82.830002, 81.980003, 82.459999, 3815600], [82.739998, 82.830002, 81.980003, 82.459999, 3815600], [82.739998, 82.830002, 81.980003, 82.459999, 3815600], [82.739998, 82.830002, 81.980003, 82.459999, 3815600], [82.739998, 82.830002, 81.980003, 82.459999, 3815600], [82.739998, 82.830002, 81.980003, 82.459999, 3815600], [82.739998, 82.830002, 81.980003, 82.459999, 3815600], [82.739998, 82.830002, 81.980003, 82.459999, 3815600], [82.739998, 82.830002, 81.980003, 82.459999, 3815600], [82.739998, 82.830002, 81.980003, 82.459999, 3815600], [82.739998, 82.830002, 81.980003, 82.459999, 3815600], [82.739998, 82.830002, 81.980003, 82.459999, 3815600], [82.739998, 82.830002, 81.980003, 82.459999, 3815600], [82.739998, 82.830002, 81.980003, 82.459999, 3815600], [82.739998, 82.830002, 81.980003, 82.459999, 3815600], [82.739998, 82.830002, 81.980003, 82.459999, 3815600], [82.739998, 82.830002, 81.980003, 82.459999, 3815600], [82.739998, 82.830002, 81.980003, 82.459999, 3815600], [82.739998, 82.830002, 81.980003, 82.459999, 3815600], [82.739998, 82.830002, 81.980003, 82.459999, 3815600], [82.739998, 82.830002, 81.980003, 82.459999, 3815600], [82.739998, 82.830002, 81.980003, 82.459999, 3815600], [82.739998, 82.830002, 81.980003, 82.459999, 3815600], [82.739998, 82.830002, 81.980003, 82.459999, 3815600], [82.739998, 82.830002, 81.980003, 82.459999, 3815600], [82.739998, 82.830002, 81.980003, 82.459999, 3815600], [82.739998, 82.830002, 81.980003, 82.459999, 3815600], [82.739998, 82.830002, 81.980003, 82.459999, 3815600], [82.739998, 82.830002, 81.980003, 82.459999, 3815600], [82.739998, 82.830002, 81.980003, 82.459999, 3815600], [82.739998, 82.830002, 81.980003, 82.459999, 3815600], [82.739998, 82.830002, 81.980003, 82.459999, 3815600], [82.739998, 82.830002, 81.980003, 82.459999, 3815600], [82.739998, 82.830002, 81.980003, 82.459999, 3815600], [82.739998, 82.830002, 81.980003, 82.459999, 3815600], [82.739998, 82.830002, 81.980003, 82.459999, 3815600]


              ])
Y = np.array([[
    82.459999,82.459999,82.459999,82.459999,82.459999,82.459999,82.459999,82.459999,82.459999,82.459999,82.459999,82.459999,82.459999,82.459999,82.459999,82.459999,82.459999,82.459999,82.459999,82.459999,82.459999,82.459999,82.459999,82.459999,82.459999,82.459999,82.459999,82.459999,82.459999,82.459999,82.459999,82.459999,82.459999,82.459999,82.459999,82.459999,82.459999,82.459999,82.459999,82.459999,82.459999,82.459999,82.459999,82.459999,82.459999,82.459999,82.459999,82.459999
]]).T


def duel_plot(X1, X2, Y):
    fig = plt.figure(figsize=(15, 5))
    ax1 = fig.add_subplot(1, 2, 1)
    ax2 = fig.add_subplot(1, 2, 2)

    ax1.plot(Y, X[:, 0])
    ax1.set_title('xét diện tích với giá tiền')
    ax1.set_xlabel('giá tiền')
    ax1.set_ylabel('Diện tích m2')

    ax2.plot(Y, X[:, 1])
    ax2.set_title('xét số mét mặt tiền với giá tiền')
    ax2.set_xlabel('giá tiền')
    ax2.set_ylabel('số mét mặt tiền')
    return fig


def duel_plot2(X4, X5, Y):

    fig = plt.figure(figsize=(15, 5))
    ax3 = fig.add_subplot(1, 2, 1)
    ax4 = fig.add_subplot(1, 2, 2)
    ax3.plot(Y, X[:, 2])
    ax3.set_title('xét số tầng nhà với giá tiền')
    ax3.set_xlabel('giá tiền')
    ax3.set_ylabel('số tầng nhà')

    ax4.plot(Y, X[:, 3])
    ax4.set_title('xét khoảng cách với giá tiền')
    ax4.set_xlabel('giá tiền')
    ax4.set_ylabel('khoảng cách tới hồ gươm')
    return fig


st.set_option('deprecation.showPyplotGlobalUse', False)
st.pyplot(duel_plot(X[:, 0], X[:, 1], Y))
st.pyplot(duel_plot2(X[:, 2], X[:, 3], Y))


st.sidebar.title('Dự đoán giá các mẫu nhà')
dt_name = st.sidebar.text_input('Nhập diện tích đất(m2) ')
cd_name = st.sidebar.text_input('Nhập chiều dài mặt tiền(m) ')
tn_name = st.sidebar.text_input('Nhập số tầng nhà(tầng) ')
kc_name = st.sidebar.text_input('Nhập khoảng cách nhà tới hồ gươm(m) ')
one = np.ones((X.shape[0], 1))
Xbar = np.concatenate((one, X), axis=1)

x_train, x_test, y_train, y_test = train_test_split(Xbar, Y, test_size=0.2)

A = np.dot(Xbar.T, Xbar)
b = np.dot(Xbar.T, Y)
w = np.dot(np.linalg.pinv(A), b)


w_0 = w[0][0]
w_1 = w[1][0]
w_2 = w[2][0]
w_3 = w[3][0]
w_4 = w[4][0]

st.write("Độ chính xác (R2 square) : ", r2_score(y_test, np.dot(x_test, w)))

vd = np.array([dt_name, cd_name, tn_name, kc_name, 1])
if st.sidebar.button('Dự đoán'):
    y1 = w_1*float(dt_name)+w_2*float(cd_name)+w_3 * \
        float(tn_name)+w_4*float(kc_name) + w_0
    st.sidebar.write('Giá của ngôi nhà là : ', y1, 'tỷ đồng')
