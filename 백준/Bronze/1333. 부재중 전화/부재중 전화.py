import sys
input = sys.stdin.readline

# 입력값 처리
N, L, D = map(int, input().split())

# 앨범의 전체 길이 계산 (노래 시간 + 공백 시간 포함)
album_length = N * L + (N - 1) * 5

# 노래가 재생되는 시간을 표시할 리스트
play_times = [False] * album_length

# 각 노래가 재생되는 시간 표시
for start in range(0, album_length, L + 5):
    for time in range(start, start + L):
        play_times[time] = True

# D초 간격으로 벨소리가 울릴 때 노래가 재생되지 않는 시간 찾기
for bell_time in range(0, album_length, D):
    if not play_times[bell_time]:  # 노래가 재생되지 않는다면
        print(bell_time)
        break
else:
    # 앨범 전체 재생 후 처음 벨소리가 울리는 시간 출력
    print(bell_time + D)

# 블로그 참고함
# 뭐 이리 어려움?
