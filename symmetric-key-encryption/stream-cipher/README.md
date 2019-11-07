# Steram cipher
## Descryition
共通鍵暗号方式の１種．  
平文をbitもしくはbyte単位で暗号化を行う方式．  
RC4を採用．
- 暗号化
秘密鍵をシードとして擬似乱数系列に入力．  
任意長の擬似乱数系列（キーストリーム）Zを生成．  
平文PとキーストリームZの排他的論理和をとることで  
暗号文Cを出力．  
P xor Z = C  
- 復号
暗号文CとキーストリームZの排他的論理和をとることで  
平文Pを出力．  
C xor Z = P xor Z xor Z = P  

## Requirements
* Python 3 version 3.5
## Usage
### Python 3
```sh
$ python3 stream.py
```
Input key and plain/cipher text.
Return key and plain/cipher text.

## Reference
M. MORII, R. TERAMURA, "ストリーム暗号の現状と課題", (https://www.jstage.jst.go.jp/article/essfr/2/3/2_3_3_66/_pdf).
