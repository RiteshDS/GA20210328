# -*- coding: utf-8 -*-
"""
Created on Sun Mar 28 15:11:43 2021

@author: ritesh
"""

class ReadArticles:
    def __init__(self):
        self.dataPath = r'C:\Users\ritesh\Desktop\GA2021_28032021\ga2803\data\article1.txt'
        
    def loadArticles1(self,path):
        with open(path,'r') as f1:
            text = f1.read()
            return text
        
    def loadArticles(self):
        with open(self.dataPath,'r') as f1:
            text = f1.read()
            return text
    def loadArticlesFromDb(self):
        pass
        
    def loadArticlesFromApi(self):
        pass
    
readObj = ReadArticles()

articleText = readObj.loadArticles()
print('The text is:\n\n{}'.format(articleText))