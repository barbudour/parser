# ITessaApplicationServiceHost - интерфейс
Описание интерфейса для объектов осуществляющих размещение сервиса
платформенного приложения осуществляющего взаимодействие с диспетчером
приложений.
## __Definition
 **Пространство имён:**
[Tessa.Applications.Services.PlatformApplication](N_Tessa_Applications_Services_PlatformApplication.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface ITessaApplicationServiceHost : IAsyncDisposable, 
    	IDisposable
VB __Копировать
     Public Interface ITessaApplicationServiceHost
    	Inherits IAsyncDisposable, IDisposable
C++ __Копировать
     public interface class ITessaApplicationServiceHost : IAsyncDisposable, 
    	IDisposable
F# __Копировать
     type ITessaApplicationServiceHost = 
        interface
            interface IAsyncDisposable
            interface IDisposable
        end
Implements
    [IAsyncDisposable](https://learn.microsoft.com/dotnet/api/system.iasyncdisposable), [IDisposable](https://learn.microsoft.com/dotnet/api/system.idisposable)
##  __Свойства
[ServiceAddress](P_Tessa_Applications_Services_PlatformApplication_ITessaApplicationServiceHost_ServiceAddress.htm)|
Gets Адрес сервиса по которому диспетчер приложений может отправлять
экземпляру приложений сообщения.  
---|---  
[ServiceStarted](P_Tessa_Applications_Services_PlatformApplication_ITessaApplicationServiceHost_ServiceStarted.htm)|
Gets a value indicating whether Признак нахождения сервиса в запущенном
состоянии  
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
[StartServiceAsync](M_Tessa_Applications_Services_PlatformApplication_ITessaApplicationServiceHost_StartServiceAsync.htm)|
Запускает сервис приложения, если он ещё не запущен  
[StopServiceAsync](M_Tessa_Applications_Services_PlatformApplication_ITessaApplicationServiceHost_StopServiceAsync.htm)|
Останавливает сервис приложения, если он запущен  
## __См. также
#### Ссылки
[Tessa.Applications.Services.PlatformApplication - пространство
имён](N_Tessa_Applications_Services_PlatformApplication.htm)
