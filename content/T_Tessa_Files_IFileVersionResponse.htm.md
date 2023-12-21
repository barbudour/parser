# IFileVersionResponse - интерфейс
Ответ на запрос на получение коллекции доступных версий файла.
## __Definition
 **Пространство имён:** [Tessa.Files](N_Tessa_Files.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IFileVersionResponse
VB __Копировать
     Public Interface IFileVersionResponse
C++ __Копировать
     public interface class IFileVersionResponse
F# __Копировать
     type IFileVersionResponse = interface end
##  __Свойства
[AllowCaching](P_Tessa_Files_IFileVersionResponse_AllowCaching.htm)|  Признак
того, что полученный список версий может быть сохранён для последующего
многократного использования.  
---|---  
[File](P_Tessa_Files_IFileVersionResponse_File.htm)| Файл, для которого был
выполнен запрос.  
[ValidationResult](P_Tessa_Files_IFileVersionResponse_ValidationResult.htm)|
Результат валидации, отражающий произошедшие события и ошибки в процессе
выполнения запроса.  
[Versions](P_Tessa_Files_IFileVersionResponse_Versions.htm)| Коллекция версий,
доступных для файла.  
##  __См. также
#### Ссылки
[Tessa.Files - пространство имён](N_Tessa_Files.htm)
