# Socket

네트워크 통신을 하기 위해서는 TCP/IP 계층을 통해 이루어지는데 소켓은 전송 계층과 응용 계층 사이에 있는 인터페이스이다

통신의 시작점과 종료점 즉 엔드포인트라고도 한다 소켓을 이용하여 TCP나 UDP에 접근할 수 있게 되는 것이다

### Socket의 구성 요소
소켓은 프로토콜, IP주소, 포트번호로 이루어져 있다

### Socket 통신 과정

소켓은 서버 소켓(Server Socket) 클라이언트 소켓(Client Socket)으로 구성되어 있다

TCP 통신 과정
1. socket()으로 통신을 위한 엔드포인트를 작성하고 해당 종료점을 나타내는 정수로 이루어진 소켓 설명자를 리턴한다
2. 소켓 설명자가 있는 어플리케이션은 고유한 이름을 소켓에 바인드 할 수 있다
3. 서버 소켓에서 listen()으로 클라이언트 연결 요청을 승인하려는 의사를 표시한다
4. 클라이언트 애플리케이션이 connect() API를 사용하여 서버 소켓에 대한 연결을 설정한다
5. 서버 애플리케이션이 accept() API를 사용하여 클라이언트 연결 요청을 승인한다
6. 서버와 클라이언트 간 연결이 이루어지면 데이터를 주고 받는다
7. 조작을 중단하려는 경우에는 서버나 클라이언트가 close()를 실행하여 서로의 연결을 해제하고 소켓이 점유하고 있는 시스템 자원을 해제한다

서버와 클라이언트가 연결을 둘중 한쪽이 끊기 전까지 유지되므로 실시간으로 데이터를 주고 받을 수도 있다

### Java Socket Class

자바에서 네트워크 연결을 생성하는 클라이언트 기반의 클래스들은 전부
java.net.Socket을 호출한다

소켓은 Server, Client가 존재하며 Server는 데이터를 전송하고 Client는 데이터를 수신하는 역할이다

Socket 클래스는 운영체제의 로컬 TCP 스택과의 통신을 위해 네이터브 코드를 사용한다

여느 클래스들과 같이 생성자로 객체를 생성할 수 있는데 매개변수로는 ```원격 호스트의 주소```, ```포트번호```를 받는다, 생성하는 동시에 원격 호스트에 대한 연결이 생성된다
public Socket(String host, int port)
public Socket(InetAdress host, int port)

연결에 사용할 로컬 인터페이스를 지정하기 위해서는 다음과 같은 생성자를 사용하면 된다
Socket(String host, int port, InetAddress interface, int localPort)
Socket(InetAddress host, int port, InetAddress interface, int localPort)

3, 4번째의 네트워크 인터페이스와 포트로 1, 2번째 호스트와 포트로 접속을 시도하게 된다

예시 코드
Server
```Kotlin
import java.net.ServerSocket

fun main() = with(System.`in`.bufferedReader()) {
    val serverSocket = ServerSocket(8080)

    val socket = serverSocket.accept()

    serverSocket.use {
        socket.use {
            val input = it.getInputStream()
            val output = it.getOutputStream()

            val data = ByteArray(100)
            input.read(data)
            println(String(data))


            val sendMessage = "으아아"
            output.write(sendMessage.toByteArray())
            output.flush()
        }
    }
}
```

Client
```Kotlin
import java.net.Socket

fun main() {
    val socket = Socket("127.0.0.1", 8080)

    socket.use {
        val input = it.getInputStream()
        val output = it.getOutputStream()

        val sendMessage = "꾸아아"
        output.write(sendMessage.toByteArray())
        output.flush()

        val data = ByteArray(100)
        input.read(data)

        println(String(data))
    }
}
```