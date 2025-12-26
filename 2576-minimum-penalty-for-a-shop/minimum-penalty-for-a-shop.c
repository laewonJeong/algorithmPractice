int
count_Y(char* str){
    int i;
    int count = 0;

    for(i = 0; str[i] != '\0'; i++){
        if(str[i] == 'Y'){
            count++;
        }
    }

    return count;
}

int bestClosingTime(char* customers) {
    int i;
    char current;

    int len             = strlen(customers) + 1;
    int min_hour        = 0;
    int current_penalty = count_Y(customers);
    int min_penalty     = current_penalty;

    if(current_penalty == 0)
        return 0;
    
    for(i = 1; i < len; i++)
    {
        current         = customers[i - 1];
        current_penalty += (current == 'Y') ? -1 : 1;

        if(current_penalty < min_penalty){
            min_penalty = current_penalty;
            min_hour    = i;
        }
    }

    return min_hour;
}