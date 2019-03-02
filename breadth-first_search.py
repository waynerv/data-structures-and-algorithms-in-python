from collections import deque

graph = {
    'kaka': ['waynerv']
}

def check_method(person):
    return person[-1] == 'v'

def search(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = []
    while search_queue:
        person = search_queue.popleft()
        if person not in searched:
            if check_method(person):
                print(f'{person} pass the check.')
                return True
            else:
                search_queue += graph[person]
                searched.append(person)
        return False

search('kaka')