# IApplicationService - интерфейс
Сервис для инициализации приложения с передачей приложению всех данных,
требуемых для его работы.
## __Definition
 **Пространство имён:**
[Tessa.Applications.Services.TessaServer](N_Tessa_Applications_Services_TessaServer.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IApplicationService
VB __Копировать
     Public Interface IApplicationService
C++ __Копировать
     public interface class IApplicationService
F# __Копировать
     type IApplicationService = interface end
##  __Методы
[DownloadAsync](M_Tessa_Applications_Services_TessaServer_IApplicationService_DownloadAsync.htm)|
Операция скачивания приложения.  
---|---  
[GetApplicationsAsync](M_Tessa_Applications_Services_TessaServer_IApplicationService_GetApplicationsAsync.htm)|
Возвращает список всех приложений, доступных пользователю.  
[GetDownloadReaderFlags](M_Tessa_Applications_Services_TessaServer_IApplicationService_GetDownloadReaderFlags.htm)|
Возвращает флаги, которые необходимо добавить при чтении пакета посредством
[ApplicationPackageReader](T_Tessa_Applications_Synchronization_ApplicationPackageReader.htm)
из потока, полученного в результате десериализации
[DownloadAsync(ApplicationDownloadRequest, ApplicationDownloadFlags,
CancellationToken)](M_Tessa_Applications_Services_TessaServer_IApplicationService_DownloadAsync.htm).
Обычно это флаг
[PackageBinarySerialization](T_Tessa_Applications_Services_TessaServer_ApplicationDownloadFlags.htm)
при подключении к веб-сервису предыдущей версии платформы. Со стороны сервера
всегда возвращает
[None](T_Tessa_Applications_Services_TessaServer_ApplicationDownloadFlags.htm).  
[TryGetApplicationIdAsync](M_Tessa_Applications_Services_TessaServer_IApplicationService_TryGetApplicationIdAsync.htm)|
Осуществляет попытку получения идентификатора приложения по его алиасу.  
[TryGetFaultedResultAsync](M_Tessa_Applications_Services_TessaServer_IApplicationService_TryGetFaultedResultAsync.htm)|
Возвращает ошибки при скачивании приложения как объект
[ValidationResult](T_Tessa_Platform_Validation_ValidationResult.htm) или null,
если информация недоступна: ошибок не было или пользователь не имеет доступа к
этой записи в истории.  
[TryGetModifiedAsync](M_Tessa_Applications_Services_TessaServer_IApplicationService_TryGetModifiedAsync.htm)|
Возвращает дату изменения приложения и признак того, что приложение является
64-битным.  
## __См. также
#### Ссылки
[Tessa.Applications.Services.TessaServer - пространство
имён](N_Tessa_Applications_Services_TessaServer.htm)
