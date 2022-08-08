def ranMag(x, mag):
    ransomNote = x
    magazine = mag
    mag_list = list(magazine)

    counts = 0
    for char in ransomNote:
        if char in mag_list:
            counts += 1
            mag_list.remove(char)

    if counts != len(ransomNote):
        ans = False
    else:
        ans = True

    return ans


print(ranMag('a', 'b'))
print(ranMag('aa', 'ab'))
print(ranMag('aa', 'aab'))
