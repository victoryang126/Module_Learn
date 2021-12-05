"""
bytes 对象是由单个字节构成的不可变序列。 由于许多主要二进制协议都基于 ASCII 文本编码，因此 bytes 对象提供了一些仅在处理 ASCII 兼容数据时可用，并且在许多特性上与字符串对象紧密相关的方法。
bytes 字面值中只允许 ASCII 字符（无论源代码声明的编码为何）。 任何超出 127 的二进制值必须使用相应的转义序列形式加入 bytes 字面值

"""

# classmethod fromhex(string)
# 此 bytes 类方法返回一个解码给定字符串的 bytes 对象。 字符串必须由表示每个字节的两个十六进制数码构成，其中的 ASCII 空白符会被忽略

print(bytes.fromhex('2Ef0 F1f2  '))
#b'.\xf0\xf1\xf2'

# hex([sep[, bytes_per_sep]])
# 返回一个字符串对象，该对象包含实例中每个字节的两个十六进制数字

print(b'\xf0\xf1\xf2'.hex())
#'f0f1f2'

value = b'\xf0\xf1\xf2'
print(value.hex('-'))
# 'f0-f1-f2'
print(value.hex('_', 2))
# 'f0_f1f2'
print(b'UUDDLRLRAB'.hex(' ', -4))
# '55554444 4c524c52 4142'
#
# 由于 bytes 对象是由整数构成的序列（类似于元组），因此对于一个 bytes 对象 b，
# b[0] 将为一个整数，而 b[0:1] 将为一个长度为 1 的 bytes 对象。
# （这与文本字符串不同，索引和切片所产生的将都是一个长度为 1 的字符串）
print(value[0]) #240
print(value[0:1]) #b'\xf0'
# value[0] = 241 #不可改变 异常  'bytes' object does not support item assignment
print(value)
# bytearray 对象是 bytes 对象的可变对应物。

print(bytearray.fromhex('2Ef0 F1f2  '))
# bytearray(b'.\xf0\xf1\xf2')

print(bytearray(b'\xf0\xf1\xf2').hex())
# 'f0f1f2'

value = bytearray(b'\xf0\xf1\xf2')

value[0] = 241;
print(value) #bytearray(b'\xf1\xf1\xf2')