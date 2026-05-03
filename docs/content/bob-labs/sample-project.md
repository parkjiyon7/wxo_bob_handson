# Bob 데모 프로젝트

이 프로젝트는 Lab 1과 Lab 2에서 언급된 Bob의 기능을 실제로 체험할 수 있는 샘플 프로젝트입니다.

## 프로젝트 개요

간단한 사용자 관리 시스템으로, Bob의 다양한 기능을 테스트할 수 있도록 설계되었습니다:

- **파일 탐색 및 읽기**: 여러 모듈로 구성된 프로젝트 구조
- **코드 검색**: TODO 주석과 개선이 필요한 코드 포함
- **리팩토링**: 의도적으로 개선이 필요한 코드 패턴
- **디버깅**: 수정이 필요한 버그 포함
- **다중 파일 작업**: 모델, 컨트롤러, 테스트 파일 간 연결

## 프로젝트 구조

```
sample-project/
├── README.md                 # 이 파일
├── requirements.txt          # Python 의존성
├── config.json              # 설정 파일
├── src/
│   ├── __init__.py
│   ├── models/
│   │   ├── __init__.py
│   │   └── user.py          # User 모델 (getUserData 함수 포함)
│   ├── controllers/
│   │   ├── __init__.py
│   │   └── user_controller.py  # User 컨트롤러 (버그 포함)
│   └── utils/
│       ├── __init__.py
│       ├── validators.py    # 검증 유틸리티 (보안 이슈 포함)
│       └── analytics.py     # 분석 유틸리티 (오타 및 성능 개선 필요)
└── tests/
    ├── __init__.py
    ├── test_user.py         # User 테스트 (실패하는 테스트 포함)
    └── test_validators.py   # Validator 테스트
```

## 설치 및 실행

```bash
# 가상 환경 생성 (선택사항)
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 의존성 설치
pip install -r requirements.txt

# 테스트 실행
pytest

# 특정 테스트 파일 실행
pytest tests/test_user.py -v
```

---

## Lab 1: 기본 작업 실습 가이드

### Exercise 1: 파일 탐색 및 읽기 

**Bob에게 요청할 프롬프트**:
```
현재 디렉토리의 모든 파일을 재귀적으로 나열하고, config.json 파일을 읽어주세요.
```

**또는**:
```
src/models/user.py와 src/controllers/user_controller.py를 함께 읽고 
사용자 관리 시스템이 어떻게 작동하는지 설명해주세요.
```

**기대 결과**: 프로젝트 구조 파악 및 주요 파일 내용 이해

---

### Exercise 2: 코드 검색 및 발견 

**Bob에게 요청할 프롬프트**:
```
src 디렉토리에서 모든 TODO 주석을 검색해주세요.
```

**또는**:
```
src/utils/validators.py의 모든 함수 정의를 나열해주세요.
```

**또는**:
```
getUserData 함수를 사용하는 모든 파일을 찾아주세요.
```

**기대 결과**: 
- 6개 이상의 TODO 주석 발견
- validators.py의 4개 함수 확인
- user.py와 user_controller.py에서 getUserData 사용 확인

---

### Exercise 3: 간단한 코드 변경 

**Bob에게 요청할 프롬프트**:
```
config.json 파일에서 "debug" 값을 false에서 true로 변경해주세요.
```

**또는**:
```
src/utils/analytics.py에서 함수 이름 "calcualte_total"의 오타를 "calculate_total"로 수정해주세요.
```

**기대 결과**: 
- config.json의 debug 값이 true로 변경
- calcualte_total → calculate_total 수정

---

### Exercise 4: 명령 실행 

**Bob에게 요청할 프롬프트**:
```
pytest를 사용하여 모든 테스트를 실행해주세요.
```

**또는**:
```
tests/test_validators.py 파일의 테스트만 실행해주세요.
```

**기대 결과**: 테스트 실행 결과 확인 (일부 테스트 실패 예상)

---

### Exercise 6: 리터럴 코딩 - 코드 이해 

**Bob에게 요청할 프롬프트**:
```
src/utils/analytics.py의 calculate_statistics 함수를 읽고 다음을 설명해주세요:
1. 이 함수는 무엇을 하나요?
2. 입력과 출력은 무엇인가요?
3. 성능 문제가 있나요?
4. 어떻게 개선할 수 있나요?
```

**기대 결과**: 함수의 목적, 비효율적인 루프 사용, 개선 방안 제시

---

### Exercise 8: Bob Findings - 자동 코드 분석 

**Bob에게 요청할 프롬프트**:
```
src/controllers/user_controller.py를 보안 문제, 코드 품질 문제, 
잠재적 버그에 대해 분석하고 심각도별로 정리해주세요.
```

**또는**:
```
src/utils/validators.py의 validate_email 함수를 분석하고 
보안 취약점을 찾아주세요.
```

**기대 결과**: 
- user_controller.py: 음수 나이 검증 누락 발견
- validators.py: 간단한 정규식의 보안 문제 지적

---

## Lab 2: 고급 워크플로우 실습 가이드

### Exercise 1: 다중 파일 리팩토링 

