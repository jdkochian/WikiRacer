import wikipedia
from collections import deque
from NodeData import NodeData
from datamuse import datamuse

api = datamuse.Datamuse()

def bfs(u, v) -> list:
    """
    Perform a modified breadth first search to find 
    the shortest* path between two articles on Wikipedia. 

    `u`: Source article 
    `v`: Target Article 

    Returns list of articles in the shortest* path 
    """
    SFMap = {}
    q = deque()
    q.append(u)
    SFMap[u.title] = NodeData(0, None)

    lst = get_related_articles(v)

    while q:
        u = q.popleft()

        print("Popping " + u.title + "...")
        if u == v:
            return pathify(SFMap, v)

        for pageTitle in u.links:
            if(len(lst) == 1 or pageTitle.lower() in lst):

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

                if (pageTitle == v.title):
                # if(wikipage == v):
                    q.appendleft(wikiPage)
                    break

    return []

def pathify(SFMap, v) -> list:
    """
    Using backpointers, create a path back from the target article
    to the source article 

    `SFMap`: Dictionary that corresponds to the settled/frontier set in tradiitonal Dijkstra's Algorithm 
    `v`: Target article 

    """
    lst = []
    page = v

    while(page != None):
        lst.append(page)
        page = SFMap[page.title].bkptr

    return lst

def get_related_articles(v) -> list:
    """
    Create a list of related articles to the target article in order to
    pare down searchable articles from all of wikipedia. 

    `v`: Target article 
    """
    jsonList = api.words(ml=v.title, v = 'enwiki')
    lst = []
    for j in jsonList:
        lst.append(j['word'])
        children = api.words(ml=j['word'], v ='enwiki')
        for k in children:
            if k['word'] not in lst:
                lst.append(k['word'])
    lst.append(v.title.lower())
    # for d in v.links:
    #     if d not in lst:
    #         lst.append(d.lower())
    print(lst)
    return lst

def main():
    #Start article and end article:
    m = wikipedia.page('Dog', auto_suggest = False)
    s = wikipedia.page('Angst', auto_suggest = False)
    lst = bfs(m, s)
    print("This is the path:")
    for i in lst:
        print(i.title)

if __name__ == "__main__":
    main()
