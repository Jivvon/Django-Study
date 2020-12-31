# Django Study

### COMMANDS
```shell
django-admin startproject config .
django-admin startapp pybo

python manage.py runserver

python manage.py makemigrations # 테이블 작업 파일 만든 후
python manage.py migrate # 테이블 생성
```

config.urls.py를 수정하여 'URL 매핑을 추가'한다.
config.urls.py는 페이지 요청 시 가장 먼저 호출되며, 요청 URL과 뷰 함수를 1:1로 매칭해준다.

view 함수의 매개변서 request는 장고에 의해 자동으로 전달되는 http 요청 객체이다.

### config/settings.py
- BASEDIR: 프로젝트 디렉토리로 현재 DjangoStudy/mysite이다.
- INSTALLED_APPS: 프로젝트에 설치된 앱
- DATABASES: 데이터베이스 엔진, 데이터베이스 위치(NAME)


### models.py
- CharField: 글자 수 제한
- TextField
- DateTimeField
- ForeignKey(Question, on_delete=models.CASCADE)

---

#### 모델 만들고 테이블 생성하기

모델을 만들고 이를 이용하여 테이블을 생성하려면 config/settings.py 파일에서 INSTALLED_APPS 항목에 앱을 추가해야 한다.

장고는 모델을 이용하여 데이터베이스의 실체가 될 테이블을 만드는데, 모델은 앱에 종속되어 있으므로 반드시 장고에 앱을 등록해야 테이블 작업을 진행할 수 있다. 

*`python manage.py sqlmigrate pybo 0001` 명령을 실행하면 실제로 어떤 쿼리문이 실행되는지 볼 수 있다*


