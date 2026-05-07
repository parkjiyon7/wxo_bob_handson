# 🤖 IBM Bob & watsonx Orchestrate Hands-on Labs

IBM Bob AI 코딩 어시스턴트와 watsonx Orchestrate를 활용한 실습 자료 모음입니다.

> **⚠️ 중요**: 모든 실습은 **IBM watsonx SaaS** 환경을 기준으로 작성되었습니다.

## 📚 실습 자료 구성

### 💻 Bob Hands-on Labs

#### 1. Competitive Analysis Deploy
Bob을 사용하여 AI 에이전트를 프로덕션 웹사이트에 배포하는 실습

- **위치**: `bob_handson/competitve_Analysis_deploy/`
- **주요 내용**:
  - watsonx Orchestrate 에이전트 통합
  - Bob을 활용한 자동 코드 생성
  - 웹사이트에 AI 기능 임베딩
  - 실시간 제품 비교 분석
- **원본 출처**: [IBM Agentic AI Client Bootcamp](https://github.ibm.com/skol/agentic-ai-client-bootcamp/blob/main/usecases/add-ons/bob-orchestrate/bob-lab-instructions.md)

#### 2. Lab 1: Basic Operations
Bob의 기본 작업 실습

- **위치**: `bob_handson/labs/`
- **주요 내용**:
  - 파일 탐색 및 읽기
  - 코드 검색 및 발견
  - 리터럴 코딩
  - Bob Findings

#### 3. Lab 2: Advanced Workflows
복잡한 워크플로우 및 고급 기능 실습

- **위치**: `bob_handson/labs/`
- **주요 내용**:
  - 다중 파일 리팩토링
  - 기능 구현
  - 디버깅 및 문제 해결
  - 코드 품질 개선

### 🔄 watsonx Orchestrate Hands-on

#### 1. Getting Started with ADK
watsonx Orchestrate ADK 설치 및 첫 번째 에이전트 생성

- **위치**: `wxo_handson/getting-started-adk/`
- **주요 내용**:
  - ADK 설치 및 설정
  - Hello World 에이전트 생성
  - 에이전트 배포
  - 테스트 및 검증

#### 2. Agentic Competitive Insights
이미지 인식, MCP, RAG를 활용한 AI 기반 경쟁 인텔리전스 시스템

- **위치**: `wxo_handson/Agentic_Competitive_Insights/`
- **주요 내용**:
  - 이미지 인식으로 제품 정보 추출
  - MCP를 통한 모델 통신
  - RAG 기반 경쟁사 분석
  - 멀티 에이전트 오케스트레이션
  - 자동화된 SWOT 분석

## 🌐 GitHub Pages 웹사이트

실습 자료는 GitHub Pages를 통해 웹사이트로 제공됩니다:

**URL**: https://parkjiyon7.github.io/wxo_bob_handson/


## 📁 프로젝트 구조

```
git_jiyon_wxobob_handson/
├── README.md                          # 이 파일
├── Today_info.md                      # 실습 당일 정보 (강사가 업데이트)
├── .gitignore                         # Git 제외 파일 설정
│
├── bob_handson/                       # Bob 실습 자료
│   ├── competitve_Analysis_deploy/    # AI 에이전트 배포 실습
│   │   ├── handson_lab.md            # 실습 가이드
│   │   ├── competitive_Analysis_deploy.md  # 개요 문서
│   │   ├── image/                    # 스크린샷 (image1-13.png)
│   │   └── asset/                    # 다운로드 파일
│   │       └── abc-robots-website-final_v2.zip
│   └── labs/                         # Lab 1, 2 실습 자료
│       ├── lab1_basic_operations_ko.md
│       ├── lab1_basic_operations.md
│       ├── lab2_advanced_workflows_ko.md
│       ├── lab2_advanced_workflows.md
│       └── sample-project/           # 샘플 프로젝트
│
├── wxo_handson/                      # watsonx Orchestrate 실습 자료
│   ├── getting-started-adk/          # ADK 튜토리얼
│   │   ├── wxO_ADK_tutorial.md
│   │   ├── image/                    # 스크린샷
│   │   └── agents/                   # 샘플 에이전트
│   └── Agentic_Competitive_Insights/ # 경쟁 인텔리전스 실습
│       ├── Agentic_Competitive_Insights.md  # 개요
│       ├── handson_guide.md          # 실습 가이드
│       ├── image/                    # 스크린샷 (51개)
│       ├── Vaccum_cleaners_v2.docx   # 샘플 데이터
│       └── abc-robots-website-final.zip
│
└── docs/                             # GitHub Pages 웹사이트
    ├── index.html                    # 메인 페이지
    ├── bob-competitive-deploy.html   # Bob 배포 실습
    ├── bob-lab1-ko.html / bob-lab1-en.html
    ├── bob-lab2-ko.html / bob-lab2-en.html
    ├── wxo-adk-tutorial.html         # ADK 튜토리얼
    ├── wxo-competitive-insights.html # 경쟁 인텔리전스
    ├── wxo-competitive-insights-guide.html
    ├── css/style.css                 # 스타일시트
    ├── js/main.js                    # JavaScript
    └── content/                      # 마크다운 콘텐츠
        ├── bob-labs/                 # Bob 실습 마크다운
        ├── wxo/                      # ADK 튜토리얼 마크다운
        └── wxo-labs/                 # 경쟁 인텔리전스 마크다운
```

## 🚀 시작하기

### 사전 요구사항

- IBM Bob IDE 설치
- IBM Cloud 계정
- watsonx Orchestrate 인스턴스 액세스
- API Keys (강사 제공)

### 실습 순서 (권장)

1. **Bob Lab 1**: Basic Operations - Bob 기본 기능 익히기
2. **Bob Lab 2**: Advanced Workflows - 고급 기능 실습
3. **Agentic Competitive Insights**: 종합 프로젝트
4. **Competitive Analysis Deploy**: AI 에이전트 배포 실습
5. **watsonx Orchestrate ADK**: 에이전트 개발 기초


## 📝 Today Info 업데이트 방법

강사는 `Today_info.md` 파일을 수정하여 실습 당일 정보를 업데이트할 수 있습니다:

```markdown


## 📄 라이선스

© 2024 IBM. All rights reserved.  
Created for hands-on training purposes.

## 👥 문의

실습 중 문제가 발생하면 강사에게 문의하거나 Bob에게 도움을 요청하세요.

---

**Made with ❤️ by IBM**