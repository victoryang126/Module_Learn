import decimal

#格式字符串语法
'''
内置的字符串类提供了通过使用 PEP 3101 所描述的 format() 方法进行复杂变量替换和值格式化的能力。
string 模块中的 Formatter 类允许你使用与内置 format() 方法相同的实现来创建并定制你自己的字符串格式化行为。
格式字符串包含有以花括号 {} 括起来的“替换字段”。 不在花括号之内的内容被视为字面文本，会不加修改地复制到输出中。
如果你需要在字面文本中包含花括号字符，可以通过重复来转义: {{ and }}

格式字符串字面值示例如下

f_string          ::=  (literal_char | "{{" | "}}" | replacement_field)*
replacement_field ::=  "{" f_expression ["="] ["!" conversion] [":" format_spec] "}"
f_expression      ::=  (conditional_expression | "*" or_expr)
                         ("," conditional_expression | "," "*" or_expr)* [","]
                       | yield_expression
conversion        ::=  "s" | "r" | "a"
format_spec       ::=  (literal_char | NULL | replacement_field)*
literal_char      ::=  <any code point except "{", "}" or NULL>
>>> name = "Fred"
>>> f"He said his name is {name!r}."
"He said his name is 'Fred'."
>>> f"He said his name is {repr(name)}."  # repr() is equivalent to !r
"He said his name is 'Fred'."
>>> width = 10
>>> precision = 4
>>> value = decimal.Decimal("12.34567")
>>> f"result: {value:{width}.{precision}}"  # nested fields
'result:      12.35'
>>> today = datetime(year=2017, month=1, day=27)
>>> f"{today:%B %d, %Y}"  # using date format specifier
'January 27, 2017'
>>> f"{today=:%B %d, %Y}" # using date format specifier and debugging
'today=January 27, 2017'
>>> number = 1024
>>> f"{number:#0x}"  # using integer format specifier
'0x400'
>>> foo = "bar"
>>> f"{ foo = }" # preserves whitespace
" foo = 'bar'"
>>> line = "The mill's closed"
>>> f"{line = }"
'line = "The mill\'s closed"'
>>> f"{line = :20}"
"line = The mill's closed   "
>>> f"{line = !r:20}"
'line = "The mill\'s closed" '
'''

#1.
# f_string          ::=  (literal_char | "{{" | "}}" | replacement_field)*
# 指定了转换符时，表达式求值的结果会先转换，再格式化。转换符 '!s'
# 调用 str() 转换求值结果，'!r' 调用 repr()，'!a' 调用 ascii()。
# name = "Fred"
# print(f"He said his name is {name!r}.")
# print(f"He said his name is {repr(name)}.") # repr() is equivalent to !r
# print(f"He said his name is {name}.")
# "He said his name is 'Fred'."

#2.
#replacement_field ::=  "{" f_expression ["="] ["!" conversion] [":" format_spec] "}"
# import datetime
# width = 10
# precision = 4
# value = decimal.Decimal("12.34567")
# print(f"result: {value:{width}.{precision}}")  # nested fields, 改变数据占的长度和精确度
# print()
# 'result:      12.35'
#  result:     12.346
#
# today = datetime.datetime(year=2017, month=1, day=27)
# print(f"{today:%B %d, %Y}")  # using date format specifier
# # 'January 27, 2017'
# print(f"{today=:%B %d, %Y}")# using date format specifier and debugging
# # 'today=January 27, 2017'
# number = 1024
# print(f"{number:#0x}")  # using integer format specifier
# # '0x400'
# foo = "bar"
# print(f"{ foo = }") # preserves whitespace
# " foo = 'bar'"
# >>> line = "The mill's closed"
# >>> f"{line = }"
# 'line = "The mill\'s closed"'
# >>> f"{line = :20}"
# "line = The mill's closed   "
# >>> f"{line = !r:20}"
# 'line = "The mill\'s closed" '

'''
format_spec     ::=  [[fill]align][sign][#][0][width][grouping_option][.precision][type]
fill            ::=  <any character>
align           ::=  "<" | ">" | "=" | "^"
sign            ::=  "+" | "-" | " "
width           ::=  digit+
grouping_option ::=  "_" | ","
precision       ::=  digit+
type            ::=  "b" | "c" | "d" | "e" | "E" | "f" | "F" | "g" | "G" |
 "n" | "o" | "s" | "x" | "X" | "%"
 '<' 强制字段在可用空间内左对齐（这是大多数对象的默认值）。
'>' 强制字段在可用空间内右对齐（这是数字的默认值）。
'=' 强制将填充放置在符号（如果有）之后但在数字之前。这用于以“+000000120”形式打印字段。此对齐选项仅对数字类型有效。当'0'紧接在 字段宽度之前时，它成为默认值。
'^'  强制字段在可用空间内居中。
+'    表示标志应该用于正数和负数。
'-'   表示标志应仅用于负数（这是默认行为）。
space   表示应在正数上使用前导空格，在负数上使用减号
'#' 选项可让“替代形式”被用于执行转换
'''

