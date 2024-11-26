from collections import defaultdict

def solution(genres, plays):
    answer = []
    total_play = defaultdict(int)
    genre_based_db = defaultdict(list)
    
    sort_genres_plays = [[i, genres[i], plays[i]] for i in range(len(genres))]
    sort_genres_plays.sort(key = lambda x:x[2], reverse = True)
    
    for idx, genre, play in sort_genres_plays:
        total_play[genre] += play
        genre_based_db[genre].append([idx, play])
    
    sort_total_play = [[genre, total_play[genre]] for genre in total_play]
    sort_total_play.sort(key=lambda x:x[1], reverse = True)
    
    for genre, play in sort_total_play:
        answer.append(genre_based_db[genre][0][0])
        if len(genre_based_db[genre]) > 1:
            answer.append(genre_based_db[genre][1][0])
    
    return answer
