# IApplicationManagerServiceHost - интерфейс
Описание интерфейса для классов осуществляющих хостинг сервиса
предоставляемого диспетчером приложений, для запущенных экземпляров сервиса
приложений
## __Definition
 **Пространство имён:**
[Tessa.Applications.Services.ApplicationManager](N_Tessa_Applications_Services_ApplicationManager.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IApplicationManagerServiceHost : IAsyncDisposable, 
    	IDisposable
VB __Копировать
     Public Interface IApplicationManagerServiceHost
    	Inherits IAsyncDisposable, IDisposable
C++ __Копировать
     public interface class IApplicationManagerServiceHost : IAsyncDisposable, 
    	IDisposable
F# __Копировать
     type IApplicationManagerServiceHost = 
        interface
            interface IAsyncDisposable
            interface IDisposable
        end
Implements
    [IAsyncDisposable](https://learn.microsoft.com/dotnet/api/system.iasyncdisposable), [IDisposable](https://learn.microsoft.com/dotnet/api/system.idisposable)
##  __Свойства
[ServiceStarted](P_Tessa_Applications_Services_ApplicationManager_IApplicationManagerServiceHost_ServiceStarted.htm)|
Gets a value indicating whether Признак наличия запущенного экземпляра сервиса
приложений  
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
[StartServiceAsync](M_Tessa_Applications_Services_ApplicationManager_IApplicationManagerServiceHost_StartServiceAsync.htm)|
Осуществляет создание и запуск сервиса
[IApplicationManagerService](T_Tessa_Applications_Services_ApplicationManager_IApplicationManagerService.htm),
если сервис не был ранее запущен.  
[StopServiceAsync](M_Tessa_Applications_Services_ApplicationManager_IApplicationManagerServiceHost_StopServiceAsync.htm)|
Осуществляет прекращение работы сервиса
[IApplicationManagerService](T_Tessa_Applications_Services_ApplicationManager_IApplicationManagerService.htm),
если он был ранее запущен.  
## __См. также
#### Ссылки
[Tessa.Applications.Services.ApplicationManager - пространство
имён](N_Tessa_Applications_Services_ApplicationManager.htm)