**Bob에게 요청할 프롬프트**:
```
getUserData 함수를 get_user_data로 리팩토링해야 합니다. 
먼저 getUserData를 사용하는 모든 파일을 검색하세요. 
그런 다음 해당 파일들을 읽고, 함수 정의와 모든 호출을 업데이트하고, 
테스트를 실행하여 모든 것이 여전히 작동하는지 확인하세요.
```

**기대 결과**:
- src/models/user.py의 getUserData → get_user_data 변경
- src/controllers/user_controller.py의 getUserData() 호출 업데이트
- tests/test_user.py의 getUserData() 호출 업데이트
- 테스트 통과 확인

---

### Exercise 2: 기능 구현 

**Bob에게 요청할 프롬프트**:
```
User 모델에 "email" 필드를 추가해야 합니다. 다음을 수행하세요:
1. src/models/user.py의 User 클래스에 email 필드 추가
2. src/controllers/user_controller.py의 create_user 메서드를 이메일을 받도록 수정
3. src/utils/validators.py의 validate_email을 사용하여 검증 추가
4. tests/test_user.py에 이메일 검증 테스트 추가

이 작업을 추적하기 위한 todo 리스트를 만드세요.
```

**기대 결과**:
- User 모델에 email 필드 추가
- UserController에서 이메일 검증 및 저장
- 새로운 테스트 케이스 추가
- Todo 리스트로 진행 상황 추적

---

### Exercise 3: 디버깅 및 문제 해결 

**Bob에게 요청할 프롬프트**:
```
tests/test_user.py의 test_update_user_with_negative_age 테스트를 실행하고 
실패 원인을 분석해주세요. 그런 다음 src/controllers/user_controller.py의 
update_user 메서드를 수정하여 음수 나이를 거부하도록 해주세요.
```

**기대 결과**:
- 버그 발견: update_user에서 나이 검증 누락
- validate_age 함수를 사용하여 검증 추가
- 테스트 통과 확인

---

### Exercise 4: 코드 품질 개선 

**Bob에게 요청할 프롬프트**:
```
src/utils/analytics.py의 calculate_statistics 함수를 검토하세요. 
더 읽기 쉽고 효율적이도록 리팩토링하세요. 
docstring과 주석을 추가하고, 모든 테스트가 여전히 통과하는지 확인하세요.
```

**기대 결과**:
- 두 개의 루프를 하나로 통합
- 더 명확한 변수명 사용
- 개선된 docstring
- 테스트 통과 확인

---

## 의도적으로 포함된 문제들

이 프로젝트는 학습 목적으로 다음과 같은 문제들을 의도적으로 포함하고 있습니다:

### 🐛 버그
1. **user_controller.py**: `update_user` 메서드에서 음수 나이 검증 누락
2. **analytics.py**: `find_oldest_user`가 빈 리스트에 대해 None 반환 (예외 발생해야 함)
3. **analytics.py**: 함수 이름 오타 `calcualte_total` (calculate_total이어야 함)

### ⚠️ 코드 품질 문제
1. **user.py**: `getUserData` 함수명이 Python 네이밍 컨벤션 위반 (snake_case여야 함)
2. **analytics.py**: `calculate_statistics`에서 비효율적인 다중 루프 사용
3. **user_controller.py**: 중복 사용자명 검증 누락

### 🔒 보안 문제
1. **validators.py**: `validate_email`의 정규식이 너무 단순함
2. **validators.py**: `validate_password`에 강도 검증 로직 누락
3. **user_controller.py**: 입력 검증이 불완전함

### 📝 TODO 주석
프로젝트 전체에 6개 이상의 TODO 주석이 있어 개선이 필요한 부분을 표시합니다.

---

## Bob 모드 활용 예시

### Ask 모드
```
이 프로젝트의 아키텍처를 설명하고 개선할 수 있는 부분을 제안해주세요.
```

### Plan 모드
```
이 프로젝트에 JWT 기반 인증 시스템을 추가하는 계획을 단계별로 만들어주세요.
```

### Code 모드
```
계획의 첫 번째 단계를 구현해주세요.
```

---

## 추가 도전 과제

Bob의 고급 기능을 더 탐색하고 싶다면:

1. **데이터베이스 통합**: SQLite 데이터베이스 추가
2. **API 엔드포인트**: Flask/FastAPI로 REST API 구현
3. **로깅 시스템**: 구조화된 로깅 추가
4. **에러 처리**: 포괄적인 예외 처리 구현
5. **문서화**: 자동 문서 생성 설정

---

## 학습 목표 체크리스트

이 프로젝트를 통해 다음을 배울 수 있습니다:

- [ ] Bob의 파일 탐색 및 읽기 기능
- [ ] 코드 검색 및 패턴 매칭
- [ ] 정확한 코드 편집 (apply_diff)
- [ ] 다중 파일 리팩토링
- [ ] 디버깅 및 문제 해결
- [ ] 코드 품질 개선
- [ ] Bob Findings를 통한 자동 분석
- [ ] Todo 리스트를 통한 작업 관리
- [ ] 다양한 Bob 모드 활용 (Ask, Plan, Code)

---

## 문의 및 지원

문제가 발생하거나 질문이 있으면 Bob에게 물어보세요!

```
이 프로젝트에서 [특정 작업]을 어떻게 수행하나요?
```

Bob은 항상 도와줄 준비가 되어 있습니다! 🤖