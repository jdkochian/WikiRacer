import wikipedia
from collections import deque
from NodeData import NodeData
from datamuse import datamuse

def bfs(u, v) -> list:
    api = datamuse.Datamuse()
    SFMap = {}
    q = deque()
    q.append(u)
    SFMap[u.title] = NodeData(0, None)

    list = createList(v, api)

    while q:
        u = q.popleft()

        print("Popping " + u.title + "...")
        if u == v:
            return pathify(SFMap, v)

        for pageTitle in u.links:
            if(len(list) == 1 or pageTitle.lower() in list):

                try:
                    wikiPage = wikipedia.page(pageTitle, auto_suggest = False)
                except wikipedia.DisambiguationError:
                    continue
                except wikipedia.PageError:
                    continue
                pageDist = 1 + SFMap.get(u.title).dist

                if(wikiPage.title not in SFMap):
                    print("Adding " + pageTitle + "...")
                    SFMap[wikiPage.title] = NodeData(pageDist, u)
                    q.append(wikiPage)
                    if(len(q) % 100 == 0):
                        print("Queue Size: " + str(len(q)) + " articles!")
                        print("\n")

                #if (pageTitle == v.title):
                if(wikipage == v):
                    q.appendleft(wikiPage)
                    break

    return []

def pathify(map, v) -> list:
    list = []
    page = v

    while(page != None):
        list.append(page)
        page = map.get(page.title).bkptr

    return list

def createList(v, api) -> list:
    jsonList = api.words(ml=v.title, v = 'enwiki')
    list = []
    for j in jsonList:
        list.append(j['word'])
        children = api.words(ml=j['word'], v ='enwiki')
        for k in children:
            if k['word'] not in list:
                list.append(k['word'])
    list.append(v.title.lower())
    for d in v.links:
        if d not in list:
            list.append(d.lower())
    print(list)
    return list

def main():
    m = wikipedia.page('Dog', auto_suggest = False)
    s = wikipedia.page('Hug', auto_suggest = False)
    list = bfs(m, s)
    print('I MADE IT THIS FAR!')
    for i in list:
        print(i.title)

if __name__ == "__main__":
    main()
