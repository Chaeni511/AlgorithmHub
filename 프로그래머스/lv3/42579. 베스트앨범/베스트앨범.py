def solution(genres, plays):
    answer = []
    cnt = {}

    for i, (genre, play) in enumerate(zip(genres, plays)):
        if genre in cnt:
            cnt[genre][0] += play
            cnt[genre][1].append((play, i))
            # cnt[genre] = [cnt[genre][0] + play, cnt[genre][1]+[(play,i)]]
        else:
            cnt[genre] = [play, [[play,i]]]
    
    for genre, play in sorted(cnt.items(), key = lambda x: -x[1][0]):
        for p, i in sorted(play[1], key = lambda x: -x[0])[:2]:
            answer.append(i)

    return answer