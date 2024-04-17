# mchain
構文解析ゴリラへの道
# Docs
[Documentation](docs.md)
# Usage
```sh
python main.py [path_to_file]
```
# Example
Solution for [ABC348-B](https://atcoder.jp/contests/abc348/tasks/abc348_b)  
[examples/abc348-b.mcn](examples/abc348-b.mcn)
```:example.mc
N = nextIn~parseInt();
XY = newList<N, newList<2, 0>> ~map(FUNC<i, i ~map(FUNC<j, nextIn ~parseInt()>)>);
// _ = XY ~println();
_ = newList<N,0> 
    ~iota(0, 1)
    ~map(FUNC<
        i,
        newList<N,0> 
            ~iota(N ~sub(1), -1) 
            ~reduce(
                newList<2,0>, // [idx, maValue]
                FUNC<
                    a, b, 
                    a ~ifElse(
                        a ~at(1) ~gt(XY ~at(i) ~at(0) ~sub(XY ~at(b) ~at(0)) ~pow(2) ~add(XY~at(i)~at(1) ~ sub(XY ~at(b) ~at(1)) ~pow(2))),
                        FUNC<tmp, tmp>,
                        FUNC<tmp, newList<2,b> ~set(1,XY ~at(i) ~at(0) ~sub(XY ~at(b) ~at(0)) ~pow(2) ~add(XY~at(i)~at(1) ~ sub(XY ~at(b) ~at(1)) ~pow(2)))>,
                    )
                >
            ) ~at(0) ~add(1)
            ~println()
    >);
```
