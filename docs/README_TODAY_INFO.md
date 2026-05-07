# Today_info.md 사용 방법

## 🔒 보안 주의사항

`Today_info.md` 파일에는 API key와 같은 민감한 정보가 포함되어 있어 GitHub 저장소에 커밋되지 않습니다.

## 📝 로컬에서 사용하기

1. 템플릿 파일을 복사합니다:
   ```bash
   cp docs/Today_info.template.md docs/Today_info.md
   ```

2. `docs/Today_info.md` 파일을 열고 실제 값으로 교체합니다:
   - `YOUR_INSTANCE_URL_HERE` → 실제 Instance URL
   - `YOUR_API_KEY_HERE` → 실제 API Key
   - `YOUR_MCP_SERVER_URL_HERE` → 실제 MCP Server URL

3. 파일은 `.gitignore`에 포함되어 있어 Git에 커밋되지 않습니다.

## 🌐 GitHub Pages에 배포하기

GitHub Pages에서 실습 정보를 보여주려면:

1. 로컬에서 `docs/Today_info.md` 파일을 생성합니다 (위 단계 참조)
2. GitHub Pages는 로컬 파일을 직접 사용하지 않으므로, 다음 중 하나를 선택:

### 옵션 A: 수동으로 HTML에 포함
HTML 파일에 직접 정보를 하드코딩합니다.

### 옵션 B: JavaScript로 동적 로드
별도의 안전한 서버에서 정보를 가져와 표시합니다.

### 옵션 C: GitHub Actions 사용 (권장)
GitHub Secrets에 민감한 정보를 저장하고, Actions를 통해 배포 시 자동으로 삽입합니다.

## ⚠️ 중요
- `Today_info.md` 파일은 절대 Git에 커밋하지 마세요
- API key가 노출되면 즉시 재발급하세요