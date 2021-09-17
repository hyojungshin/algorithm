### 10930
### SHA-256

# SHA-256 : SHA(Secure Hash Algorithm, 안전한 해시 알고리즘) 
# 데이터 입력 -> SHA 변환 -> 인덱스 생성 
# 같은 데이터 입력 시 항상 동일한 인덱스 반환됨, 인덱스 검색이라 속도 빠름
# 원래의 데이터를 복호화 하고 하나의 해시값으로 기억하므로 보안에 주로 사용

import hashlib

data = input()
encoded_data = data.encode()
result = hashlib.sha256(encoded_data).hexdigest()
print(result)
