# EBNFもどき
```bnf
<code> ::= {<line>;[//{? all visible characters ?}"\n"]}
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
funcの引数は1つ
## at(idx)
配列のidx番目の要素を返す
## reduce(start_val, func)
なんかこう、想像通りな感じのやつ  
funcの引数は2つ
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
## iota(begin, step)
配列のi番目をbegin+i*stepで埋める
## ifElse(condition, iftrue, iffalse)
conditionが真ならiftrue(元の値)、偽ならiffalse(元の値)を返す
## set(idx, value)
元の配列のidx番目をvalueに変えた配列を返す
## subSeq(start,end)
文字列または配列LのL[start,end)を返します
## and(rhs)
intまたはboolのandをする
## or(rhs)
intまたはboolのorをする
## xor(rhs)
intまたはboolのxorをする

# \<init>のところのやつ一覧
## nextIn<>
スペース改行区切りで標準入力の次の文字列を返す
## newList<size, value>
valueで初期化された長さsizeのリストを返す
## FUNC<arg1, arg2, ... , func>
ラムダ式。arg1, arg2, ... を引数としてfuncを実行する関数を返す
## それ以外
文字列、int、floatの定数が使えます