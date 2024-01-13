# Java Reflection

리플렉션은 컴파일 시점이 아닌 자바 런타임에 클래스의 생성자 메소드 필드와 같은 클래스의 멤버들의 정보를 읽어오는 기능인데, 이것이 마치 거울에 투영된 모습과 비슷하다 하여 리플렉션이라 한다

## java.lang.Class

리플렉션의 핵심 클래스 중 하나이며, 현재 실행중인 애플리케이션의 클래스 또는 인터페이스를 나타낸다

public 생성자는 존재하지 않지만 클래스 로더의 defineClass의 메서드 호출을 통해 JVM이 Class 객체를 생성한다

모든 클래스의 인스턴스에는 ```getClass()``` 메서드가 존재하며, 이를 호출하여 Class 객체를 얻을 수 있다. 또는 ```Class```클래스의 ```forName()``` 메서드에 Fully Qualified Class Name을 전달하여 해당 경로와 대응하는 클래스의 인스턴스를 얻는 방법이다

* Class 클래스에는 많은 메서드들이 존재하는데 그중에 getxxx(), getDeclaredxxx() 메서드들은 클래스에 정의된 필드, 메소드, 어노테이션들을 가져오기 위해 사용된다.

    * getxxx() : 상속받은 클래스나 인터페이스를 포함한 모든 public 요소들을 가져온다
    * getDeclaredxxx() : 상속받은 클래스나 인터페이스를 제외한 해당 클래스의 private, protect, public 메소드를 전부 가져온다.


## java.lang.reflect.Constructor

Class를 통해 Constructor 객체를 받아올 수 있고, 클래스의 생성자에 대한 정보와 접근을 할 수 있으며
* ```getConstructor()```를 통하여 객체의 생성자를 받아올 수 있는데 만약에 생성자에 파라미터가 존재한다면 ```getConstructor()```파라미터에 생성자의 파라미터에 대응하는 타입을 전달하면 된다
* ```newInstance()```를 사용하여 객체를 직접 생성할 수 있다
> 단 private 생성자를 사용할 때에는 ```setAccessible(true)```를 사용해주어야 한다

## java.lang.reflect.Field

```getDeclaredFields()``` 또는 ```getDeclaredField(fieldName)```를 통해 객체의 필드에 접근할 수 있으며, ```set()``` 메서드를 통하여 setter가 없더라도 객체의 값을 강제로 변경할 수 있다

## java.lang.reflect.Method

```getDeclaredMethods()``` 또는 ```getDeclaredMethod(methodName)```를 통해 객체의 필드에 접근할 수 있으며, ```invoke()```메서드를 사용하여 메서드를 호출할 수도 있다

## Annotation

```getAnnotation()```메서드에 어노테이션 타입을 넣어서 클래스에 붙은 어노테이션 타입을 지정할 수 있고, 어노테이션의 필드에 접근할 수 있따

## 마무리

리플렉션은 호출하면 런타임에 클래스를 분석하여 가져오기 때문에 이미 분석되어 있는 메서드를 호출하는 것과 다르게 속도가 매우 느리다. 그리고 이러한 특징으로 인하여 컴파일 단계에서 타입 체크가 불가능하다

또한 접근 제어자가 있는 메서드나 필드에도 자유롭게 접근하며, setter없이 필드의 값을 조작하는 등 객체지향 프로그래밍의 추상화를 망가뜨릴 수 있기 때문에 조심하여 사용하여야 한다