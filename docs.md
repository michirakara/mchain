# EBNFもどき
```bnf
<code> ::= {<line>;}
<line> ::= <rhs> = <expression>
<rhs> ::= ("_"|"a"|...|"z"|"A"|...|"Z")* | _
<expression> ::= <init>{"~"<chain>}
<init> ::= <func_name>"<"{<expression>","}">"
<chain> ::= <func_name>"("{<expression>","}")"
```

# \<chain>のところのやつ一覧
## add(to_add)
元の値にto_addを足したものを返す
## sub(to_sub)
元の値にto_subを引いたものを返す
## mult(to_mult)
元の値にto_multを掛けたものを返す
## div(to_div)
元の値にto_divを割ったものを返す
## pow(to_pow)
元の値にto_powを累乗したものを返す
## print()
元の値を標準出力に表示して元の値をそのまま返す
## println()
元の値を標準出力に表示したあとに改行し、元の値をそのまま返す
## parseInt()
文字列の値を整数に変換して返す
## parseFloat()
文字列の値を浮動小数点数に変換して返す
## map(func)
元の配列のそれぞれの要素iをfunc(i)に置き換えた配列を返す
## at(idx)
配列のidx番目の要素を返す
## reduce(start_val, func)
なんかこう、想像通りな感じのやつ
## eq(rhs)
rhsが等しいか判定する
## gt(rhs)
元の値がrhsより大きいか判定
## lt(rhs)
元の値がrhsより小さいか判定
## geq(rhs)
元の値がrhs以上か判定
## leq(rhs)
元の値がrhs以下か判定
## flip()
真偽値を反転
