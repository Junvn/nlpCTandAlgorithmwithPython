#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:janvn
# datetime:18-7-29 下午4:11
# software:PyCharm

class IMM(object):

    def __init__(self,dic_path):
        self.dictionary = set()
        self.maxiumn = 0

        with open(dic_path,'r',encoding='utf8') as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                self.dictionary.add(line)
                self.maxiumn = len(line)

    def cut(self,text):
        result = []
        index = len(text)
        while index > 0:
            word = None
            for size in range(self.maxiumn,0,-1):
                if index - size < 0 :
                    continue
                piece = text[(index-size):index]
                if piece in self.dictionary:
                    word = piece
                    result.append(word)
                    index -= size
                    break

            if word is None:
                index = -1
        return result[::-1]


def main():
    text = '南京长江大桥'
    tokenizer = IMM('./data/imm_dic.utf8')
    print(tokenizer.cut(text))


if __name__ == '__main__':
    main()











