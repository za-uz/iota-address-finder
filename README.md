# IOTA Address Finder
Python Command Line Tool for recovering your IOTA balance after a snapshot

## Usage

```bash
python address_finder.py -a <adapter> -s <seed> -n <number> [options]
```
### Options
```bash
-a, --adapter <adapter>  URI or IP + port of the public node to use
                         e.g. https://nodes.thetangle.org:443
-b, --balances           include address balances, ignored if there is no -l
-c, --checksums          include address checksums, ignored if there is no -l
-i, --indices            include address indices, ignored if there is no -l
-l, --list-addresses     list addresses
-n, --number <number>    number of addresses that (you think) have been used
-s, --seed <seed>        your seed          
-t, --trim               generate a new seed that you can use instead of your old one
```



### Examples

```bash
$ python address_finder.py -a https://nodes.thetangle.org:443 -s MY9SEED9HERE -n 15
Fetching 15 addresses...
Fetched addresses.
Fetching balances...
Fetched balances.
Your total balance in Iotas: 228
```

Since no additional options are given, only the total balance (= sum of the first `-n` addresses of the seed) is displayed.

---

```bash
$ python address_finder.py -a https://nodes.thetangle.org:443 -s MY9SEED9HERE -n 15 -l
Fetching 15 addresses...
Fetched addresses.
Fetching balances...
Fetched balances.
GGFMBLVIMAGEFOVROGBSNFWMQXPTVOPROWJWHCMAWEFPPFMK99TEOHNOXKSSPMUESHJGEEBHIYADABMZ9
HQV9GGUDVG9KKDSRICTIVXPUFR9ZLHMZXFETBLNBTHAKIVFSKBBUJYCDZPOOKTNMRWRVXIMTSHLGCPGOC
BQDSGICAGVWMNQAYSCNHZAMJY9WUDNSVQGZVF9NXFIFAREHHXDMKW9VZYOMSTQJMLOHOMRDQCTTTIGEZY
BFLWKFA9OOEYPKXNRAUA9MNBOREOQH9YSSNHENWUIUXOCDIOVXXRPY9DXXGTNWJSQJTEIDRESWSZYHLRW
FTMCWDTDERAVRUJCRWKUSDSIKREUPNDJXUGQHUZPZTCLQ9CHSWWEONKRBBDXGFTMTZVGZPGEXAILJDBMC
AF99XSEZJSMAIAQMFULPXSUZGVEBNUMMYP9TGQDBFTHPMCKHRXBTOWJGPWAZUWETSRYWTGSDNYTGXANOA
CTKZSZBZXAENNJZZKEFZXMJVJHNVRGIGKMRNLGSAEEOYVVJFMPZSX9OOJYTRMTZAQQEGDFOHGIABJAND9
KBTJFDD9NECPRTIKFIIULWZAWALJCOR9SEUJDPPINTECHAOFWPHANWYERULJWPJQCKCXZQDJFDHEPNBFW
MPVIUVXHCPYZZSRQXYELIZCVJLBIKUJLJLWRVXFHTCTDHLCLRRZZAHYSSIXPWBVIBQISJOFYNZUBWXKPX
ZFWBFJNHGCNWRTPODNQAWEC9SFUQLDBDFDHRXVYDLZYBZBFMWCYBZEIXKCFNKIEZM9PXZDCPK9JNAWOJX
IFY9MKLFTHPMQHWJHXRTQSRSIDXRLOFFEFQHWUIAUBWZJBBPJDTRKGPEQSAASPSFRXWUYGPIAMVUFFKZB
HD9JMRBOUZ9XVPCEG9THYOQITXRNAAGQEPGCBETXKFVNFDOPU9CXSQDPBKFWYEIYQRTGJSSRRSQRMRQLW
GCCXMLZOZDBRRDARWFFTHDWEROICMSOXLKYLZPNRSNIZMGRGDGODENMAZACYCJSTCMPHLESYLU9TTYIJ9
MROFDONLBXTRRKDEX9PJ9KKMZOJBCDRMXGJCYTAYQAXRSILYSGQUC9USUAJYWKFPQMYQQDAOCIGDQDUYC
VGMTEKQVPRATXMJPYTIEBOIASKMIEOOJNNDLRLNTA9SYFBEVEVGTLGVOMJEIKCCCRATCWGYKRVNPU9SUD
Your total balance in Iotas: 228
```

