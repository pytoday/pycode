import re
from functools import reduce
class SearchEngineBase(object):
    def __init__(self):
        pass
    
    def add_corpus(self, fpath):
        with open(fpath)  as fn:
            text = fn.read()
            self.process_corpus(fpath, text)
            
    def process_corpus(self, id, text):
        raise Exception("Process_corpus not implemented.")
        
    def search(self, query):
        raise Exception("Search not implemented.")
    

class BOWInvertedIndexEngine(SearchEngineBase):
    def __init__(self):
        super().__init__()
        self.inverted_index = {}
        
    def process_corpus(self, id, text):
        words = self.parse_text_to_words(text)
        for word in words:
            if word not in self.inverted_index:
                self.inverted_index[word] = []
            self.inverted_index[word].append(id)
    
    def search(self, query):
        query_words = list(self.parse_text_to_words(query))
        '''
        query_words_index = []
        for query_word in query_words:
            query_words_index.append(0)
        
        #如果一个查询的索引为空则直接返回空值
        for query_word in query_words:
            if query_word not in self.inverted_index:
                return []
        
        result = []
        while True:
            #当前状态下所有倒序索引的index
            current_ids = []
            for idx, query_word in enumerate(query_words):
                current_index = query_words_index[idx]
                current_inverted_list = self.inverted_index[query_word]
                # 已经遍历到了某一个倒序索引的末尾，结束 search
                if current_index >= len(current_inverted_list):
                    return result
                current_ids.append(current_inverted_list[current_index])
            # 然后，如果 current_ids 的所有元素都一样，那么表明这个单词在这个元素对应的文档中都出现了 
            if all(x == current_ids[0] for x in current_ids): 
                result.append(current_ids[0]) 
                query_words_index = [x + 1 for x in query_words_index] 
                continue 
            # 如果不是，我们就把最小的元素加一 
            min_val = min(current_ids) 
            min_val_pos = current_ids.index(min_val) 
            query_words_index[min_val_pos] += 1
        '''
        #inverted index 为单个词到对应文件的字典映射，判断多个词同时在某个文件，只需要求以查询词为key的列表的交集
        if set(query_words) < set(self.inverted_index.keys()):
            result=set(reduce(lambda x, y: x & y, [set(self.inverted_index[qv]) for qv in query_words]))
            return result
        return []
        
    
    @staticmethod
    def parse_text_to_words(text):
        #删除标点等特殊字符
        text = re.sub(r'[^\w]', ' ', text)
        #转小写
        text = text.lower()
        #字符转列表
        word_list = text.split(' ')
        #过滤空值
        word_list = filter(None, word_list)
        return set(word_list)
        
def main(search_engine):
    for fpath in ['1.txt', '2.txt', '3.txt', '4.txt', '5.txt']:
        search_engine.add_corpus(fpath)
        
    while True:
        query = input()
        results = search_engine.search(query)
        print("Found {} result(s)".format(len(results)))
        for result in results:
            print(result)
            
search_engine = BOWInvertedIndexEngine()
main(search_engine)