# Bob 스킬과 watsonx Orchestrate를 사용하여 BPMN 다이어그램을 프로덕션 준비 에이전트로 전환

**사전 요구사항:** Bob 및 watsonx Orchestrate에 대한 기본 이해

> **출처**: 이 튜토리얼은 IBM Developer의 공식 튜토리얼을 기반으로 작성되었습니다.  
> 원문: https://developer.ibm.com/tutorials/bpmn-to-agents-bob-skills-watsonx-orchestrate/

## 개요

비즈니스 프로세스 다이어그램을 실제 작동하는 소프트웨어로 전환하는 작업은 일반적으로 시간, 전문 기술, 그리고 팀 간의 많은 인수인계가 필요합니다. 비즈니스 분석가는 BPMN(Business Process Model and Notation)과 같은 모델로 워크플로우를 정의합니다. 그런 다음 개발자는 이러한 모델을 코드로 변환하고, 로직을 검증하며, 의도와 구현 간의 격차를 수정하는 데 몇 주를 소비합니다.

### BPMN이란?

**BPMN(Business Process Modeling Notation)은 비즈니스 프로세스를 누구나 이해하기 쉽게 시각적으로 표현하는 글로벌 표준 그래픽 표기법입니다.**

이 튜토리얼은 더 빠르고 신뢰할 수 있는 방법을 보여줍니다. IBM Bob 스킬을 사용하여 BPMN 비즈니스 프로세스를 완전히 작동하는 watsonx Orchestrate 에이전트로 변환합니다. Bob은 프로세스 모델을 분석하고, 명확한 표준 운영 절차(SOP)를 생성하며, 해당 사양을 사용하여 에이전트, 워크플로우, 도구, 테스트 및 배포 스크립트를 구축합니다.

이 튜토리얼을 완료하면 비즈니스 사양이 실행 가능한 자동화로 직접 전환되는 방법을 확인할 수 있습니다. 또한 Bob 스킬과 watsonx Orchestrate MCP 서버가 수동 작업을 줄이고, 모범 사례를 적용하며, 개발자가 처음부터 시작하는 대신 검토 및 사용자 정의에 집중할 수 있도록 돕는 방법을 확인할 수 있습니다.




