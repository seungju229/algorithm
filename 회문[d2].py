# 전치행렬하는 함수
def trans(arr):
    size = len(arr)
    for i in range(size):
        for j in range(size):
            if i < j:
                arr[i][j], arr[j][i] = arr[j][i], arr[i][j]
    return arr  # #for문이 다 돌아서 전치행렬로 완성된 다음 리턴해야되니까 for밖으로 나와야됨

            

# 행 우선 탐색해서 회문 찾는 함수
def r(N, M, arr):
    for i in range(N):
        for j in range(N - M + 1):  # N하면 안되는 이유: 밑에서 j에 k만큼 더 갈건데, N이면 이미 인덱스의 끝에 도달하므로 나중에 인덱스 에러가 남.
            for k in range(M // 2):
                if arr[i][j + k] != arr[i][j + M - 1 - k]:
                    break  # False 반환(회문이 없다.) #return false가 안되는 이유: return은 함수를 끝내겠다는 거니까 첫줄에 회문이 없으면 false반환하고 끝내버림. break하면 해당 반복문만 탈출함.
            else:  # break가 한번도 안걸리고 순환이 무사히 끝나면 else. else가 하나 더 오른쪽으로 가면 안되는 이유는 위의 if에서 반복문이 두번 돌면 두쌍 다 일치해야하는데, 한쌍만 일치해도 다음 else로 가게 됨.
                return arr[i][j:j + M]  # 슬라이싱해서 문자열 반환
    return False  # N까지 다 돌았는데 회문이 없으면 False를 반환해라.


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())  # N은 글자판 크기, M은 회문 길이
    arr = [list(map(str, input())) for _ in
           range(N)]  # map함수를 사용해서 인풋값을 str로 변환. str은 변경 불가능하기때문에 list로 한번에 들어오는 인풋 값은 전치행렬에서 사용이 안됨.

    result1 = r(N, M, arr)

    if result1 == False:  # result 1에 없으면
        result2 = r(N, M, trans(arr))
        print(f"#{tc} {''.join(result2)}")  # result2
    else:
        print(f"#{tc} {''.join(result1)}")




'''
1. 인덱스 에러 주의하기. 반복문 범위 다시 생각하기
2. 함수에서 return은 해당 반환값 반환하고 끝내버림. 반복문 내에서 조건을 설정하고 싶다면, return보다 break를 사용해서 나오기
3. 리스트에서 글자 하나하나 나오는 것을 하나로 합치고 싶으면 언패킹 *하기
4. for - else: 반복문을 무사히 마치면 else 실행 
5. 인풋 받을 때 잘 확인하기. 문자열이 통째로 있을 때 input().split()하면 띄어쓰기 기준으로 받아오는 거니까 문자열이 통째로 들어옴. 
'''