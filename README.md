# SmartCity_Model
A model of a city which has autonomous vehicles, done for AI Center Lipik, 2021
_____________________________________________________________________________________________________


### THE MAP ###
![nodes](https://user-images.githubusercontent.com/72471213/133169872-9067c041-cc16-4ef4-aa67-e9fad895db73.png)

red circles represent **nodes**, which were named according to our needs

blue numbers represent **distances** between *nodes*

and here it is represented in an **ajdacency matrix**:

    # o1,o2,o3,o4,o5,o6,o7,r1,r2,r3,r4,c1,c2,s, k
    [0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 3], # o1
    [5, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], # o2
    [0, 3, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5], # o3
    [0, 0, 3, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], # o4
    [0, 0, 0, 2, 0, 3, 0, 0, 0, 0, 0, 1, 0, 0, 0], # o5
    [0, 0, 0, 0, 3, 0, 3, 0, 0, 0, 0, 0, 1, 0, 0], # o6
    [0, 0, 0, 0, 0, 3, 0, 0, 0, 2, 0, 0, 0, 0, 0], # o7
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 2, 0], # r1
    [0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 2], # r2
    [0, 0, 0, 0, 0, 0, 2, 0, 1, 0, 0, 0, 0, 0, 0], # r3
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], # r4
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0], # c1
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 3, 0, 0, 2], # c2
    [5, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0], # s
    [3, 0, 5, 0, 0, 0, 0, 0, 2, 0, 0, 0, 2, 0, 0], # k


I've also made this graph in the following app, where I could test out if my Dijkstra implementation was correct
http://graphonline.ru/en/?graph=FLrknpVUCFzBzCfH (graph might expire after some time, but isn't hard to recreate)