With the `-l` option the first `-n` addresses are listed which still isn't all that useful.

---

```
$ python address_finder.py -a https://nodes.thetangle.org:443 -s MY9SEED9HERE -n 15 -lbi
Fetching 15 addresses...
Fetched addresses.
Fetching balances...
Fetched balances.
[0] - GGFMBLVIMAGEFOVROGBSNFWMQXPTVOPROWJWHCMAWEFPPFMK99TEOHNOXKSSPMUESHJGEEBHIYADABMZ9 : 0
[1] - HQV9GGUDVG9KKDSRICTIVXPUFR9ZLHMZXFETBLNBTHAKIVFSKBBUJYCDZPOOKTNMRWRVXIMTSHLGCPGOC : 0
[2] - BQDSGICAGVWMNQAYSCNHZAMJY9WUDNSVQGZVF9NXFIFAREHHXDMKW9VZYOMSTQJMLOHOMRDQCTTTIGEZY : 0
[3] - BFLWKFA9OOEYPKXNRAUA9MNBOREOQH9YSSNHENWUIUXOCDIOVXXRPY9DXXGTNWJSQJTEIDRESWSZYHLRW : 0
[4] - FTMCWDTDERAVRUJCRWKUSDSIKREUPNDJXUGQHUZPZTCLQ9CHSWWEONKRBBDXGFTMTZVGZPGEXAILJDBMC : 0
[5] - AF99XSEZJSMAIAQMFULPXSUZGVEBNUMMYP9TGQDBFTHPMCKHRXBTOWJGPWAZUWETSRYWTGSDNYTGXANOA : 0
[6] - CTKZSZBZXAENNJZZKEFZXMJVJHNVRGIGKMRNLGSAEEOYVVJFMPZSX9OOJYTRMTZAQQEGDFOHGIABJAND9 : 0
[7] - KBTJFDD9NECPRTIKFIIULWZAWALJCOR9SEUJDPPINTECHAOFWPHANWYERULJWPJQCKCXZQDJFDHEPNBFW : 0
[8] - MPVIUVXHCPYZZSRQXYELIZCVJLBIKUJLJLWRVXFHTCTDHLCLRRZZAHYSSIXPWBVIBQISJOFYNZUBWXKPX : 0
[9] - ZFWBFJNHGCNWRTPODNQAWEC9SFUQLDBDFDHRXVYDLZYBZBFMWCYBZEIXKCFNKIEZM9PXZDCPK9JNAWOJX : 14
[10] - IFY9MKLFTHPMQHWJHXRTQSRSIDXRLOFFEFQHWUIAUBWZJBBPJDTRKGPEQSAASPSFRXWUYGPIAMVUFFKZB : 214
[11] - HD9JMRBOUZ9XVPCEG9THYOQITXRNAAGQEPGCBETXKFVNFDOPU9CXSQDPBKFWYEIYQRTGJSSRRSQRMRQLW : 0
[12] - GCCXMLZOZDBRRDARWFFTHDWEROICMSOXLKYLZPNRSNIZMGRGDGODENMAZACYCJSTCMPHLESYLU9TTYIJ9 : 0
[13] - MROFDONLBXTRRKDEX9PJ9KKMZOJBCDRMXGJCYTAYQAXRSILYSGQUC9USUAJYWKFPQMYQQDAOCIGDQDUYC : 0
[14] - VGMTEKQVPRATXMJPYTIEBOIASKMIEOOJNNDLRLNTA9SYFBEVEVGTLGVOMJEIKCCCRATCWGYKRVNPU9SUD : 0
Your total balance in Iotas: 228
```

