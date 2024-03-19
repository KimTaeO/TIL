# 데이터베이스 Lock

* 데이터베이스에 값을 추가하거나 삭제 또는 변경하지 못하도록 데이터베이스를 잠그는 것을 의미한다
* 데이터베이스의 일관성을 유지하며, 하나의 행에 여러 트랜잭션이 접근하지 못하도록 한다

MySQL은 ```MySQL Engine Lock```과 ```Storage Level Lock```을 지원한다

* ```MySQL Engine Lock```은 각 스토리지 엔진에 영향을 미친다
* ```Storage Level Lock```은 각 스토리지 엔진에 영향을 미치지 않는다

## MySQL Engine Lock
* Global Lock
    * 특정 세션에서 Global Lock을 획득하면 단순 조회 이외의 대부분의 기능들을 사용할 수 없게 된다
    > MyISAM과 MEMORY 엔진에서 트랜잭션을 지원하지 않아 백업할떄 글로벌 락을 사용했다
* Backup Lock
    * 특정 세션에서 Backup Lock이 걸려있는 동안에도 단순 조회, 수정, 삭제 기능들을 사용할 수 있다
    > 데이터의 수정이나 삭제를 기록해 두었다가 트랜잭션의 마지막에 일괄적으로 삭제, 수정한다
* Table Lock
    * 테이블의 구조를 바꾸거나 데이터를 변경할 떄에 묵시적으로 Table Lock을 획득하게 된다(단 InnoDB에서는 데이터를 변경할 때에는 락을 획득하지 않는다)
    > 

## Storage Level Lock
* Record Lock
    * 테이블의 레코드들을 잠그는데 실제로는 레코드의 인덱스를 잠근다. 하지만 테이블이 인덱스가 걸려있지 않는다면 해당 테이블의 전체 레코드들을 잠근다.
* Gap Lock
    * 레코드와 인접한 레코드 사이에 새로운 데이터를 생성할 수 없도록 한다
    * 데이터를 수정하기 위해 ```SELECT ... FOR UPDATE```를 사용하여 조회한 레코드들 사이에 Gap Lock이 발생하게 된다
* Next Key Lock
    * Record Lock과 Gap Lock을 합쳐서 사용하는 것과 같다