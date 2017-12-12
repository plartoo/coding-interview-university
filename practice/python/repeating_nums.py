from collections import defaultdict

# URL: https://www.reddit.com/r/dailyprogrammer/comments/7eh6k8/20171121_challenge_341_easy_repeating_numbers/?ref=share&ref_source=link
num = 1222
num = 11325992321982432123259
num = 1234565943210
cnt_table = defaultdict(int)
str_num = str(num)
for i,d1 in enumerate(str_num):
    for j,d2 in enumerate(str_num[(i+1):]):
        temp_str = d1+(str_num[(i+1):][0:j+1])
        cnt_table[temp_str] += 1

# sort by value: https://stackoverflow.com/a/2258273
for k,v in sorted(cnt_table.items(), key=lambda (k,v): v, reverse=True):
    print("{0}: {1}".format(k, cnt_table[k]))


