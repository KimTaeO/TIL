## CI/CD란?

* CI/CD는 Continuous Integration(지속적 통합)/ Continuous Delivery(지속적 전달)의 줄임말이다.

* 애플리케이션 개발단계를 자동화하여 애플리케이션을 보다 짧은 주기로 고객에게 제공하는 방법이다.

* 통상적으로, CI/CD는 새로 개발한 기능 버그 수정점 등을 실제 배포 중인 서비스에 통합하기 위해서는 여러 과정이 필요하다. 소스코드를 테스트하고, 빌드하고, 컨테이너화하여 통합적인 저장소에 전달 후 서비스 무중단 배포 등의 과정이 그것이다

* CI는 테스트, 빌드, Dockerizing, 저장소에 전달까지 프로덕션 환경으로 서비스를 배포 할 수 있도록 준비하는 프로세스를 말한다

* CD는 저장소로 전달된 프로덕션 서비스를 실제 사용자들에게 배포하는 프로세스를 의미한다

## Github Actions란?

* github에서 공식적으로 제공하는 CI/CD툴(개발 워크 플로우 자동화 툴)이다

### Github Actions로 할 수 있는 일

* npm에 패키지를 배포, Docker Hub에 이미지를 배포, AWS에 서비스를 배포, GCP에 서비스를 배포하는 작업 등을 Github에서 바로 할 수 있다

* 브랜치별로 어떤 Action을 실행 할 지 설정할 수 있어 각 개발 팀에 최적화 된 workflow를 만들어 낼 수 있다

### Github Actions의 개념

* Workflow : 자동화된 전체 프로세스를 나타낸 순서도 Github에게 YAML파일로 정의한 자동화 동작을 전달하면, Github Actions는 해당 파일을 기반으로 그대로 실행시킨다

* Job 그룹의 역할로, 단일 가상 환경을 제공한다

* Step Job 안에서 순차적으로 실행되는 프로세스 단위로, 파일 시스템을 통해 서로 정보를 공유, 교환  할수 있다. step에서 명령 내리거나, action을 실행 할 수 있다

* Action 타인들 또는 작성자에 의해서 미리 정의된 호출 매커니즘을 불러와 사용 할 수 있다. 사용자가 직접 커스터마이징하거나. 어떤 사람이 정의한 action을 불러와 사용할 수 있다. Github Marketplace에서 공유되고, marketplace에 공유된 action은 yaml 파일에서 곧바로 사용할 수 있다

* Event workflow 실행 기준으로, cron과 같이 시간에 따라 작업을 실행하게 할 수도, git push/pull~request 등의 Github Repository 이벤트를 기준으로 실행하게 할 수도 있다