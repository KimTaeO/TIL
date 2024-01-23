# Column Family Database

No-SQL의 한 종류이며, Wide Column Database라고도 불린다. Google BigTable Data Storage에서 파생된 개념이며, 데이터를 ```Column Families```에 저장한다. 또한 대용량 데이터를 처리하는데 유용하다.

> Column Families는 주로 서로 관련된 데이터나, 함께 자주 접근하는 데이터들로 구성한다

## Column Family Database의 구조
* Row
    * Column Family Database는 여러개의 Row을 가질 수 있으며, 그 Row에는 ```Column Family```가 존재하는데 이는 RDB의 테이블과 같다
    * Row을 식별하기 위한 ```Row Key```가 존재하며 이는 데이터베이스의 ```Primary Key```와 동일한 역할을 수행한다
    * Row은 Column을 가질 수 있지만 그 Column의 개수는 서로 다를 수 있으며, Column은 필요할 때 마다 Row에 추가할 수 있다.

* Column
    * Name, Value, TimeStamp로 이루어져있으며, Name은 Column의 이름, Value에는 Database가 지원하는 여러 데이터 타입들로 저장할 수 있고, TimeStamp는 데이터가 삽입된 시간을 저장한다.