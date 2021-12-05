'''
模板字符串
模板字符串支持基于 $ 的替换，使用以下规则：

$$ 为转义符号；它会被替换为单个的 $。
$identifier 为替换占位符，它会匹配一个名为 "identifier" 的映射键。 在默认情况下，"identifier" 限制为任意 ASCII 字母数字（包括下划线）组成的字符串，不区分大小写，以下划线或 ASCII 字母开头。 在 $ 字符之后的第一个非标识符字符将表明占位符的终结。
${identifier} 等价于 $identifier。 当占位符之后紧跟着有效的但又不是占位符一部分的标识符字符时需要使用，例如 "${noun}ification"。

substitute(mapping={}, /, **kwds)
执行模板替换，返回一个新字符串。 mapping 为任意字典类对象，其中的键将匹配模板中的占位符。 或者你也可以提供一组关键字参数，其中的关键字即对应占位符。 当同时给出 mapping 和 kwds 并且存在重复时，则以 kwds 中的占位符为优先。

safe_substitute(mapping={}, /, **kwds)
类似于 substitute()，不同之处是如果有占位符未在 mapping 和 kwds 中找到，不是引发 KeyError 异常，而是将原始占位符不加修改地显示在结果字符串中。 另一个与 substitute() 的差异是任何在其他情况下出现的 $ 将简单地返回 $ 而不是引发 ValueError。

此方法被认为“安全”，因为虽然仍有可能发生其他异常，但它总是尝试返回可用的字符串而不是引发一个异常。 从另一方面来说，safe_substitute() 也可能根本算不上安全，因为它将静默地忽略错误格式的模板，例如包含多余的分隔符、不成对的花括号或不是合法 Python 标识符的占位符等等。

Template 的实例还提供一个公有数据属性：

template
这是作为构造器的 template 参数被传入的对象。 一般来说，你不应该修改它，但并不强制要求只读访问。
'''

from string import Template
# s = Template('$who likes $what')
s = Template('${who} likes ${what}')
print(s.substitute(who='tim', what='kung pao'))
# 'tim likes kung pao'
d = dict(who='tim')
c = {"who":"tim","what":"300"}
# print(Template('Give $who $100').substitute(d)) #必须提供两个才可以替换成功,所以会异常

# Traceback (most recent call last):
...
# ValueError: Invalid placeholder in string: line 1, col 11
print(Template('Give $who $what').substitute(c))
print(Template('Give $who').substitute(d))
# Template('$who likes $what').substitute(d)
# Traceback (most recent call last):
# KeyError: 'what'
print(Template('$who likes $what').safe_substitute(d))
c = {"who":"tim","what":"300","When":"1998"}
print(Template('$who likes $what').safe_substitute(c))
# 'tim likes $what'