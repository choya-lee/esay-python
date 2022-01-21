info_tuple = ("小明", 21, 1.85)

# 格式化字符串后面的 `()` 本质上就是元组
print("%s 年龄是 %d 身高是 %.2f" % info_tuple)

# 将要打印的传给变量info_str
info_str = "%s 年龄是 %d 身高是 %.2f" % info_tuple

# list tuple 相互转换
info_list = list(info_tuple)
info_tuple1 = tuple(info_list)

print(info_str)
print(info_list)
print(info_tuple1)
