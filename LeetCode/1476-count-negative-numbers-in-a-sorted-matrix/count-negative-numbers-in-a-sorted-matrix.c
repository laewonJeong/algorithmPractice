int countNegatives(int** grid, int gridSize, int* gridColSize) {
    int ans = 0;
    int n = gridSize;
    int m = gridColSize[0];
    
    for(int i = 0; i < n; i++){
        for(int j = 0; j < m; j++){
            if (grid[i][j] < 0){
                ans += m-j;
                break;
            }
        }
    }

    return ans;
}