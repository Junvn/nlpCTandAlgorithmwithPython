#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:janvn
# datetime:18-8-12 下午10:05
# software:PyCharm

import os

class HMM(object):
    '''
    隐马尔可夫模型
    '''

    def __init__(self):

        # 主要用于存取算法中间结果，不用每次都训练模型
        self.model_file = './data/hmm_model.pkl'

        self.state_list = ['B', 'M', 'E', 'S']

        self.load_para = False
    

    def try_load_model(self, trained):
        pass

    def train(self, path):
        pass

    def viterbi(self, text, states, start_p, trans_p, emit_p):
        pass

    def cut(self, text):
        pass