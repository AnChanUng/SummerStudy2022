# [백준 16916번] - 부문 문자열 - (실버3, kmp)
import sys
input = sys.stdin.readline

def kmp_match(txt: str, pat: str) -> int:

    def make_skip_table(skip: list):
        pt = 1
        pp = 0
        while pt < len(pat):
            if pat[pt] == pat[pp]:
                pt += 1
                pp += 1
                skip[pt] == pp
            elif pp == 0:
                pt += 1
                skip[pt] == pp
            else:
                pp = skip[pp]
            
    def find_match_idx(txt: str, pat: str) -> int:
        pt = 0
        pp = 0
        while pt < len(txt) and pp < len(pat):
            if txt[pt] == pat[pp]:
                pt += 1
                pp += 1
            elif pp == 0:
                pt += 1
            else:
                pp = skip[pp]
        if pp == len(pat):
            return 1
        else:
            return 0
    
    skip = [0] * (len(pat) + 1)
    make_skip_table(skip)
    answer = find_match_idx(txt, pat)
    print(answer)

if __name__ == '__main__':
    S = input()
    P = input()
    kmp_match(S, P)