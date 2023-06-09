# csv-viewer

Данный HTTP-сервис позволяет загружать/удалять/просматривать csv-файлы. 
В папке csv_files уже загружены тестовые датасеты с Kaggle. Их также можно удалить с помощью функционала сервиса.

На главной странице показаны загруженные датасеты, кликнув по ним отображается весь датасет с возможностью сортировки и фильтрации.
Кнопки:
<li>загрузить данные в БД - переброс на страницу для загрузки файлов
<li>удалить данные из БД - сервис перестает работать с датасетами, которые непосредственно удалены из БД (сами файлы могут лежать в папке)
<li>удалить файлы из папки - удаление файлов из папки с подтверждением

Кнопки и ссылки делают функционал сервиса простым и понятным.

Сервис работает таким образом: при импорте файлов из папки csv-файлов, названия и информация о колонках записывается в БД SQLite.
С помощью БД файлы получают id, а также в полях - информацию о колонках. При просмотре можно отсортировать датасет по колонкам, а также есть поля для поиска ключевых слов (фильтр).

<li>/backup - если вдруг вы удалите датасеты, а у вас не будет под рукой других для тестирования
<li>/csv_files - директория хранения датасетов, с которыми работает сервис
<li>/instanse - здесь база данных sqlite3, ей можно управлять как вручную, так и с помощью сервиса
<li>/static - папка, где хранятся стили и веб-скрипты
<li>/templates - папка с html-страницами
  
Стек:

  <b>Python3.9:</b>
  
    Flask
    SQLite3
    SQLAlchemy
    Pandas

 <b>Javascript(сортировка, фильтр)</b>
 
 Запуск сервиса:
 >pip install -r requirements.txt 
  
 >python ./app.py
 
 При наличии docker'а на вашей ОС:
 >docker image build -t <think up image_name> .
 
 >docker run -p 5000:5000 -it <think up image_name>
