from pathlib import Path   # pathlib：Python 处理文件路径的现代工具包

p = Path("notes.txt")                  # 指向当前目录下的 notes.txt
print("文件存在吗：", p.exists())        # exists 判断文件在不在
print("读到的内容：", p.read_text(encoding="utf-8"))  # 直接读，比 open 简短
print("绝对路径：", p.resolve())         # resolve 把相对路径变成从盘符开始的全路径
