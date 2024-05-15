# Python 3.8을 기반 이미지로 사용
FROM python:3.10-slim

# 컨테이너 내에서 작업 디렉토리 설정
WORKDIR /app

# Python 의존성 설치
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# 프로젝트 파일 복사
COPY . /app/

# 서버 포트 8000번 열기
EXPOSE 8000

# Django 서버 실행
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
