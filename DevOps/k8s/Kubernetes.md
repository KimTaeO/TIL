## 쿠버네티스
* 컨테이너 런타임을 이용하여 컨테이너를 다루는 도구이다

* 애플리케이션의 확장과 장애를 처리할 수 있고, 배포 패턴을 제공한다
    * 서비스 디스커버리와 로드 밸런싱
        * DNS 또는 IP를 사용하여 컨테이너를 배포할 수 있고, 트래픽을 분산시키는 로드 밸런싱을 수행할 수 있다

    * 스토리지 오케스트레이션
        * 원하는 저장소 시스템을 자동으로 탑재할 수 있다
    * 자동화된 롤아웃과 롤백
        * 컨테이너의 배포와 버전 관리를 자동으로 할 수 있다
    * 자동화된 빈 패킹
        * 컨테이너를 실행하는데 필요한 쿠버네티스 클러스터 노드를 제공한다 
        * 각 컨테이너가 필요로 하는 CPU와 RAM을 쿠버네티스에 지시하면, 쿠버네티스는 컨테이너를 노드에 맞추어 리소스를 가장 효율적으로 사용할 수 있게 해준다
    * 자동화된 복구
        * 실행에 실패한 컨테이너를 자동으로 재시작하고, 교체합니다
        * 사용자가 지정한 상태 검사에 응답하지 않는 컨테이너를 제외시킨다
        * 서비스 준비가 끝날 때 까지 클라이언트에게 이러한 과정들을 보여주지 않는다
    * 시크릿과 구성 관리
        * 쿠버네티스를 이용하면, 암호 OAuth Token, SSH키 등 민감한 정보들을 저장하고 관리할 수 있습니다
        * 컨테이너 이미지를 재구성하지 않고 스택 구성에 시크릿을 노출하지 않고도 시크릿 및 애플리케이션을 업데이트하고 배포할 수 있다


### Kubernetes Cluster
* 쿠버네티스를 배포하면 클러스터를 얻게 되는데 쿠버네티스 클러스터의 구성요소로는 다음과 같은 것들이 존재한다
    * 워커 노드(Worker Node)
        * 노드라고 하는 워커 머신들의 집합이며, 클러스터는 최소 한 개의 워커 노드를 가진다

### Control Plain Component
* kube-apiserver: 쿠버네티스 클러스터로 들어오는 요청을 가장 앞에서 받아들인다 전달받은 요청을 적절한 컴포넌트로 전달하는 역할도 한다

* etcd: 쿠버네티스 클러스터가 동작하기 위한 클러스터와 리소스의 ```구성 정보```, ```상태 정보``` 및 ```명세 정보```등을 키-값 형태로 저장하는 저장소이다 안전성을 위해 자료를 분산시켜 저장한다

* kube-scheduler: 여러 개의 노드로 이루어져 있고 기본적인 작업 단위인 Pod는 여러 노드들 중 하나에 배치되어 동작하는데 이때, 파드를 어디에 배치할 지 결정하는 것을 스케쥴링이라 하는데 이러한 작업을 담당하는 것이 kube-scheduler이다

* kube-controller-manager: 다운된 노드가 없는지, Pod가 의도한 복제 숫자를 유지하고 있는지, 서비스와 Pod가 적절히 연결되어 있는지, 네임스페이스에 대한 기본 계정과 토큰이 생성되어 있는지를 확인하고 적절하지 않다면 적절한 수준을 유지하기 위해 조치하는 역할을 한다

### Node Component
* 동작 중인 파드를 유지시키고 쿠버네티스 런타임 환경을 제공하며, 모든 노드 상에서 동작한다

* kubelet: 클러스터의 각 노드에서 실행되는 에이전트이다 Pod에서 컨테이너가 확실하게 작동하도록 관리합니다

* kube-proxy: 클러스터의 각 노드에서 실행되는 프록시이다 쿠버네티스 서비스 개념의 구현부이다 각 노드의 네트워크의 규칙을 유지 관리한다 이 네트워크 규칙이 내부 네트워크 세션이나 클러스터 바깥에서 Pod로 통신할 수 있도록 해준다

* Container Runtime: 컨테이너 실행을 담당하는 소프트웨어이다 