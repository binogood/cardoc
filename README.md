# Cardoc
![스크린샷 2021-11-28 오후 11 49 28](https://user-images.githubusercontent.com/67960152/143772991-2d0e773c-e1cf-419d-926a-8b7a8c80eed3.png)



## 1. 카닥 기업 소개

### 자동차 오너의 소비를 편하게.
자동차 오너의 소비 여정은 자동차를 구매한 이후부터 비로소 시작됩니다.
카닥은 복잡하고 어려운 자동차 관리 정보를 편리 하게 제공하고
신뢰할 수 있는 파트너와 상품, 서비스를 모아
당신의 자동차를 위한 더 나은 선택을 돕습니다.

<br>
<br>

## 2. 팀원 : 송빈호
### 🖥 Backend 1명 🖥
| **이름** | **Github Link** |
|:------|:-------------|
| 송빈호 | https://github.com/binogood |
<br>

### Stack
- FastApi
- Uvicorn
- Asyncio
- Starlette
- Alembic
- SQLAlchemy
- MySQL
- GitHub

## 3. 기업 과제
- READ.ME 작성
    - 프로젝트 빌드, 자세한 실행 방법 명시
    - 구현 방법과 이유에 대한 간략한 설명
    - **서버 구조 및 디자인 패턴에 대한 개략적인 설명**
    - 완료된 시스템이 배포된 서버의 주소
    - 해당 과제를 진행하면서 회고 내용 블로그 포스팅
- Swagger나 Postman을 이용하여 API 테스트 가능하도록 구현
## 1. 배경 및 공통 요구사항

<aside>
😁 **카닥에서 실제로 사용하는 프레임워크를 토대로 타이어 API를 설계 및 구현합니다.**

</aside>

- 데이터베이스 환경은 별도로 제공하지 않습니다.
 **RDB중 원하는 방식을 선택**하면 되며, sqlite3 같은 별도의 설치없이 이용 가능한 in-memory DB도 좋으며, 가능하다면 Docker로 준비하셔도 됩니다.
- 단, 결과 제출 시 README.md 파일에 실행 방법을 완벽히 서술하여 DB를 포함하여 전체적인 서버를 구동하는데 문제없도록 해야합니다.
- 데이터베이스 관련처리는 raw query가 아닌 **ORM을 이용하여 구현**합니다.
- Response Codes API를 성공적으로 호출할 경우 200번 코드를 반환하고, 그 외의 경우에는 아래의 코드로 반환합니다.

[Copy of Code](https://www.notion.so/08e67c3cdc8e471fb1aab50e5963fb05)

---

## 2. 사용자 생성 API

🎁 **요구사항**

- ID/Password로 사용자를 생성하는 API.
- 인증 토큰을 발급하고 이후의 API는 인증된 사용자만 호출할 수 있다.

```jsx
/* Request Body 예제 */

 { "id": "candycandy", "password": "ASdfdsf3232@" }
```

---

## 3. 사용자가 소유한 타이어 정보를 저장하는 API

🎁 **요구사항**

- 자동차 차종 ID(trimID)를 이용하여 사용자가 소유한 자동차 정보를 저장한다.
- 한 번에 최대 5명까지의 사용자에 대한 요청을 받을 수 있도록 해야한다. 즉 사용자 정보와 trimId 5쌍을 요청데이터로 하여금 API를 호출할 수 있다는 의미이다.

```jsx
/* Request Body 예제 */
[
  {
    "id": "candycandy",
    "trimId": 5000
  },
  {
    "id": "mylovewolkswagen",
    "trimId": 9000
  },
  {
    "id": "bmwwow",
    "trimId": 11000
  },
  {
    "id": "dreamcar",
    "trimId": 15000
  }
]
```

🔍 **상세구현 가이드**

- 자동차 정보 조회 API의 사용은 아래와 같이 5000, 9000부분에 trimId를 넘겨서 조회할 수 있다.
 **자동차 정보 조회 API 사용 예제 → 
📄** [https://dev.mycar.cardoc.co.kr/v1/trim/5000](https://dev.mycar.cardoc.co.kr/v1/trim/5000)
**📄** [https://dev.mycar.cardoc.co.kr/v1/trim/9000
📄](https://dev.mycar.cardoc.co.kr/v1/trim/9000) [https://dev.mycar.cardoc.co.kr/v1/trim/11000
📄](https://dev.mycar.cardoc.co.kr/v1/trim/11000) [https://dev.mycar.cardoc.co.kr/v1/trim/15000](https://dev.mycar.cardoc.co.kr/v1/trim/15000)
- 조회된 정보에서 타이어 정보는 spec → driving → frontTire/rearTire 에서 찾을 수 있다.
- 타이어 정보는 205/75R18의 포맷이 정상이다. 205는 타이어 폭을 의미하고 75R은 편평비, 그리고 마지막 18은 휠사이즈로써 {폭}/{편평비}R{18}과 같은 구조이다.
 위와 같은 형식의 데이터일 경우만 DB에 항목별로 나누어 서로다른 Column에 저장하도록 한다.

---

## 4. 사용자가 소유한 타이어 정보 조회 API

🎁 **요구사항**

- 사용자 ID를 통해서 2번 API에서 저장한 타이어 정보를 조회할 수 있어야 한다.
### 실행 방법
- cardoc database 생성 후 alembic으로 테이블 migration
```
alembic upgrade 9641370b0435 <-- alembic.ini 파일 위치에서 입력시 자동으로 migration실행         
```
- main.py 실행
- 실행 후 127.0.0.1:8000/docs 에서 swagger 확인 가능


### 실행 예제
- user create
```
- Request body
{
  "name": "candycandy2",
  "password": "11223344"
}

- Response body
{
  "user_id": 6,
  "name": "candycandy2",
  "password": "$2b$12$rhLyy.QRc7HuXKx8OdU9Zun.cRtBYr.UC7IBAxWP2A5G16/1ioyoq",
  "created_at": "2021-11-28T15:17:12",
  "updated_at": "2021-11-28T15:17:12"
}
```

- user_login
```
- Request body
{
  "name": "candycandy",
  "password": "11223344"
}

- Response body
{
  "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjoxfQ.7biMboTZqGw0kVl1wCbbydBpOt8bPmt-0-BRozeApiM",
  "token_type": "bearer"
}
```

- create_car
```
- Request body
{
  "trimId": 15000
}

- Response body
{
  "car_id": 5,
  "trimId": 15000
}
```


- create_tire_type
```
- Request body
{
  "name": "front"
}

- Response body
{
  "tire_type_id": 1,
  "name": "front"
}
```

- create_tire
```
- Request body
{
  "value": "245/45R19",
  "tire_type_id": 1
}

- Response body
{
  "tire_id": 1,
  "value": "245/45R19",
  "tire_type_id": 1
}
```

- create_car_tire
```
- Request body
{
  "car_id": 1,
  "tire_id": 1
}

- Response body
{
  "car_tire_id": 1,
  "car_id": 1,
  "tire_id": 1
}
```

- create_user_car
```
- Request body
- 최대 5개까지 동시 생성 가능
[
  {
    "name": "string",
    "trimId": 0
  }
]

- Response body
[
  {
    "user_car_list": [
      {
        "name": "candycandy",
        "trimId": 5000
      }
    ]
  }
]
```

- get_user_car
```
- Request body
- 보유중인 차량의 타이어 정보 출력
[
  {
    "name": "candycandy",
    "trimId": 5000
  }
]

- Response body
{
  "id": "candycandy",
  "trimId": "5000",
  "car_tire": {
    "front": "245/45R19",
    "rear": "245/45R20"
  }
}
```

- 데이터가 없는 경우 모든 경우에 대해서 404 에러 발생
- 중복된 데이터에 대해서는 400 

## 5. 어려웠던 점
전 과제에서 oop를 사용하여 프로젝트를 진행하는데 거의 아뭇것도 못하여서 이번에 한번 oop형태로 구현을 해보았다.
하면서 이것까지 나눠야 하나? 라는 파일이 많았다. middleware도 처음 도입을 해보았고 기본 베이스 구성하는데도 많은 어려움이 있었다.
수정해야할 부분이 있으면 알려주시면 감사하겠습니다.
