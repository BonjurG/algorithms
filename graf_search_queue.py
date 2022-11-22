from collections import deque

graph = {}
graph["me"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["tom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["tom"] = []
graph["jonny"] = ["jymaysymba"]


def person_seller(name):  # if name[-1] = a we find our man
    return name[-1] == 'a'


def search(name):
    search_queue = deque()  # create ochered
    search_queue += graph[name]  # ochered have new person
    searched = []
    while search_queue:  # while true
        person = search_queue.popleft()  # next person who say first in dequue
        if not person in searched:
            if person_seller(person):
                print(f'{person} we find you!!!!')
                return True
            else:
                search_queue += graph[person]  # add person sosedei in deque
                # print(person)
                searched.append(person)
    return False


print(search('me'))
