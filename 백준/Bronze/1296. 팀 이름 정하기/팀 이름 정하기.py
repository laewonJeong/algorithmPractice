import sys
input = sys.stdin.readline

def calc_pr(name, team):
    l = name.count('L') + team.count('L')
    o = name.count('O') + team.count('O')
    v = name.count('V') + team.count('V')
    e = name.count('E') + team.count('E')

    return ((l+o) * (l+v) * (l+e) * (o+v) * (o+e) * (v+e)) % 100

def main():
    # Write your solution here
    name = input().rstrip()
    n    = int(input())
    max  = -1

    for _ in range(n):
        team_cand = input().rstrip()
        prohibit  = calc_pr(name, team_cand)

        if prohibit > max:
            max  = prohibit
            team = team_cand
        elif prohibit == max and team_cand < team:
            team = team_cand

    print(team)

if __name__ == "__main__":
    main()