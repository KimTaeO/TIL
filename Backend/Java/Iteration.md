# Iteration
배열이나 리스트와 같은 객체들에서 각 요소에 접근하여 처리한다는 것을 의미한다

> iterate의 사전적 정의 : (계산, 컴퓨터 처리 절차를)반복한다
> iterator : 반복자

## Iterator(반복자)
Iterator는 Iterable의 요소들을 순회하는 객체를 의미하며 자바의 Iterator 인터페이스는 JDK 1.2에서 Collectioin 프레임워크가 도입되면서 함께 추가되었다
Iterator는 Collection 인터페이스를 구현 및 상속한 모든 클래스에서 사용이 가능하다 Collection 인터페이스가 구현하는 Iterable 인터페이스에 iterable()이라는 메서드를 통해 객체를 얻을 수 있다.

Iterator는 다음과 같은 기능을 가진 메서드를 제공한다

* hasNext() : 다음 요소가 존재하는지 확인하는 메서드이다. 만약에 다음 메서드가 존재한다면 true, 마지막 요소라면 false를 반환한다

* next() : 다음 요소를 가져온다

* remove() : next()로 호출된 요소를 제거한다

이러한 메서드들은 Iterator에서 내부적으로 호출될 때 hasNext(), next(), remove()순으로 호출된다