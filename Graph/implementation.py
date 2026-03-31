"""
How to store graph
"""
def using_matrix(edges, n):
    """
    Space Complexity: O(n*n)
    Time Complexity: O(n)
    """
    matrix=[[0 for _ in range(n+1)] for _ in range(n+1)]
    print(matrix)
    for u, v in edges:
        matrix[u][v]=1
        matrix[v][u]=1
    print(matrix)

def using_list(edges,n):
    """
    Space Complexity : O(2E) where e stands for number of nodes
    Time Complexity : O(n)
    """
    ls1=[[] for _ in range(n+1)]
    print(ls1)
    for u, v in edges:
        ls1[u].append(v)
        ls1[v].append(u)
    print(ls1)

def using_dict(edges,n):
    """
    Space Complexity : O(2E) where e stands for number of nodes
    Time Complexity : O(n)
    """
    dict1={}
    for i in range(1,n+1):
        dict1[i]=[]
    for u,v in edges:
        dict1[u].append(v)
        dict1[v].append(u)

    print(dict1)

        

n=5
edges=[[1,2],[2,5],[3,4],[1,3]]
using_dict(edges,n)


