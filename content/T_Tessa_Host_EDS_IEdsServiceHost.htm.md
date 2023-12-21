# IEdsServiceHost - интерфейс
Объект, управляющий сервисом подписания ЭП и проверки подписи, который
располагается в отдельном процессе.
## __Definition
 **Пространство имён:** [Tessa.Host.EDS](N_Tessa_Host_EDS.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IEdsServiceHost : IAsyncDisposable, 
    	IDisposable
VB __Копировать
     Public Interface IEdsServiceHost
    	Inherits IAsyncDisposable, IDisposable
C++ __Копировать
     public interface class IEdsServiceHost : IAsyncDisposable, 
    	IDisposable
F# __Копировать
     type IEdsServiceHost = 
        interface
            interface IAsyncDisposable
            interface IDisposable
        end
Implements
    [IAsyncDisposable](https://learn.microsoft.com/dotnet/api/system.iasyncdisposable), [IDisposable](https://learn.microsoft.com/dotnet/api/system.idisposable)
##  __Свойства
[ServiceStarted](P_Tessa_Host_EDS_IEdsServiceHost_ServiceStarted.htm)|
Признак того, что сервис запущен.  
---|---  
## __Методы
[Dispose](https://learn.microsoft.com/dotnet/api/system.idisposable.dispose#system-
idisposable-dispose)| Performs application-defined tasks associated with
freeing, releasing, or resetting unmanaged resources.  
(Унаследован от
[IDisposable](https://learn.microsoft.com/dotnet/api/system.idisposable))  
---|---  
[DisposeAsync](https://learn.microsoft.com/dotnet/api/system.iasyncdisposable.disposeasync#system-
iasyncdisposable-disposeasync)| Performs application-defined tasks associated
with freeing, releasing, or resetting unmanaged resources asynchronously.  
(Унаследован от
[IAsyncDisposable](https://learn.microsoft.com/dotnet/api/system.iasyncdisposable))  
[StartServiceAsync](M_Tessa_Host_EDS_IEdsServiceHost_StartServiceAsync.htm)|
Запускает сервис в отдельном процессе.  
[StopServiceAsync](M_Tessa_Host_EDS_IEdsServiceHost_StopServiceAsync.htm)|
Останавливает сервис в отдельном процессе.  
## __См. также
#### Ссылки
[Tessa.Host.EDS - пространство имён](N_Tessa_Host_EDS.htm)
