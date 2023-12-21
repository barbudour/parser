# ICardFileSource - интерфейс
Настройки по местоположению контента файла.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface ICardFileSource
VB __Копировать
     Public Interface ICardFileSource
C++ __Копировать
     public interface class ICardFileSource
F# __Копировать
     type ICardFileSource = interface end
##  __Свойства
[FileExtensions](P_Tessa_Cards_ICardFileSource_FileExtensions.htm)|  Строка со
списком расширений, которые рекомендуется использовать с этим источником
файлов. Расширения разделены пробелами и обычно без ведущей точки. Строка
может быть равна null.  
---|---  
[IsDatabase](P_Tessa_Cards_ICardFileSource_IsDatabase.htm)| Признак того, что
местоположение соответствует базе данных, а не файловой папке.  
[MaxSize](P_Tessa_Cards_ICardFileSource_MaxSize.htm)|  Максимальный размер
занятого места в местоположении. Не заполняется и не используется системой,
возможно использование в расширениях.  
[Name](P_Tessa_Cards_ICardFileSource_Name.htm)| Отображаемое имя
местоположения.  
[Path](P_Tessa_Cards_ICardFileSource_Path.htm)|  Путь к местоположению.
Соответствует имени строки подключения к БД из конфигурационного файла или
полному путь к файловой папке.  
[Size](P_Tessa_Cards_ICardFileSource_Size.htm)|  Текущий размер занятого места
в байтах в местоположении. Не заполняется и не используется системой, возможно
использование в расширениях.  
[Type](P_Tessa_Cards_ICardFileSource_Type.htm)| Тип местоположения.  
[UseSimpleNamingScheme](P_Tessa_Cards_ICardFileSource_UseSimpleNamingScheme.htm)|
Признак того, что используется упрощённая схема именования папок, где для
карточек не создаются дополнительные подпапки. Значение true не рекомендуется,
если в системе возможны миллионы карточек с файлами, т.к. это приведёт к
миллионам подпапок внутри одной папки в файловой системе. Значение неактуально
для файлов в базе данных.  
## __Методы
[IsRecommendedExtension](M_Tessa_Cards_ICardFileSource_IsRecommendedExtension.htm)|
Возвращает признак того, что заданное расширение файла является рекомендуемым
для использования совместно с этим источником файлов.  
---|---  
## __См. также
#### Ссылки
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
