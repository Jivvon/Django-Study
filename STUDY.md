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


#### 모델 사용하기: 데이터 만들고 저장, 조회하기

`python manage.py shell`: 셸 접속
```shell
>>> q = Question(subject='1번제목', content='1번내용', create_date=timezone.now())
>>> q.save()
>>> q.id # 1 : id값 자동 생성

>>> Question.objects.all() -> <QuerySet [Question object(1)] >
>>> Question.objects.all() -> <QuerySet [Question object(1번제목)] > # __str__
>>> Question.objects.get(id=1) -> <Question: 1번제목> # 한 개 반환
>>> Question.objects.filter(id<5) -> <QuerySet [~]> # list (여러 개) 반환
>>> Question.objects.filter(subject__contains='1번') # 문자열 포함 여부
>>> q.delete() # (1, {'pybo.Question': 1})

>>> q.answer_set.all() -> <QuerySet [<Answer: Answer object (1)>]> # _set
```

- 데이터 생성, 수정 모두 `save()` 해야 적용된다. `delete()`는 즉시 삭제된다.
- **Question 모델과 Answer 모델처럼 서로 연결되어 있으면 `연결모델명_set`과 같은 방법으로 연결된 데이터를 조회할 수 있다.**


