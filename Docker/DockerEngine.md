## 도커 엔진
* 클라이언트와 서버 아키텍쳐를 따르는 애플리케이션이며 호스트 시스템에 설치되어 기본적으로 3가지 구성요소를 가진다
    * Server: Dockered라는 Docker Daemon을 통해 도커 Image를 만들고 관리할 수 있다
    * REST API: Docker Daemon에게 무슨 작업을 할지 지시하는 용도이다
    * CLI: 도커 명령어를 입력하는데 사용되는 입력 글라이언트이다