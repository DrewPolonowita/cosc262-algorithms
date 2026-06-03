from cosc262 import *

def is_subsequence(sub, s):
    i = 0
    for c in s:
        if i < len(sub) and c == sub[i]:
            i += 1
    return i == len(sub)

tests = [
    ("abcdef", "abc", 3),          # "abc"
    ("abcdef", "acdf", 4),         # "acdf"
    ("AGGTAB", "GXTXAYB", 4),      # "GTAB"
    ("XMJYAUZ", "MZJAWXU", 4),     # "MJAU"
    ("zxabcdezy", "yzabcdezx", 7)  # "zabcdez"
]

for s1, s2, expected_len in tests:
    td = longest_common_subsequence_top_down(s1, s2)
    bu = longest_common_subsequence_bottom_up(s1, s2)

    if not is_subsequence(td, s1):
        print(f"TOP DOWN FAIL: {td!r} is not a subsequence of {s1!r}")
        break

    if not is_subsequence(td, s2):
        print(f"TOP DOWN FAIL: {td!r} is not a subsequence of {s2!r}")
        break

    if len(td) != expected_len:
        print(
            f"TOP DOWN FAIL: inputs=({s1!r}, {s2!r}) "
            f"expected length {expected_len}, got {len(td)} ({td!r})"
        )
        break

    if not is_subsequence(bu, s1):
        print(f"BOTTOM UP FAIL: {bu!r} is not a subsequence of {s1!r}")
        break

    if not is_subsequence(bu, s2):
        print(f"BOTTOM UP FAIL: {bu!r} is not a subsequence of {s2!r}")
        break

    if len(bu) != expected_len:
        print(
            f"BOTTOM UP FAIL: inputs=({s1!r}, {s2!r}) "
            f"expected length {expected_len}, got {len(bu)} ({bu!r})"
        )
        break
else:
    print("All tests passed!")