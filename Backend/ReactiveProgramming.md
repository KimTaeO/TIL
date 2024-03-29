## 리액티브 프로그래밍
* 대규모 사용자가 접속하는 서비스는 서버가 견고해야하는데 이런 품질을 위주로 따지는 시스템은 비동기적으로 들어오는 데이터 스트림을 논블로킹 방식으로 처리하기 위해 리액티브 프로그래밍 패러다임이 등장하였다

### 리액티브 스트림
* 기존 자원을 더 효율적이고 일관성 있게 사용하기 위하여 리액티브 스트림이라는 내용을 도입하였다
* ```발행자(Publisher)```와 ```구독자(Subscriber)```간의 간단한 계악을 정의하는 명세이다
    * ```발행자```는 트래픽을 가능한 한 빨리 발행하면서 ```구독자는``` 정해진 양만큼의 트래픽만을 수용할 수 있다고 알리는 방식으로 트래픽을 제어할 수 있다

### 리액터 타입(Spring Project Reactor)
* 리액티브 스트림은 수요 조절에 기반하기 때문에 프로젝트 리액터는 객체를 담는 컨테이너 같은 공간인 ```Flux<T>```를 사용하여 수요 조절을 구현한다

* ```Flux<T>```는 물건을 전달해주는 ```Placeholder```이며 원래 객체 대신에 ```Flux<T>```를 받아 Flux 내부 객체의 결과가 정해지지 않아도 받을 수 있도록 한다

* 논블로킹 방식이기 때문에 결과가 정해질 때 까지 스레드가 멈추게 하지 않는다

### 리액티브 스트림 수명주기
1. 리액티브 스트림의 onNext() 시그널을 받으면 doOnNext()를 통해 ()내부의 코드를 실행
2. onError() 시그널을 받으면 doOnError()를 통해 ()내부 코드 실행
3. onComplete() 시그널을 받으면 doOnComplete()fmf xhdgo () 내부의 코드 실행
> 각각 ```리액티브 스트림의 시그널```을 받으면 시그널에 맞는 함수를 실행

* 이러한 흐름을 시작하기 위해서는 구독이 일어나야 한다
    * 프로젝트 리액터에서는 모든 흐름과 핸들러는 구현할 수 있지만 구독하지 않는다면 
    프로잭트 리액터를 호출하더라도 아무일도 일어나지 않는다