def solution(genres, plays):
    answer = []
    
    album = {}
    a = []
    
    for idx, genre in enumerate(genres):
        answer.append([genre, idx, plays[idx]])
        if genre in album:
            album[genre][0] += plays[idx]
        else:
            album[genre] = [plays[idx]]
    
    answer.sort(key=lambda x: (-x[2], x[1]))
    
    for item in answer:
        album[item[0]].append(item[1])
    
    genres = list(album.keys())
    genres.sort(key=lambda x: album[x][0], reverse=True)
    
    for genre in genres:
        a.append(album[genre][1])
        if len(album[genre]) > 2:
            a.append(album[genre][2])
    
    return a

  
print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]	))