#按位置访问
'''
print('{0}, {1}, {2}'.format('a', 'b', 'c'))
# 'a, b, c'
print('{}, {}, {}'.format('a', 'b', 'c'))  # 3.1+ only
# 'a, b, c'
print('{2}, {1}, {0}'.format('a', 'b', 'c'))
# 'c, b, a'
print('{2}, {1}, {0}'.format(*'abc') )     # unpacking argument sequence
# 'c, b, a'
print('{0}{1}{0}'.format('abra', 'cad') )  # arguments' indices can be repeated
# 'abracadabra'
'''

#按名称访问
'''
print('Coordinates: {latitude}, {longitude}'.format(latitude='37.24N', longitude='-115.81W'))
# 'Coordinates: 37.24N, -115.81W'
coord = {'latitude': '37.24N', 'longitude': '-115.81W'}
print('Coordinates: {latitude}, {longitude}'.format(**coord))
# 'Coordinates: 37.24N, -115.81W'
'''

# 访问参数的属性:
'''
c = 3-5j
print(('The complex number {0} is formed from the real part {0.real} ' 'and the imaginary part {0.imag}.').format(c))
# 'The complex number (3-5j) is formed from the real part 3.0 and the imaginary part -5.0.'
#  class Point:
# ...     def __init__(self, x, y):
#     ...         self.x, self.y = x, y
# ...     def __str__(self):
#     ...         return 'Point({self.x}, {self.y})'.format(self=self)
# ...
# str(Point(4, 2))
# 'Point(4, 2)'
'''
#访问参数的项
'''
coord = (3, 5)
print('X: {0[0]};  Y: {0[1]}'.format(coord))
# 'X: 3;  Y: 5'
# 替代 %s 和 %r:
print("repr() shows quotes: {!r}; str() doesn't: {!s}".format('test1', 'test2'))
"repr() shows quotes: 'test1'; str() doesn't: test2"
'''
# 对齐文本以及指定宽度:
'''
print('{:<30}'.format('left aligned'))
# 'left aligned                  '
print('{:>30}'.format('right aligned'))
print('{:^30}'.format('centered'))
# '           centered           '
print('{:*^30}'.format('centered'))   # use '*' as a fill char
# '***********centered***********'
'''
# 替代 %+f, %-f 和 % f 以及指定正负号:
'''
print('{:+f}; {:+f}'.format(3.14, -3.14)) # show it always
# '+3.140000; -3.140000'
print('{: f}; {: f}'.format(3.14, -3.14)) # show a space for positive numbers
print('{:-f}; {:-f}'.format(3.14, -3.14))  # show only the minus -- same as '{:f}; {:f}'
# '3.140000; -3.140000'
'''
# 替代 %x 和 %o 以及转换基于不同进位制的值:
# 使用逗号作为千位分隔符:
# 表示为百分数:
# 使用特定类型的专属格式化:
'''
print('{:+f}; {:+f}'.format(3.14, -3.14))  # show it always
# '+3.140000; -3.140000'
print('{: f}; {: f}'.format(3.14, -3.14))  # show a space for positive numbers
# ' 3.140000; -3.140000'
print('{:-f}; {:-f}'.format(3.14, -3.14))  # show only the minus -- same as '{:f}; {:f}'
# '3.140000; -3.140000'
# >>> # format also supports binary numbers
print("int: {0:d};  hex: {0:x};  oct: {0:o};  bin: {0:b}".format(42))
# 'int: 42;  hex: 2a;  oct: 52;  bin: 101010'
# >>> # with 0x, 0o, or 0b as prefix:
print("int: {0:d};  hex: {0:#x};  oct: {0:#o};  bin: {0:#b}".format(42))
# int: 42;  hex: 0x2a;  oct: 0o52;  bin: 0b101010
print('{:,}'.format(1234567890))
# '1,234,567,890'

points = 19
total = 22
print('Correct answers: {:.2%}'.format(points/total))
# 'Correct answers: 86.36%'

import datetime
d = datetime.datetime(2010, 7, 4, 12, 15, 58)
print(d)
print('{:%Y-%m-%d %H:%M:%S}'.format(d))
# '2010-07-04 12:15:58'

'''

#嵌套参数以及更复杂的示例:
# '''
# print('{0:{fill}{align}16}'.format('left', fill='<', align='<'))
for align, text in zip('<^>', ['left', 'center', 'right']):
    print(align,text)
    # print('{0:{fill}{align}16}'.format(text, fill=align, align=align))
    # print('{0:{fill}{align}16}'.format(text, fill=align, align=align))
    print('{0:{fill}{align}16}'.format(text, fill=align, align=align))

# 'left<<<<<<<<<<<<'
# '^^^^^center^^^^^'
# '>>>>>>>>>>>right'

octets = [192, 168, 0, 1]
print('{:#02x}{:02X}{:02X}{:02X}'.format(*octets))
# 'C0A80001'
# print(int(_, 16))
# 3232235521

width = 5
for num in range(5,12):
    for base in 'dXob':
        print('{0:{width}{base}}'.format(num, base=base, width=width), end=' ')
    print()

   #  5     5     5   101
   #  6     6     6   110
   #  7     7     7   111
   #  8     8    10  1000
   #  9     9    11  1001
   # 10     A    12  1010
   # 11     B    13  1011
# '''