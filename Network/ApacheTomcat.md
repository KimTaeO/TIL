# Apache Tomcat

아파치 톰캣은 Java 플랫폼에서의 컴포넌트 기반 애플리케이션 개발을 위한 표준 플랫폼인 Jakarta 플랫폼의 일부인 ```Jakarta Servlet```, ```Jakarta Server Page```, ```Jakarta Expression Language```, ```Jakarta Web Socket```, ```Jakarta Annotations```, ```Jakarta Authentication```의 명세를 구현하는 오픈소스 소프트웨어이다.

## Apache Tomcat의 구성 요소
* Server
    * 모든 컨테이너를 표현하는 요소로 톰캣은 기본 Server 인터페이스를 제공하며, 사용자가 커스터마이징 하는 것도 가능하다

* Service
    * ```Server```내에 존재하는 중간 컴포넌트로 단 하나의 ```Engine```과 여러개의 커넥터들을 묶어놓은 컴포넌트이다

* Engine 
    * 특정 ```Server``` 내의 요청을 처리하는 파이프라인을 나타내며 하나의 서비스는 여러 개의 커넥터를 가질 수 있으며, 엔진은 커넥터로부터 요청을 받아 처리하고 적절한 커넥터에 응답을 반환한다 

* Host
    * ```Engine```은 여러 ```Host```를 포함할 수 있고, 각 호스트의 요소는 별칭을 지원한다

* Connect
    * ```Connect```는 사용자와의 소통을 담당하며, 톰캣에서는 여러 개의 커넥터를 사용할 수 있다
        * HTTP 커넥터 - 대부분의 HTTP 통신에 사용된다. 특히 독립형 톰캣을 실행하는 경우 사용한다
        * AJP 커넥터 - AJP 프로토콜을 구현하여 Apache Httpd 서버와 같은 웹 서버와 연결할 때 사용한다

* Context
    * 웹 어플리케이션을 나타내며, 한 호스트는 여러 ```Context```를 포함할 수 있으며, 각 ```Context```는 고유한 경로를 갖는다