# mchain
構文解析ゴリラへの道
# Docs
[Documentation](docs.md)
# Usage
```sh
python main.py [path_to_file]
```
# Example
Solution for [ABC349-A](https://atcoder.jp/contests/abc349/tasks/abc349_a)  
[example.mc](example.mcn)
```:example.mc
n = nextIn<> ~parseInt() ~sub(1);
_ = newList<n, 0> ~map(FUNC<i, nextIn ~parseInt()>) ~reduce(0, FUNC<i, j, i ~sub(j)>) ~println();
```