# 👨🏻‍💻 사용 사례: 경쟁 분석

## 🏛 아키텍처

![Architecture](image/image3.png)

## 사용 사례 설명

ABC Robots는 시장 조사 및 경쟁사 분석을 자동화하기 위해 AI 기반 경쟁 인텔리전스 시스템을 구현할 계획입니다. 이 시스템은 영업 팀이 경쟁사 대비 제품을 신속하게 식별하고 포지셔닝하는 데 도움을 주어, 수동 리서치의 비효율성과 오래된 인사이트 문제를 극복합니다. 목표는 다음을 통해 경쟁 분석 및 시장 조사를 지원하는 AI 기반 시스템을 구축하는 것입니다:

- 회사의 제품 카탈로그에서 제품 추출
- 각 제품의 주요 기능 식별 및 추출
- 주요 속성을 기반으로 경쟁사 제품 검색
- 가격, 기능 및 차별화 요소가 포함된 구조화된 경쟁 비교 표 생성

이러한 작업을 자동화함으로써 회사는 영업 프로세스를 가속화하고, 데이터 정확성을 개선하며, 영업 팀이 더 빠르게 정보에 입각한 의사결정을 내릴 수 있도록 지원합니다.

## 사전 요구사항

### 참가자:

- 이 실습에 적합한 TechZone 환경에 대한 액세스 권한이 있는지 확인하세요.
- API 키 생성 및 프로젝트 설정 단계는 환경 설정 가이드를 완료하세요.
- 강사가 MCP 서버에 연결할 URL을 제공했는지 확인하세요.
- 강사가 지식으로 로드할 `Vaccum_cleaners_v2.docx` 파일을 제공했는지 확인하세요.
- 강사가 웹사이트에 채팅을 임베드할 `abc-robots-website-final.zip` 파일을 제공했는지 확인하세요.
- 강사가 필요한 모든 자격 증명을 제공했는지 확인하세요.

## 실습 단계 개요

1. watsonx Orchestrate에 연결
2. Identifier Agent 생성 - MCP Tool `extract_from_image` 사용
3. Comparison Analysis Agent 생성 - MCP Tool `search_and_review_high_rated_products` 사용
4. ABC Robots Agent 생성 - RAG 에이전트
5. Master Agent 생성 - 오케스트레이터 에이전트

시작하겠습니다.

## 실습 지침

### 할당된 Watsonx Orchestrate 인스턴스에 연결

1. IBM Cloud(cloud.ibm.com)에 로그인합니다.
2. 왼쪽 상단의 햄버거 메뉴로 이동한 다음 **Resource List**로 이동합니다.
3. **AI/Machine Learning** 섹션을 엽니다.
4. **watsonx Orchestrate** 서비스가 표시됩니다. 클릭하여 엽니다.

![Hands-on Step 1](image/handson1.png)

5. **Launch watsonx Orchestrate** 버튼을 클릭합니다.

![Hands-on Step 2](image/handson2.png)

## Identifier Agent 생성

Identifier Agent는 이미지에서 제품을 인식합니다. 이 에이전트는 이미지 인식을 위해 watsonx.ai에서 호스팅되는 멀티모달 모델을 호출하는 MCP 서버에 사전 배포된 서비스를 사용합니다. 이 서비스를 watsonx Orchestrate 에이전트에 통합해 보겠습니다.

> **팁**
> 
> MCP 서버는 Model Context Protocol(MCP)의 구현을 실시간으로 배포한 것으로, 외부 도구, 데이터 및 서비스에 안전하고 일관되게 표준화된 액세스를 제공합니다.

1. watsonx Orchestrate 홈 페이지로 이동하여 햄버거 메뉴(☰)를 클릭하고 **Build**를 선택한 다음 **Agent Builder**를 선택합니다.

2. **Create agent** 버튼을 클릭합니다.

   ![Hands-on Step 3](image/handson3.png)

3. **Create from scratch**를 선택하고 다음 정보를 추가합니다:

   **Name:**
   ```
   Identifier Agent
   ```

   **Description:**
   ```
   This agent will extract the brand name and product name from the image.
   ```

4. **Create** 버튼을 클릭합니다.

   ![Hands-on Step 4](image/handson4.png)

5. **Toolset** 섹션으로 이동하여 **Add tool**을 클릭합니다.

   ![Hands-on Step 5](image/handson5.png)

6. **Add from file or MCP server**를 선택합니다.

   ![Hands-on Step 6](image/handson6.png)

7. **Add tools and manage MCP servers** 창에서 **Add MCP server**를 클릭합니다.

   ![Hands-on Step 7](image/handson7.png)

   **Remote MCP server**를 클릭하고 **Next**를 클릭합니다.

   ![Hands-on Step 8](image/handson8.png)

8. **Add MCP server** 창에서 다음 매개변수를 추가한 다음 **Connect**를 클릭합니다:

   **Server Name:**
   ```
   mcp-competitive-tools-<본인이름>
   ```
   예시: `mcp-competitive-tools-jiyon`

   **MCP Server URL:**
   강사로부터 받은 MCP Server URL을 입력합니다.
   
   예시:
   ```
   https://remote-mcp-tools.29gh2180kcpr.us-south.codeengine.appdomain.cloud/sse
   ```

   **Transport Type:**
   **Server-Sent Events**를 선택합니다.

   모든 정보를 입력한 후 **Connect** 버튼을 클릭합니다.

   ![Hands-on Step 9](image/handson9.png)

9. **Add tools and manage MCP servers** 창에서 **extract_from_image**를 체크하고 **Add to agent**를 클릭합니다.

   ![Hands-on Step 10](image/handson10.png)

10. 그러면 **Tools**에 추가된 것을 다음 화면과 같이 볼 수 있습니다.

    ![Hands-on Step 11](image/handson11.png)