
def mergeandsort(src1, src2, dst):
    # Use `with` statements to close file automatically
    with open(src1, 'r') as s1, open(src2, 'r') as s2, open(dst, 'w') as d:
        l = list(s1) + list(s2)
        l = [x.strip() for x in l]
        l.sort(reverse=True)
        c = '\n'.join(l)
        d.write(c)


mergeandsort('file1.txt', 'file2.txt', 'sorted.txt')