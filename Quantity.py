# -*- coding: utf-8 -*-
import pickle

class Quantity:
    def __init__(self, alpha, gamma, initial_q=50.0):
        self._values = {}
        self._alpha = alpha
        self._gamma = gamma
        self._initial_q = initial_q

    def select_q(self, state, act):
        if(state, act) in self._values:
            # 学習済みのQ値を返却する。
            return self._values[(state, act)]
        else:
            # 未学習の場合、初期値を返却する。
            self._values[(state, act)] = self._initial_q
            return self._initial_q
        
    def save(self):
        with open('qlearn.pickle', mode = 'wb') as f:
            pickle.dump(self._values, f)
            
    def load(self):
        with open('qlearn.pickle', mode = 'rb') as f:
            self._values = pickle.load(f);
        
    def set(self, state, act, q_value):
        """Q 値設定"""
        self._values[(state, act)] = q_value

    def lerning(self, state, act, max_q):
        """Q 値更新"""
        pQ = self.select_q(state, act)
        new_q = pQ + self._alpha * (self._gamma * (max_q - pQ))
        self.set(state, act, new_q)

    def add_fee(self, state, act, fee):
        """報酬を与える"""
        pQ = self.select_q(state, act)
        new_q = pQ + self._alpha * (fee - pQ)
        self.set(state, act, new_q)