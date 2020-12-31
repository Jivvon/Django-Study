# Django Study

### COMMANDS
```shell
django-admin startproject config .
django-admin startapp pybo

python manage.py runserver
```

config.urls.py를 수정하여 'URL 매핑을 추가'한다.
config.urls.py는 페이지 요청 시 가장 먼저 호출되며, 요청 URL과 뷰 함수를 1:1로 매칭해준다.

view 함수의 매개변서 request는 장고에 의해 자동으로 전달되는 http 요청 객체이다.

### config/settings.py
- BASEDIR: 프로젝트 디렉토리로 현재 DjangoStudy/mysite이다.
- INSTALLED_APPS: 프로젝트에 설치된 앱
- DATABASES: 데이터베이스 엔진, 데이터베이스 위치(NAME)

