# python3

from math import floor


class Query:
    def __init__(self, query):
        self.type = query[0]
        self.number = int(query[1])
        if self.type == 'add':
            self.name = query[2]

def read_queries():
    n = int(input())
    return [Query(input().split()) for i in range(n)]

def write_responses(result):
    print('\n'.join(result))

def process_queries(queries):
    pass
    # a=0.75
    # m=3000;
    # n=2250;
    # result = []
    # # Keep list of all existing (i.e. not deleted yet) contacts.
    # contacts = []
    # for cur_query in queries:
    #     if cur_query.type == 'add':
            
            
    #     elif cur_query.type == 'del':
            
    #     else:
            
    # return result

class Buckets:
    buckets= [[]] * 3000
    m=3000
    n=2250
    a=0.75
    p=5051


def make_hash(s):
    ans=0
    for c in reversed(str(s)):
        ans=floor(ans * 0.75 + ord(c))%5051
    
    return ans%3000

def add(address, name, buckets):
    hashed= make_hash(address)
    bucket = buckets[hashed]
    index=False
    if bucket is None:
        bucket=[address, name]
        buckets[hashed]=bucket
        return buckets
    for i, item in enumerate(bucket):
        if item[0]==address:
            index=True
            item=[address, name]
            buckets[hashed][i]=item
    if not index:
        bucket.append([address, name])
        buckets[hashed]=bucket
    return buckets

def find(query, buckets):
    hashed= make_hash(query)
    bucket = buckets[hashed]
    
    if len(bucket)==1:
        print(bucket[0][1])
        return

    index=False
    for item in bucket:
        if item[0]==query:
            index=True
            print(item[1])
    if not index:
        print("not found")


def delete(query, buckets):
    hashed= make_hash(query)
    bucket = buckets[hashed]
    index=False
    for item in bucket:
        if item[0]==query:
            index=True
            bucket.remove(item)
            buckets[hashed]=bucket
            
    if not index:
        print("not found")
    return buckets

if __name__ == '__main__':
    queries=read_queries()
    buckets= [[]] * 3000
    
    for index, item in enumerate(queries):
        if item.type == 'add':
            buckets = add(item.number, item.name, buckets)
        elif item.type == 'find':
            find(item.number, buckets)
        else:
            buckets=delete(item.number, buckets)
    #write_responses(process_queries(read_queries()))

