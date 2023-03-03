from subprocess import *

# Tạo process mới và chuyển hướng stdin, stdout,
p = Popen([r'VULNERABLE_o_NO.exe','f'], stdout=PIPE, stdin=PIPE, stderr=STDOUT)
print "ATACHEA EL DEBUGGER Y APRETA ENTER\n"
# Script dừng lại đợi tới khi nhấn Enter
raw_input()
size = "10\n"

# Truyền dữ liệu cho process
p.stdin.write(size)
user_input = "AAAA\n"
p.stdin.write(user_input)

# Lấy kết quả
testresult = p.communicate()[0]
print(testresult, size, user_input)
