# Cyber security base course project
### Project is a simple diary application where users can create and see notes. The application contains cyber security flaws on purpose. It is only meant for local testing.
---
### Project is a web application that has 5 flaws and their fixes commented in source code. For each flaw there are screenshots before and after the fix in the screenshots folder.
In this project the flaws are chosen from OWASP 2021 list:
---
1. A01 Broken Access Control
2. A02 Cryptographic Failures
3. A03 Injection
4. A07 Identification and Authentication Failures
5. A09 Security Logging and Monitoring Failures
---
# Instructions for installation and setup

Requirements:
- Python version 3.14
- Django version 6.1.2
- cryptography version 50.0.2
---
1. Clone the repository
```
git clone https://github.com/AnnaKivekass/cybersecurity.git
```
```
cd cybersecurity
```
2. Create and activate the virtual environment
```
python -m venv venv
```
for linux and macOS use
```
source venv/bin/activate
```
for windows use
```
.\venv\Scripts\Activate.ps1
```
3. Install depencies
```
python -m pip install Django==6.1.2 cryptography==50.0.2
```
4. Set the django secret key
for linux and macOS you can set django secret key with
```
export DJANGO_SECRET_KEY="$(python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())')"
```
for windows you can set django secret key with
```
$env:DJANGO_SECRET_KEY = python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```
5. Apply database migrations
```
python manage.py migrate
```
6. Start the development server
```
python manage.py runserver
```
---
