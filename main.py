from solution import Solution  

def main():
    solution = Solution()
    
    s = input("Enter string s (subsequence): ")
    t = input("Enter string t: ")
    
    result = solution.isSubsequence(s, t)
    
    if result:
        print(f"'{s}' is a subsequence of '{t}'.")
    else:
        print(f"'{s}' is NOT a subsequence of '{t}'.")


if __name__ == "__main__":
    main()
