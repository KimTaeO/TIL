# 데이터 모델

## 1. 데이터 모델의 정의

* 현실 세계의 정보들을 컴퓨터에 표현하기 위해서 단순화, 추상화, 명확화하여 체계적으로 표현한 개념적 모형

    * 추상화 : 현실세계를 일정한 형식에 맞추어 표현을 한다 즉, 다양한 현상을 일정한 양식인 표기법에 의해 표현한다는 것이다

    * 단순화 : 복잡한 현실세계를 약속된 규약에 의해 제한된 표기법이나 언어로 표현하여 쉽게 이해할 수 있도록 하는 개념을 의미한다

    * 명확화 : 누구나 이해하기 쉽게 하기 위해 대상에 대한 애매함을 제거하고 정확하게 현상을 기술하는 것을 의미한다

* 데이터, 데이터의 관계, 데이터의 의미 및 일관성, 제약 조건 등을 기술하기 위한 개념적 도구들의 모형이다.

* 현실 세계를 데이터베이스에 표현하는 중간 과정, 즉 데이터베이스 설계 과정에서 데이터의 구조(Schema)를 논리적으로 표현하기 위해 사용되는 지능적 도구이다.

* 정보시스템을 구축하기 위해, 해당 업무에 어떤 데이터가 존재하는지 또는 업무가 필요로 하는 정보는 무엇인지를 분석하는 방법

* 기업 업무에 대한 종합적인 이해를 바탕으로 데이터에 존재하는 업무 규칙에 대하여 참 또는 거짓을 판별할 수 있는 사실을 데이터에 접근하는 방법, 사람, 전산화와는 별개의 관점에서 이를 명확하게 표현하는 추상화 기법

## 2. 모델링의 관점

* 시스템의 대상이 되는 업무를 분석하여 정보시스템으로 구성하는 과정에서 업무의 내용과 정보시스템의 모습을 적정한 표기법으로 표현하는 것

* 모델링의 세 가지 관점

    * 데이터 관점 : 업무가 어떤 데이터와 관련이 있는지 또는 데이터 간의 관계는 무엇인지에 대해서 모델링하는 방법

    * 프로세스 관점 : 업무가 실제하고 있는 일은 무엇인지 또는 무엇을 해야 하는지를 모델링 하는 방법

    * 데이터와 프로세스의 상관관점 : 업무가 처리하는 일의 방법에 따라 데이터는 어떻게 영향을 받고 있는지 모델링하는 방법

## 3. 데이터 모델의 구성 요소

* 개체(Entity)
    * 개체는 데이터베이스에 표현하려는 것으로, 사람이 생각하는 개념이나 정보 단위 같은 현실 세계의 대상체이다.

    * 개체는 유형, 무형의 정보로서 서로 연관되 몇 개의 속성으로 구성된다.

    * 파일 시스템의 레코드에 대응하는 것으로 어떤 정보를 제공하는 역할을 수행한다.

    * 독립적으로 존재하거나 그 자체로서도 구별 가능하다.

* 속성(Attribute)

    * 속성은 데이터의 가장 작은 논리적 단위로서 파일 구조상의 데이터 항목 또는 데이터 필드에 해당한다.

    * 어떤 데이터 개체의 구성 요소로서 그 개체의 성질이나 상태를 기술해 주는 역할을 하며, 그 자체로는 중요한 의미를 가지지 못한다.

    * 릴레이션에서는 열(Column)에, 파일 시스템에서는 필드(Field)에 해당한다.

    * 속성은 개체를 구성하는 항목이다.

* 관계(Relationship)

    * 관계는 두 개 이상의 개체 간의 연관성을 결정짓는 의미 있는 연결로, 개체 간의 관계 또는 속성 간의 관계를 나타낸다.

    * 개체를 구성하는 것들 사이에서의 대응성을 나타내는 것으로, 현실 세계를 개념 세계로 표현할 때 집합들의 구성원소 사이에 1:1, 1:N, N:M 등의 사상을 의미하는 것이다.

    * **관계의 형태**
       
        * 1:1, 1:N, N:M등이 있다.