When adding the `--balances` and `-indices` options, it starts getting interesting: Imaging a snapshot just happened and you want to know many addresses you have to generate (with the GUI-Wallet) until you see your balance again.

## Trim

When you add the `--trim` option, the program will generate a new seed that doesn't *contain* all of the empty addresses. Using a trimmed seed might result in a faster *login time* at the GUI-Wallet. Seeds can be trimmed whenever you feel you used a lot of addresses or the login is very slow, not just after a snapshot.

When using it after a snapshot you need to generate fewer addresses with the GUI-Wallet than if you didn't trim it.

```bash
$ python address_finder.py -a http://localhost:14265 -s MY9SEED9HERE -n 15 -lbit
Fetching 15 addresses...
Fetched addresses.
Fetching balances...
Fetched balances.
[0] - GGFMBLVIMAGEFOVROGBSNFWMQXPTVOPROWJWHCMAWEFPPFMK99TEOHNOXKSSPMUESHJGEEBHIYADABMZ9 : 0
[1] - HQV9GGUDVG9KKDSRICTIVXPUFR9ZLHMZXFETBLNBTHAKIVFSKBBUJYCDZPOOKTNMRWRVXIMTSHLGCPGOC : 0
[2] - BQDSGICAGVWMNQAYSCNHZAMJY9WUDNSVQGZVF9NXFIFAREHHXDMKW9VZYOMSTQJMLOHOMRDQCTTTIGEZY : 0
[3] - BFLWKFA9OOEYPKXNRAUA9MNBOREOQH9YSSNHENWUIUXOCDIOVXXRPY9DXXGTNWJSQJTEIDRESWSZYHLRW : 0
[4] - FTMCWDTDERAVRUJCRWKUSDSIKREUPNDJXUGQHUZPZTCLQ9CHSWWEONKRBBDXGFTMTZVGZPGEXAILJDBMC : 0
[5] - AF99XSEZJSMAIAQMFULPXSUZGVEBNUMMYP9TGQDBFTHPMCKHRXBTOWJGPWAZUWETSRYWTGSDNYTGXANOA : 0
[6] - CTKZSZBZXAENNJZZKEFZXMJVJHNVRGIGKMRNLGSAEEOYVVJFMPZSX9OOJYTRMTZAQQEGDFOHGIABJAND9 : 0
[7] - KBTJFDD9NECPRTIKFIIULWZAWALJCOR9SEUJDPPINTECHAOFWPHANWYERULJWPJQCKCXZQDJFDHEPNBFW : 0
[8] - MPVIUVXHCPYZZSRQXYELIZCVJLBIKUJLJLWRVXFHTCTDHLCLRRZZAHYSSIXPWBVIBQISJOFYNZUBWXKPX : 0
[9] - ZFWBFJNHGCNWRTPODNQAWEC9SFUQLDBDFDHRXVYDLZYBZBFMWCYBZEIXKCFNKIEZM9PXZDCPK9JNAWOJX : 14
[10] - IFY9MKLFTHPMQHWJHXRTQSRSIDXRLOFFEFQHWUIAUBWZJBBPJDTRKGPEQSAASPSFRXWUYGPIAMVUFFKZB : 214
[11] - HD9JMRBOUZ9XVPCEG9THYOQITXRNAAGQEPGCBETXKFVNFDOPU9CXSQDPBKFWYEIYQRTGJSSRRSQRMRQLW : 0
[12] - GCCXMLZOZDBRRDARWFFTHDWEROICMSOXLKYLZPNRSNIZMGRGDGODENMAZACYCJSTCMPHLESYLU9TTYIJ9 : 0
[13] - MROFDONLBXTRRKDEX9PJ9KKMZOJBCDRMXGJCYTAYQAXRSILYSGQUC9USUAJYWKFPQMYQQDAOCIGDQDUYC : 0
[14] - VGMTEKQVPRATXMJPYTIEBOIASKMIEOOJNNDLRLNTA9SYFBEVEVGTLGVOMJEIKCCCRATCWGYKRVNPU9SUD : 0
Your total balance in Iotas: 228
Your new trimmed seed: VZ9SEED9HERE
```

