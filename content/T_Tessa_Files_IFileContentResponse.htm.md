# IFileContentResponse - интерфейс
Ответ на запрос на получение контента файла.
## __Definition
 **Пространство имён:** [Tessa.Files](N_Tessa_Files.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IFileContentResponse
VB __Копировать
     Public Interface IFileContentResponse
C++ __Копировать
     public interface class IFileContentResponse
F# __Копировать
     type IFileContentResponse = interface end
##  __Свойства
[Info](P_Tessa_Files_IFileContentResponse_Info.htm)|  Информация для
расширений. Информация может быть не сериализуемой. В стандартной реализации
[IFileSource] информация не используется.  
---|---  
[ResponseInfo](P_Tessa_Files_IFileContentResponse_ResponseInfo.htm)|  Данные,
которые были записаны из ответа на запрос response.Info, который получен от
сервера (в типовом сценарии).  
[SuggestedFileName](P_Tessa_Files_IFileContentResponse_SuggestedFileName.htm)|
Предпочитаемое название загруженного файла или null, если название не
изменяется относительно заданного в версии.  
[ValidationResult](P_Tessa_Files_IFileContentResponse_ValidationResult.htm)|
Результат валидации, отражающий произошедшие события и ошибки в процессе
выполнения запроса.  
[Version](P_Tessa_Files_IFileContentResponse_Version.htm)| Версия файла, для
которой был выполнен запрос.  
##  __См. также
#### Ссылки
[Tessa.Files - пространство имён](N_Tessa_Files.htm)
