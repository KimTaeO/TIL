## JVM(Java Virtual Machine)

* 자바 바이트 코드를 해석하고 실행하는 역할을 한다
* 자바는 타겟 플랫폼에 상관없이 JVM 위에서 실행되므로 어떤 OS에서도 동일하게 실행된다

* 자바 실행 과정
  * 자바 소스코드인 .java 파일을 컴파일러가 자바 바이트 코드인 .class로 변환시킨다
  * 변환된 .class 코드를 클래스 로더에게 보낸다
  * 클래스 로더는 JVM의 런타임 영역으로 로딩시켜 JVM의 메모리에 올린다
  ![jvm](/image/Java%20%EC%BD%94%EB%93%9C%20%EC%8B%A4%ED%96%89%20%EA%B3%BC%EC%A0%95.png)
  > 프로그램이 실행되면, JVM은 OS로부터 프로그램을 수행하는데 필요한 메모리를 할당받는다

### JVM의 메모리 영역

* JVM은 용도에 따라 메모리 영역을 구분하여 사용합니다

* ## Method Area
  * 패키지 정보, 클래스 정보, 변수 정보, 메서드 정보, static 변수 등이 저장된다
  * JVM이 동작해서 클래스가 로딩될 떄 생성된다
  * JVM이 종료될 때 까지 유지된다

* ## Heap
  * 인스턴스를 생성할 때 생성되는 메모리 영역이다
  * 참조형(class, interface), 자료형(Int, String, Boolean)도 같이 저장된다
  * Heap의 참조 주소는 **Stack**이 가지고 있으며, 해당 객체를 통해서만 **Heap** 영역에 있는 인스턴스를 핸들링할 수 있다
  * **Garbage Collector**가 정리하기 전까진 남아있다

> Method Area와 Heap 영역은 모든 스레드가 공유하는 영역이므로 멀티스레드 프로그래밍 시 주의 필요

* ## Stack
  * 기본 자료형들을 생성할 때 저장하는 공간으로, 임시적으로 사용되거나 사용되는 변수들의 정보들이 저장되는 영역이다
  * 스레드별로 1개만 생성된다
  * ```Frame```이라는 자료구조가 들어가는데, 메소드가 호출될 때마다 생성되고, 메서드 실행이 끝나면 pop되어 사라진다

* ## Frame
  * ```Frame```은 ```Local Variable Array```, ```Constant Pool Reference```, ```Operand Stack```으로 이루어져 있다

  * ### Local Variable Array
    * 메서드 내의 지역 변수를 담는 배열 
    * 매개변수, 지역변수들을 배열에 담아 인덱스로 빠르게 접근할 수 있도록 한다
    * 첫번째 인덱스에는 현재 인스턴스에 대한 참조를 가진다

  * ### Operand Stack
    * 피연산값(Operand), 연산의 중간 값들을 저장하는 자료구조이다

  * ### Constant Pool Reference
    * 클래스 내에서 사용되고 있는 상수를 담은 테이블
    * ```index & Type```, ```value```로 이루어져있다
    * ```value```의  ```Symbolic Reference```는 클래스의 이름을 문자열로 가지고 있음, 호출 시 해당 클래스가 로드되지 않았다면 ```Class Loader```에게 요청을 보내 클래스를 로드하고 로드한 클래스를 가리키도록 변경(Constant Pool Resolution)

* ## PC Register
  * 현재 실행되고 있는 명령어의 주소를 저장

* ## Native Method Stacks
  * C나 C++로 작성된 메서드를 실행하기 위한 스택

> ```Stack```, ```PC Register```, ```Native Method Stacks```는 한 스레드가 생성될 때 같이 생성되며, 서로 다른 스레드가 접근할 수 없는 영역이다

     