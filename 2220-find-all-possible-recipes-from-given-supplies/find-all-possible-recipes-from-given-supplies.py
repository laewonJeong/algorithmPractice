class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        graph = defaultdict(list)
        in_degree = defaultdict(int)
        supplies = set(supplies)

        for i, ingredient in enumerate(ingredients):
            for ing in ingredient:
                if recipes[i] not in in_degree:
                    in_degree[recipes[i]] = 0
                if ing not in supplies:
                    graph[ing].append(recipes[i])
                    in_degree[recipes[i]] += 1
        
        q = deque()

        for key in in_degree:
            if in_degree[key] == 0:
                q.append(key)
        
        answer = []
        while q:
            recipe = q.popleft()
            answer.append(recipe)

            for ingredient in graph[recipe]:
                in_degree[ingredient] -= 1
                if in_degree[ingredient] == 0:
                    q.append(ingredient)
        
        return answer