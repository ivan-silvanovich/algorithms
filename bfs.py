from collections import deque

graph = {
    "you": ["alice", "bob", "claire"],
    "bob": ["anuj", "peggy"],
    "alice": ["peggy"],
    "claire": ["thom", "jonny"],
    "anuj": [],
    "peggy": [],
    "thom": [],
    "jonny": []
}


def mango_seller_check(person: str):
    return person[-1] == 'm'


def simple_bfs(graph: dict, start_point: str):
    q = deque()
    checked_list = []

    q += graph[start_point]
    while q:
        person = q.popleft()

        if person not in checked_list:
            if mango_seller_check(person):
                return person
            else:
                checked_list.append(person)
                q += graph[person]

    return None


print(simple_bfs(graph, 'you'))
