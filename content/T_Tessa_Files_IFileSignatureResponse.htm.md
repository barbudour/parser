# IFileSignatureResponse - интерфейс
Ответ на запрос на получение коллекции доступных подписей для версии файла.
## __Definition
 **Пространство имён:** [Tessa.Files](N_Tessa_Files.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IFileSignatureResponse
VB __Копировать
     Public Interface IFileSignatureResponse
C++ __Копировать
     public interface class IFileSignatureResponse
F# __Копировать
     type IFileSignatureResponse = interface end
##  __Свойства
[AllowCaching](P_Tessa_Files_IFileSignatureResponse_AllowCaching.htm)|
Признак того, что полученный список подписей может быть сохранён для
последующего многократного использования.  
---|---  
[Signatures](P_Tessa_Files_IFileSignatureResponse_Signatures.htm)| Коллекция
подписей, доступных для версии файла.  
[ValidationResult](P_Tessa_Files_IFileSignatureResponse_ValidationResult.htm)|
Результат валидации, отражающий произошедшие события и ошибки в процессе
выполнения запроса.  
[Version](P_Tessa_Files_IFileSignatureResponse_Version.htm)| Версия файла, для
которой был выполнен запрос.  
##  __См. также
#### Ссылки
[Tessa.Files - пространство имён](N_Tessa_Files.htm)
