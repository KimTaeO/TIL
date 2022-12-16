## 객체지향 개발 5대 원칙(SOLID)

* 프로그래머가 유지보수와 확장이 쉬운 시스템을 개발하고자 로버트 마틴이 명명한 객체지향 프로그래밍의 5대 원칙

    * 단일 책임 원칙(Single Responsibility principle)
        * 한 클래스는 하나의 책임만 가져야 한다

    * 개방/폐쇄 원칙(Opne/Closed principle)
        * 소프트웨어 요소는 확장에는 열려 있으나, 변경에는 닫혀 있어야 한다

    * 리스코프 치환 원칙(Liskov substitution principle)
        * 프로그램의 객체는 프로그램의 정확성을 깨뜨리지 않으면서 하위 타입의 인스턴스로 바꿀 수 있어야 한다

    * 인터페이스 분리 원칙(Interface segregation principle)
        * 특정 클라이언트를 위한 인터페이스 여러 개가 범용 인터페이스 하나보다 낫다

    * 의존관계 역전 원칙(Dependency inversion principle)
        * 프로그래머는 추상화에 의존해야지 구체화에 의존하면 안된다