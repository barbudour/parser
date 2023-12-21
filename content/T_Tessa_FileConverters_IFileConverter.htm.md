# IFileConverter - интерфейс
Объект, выполнющий преобразование файлов из одного формата в другой.
## __Definition
 **Пространство имён:** [Tessa.FileConverters](N_Tessa_FileConverters.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IFileConverter
VB __Копировать
     Public Interface IFileConverter
C++ __Копировать
     public interface class IFileConverter
F# __Копировать
     type IFileConverter = interface end
##  __Методы
[ConvertFileAsync](M_Tessa_FileConverters_IFileConverter_ConvertFileAsync.htm)|
Выполняет асинхронную конвертацию файла карточки в заданный формат. Это
рекомендуемый способ выполнения конвертации. Возвращает асинхронный
[System.Threading.Tasks.Task], при завершении которого будет получен результат
конвертации, который предоставляет доступ к содержимому файла, для которого
была выполнена конвертация. Результат всегда не равен null, ошибки и
исключения будут сохранены в объекте результата.  
---|---  
[DeleteFileAsync](M_Tessa_FileConverters_IFileConverter_DeleteFileAsync.htm)|
Удаляет сконвертированный файл из кэша файлов, если он там присутствует.
Возвращает результат удаления с сообщениями об ошибках и предупреждениями, а
также признак того, был ли файл в кэше на момент вызова метода. Используйте
метод в таких сценариях, как конвертация, инициируемая с веб-сервиса, но
фактически выполняемая в плагине Chronos, где кэш файлов требуется как способ
передачи содержимого файла после конвертации. Если известно, что операция по
конвертации уникальна и результат конвертации не будет нужен, то посредством
этого метода можно удалить содержимое файла из кэша файлов.  
[TryGetRequestAsync](M_Tessa_FileConverters_IFileConverter_TryGetRequestAsync.htm)|
Возвращает запрос на выполнение операции по конвертации заданной версии файла
в карточке или null, если параметры файла не найдены по идентификатору версии.
Используйте метод для физических файлов, информация по которым может быть
найдена по указанному идентификатору версии. Для виртуальных файлов создайте
объект запроса через конструктор [Tessa.FileConverters.FileConverterRequest].  
## __Методы расширения
[GetRequestOrThrowAsync](M_Tessa_FileConverters_FileConverterExtensions_GetRequestOrThrowAsync.htm)|
Возвращает запрос на выполнение операции по конвертации заданной версии файла
в карточке. Возвращаемое значение гарантированно не равно null. Если параметры
файла не найдены по идентификатору версии, то выбрасывается исключение.  
(Определяется
[FileConverterExtensions](T_Tessa_FileConverters_FileConverterExtensions.htm))  
---|---  
##  __См. также
#### Ссылки
[Tessa.FileConverters - пространство имён](N_Tessa_FileConverters.htm)