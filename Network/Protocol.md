## 프로토콜
* 원거리 통신 장비 사이에서 메시지를 주고받는 양식과 규칙의 체계이다. 즉 통신 규약 및 약속이라 할 수 있다

### 프로토콜의 기본 요소
* 구문: 전송하고자 하는 데이터의 형식, 부호화, 신호 레벨 등을 규정
* 의미: 두 기기 간의 효율적이고 정확한 정보 전송을 위한 협조 사항과 오류 관리를 위한 제어 정보를 규정
* 시간: 두 기기 간의 통신 속도, 메시지의 순서 제어 등을 규정

### 프로토콜의 기능
* 단편화와 재합성
    * 단편화: 송신 측에서는 긴 데이터 블록을 손쉽게 전송할 수 있도록 크기가 똑같은 작은 블록으로 나누어 전송
    * 재합성: 수신 측에서 나누어진 블록들을 재합성하여 원래의 메시지로 복원하는 기능

* 캡슐화: 각 프로토콜에 적합한 데이터 블록을 만들기 위해 데이터에 정보를 추가하는 것 플래그, 주소 정보, 제어 정보, 오류 검출 부호 등을 부착하는 기능

* 연결 제어: 비연결 데이터 전송과 연결 위주 데이터 전송을 위한 통신로를 개설 유지, 종결하는 기능

* 흐름 제어: 데이터 양이나 통신속도 등이 수신 측의 처리 능력을 초과하지 않도록 조정하는 기능

* 순서 결정: 연결 위주의 데이터를 전송할 때 송신 측이 보내는 데이터 단위 순서대로 수신 측에 전달하는 기능

* 주소 설정: 발생지 목적지 등의 주소를 명기하여 데이터를 명확하게 전달하는 기능

* 동기화: 두 통신 객체의 상태를 일치시키는 기능

* 다중화: 계층 여러 개의 소켓에서 전송되는 데이터를 모아 하나로 만드는 것