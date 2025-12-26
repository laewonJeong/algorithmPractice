int bestClosingTime(char* customers) {
    int i;
    char current;
    
    int len             = strlen(customers) + 1;
    int min_hour        = 0;
    int current_penalty = 0;

    for(i = 0; i < len; i++)
        current_penalty += (customers[i] == 'Y') ? 1 : 0;

    if(current_penalty == 0)
        return min_hour;

    int min_penalty = current_penalty;
    
    for(i = 1; i < len; i++){
        current         = customers[i - 1];
        current_penalty += (current == 'Y') ? -1 : 1;

        if(current_penalty < min_penalty){
            min_penalty = current_penalty;
            min_hour    = i;
        }
    }

    return min_hour;
}