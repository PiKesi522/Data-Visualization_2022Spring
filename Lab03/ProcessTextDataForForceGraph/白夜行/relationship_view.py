# -*- coding: utf-8 -*-
from __future__ import print_function
"""
Created on 2017/10/15 19:24

@file: relationship_view.py
@author: Qingyu Mao
"""
import jieba
import codecs
from collections import defaultdict

TEXT_PATH = './byx.txt'  # 文本路径
DICT_PATH = './person.txt'  # 人物字典路径
SYNONYMOUS_DICT_PATH = './synonymous_dict.txt'  # 同义词路径
SAVE_NODE_PATH = './node.csv'
SAVE_EDGE_PATH = './myedge.csv'


class RelationshipView:

    def __init__(self, text_path, dict_path, synonymous_dict_path):
        self._text_path = text_path
        self._dict_path = dict_path
        self._synonymous_dict_path = synonymous_dict_path
        '''
        person_counter是一个计数器，用来统计人物出现的次数。{'a':1,'b':2}
        person_per_paragraph每段文字中出现的人物[['a','b'],[]]
        relationships保存的是人物间的关系。key为人物A，value为字典，包含人物B和权值。
        '''
        self._person_counter = defaultdict(int)
        self._person_per_paragraph = []
        self._relationships = {}
        self._synonymous_dict = {}

    def generate(self):
        self.count_person()
        self.calc_relationship()
        self.save_node_and_edge()

    def synonymous_names(self):
        '''
        获取同义名字典
        :return:
        '''
        with codecs.open(self._synonymous_dict_path, 'r', 'utf-8') as f:
            lines = f.read().split('\n')
            # print(lines)
        for line in lines:
            # print(line)
            # print(line.split(' ')[0])
            # print(line.split(' ')[1])
            self._synonymous_dict[line.split(' ')[0]] = line.split(' ')[1]
        print(self._synonymous_dict)
        return self._synonymous_dict

    def get_clean_paragraphs(self):
        '''
        以段为单位分割全文
        :return:
        '''
        new_paragraphs = []
        last_paragraphs = []
        with codecs.open(self._text_path, 'r', 'utf-8') as f:
            # paragraphs = f.read().split('\n\n')
            paragraphs = f.read().split('\n')
            # print(paragraphs)
            # paragraphs = paragraphs[0].split('\u3000')
        # print(len(paragraphs))
        for i in range(len(paragraphs) - 1):
            if paragraphs[i] != '':
                if paragraphs[i][-1] == '”':
                    paragraphs[i + 1] = paragraphs[i] + paragraphs[i + 1]
                    paragraphs[i] = ''
        for i in range(len(paragraphs)):
            if paragraphs[i] != '':
                new_paragraphs.append(paragraphs[i])
        for i in range(len(new_paragraphs)):
            new_paragraphs[i] = new_paragraphs[i].replace('\u3000', '')
            new_paragraphs[i] = new_paragraphs[i].replace('\n', '')
            new_paragraphs[i] = new_paragraphs[i].replace(' ', '')
            last_paragraphs.append(new_paragraphs[i])
        # print(last_paragraphs)
        print(len(last_paragraphs))
        return last_paragraphs

    def count_person(self):
        '''
        统计人物出场次数，添加每段的人物
        :return:
        '''
        paragraphs = self.get_clean_paragraphs()  # checked
        synonymous = self.synonymous_names()  # checked
        print('start process node')
        with codecs.open(self._dict_path, 'r', 'utf-8') as f:
            name_list = f.read().split('\n')  # 获取干净的name_list
            print(name_list)
        for p in paragraphs:
            jieba.load_userdict(self._dict_path)
            # 分词，为每一段初始化新字典
            poss = jieba.cut(p)
            self._person_per_paragraph.append([])
            for w in poss:
                # 判断是否在姓名字典以及同义词区分
                if w not in name_list:
                    continue
                if synonymous.get(w):
                    w = synonymous[w]
                # 往每段中添加人物
                self._person_per_paragraph[-1].append(w)
                # 初始化人物关系，计数
                if self._person_counter.get(w) is None:
                    self._relationships[w] = {}
                self._person_counter[w] += 1
        return self._person_counter

    def calc_relationship(self):
        '''
        统计人物关系权值
        :return:
        '''
        print("start to process edge")
        # 遍历每一段落，笛卡尔积形式，统计人物关系
        # print(self._person_per_paragraph)
        for p in self._person_per_paragraph:
            for name1 in p:
                for name2 in p:
                    if name1 == name2:
                        continue
                    if self._relationships[name1].get(name2) is None:
                        self._relationships[name1][name2] = 1
                    else:
                        self._relationships[name1][name2] += 1
        return self._relationships

    def save_node_and_edge(self):
        peopleCount = 1
        with codecs.open(SAVE_NODE_PATH, "a+", "utf-8") as f:
            # f.write("Id,Label,Weight\r\n")
            for name, times in self._person_counter.items():
                # f.write(name + "," + str(times) + "\r\n")
                f.write("{\"id\": \"" + peopleCount + "\", \"name\": " + name +
                        "\", \"val\": " + str(times) + "},\r\n")
                peopleCount += 1
        # print(self._person_counter)

        relationCount = 0
        i = 0
        maxRecord = []
        maxEdge = []
        with codecs.open(SAVE_EDGE_PATH, "a+", "utf-8") as f:
            # f.write("Source,Target,Weight\r\n")
            for name, edges in self._relationships.items():
                max = 0
                maxedge = ""
                for v, w in edges.items():
                    relationCount += w
                    if max < w:
                        max = w
                        maxedge = v
                maxRecord.append(max)
                maxEdge.append(maxedge)
                i += 1

            i = 0
            for name, edges in self._relationships.items():
                print(name + ":" + str(maxRecord[i]))
                for v, w in edges.items():
                    if maxRecord[i] < 20:
                        f.write("{\"source\": \"" + name +
                                "\", \"target\": \"" + maxEdge[i] +
                                "\", \"value\": " + str(maxRecord[i]) +
                                "},\r\n")
                        break
                    if w > 20:
                        f.write("{\"source\": \"" + name +
                                "\", \"target\": \"" + v + "\", \"value\": " +
                                str(w) + "},\r\n")
                i += 1
        # print(self._relationships)
        print('save file successful!')


if __name__ == '__main__':
    v = RelationshipView(TEXT_PATH, DICT_PATH, SYNONYMOUS_DICT_PATH)
    v.generate()
