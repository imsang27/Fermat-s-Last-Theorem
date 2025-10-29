import random

print("엔터를 누를 때마다 새로운 랜덤 계산을 수행합니다. (종료: Ctrl + C)\n")

while True:
    input("계산을 시작하려면 엔터를 누르세요...")
    
    # 1. 랜덤 정수 두 개 생성 (1~100 사이)
    a = random.randint(1, 100)
    b = random.randint(1, 100)

    # 2. 각각 3제곱
    a_cubed = a ** 3
    b_cubed = b ** 3

    # 3. 두 수를 더함
    total = a_cubed + b_cubed

    # 4. n^3 = total → n = total ** (1/3)
    n = total ** (1/3)

    # 5. 결과 출력
    print(f"\n🎲 랜덤 숫자: {a}, {b}")
    print(f" {a}³ = {a_cubed:,}")
    print(f" {b}³ = {b_cubed:,}")
    print(f" ➕ 두 수의 합: {total:,}")
    print(f" ➡️ n³ = {total:,} → n ≈ {n:.4f}\n")
