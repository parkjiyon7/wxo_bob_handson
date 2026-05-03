# IBM Bob & watsonx Orchestrate Hands-on Website

이 디렉토리는 GitHub Pages로 배포되는 웹사이트입니다.

## 🌐 배포된 사이트

GitHub Pages를 통해 다음 URL에서 접근할 수 있습니다:
- `https://parkjiyon7.github.io/wxo_bob_handson/`

## 📁 구조

```
docs/
├── index.html                  # 메인 페이지
├── bob-lab1-ko.html           # Bob Lab 1 (한국어)
├── bob-lab1-en.html           # Bob Lab 1 (English)
├── bob-lab2-ko.html           # Bob Lab 2 (한국어)
├── bob-lab2-en.html           # Bob Lab 2 (English)
├── bob-sample-project.html    # Sample Project 가이드
├── wxo-adk-tutorial.html      # watsonx Orchestrate ADK 튜토리얼
├── css/
│   └── style.css              # Duolingo 스타일 CSS
├── js/
│   └── main.js                # JavaScript 기능
└── .nojekyll                  # Jekyll 비활성화
```

## 🎨 디자인

Duolingo의 디자인 시스템을 참조하여 만들어졌습니다:
- 밝고 친근한 색상 팔레트
- 카드 기반 레이아웃
- 부드러운 애니메이션
- 반응형 디자인

### 색상 팔레트

- Primary: `#1cb0f6` (밝은 파란색)
- Primary Dark: `#1899d6`
- Success: `#58cc02` (초록색)
- Warning: `#ff9600` (주황색)
- Accent: `#ce82ff` (보라색)

## 🚀 GitHub Pages 배포 방법

### 1. Repository 설정

1. GitHub 저장소로 이동
2. Settings > Pages 메뉴 선택
3. Source: Deploy from a branch
4. Branch: `main` 선택
5. Folder: `/docs` 선택
6. Save 클릭

### 2. 배포 확인

- 몇 분 후 `https://parkjiyon7.github.io/wxo_bob_handson/`에서 사이트 확인
- Actions 탭에서 배포 진행 상황 확인 가능

## 📝 콘텐츠 업데이트

### 마크다운 파일 수정

1. `bob_handson/labs/` 또는 `wxo_handson/` 디렉토리의 마크다운 파일 수정
2. 변경사항 커밋 및 푸시
3. 웹사이트가 자동으로 업데이트됨 (marked.js가 동적으로 렌더링)

### HTML/CSS 수정

1. `docs/` 디렉토리의 파일 수정
2. 변경사항 커밋 및 푸시
3. GitHub Pages가 자동으로 재배포

## 🔧 기술 스택

- **HTML5**: 시맨틱 마크업
- **CSS3**: 커스텀 스타일 (CSS Variables 사용)
- **JavaScript (ES6+)**: 인터랙티브 기능
- **marked.js**: 마크다운을 HTML로 변환
- **GitHub Pages**: 정적 사이트 호스팅

## 📱 반응형 디자인

- 데스크톱: 1200px 최대 너비
- 태블릿: 768px 이하에서 레이아웃 조정
- 모바일: 단일 컬럼 레이아웃

## ✨ 주요 기능

1. **부드러운 스크롤**: 앵커 링크 클릭 시 부드러운 스크롤
2. **애니메이션**: 스크롤 시 카드 페이드인 효과
3. **코드 복사**: 코드 블록에 복사 버튼 자동 추가
4. **맨 위로 버튼**: 스크롤 시 자동 표시
5. **활성 네비게이션**: 현재 섹션 하이라이트

## 🐛 문제 해결

### 마크다운이 로드되지 않는 경우

1. 브라우저 콘솔에서 에러 확인
2. 파일 경로가 올바른지 확인
3. CORS 문제인 경우 로컬 서버 사용:
   ```bash
   cd docs
   python -m http.server 8000
   ```

### 이미지가 표시되지 않는 경우

1. 이미지 경로가 상대 경로로 올바르게 설정되었는지 확인
2. `wxo-adk-tutorial.html`의 이미지 경로 수정 로직 확인

## 📄 라이선스

IBM 교육 목적으로 제작되었습니다.

## 👥 기여

문제가 있거나 개선 사항이 있으면 GitHub Issues를 통해 제보해주세요.