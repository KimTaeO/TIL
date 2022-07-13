# 숫자와 문자열을 다루는 함수들 

> 개요 >> 함수들이란 ? : 어떠한 코드 뒤에 괄호가 붙어서 그 자체 또는 인자들을 넣어서 어떠한 기능을 수행하도록 하는 것
>> 함수의 기본 형태 >> 코드(인자 또는 그 자체)

<br>

## 1.숫자 관련 함수들

* ```ROUND``` : 반올림
* ```CEIL``` : 올림
* ```FLOOR``` : 내림
* ```ABS``` : 절댓값
* ```GREATEST``` : 괄호 안에서의 가장 큰 값
* ```LEAST``` : 괄호 안에서의 가장 작은 값

<br>

## 2. 그룹(집계) 함수들
* ```MAX``` : 가장 큰 값
* ```MIN``` : 가장 작은 값
* ```COUNT``` : 갯수 (NULL값 제외)
* ```SUM``` : 총 합
* ```AVG``` : 평균값
* ```POW(A, B) or POWER(A, B)```
    * A 를 B만큼 제곱
* ```SQRT``` : 제곱근
* ```TRUNCATE``` : N을 소수점 n자리까지 선택

|값|인자|출력값|
|:-:|:-:|:-:|
|1234.5678|1|1234.5|
|1234.5678|2|1234.56|
|1234.5678|3|1234.567|
|1234.5678|-1|1230|
|1234.5678|-2|1200|
|1234.5678|-3|1000|

<br>

## 3. 문자열 관련 함수들
* ```UCASE, UPPER``` : 모두 대문자로
* ```LCASE, LOWER``` : 모두 소문자로
* ```CONCAT``` : 문자열을 이어붙여줌
* ```CONCAT_WS``` : 괄호 뒤에 첫번째로 오는 문자열로 문자열을 
이어붙여줌
    * 사용 예시) ![사용 예시](https://cdn.discordapp.com/attachments/951334644710776843/996603418481283133/2022-07-13_112547.png)
    ![사용 결과](https://cdn.discordapp.com/attachments/951334644710776843/996603828378013888/2022-07-13_11271223.png)

* ```SUBSTR, SUBSTRING``` : 주어진 값에 따라 문자열을 자름

    * 사용 예시) ![사용 예시](https://cdn.discordapp.com/attachments/985120659900338199/996601448500576266/2022-07-13_111415.png)
    ![사용 결과](https://cdn.discordapp.com/attachments/951334644710776843/996602510590611527/2022-07-13_112100.png)

* ```RIGHT, LEFT``` : 주어진 값에 따라 오른쪽/왼쪽 부터 문자열을 자름
* ```LENGTH``` : 문자열의 *바이트* 길이
* ```CHAR_LENGTH, CHARACTER_LENGTH``` : 문자열의 *문자* 길이
*  ```TRIM, (L,R)TRIM``` : CONCAT함수 인자 부분에 삽입하는 함수로, 공백을 삭제시켜 줌
* ```L/RPAD``` : 입력된 문자열이 입력된 길이만큼 될 때까지 입력된 인자를 이어붙여줌
* ```REPLACE``` : 문자열에서 지정한 내용을 입력한 인자로 바꾸어 줌
* ```INSTR``` : 입력받은 인자가 처음으로 위치한 위치를 반환

___
<br>

## 번외

* ```CONVERT``` : 입력받은 자료를 원하는 자료형으로 전환해줌