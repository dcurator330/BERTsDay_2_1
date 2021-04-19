# -*- coding: utf-8 -*-
from flask import Flask, render_template, request
import os
import Bert_fine_tuning as bert
import tensorflow as tf


bert_model_hub_path = 'Fine_tuned' # TODO 경로 고치기
is_bert = True

############################### TODO ##########################################
# 슬롯태깅 모델과 벡터라이저 불러오기
###############################################################################


app = Flask(__name__)
app.static_folder = 'static'

@app.route("/")
def home():

############################### TODO ##########################################
# 슬롯 사전 만들기
    app.slot_dict = {'a_slot': None, 'b_slot':None}
###############################################################################


    return render_template("index.html")
    
@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg').strip() # 사용자가 입력한 문장

############################### TODO ##########################################
# 1. 사용자가 입력한 한 문장을 슬롯태깅 모델에 넣어서 결과 뽑아내기
# 2. 추출된 슬롯 정보를 가지고 더 필요한 정보 물어보는 규칙 만들기 (if문)
    app.slot_dict['a_slot'] = ''
    print(app.slot_dict)

    return 'hi' # 챗봇이 이용자에게 하는 말을 return
###############################################################################