# WikiRacer

Python script that performs an iterative breadth-first search on Wikipedia, treating articles as nodes in a graph and links within said articles as edges. To prevent this algorithm from taking forever, this script makes use of the Datamuse API to only traverse down edges that are either strongly or loosely related to the target article. Without this, the algorithm has the potential to span through all of Wikipedia, which takes an exhaustive amount of memory and time. 

The GUI component is a WIP and is not ready for use. 
