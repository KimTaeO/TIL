# Thread

Java에서 제공하는 Thread 생성을 위한 클래스이다. 대표적으로 다음과 같은 메서드들을 제공한다
- sleep
    현재 Thread를 멈추며 자원을 점유하며 제어권을 넘기기 때문에 데드락이 발생할 수 있다

- interrupt
    다른 Thread를 깨워 InterruptException을 발생시킨다.

- join
    다른 Thread의 작업이 끝날 때까지 기다리게 하여 순서를 제어하는데 사용한다

Thread를 사용해 클래스를 구현하기 위해서는 Thread를 상속받고 run 메서드를 구현해야 한다.
run 메서드는 start 메서드 호출 시 같이 실행된다

> 여기서 run을 직접 호출하는 것은 main 스레드에서 Thread 클래스의 run 메서드를 호출하는 것이기 떄문에 start를 호출한다.

start 메서드에서 하는 일을 간략히 살펴보면 다음과 같다
- 스레드가 실행 가능한지 확인한다
    스레드에는 여러 상태가 있는데 그중 New(0) 상태인지 확인한다. 만약에 New 상태가 아니라면 IllegalThreadStateException을 발새이킨다

- 스레드를 그룹에 추가한다
    관련된 스레드들을 하나로 그룹으로 관리하기 위한 작업이다

- JVM이 스레드를 실행한다
    네이티브 메서드인 start0()를 호출하여 스레드를 생성하고 스레드의 상태를 변경한다.

```java
    public synchronized void start() {
        // 스레드가 실행 가능한지 확인
        if (threadStatus != 0)
            throw new IllegalThreadStateException();

        // 스레드를 그룹에 추가
        group.add(this);

        boolean started = false;
        try {
            // 네이티브 메서드 호출
            start0();
            started = true;
        } finally {
            try {
                if (!started) {
                    group.threadStartFailed(this);
                }
            } catch (Throwable ignore) {
                /* do nothing. If start0 threw a Throwable then
                  it will be passed up the call stack */
            }
        }
    }
```

스레드 생성 예시
```Java
public class Main {

    static Thread thread = new MyThread();


    public static void main(String[] args) {
        thread.start();

        // main
        System.out.println(Thread.currentThread());
    }

    public static class MyThread extends Thread {
        @Override
        public void run() {
            // Thread-X
            System.out.println(Thread.currentThread());
        }
    }
}
```

## Runnable

run 메소드 하나만을 멤버로 가지는 함수형 인터페이스이다. 해당 인터페이스의 구현체를 만들고 Thread 객체 생성 시에 넘겨주면 실행 가능하다.
Thread가 run을 구현하는 이유도 Runnable을 구현하기 때문이다.

스레드 생성 예시를 Runnable을 사용하여 구현하면 다음과 같다
```Java
public class Main {
    static Runnable runnable = new Runnable() {
        @Override
        public void run() {
            System.out.println(Thead.currentThread());
        }
    }

    static Thread thread = new Thread(runnable);

    public static void main(String[] args) {
        thread.start();

        System.out.println(Thread.currentThread());
    }
}
```