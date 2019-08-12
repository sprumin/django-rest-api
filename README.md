# Django-rest-api

### Django 를 이용한 RESTFUL API 제작

django-rest-framework 를 사용하지않은 프로젝트입니다.
Python3, Django 2.0  설치되어있다는 가정하에 작성하였습니다.



#### How to Use

- Repository clone 및 DB migrate
  - `git clone https://github.com/sprumin/django-rest-api.git` 
  - `python manage.py makemigrations`
  - `python manage.py migrate`
- KEY 생성/조회/삭제
  - `python manage.py keymanager`
  - 생성 : add 명령어 입력 후 name 입력
  - 조회 : show 명령어 입력
  - 삭제 : delete 명령어 입력 후 name 입력
  - 중지 : exit 명령어 입력 or Ctrl + C
- Django Server 실행
  - `python manage.py runserver`



기본적인 세팅은 끝마쳤으니 API를 사용해보도록 하겠습니다.

테스트는 Advanced REST Client 를 사용하였습니다. ( 또는 POSTMAN )

**Request시 header에 {"AUTHORIZATION": "your-api-key"} 를 삽입해야합니다.**

- GET

  - http://127.0.0.1:8000/user
  - 현재 DB에 저장된 유저들의 목록을 조회합니다.
  - http://127.0.0.1:8000/user/N
  - DB에 저장된 유저들중 idx가 N인 유저의 정보를 가져옵니다.

- POST

  - http://127.0.0.1:8000/user/

  - ```json
    {
      "email": "your@email.com",
      "username": "your name",
      "info": "your info",
      "password1": "your password",
      "password2": "your password confirmation"
    }
    ```

  - 위 양식에 맞게 데이터를 전송하면 유저가 생성됩니다.

- PUT

  - http://127.0.0.1:8000/user/N

  - DB에 저장된 유저들중 idx가 N인 유저의 정보를 수정합니다.

  - ```json
    {
      "email": "your@email.com",
      "username": "your name",
      "info": "your info",
      "password1": "your password",
      "password2": "your password confirmation"
    }
    ```

  - 위 양식에 맞게 데이터를 전송하면 유저의 정보가 변경됩니다.

- DELETE

  - http://127.0.0.1:8000/user/N

  - DB에 저장된 유저들중 idx가 N인 유저의 정보를 삭제합니다.

  - 위 양식에 맞게 데이터를 전송하면 유저의 정보가 삭제됩니다.



#### TODO

- [x] 소스 완성 후 커밋
- [x] API KEY 생성/조회/삭제 기능 추가 및 API Request 시 Key 검사
- [x] API KEY 인증키 전송 방법 body에서 header로 변경
- [x] ~~header에 authorization 삽입 후 전송 시 일정 확률로 0 request error 뜨는 버그~~ 일시적인 버그였음
- [x] API KEY 인증 decorator 작성
- [ ] Query 최적화
