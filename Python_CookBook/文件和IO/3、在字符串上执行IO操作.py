import io

s = io.StringIO()
s.write('hello world\n')
print('this is a test', file=s)
print(s.getvalue())
