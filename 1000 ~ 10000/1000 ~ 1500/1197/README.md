# Minimum Spanning Tree(MST)

### ***Minimum Spanning Tree***

- 신장 트리 중에서 최소 비용으로 만들 수 있는 신장 트리를 찾는 알고리즘을 ***Minimum Spanning Tree***라고 함
- 대표적인 알고리즘에는 ***Kruskal Algorithm***이 있음

### ***What is Spanning Tree?***

- **Spanning Tree**
    - 하나의 그래프가 있을 때 ***모든 노드를 포함하면서 사이클이 존재하지 않는 부분 그래프***

### ***What is Minimum Spanning Tree?***

- 신장트리의 조건을 만족하면서 최소 비용으로 만들 수 있는 신장트리
- **Kruskal Algorithm**은 신장 트리 중에서도 최소한의 비용으로 만들 수 있는 최소 신장트리를 찾는 알고리즘

## *Kruskal Algorithm 동작과정*

```html
1. 간선 데이터를 비용에 따라 오름차순으로 정렬
2. 간선을 하나씩 확인하며 현재의 간선이 사이클을 발생시키는지 확인
	a. 사이클이 발생하지 않는 경우 최소 신장 트리에 포함시킴
	b. 사이클이 발생하는 경우 최소 신장 트리에 포함시키지 않음
3. 모든 간산에 대하여 2번의 과정을 반복
```
