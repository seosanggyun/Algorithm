import sys; sys.stdin = open('input.txt')

for tc in range(10):
    tc = int(input())
    arr = [list(map(int, input().split())) for a in range(100)]

    # 좌 우 하 우선순위로 델타 정의
    # for문으로 돌 때, 0부터 2까지 돌리면
    # 0번째에 왼쪽, 1번째에 오른쪽, 2번째에 아랫쪽
    # 의 순으로 탐색
    dx = [0, 0, 1]
    dy = [-1, 1, 0]

    # x, y 두 값을 입력 받았을 때
    # 도착지점에 2가 나타나면 출발지점의 좌표를
    # 출력하는 함수 정의
    def ladder01(x, y):
        # x, y는 탐색을 해가면서 값이 변하기 때문에
        # 초기의 y값을 저장해둬야
        # 2를 찾았을 때 출발지점의 y값을 출력할 수 있음
        start_y = y

        # 방문했던 곳도 기록을 해둬야 하는 이유는
        # 기록 안 해놓으면
        # 아래로 가는 길이 없고 좌우 에만 1이 있을 경우
        # 좌우좌우좌우좌우 제자리에서 계속 맴돌 수 있음
        visited = [[0] * 100 for _ in range(100)]

        # 처음 시작지점을 방문했다고 표시 해놓아야 함
        visited[x][y] = 1

        # 99번 행에 다다를때까지 반복 돌릴거임
        while x != 99:
            # 아까 선언한 델타에 의해
            # 좌, 우, 하 우선순위로 탐색
            for a in range(3):
                # 다음에 방문할 지역의 인덱스를 설정
                nx = x + dx[a]
                ny = y + dy[a]

                # 조건문을 걸어서
                # 다음에 방문할 지역이 0과 100 사이의 범위, 즉
                # 벽을 벗어나지 않고
                # 또 방문했던 곳이 아니라면
                if 0 <= nx < 100 and 0 <= ny < 100 and visited[nx][ny] == 0:
                    # 탐색 했을 때 다음 방문 지역이 1이라면 이동
                    if arr[nx][ny] == 1:
                        # 방문했으니 방문했던 곳에 기록해야함
                        # visited에 방문 표시
                        visited[nx][ny] = 1
                        # 방문한 위치를 내 현재 위치로 변경해야
                        # 다시 탐색 가능
                        x, y = nx, ny
                    # 탐색 했을 때 다음 방문 지역이 2라면 (도착지라면)
                    elif arr[nx][ny] == 2:
                        # 아까 정의해놨던 처음 시작지점의 y 인덱스 반환
                        return start_y

    for j in range(100):
        # (0, j)가 1인 지점이 시작지점임
        # 0인 지점은 사다리 시작 아님
        if arr[0][j] == 1:
            result = ladder01(0,j)
            # 이까지만 하면
            # result 값에 뒤에 나온 result값이 덮어써지기 때문에
            # 출력해보면 None이 나옴
            # None이 아닌 값만
            # real_result에 저장되게 한 뒤 출력
            if result != None:
                real_result = result

    print(f'#{tc} {real_result}')





