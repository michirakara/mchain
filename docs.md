# EBNFもどき
```bnf
<code> ::= {<line>;}
<line> ::= <rhs> = <expression>
<rhs> ::= ("_"|"a"|...|"z"|"A"|...|"Z")* | _
<expression> ::= <init>{<chain>}
<init> ::= <func_name>"<"{<expression>","}">"
<chain> ::= <func_name>"("{<expression>","}")"
```

