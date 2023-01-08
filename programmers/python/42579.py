# Lv 3. 베스트 앨범 - 해시

def solution(genres, plays):
    answer = []
    dict = {}
    total_dict = {}
    
    for i in range(len(genres)):
        if genres[i] in dict:
            dict[genres[i]].append([plays[i],i])
        else :
            dict[genres[i]] = [[plays[i],i]]
        if genres[i] in total_dict:
            total_dict[genres[i]] += plays[i]
        else:
            total_dict[genres[i]] = plays[i]

    total_dict = sorted(total_dict.items(), key=lambda x: x[1], reverse=True)

    for key in total_dict:
        genre_songs = dict[key[0]]
        print(genre_songs)
        genre_songs = sorted(genre_songs, key=lambda x: x[0], reverse=True)
        print(genre_songs)

        if len(genre_songs) == 1:
            answer.append(genre_songs[0][1])
        else:
            for i in range(2):
                answer.append(genre_songs[i][1])

    return answer

answer = solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500])
print(answer)

"""
def solution(genres, plays):
    answer = []

    dict = {}
    total_dict = {}

    for i, (g, p) in enumerate(zip(genres, plays)):
        if g not in dict:
            dict[g] = [(i, p)]
        else:
            dict[g].append((i, p))

        if g not in total_dict:
            total_dict[g] = p
        else:
            total_dict[g] += p

    for (k, v) in sorted(total_dict.items(), key=lambda x:x[1], reverse=True):
        for (i, p) in sorted(dict[k], key=lambda x:x[1], reverse=True)[:2]:
            answer.append(i)

    return answer
"""