```bash
python address_finder.py -a http://localhost:14265 -s VZ9SEED9HERE -n 15 -lbi
Fetching 15 addresses...
Fetched addresses.
Fetching balances...
Fetched balances.
[0] - ZFWBFJNHGCNWRTPODNQAWEC9SFUQLDBDFDHRXVYDLZYBZBFMWCYBZEIXKCFNKIEZM9PXZDCPK9JNAWOJX : 14
[1] - IFY9MKLFTHPMQHWJHXRTQSRSIDXRLOFFEFQHWUIAUBWZJBBPJDTRKGPEQSAASPSFRXWUYGPIAMVUFFKZB : 214
[2] - HD9JMRBOUZ9XVPCEG9THYOQITXRNAAGQEPGCBETXKFVNFDOPU9CXSQDPBKFWYEIYQRTGJSSRRSQRMRQLW : 0
[3] - GCCXMLZOZDBRRDARWFFTHDWEROICMSOXLKYLZPNRSNIZMGRGDGODENMAZACYCJSTCMPHLESYLU9TTYIJ9 : 0
[4] - MROFDONLBXTRRKDEX9PJ9KKMZOJBCDRMXGJCYTAYQAXRSILYSGQUC9USUAJYWKFPQMYQQDAOCIGDQDUYC : 0
[5] - VGMTEKQVPRATXMJPYTIEBOIASKMIEOOJNNDLRLNTA9SYFBEVEVGTLGVOMJEIKCCCRATCWGYKRVNPU9SUD : 0
[6] - IUPIPHYKVOKOOVZLCKFTWLNXKDPDLBYMIHFCQ9WFZFEVTIZWVO9XISFZQTVGZAJGIMNRJHXMP9YGRGMLC : 0
[7] - LZZK9DWUBASVHSHHLVTWPRA9QZWPPCWYTBXFKBFVQALKGOQXCKGWZLFKO9OILICQQJBIIITWZRCMWZ9ZC : 0
[8] - GRGYEPTBNRCNTZLFGQTAIGODRVNZQLCPHPE9MCRMIPKHJTWEVXMPCZXOBAOMQJQYZBDTYPUTOLQRWGWKB : 0
[9] - ULJVFYM9GYFHQJQBNQGEYMRIPOKVGJVWBFVMBBMCXTSNFXMJDLPFGTTZVRYWZCSOQHUSZBFTFESUREB9A : 0
[10] - TEWHJR9BNELBCRRDVUSJFJAOVKPTRASGQMXRQJHJEPMFVIY9VWJNZENTNKJWZHPGDOVCXVPKGR9UHSYIB : 0
[11] - ZPPJTTWQBBRAPAISMNBRMODHDIAFJKPXNUDXAVFRAAKZOVTPRRWWTTZEVSFOR9B9NWDQBUTUCJGYMNFBD : 0
[12] - QFKJJAHNVNXPMFJOP9XJPXNMROSRY9LIGIBXIQESMBJDXBEHIORZFDZWJTTOCNEIFZUTKX9STSLGKYXJY : 0
[13] - ZGODTFBTYHOPFWXTINDYDKOYYKPZVCBXZMCGNFJLKZNHWQZUVBFUWKURHP9ZCQDDGKQPFWPJTTB9FZRHD : 0
[14] - ZFTPJWEPKQFPIIJHNDIVQOFRBGPDCAUQKEYVFTFONIAFCPSTVSTHL9FEZJUIHXLM9HSGLOXZXWQLIEEJC : 0
Your total balance in Iotas: 228
```
