def obd_to_ascii(obd_bytearray):
    # 新的ASCII格式的bytearray
    ascii_bytearray = bytearray()
    
    # 遍历原始bytearray中的每个字节
    for byte in obd_bytearray:
        # 将每个字节转换为两个字符的十六进制表示（带前导零）
        hex_str = format(byte, '02x')
        # 将每个字符的ASCII值添加到新的bytearray中
        for char in hex_str:
            ascii_bytearray.append(ord(char))
    
    return ascii_bytearray

# 测试函数
original_bytearray = bytearray([0x32, 0x34])
ascii_bytearray = obd_to_ascii(original_bytearray)

print(ascii_bytearray)  # 输出：bytearray(b'33323434')
