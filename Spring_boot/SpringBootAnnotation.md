## 스프링부트의 어노테이션들

* 어노테이션 @(주석+힌트):컴파일러가 무시하지 않는다
* // (주석):컴파일러가 무시하는 부분


* Spring에서 어노테이션은 주로 객체를 생성한다
    * @Component : 해당 클래스를 스캔해 heap 메모리에 로딩한다 (IoC컨테이너)

    * @Bean : 스프링 컨테이너에 의해 만들어진 자바 객체

    * @Autowired : 로딩된 객체를 해당 변수에 집어 넣는다. heap 공간에 객체를 읽어 동일한 타입의 객체가 없다면 null, 있다면 heap에 올라온 객체를 넣는다(DI)

    * Controller : controller임을 나타내고 bean으로 등록되며 이 클래스가 controller로 사용됨을 spring framework에 알린다

