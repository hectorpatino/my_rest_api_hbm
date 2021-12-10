web: gunicorn humbolt.wsgi --log-file -
release: python manage.py makemigrations --noinput
release: python manage.py collectstatic --noinput
release: python manage.py migrate --noinput
web: sh setup.sh && python -m spacy download en_core_web_sm && streamlit run app.py