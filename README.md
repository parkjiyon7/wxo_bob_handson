# wxo_bob_handson
wxo x Bob handson asset

## IBM watsonx Orchestrate Agent Development Kit (ADK) 튜토리얼

IBM watsonx Orchestrate는 에이전트를 구축, 테스트 및 관리하기 위한 개발자 중심 도구 세트인 Agent Development Kit (ADK)를 포함하고 있습니다. ADK를 사용하면 개발자는 경량 프레임워크와 간단한 CLI를 사용하여 강력한 에이전트를 설계할 수 있는 자유와 제어권을 얻을 수 있습니다. 명확한 YAML 또는 JSON 파일로 에이전트를 정의하고, 사용자 정의 Python 도구를 생성하며, 몇 가지 명령만으로 전체 에이전트 라이프사이클을 관리할 수 있습니다.

이 튜토리얼에서는 ADK를 설치하고, 로컬 개발 환경을 설정하며, watsonx Orchestrate SaaS 인스턴스에 첫 번째 에이전트를 배포하는 단계별 가이드를 따라갑니다. 이를 통해 유연하고 재사용 가능한 AI 에이전트를 바로 구축할 수 있습니다.

## watsonx Orchestrate Agent Development Kit (ADK) 환경 설정

## Python 설치

ADK를 설치하기 전에 호환되는 Python 버전(3.11~3.13)이 컴퓨터에 설치되어 있는지 확인하세요.

터미널 창을 열고 다음 명령을 실행하여 현재 Python 버전을 확인하세요:

```bash
python --version
```

버전이 3.11-3.13 범위를 벗어나는 경우 호환되는 버전을 설치해야 합니다. [공식 Python 웹사이트](https://www.python.org/downloads/)에서 특정 릴리스를 다운로드하거나, macOS 또는 Linux를 사용하는 경우 `pyenv`와 같은 버전 관리자를 사용하여 여러 Python 버전을 관리하고 필요한 버전을 설치할 수 있습니다.

Python을 설치한 후 Python의 패키지 설치 프로그램인 pip도 설치되어 있는지 확인하세요. 터미널에서 다음 명령을 실행하세요:

```bash
pip --version
```
