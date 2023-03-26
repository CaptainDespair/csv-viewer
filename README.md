# test-task1

Данный HTTP-сервис позволяет загружать/удалять/просматривать csv-файлы. 
В папке csv_files уже загружены тестовые датасеты с Kaggle. Их также можно удалить с помощью функционала сервиса. 

Сервис работает таким образом: при импорте файлов из папки csv-файлов, названия и информация о колонках записывается в БД SQLite.
С помощью БД файлы получают id, а также в полях - информация о колонках. При просмотре можно отсортировать датасет по колонкам, а также есть поля для поиска ключевых слов (фильтр).
Стек:

  <b>Python3.9:</b>
  
    Flask
    SQLite3
    SQLAlchemy
    Pandas

 <b>Javascript(сортировка, фильтр)</b>
 
 Запуск сервиса:
 >python ./app.py
 
 При наличии docker'а на вашей ОС:
 >docker image build -t test-task1 .
 >docker run -p 5000:5000 -it test-task1
