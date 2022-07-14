# SQL의 분류

**1. DML(Data Manipulation Langauge) 데이터 조작 언어**
* 데이터를 조작(선택, 삽입, 수정, 삭제)하는 데 사용되는 언어

* ```SELECT, INSERT, UPDATE, DELETE```구문이 여기에 포함된다

* DML구문이 사용되는 대상은 테이블의 행

* DML을 사용하기 위해서는 꼭 그 이전의 테이블이 정의되어 있어야 
함

* *트랜잭션*이 발생하는 SQL도 DML에 속한다
    * *트랜잭션*이란 테이블의 데이터를 변경(입력/수정/삭제)할 때 실제 테이블에 완전히 적용하지 않고 임시로 적용시키는 것

**2. DDL(Data Definition Langauge) 데이터 정의 언어**
* 데이터베이스, 테이블, 뷰, 인덱스 등의 데이터베이스 개체를 생성/삭제/변경하는 역할

* ```CREATE, DROP, ALTER```구문이 여기에 포함된다

* DDL은 *트랜잭션*을 발생시키지 않는다

* ROLLBACK이나 COMMIT 사용이 불가하다

* DDL문은 실행 즉시 My SQL에 적용된다

## 3. DCL(Data Control Langauge) 데이터 제어 언어
* 사용자에게 어떤 권한을 부여하거나 빼앗을 때 주로 사용하는 구문

* ```GRANT/REVOKE```등이 있다
