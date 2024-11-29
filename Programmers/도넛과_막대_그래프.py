def solution(edges):
    answer = []
    max_vertexID = 0
    stick, donut, eight = 0, 0, 0
    
    for edge in edges:
        max_vertexID = max(max(edge), max_vertexID)
    
    graph_out = [[] for _ in range(max_vertexID+1)]
    graph_in = [[] for _ in range(max_vertexID+1)]
    
    for edge in edges:
        graph_out[edge[0]].append(edge[1])
        graph_in[edge[1]].append(edge[0])

    for i in range(1, len(graph_in)):
        if len(graph_out[i]) >= 2 and len(graph_in[i]) == 0: 
            add_vertex = i

    for i in range(len(graph_out[add_vertex])):
        if len(graph_out[graph_out[add_vertex][i]]) == 0:
            stick += 1
        elif len(graph_out[graph_out[add_vertex][i]]) == 2:
            eight += 1
        else:
            x = graph_out[add_vertex][i]
            
            while 1:
                x = graph_out[x][0]
                if(len(graph_out[x]) == 2):
                    eight += 1
                    break
                if(len(graph_out[x]) == 0):
                    stick += 1
                    break
                if x == graph_out[add_vertex][i]:
                    donut += 1
                    break
                    
    answer.append(add_vertex)
    answer.append(donut)
    answer.append(stick)
    answer.append(eight)
    
    return answer
