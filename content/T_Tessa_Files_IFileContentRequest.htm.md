# IFileContentRequest - интерфейс
Запрос на загрузку содержимого файла.
## __Definition
 **Пространство имён:** [Tessa.Files](N_Tessa_Files.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IFileContentRequest
VB __Копировать
     Public Interface IFileContentRequest
C++ __Копировать
     public interface class IFileContentRequest
F# __Копировать
     type IFileContentRequest = interface end
##  __Свойства
[Info](P_Tessa_Files_IFileContentRequest_Info.htm)|  Информация для
расширений. Информация может быть не сериализуемой. В стандартной реализации
[IFileSource] информация не используется.  
---|---  
[ProcessContentActionAsync](P_Tessa_Files_IFileContentRequest_ProcessContentActionAsync.htm)|
Метод, которому передаётся полученный из внешней подсистемы контент и который
должен его обработать, например, записать в локальный кэш. Если при загрузке
происходит ошибка, то метод может быть ни разу не вызван. Делегат может быть
равен null.  
[RequestInfo](P_Tessa_Files_IFileContentRequest_RequestInfo.htm)|
Сериализуемые данные, которые будут записаны в объект запроса request.Info,
отправляемый к серверу (в типовом сценарии). Такие данные могут перезаписать
данные из [IFileObject.RequestInfo].  
[Version](P_Tessa_Files_IFileContentRequest_Version.htm)| Версия файла, для
которой требуется получить контент.  
##  __См. также
#### Ссылки
[Tessa.Files - пространство имён](N_Tessa_Files.htm)
