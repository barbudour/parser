# IApplicationServiceHost - интерфейс
##  __Definition
 **Пространство имён:**
[Tessa.Applications.Services.TessaServer](N_Tessa_Applications_Services_TessaServer.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IApplicationServiceHost
VB __Копировать
     Public Interface IApplicationServiceHost
C++ __Копировать
     public interface class IApplicationServiceHost
F# __Копировать
     type IApplicationServiceHost = interface end
##  __Свойства
[OnDownloadStreamDisposedActionAsync](P_Tessa_Applications_Services_TessaServer_IApplicationServiceHost_OnDownloadStreamDisposedActionAsync.htm)|
Делегат, выполняемый при освобождении потока, возвращаемого в методе
[DownloadAsync(ApplicationDownloadRequest, ApplicationDownloadFlags,
CancellationToken)](M_Tessa_Applications_Services_TessaServer_IApplicationService_DownloadAsync.htm),
или null, если делегат отсутствует.  
---|---  
[ServiceStarted](P_Tessa_Applications_Services_TessaServer_IApplicationServiceHost_ServiceStarted.htm)|
Признак нахождения сервиса в запущенном состоянии  
## __Методы
[StartServiceAsync](M_Tessa_Applications_Services_TessaServer_IApplicationServiceHost_StartServiceAsync.htm)|
Запускает сервис приложения, если он ещё не запущен  
---|---  
[StopServiceAsync](M_Tessa_Applications_Services_TessaServer_IApplicationServiceHost_StopServiceAsync.htm)|
Останавливает сервис приложения, если он запущен  
## __См. также
#### Ссылки
[Tessa.Applications.Services.TessaServer - пространство
имён](N_Tessa_Applications_Services_TessaServer.htm)
