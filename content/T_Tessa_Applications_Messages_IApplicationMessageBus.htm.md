# IApplicationMessageBus - интерфейс
Описание интерфейса шины обработки сообщений
## __Definition
 **Пространство имён:**
[Tessa.Applications.Messages](N_Tessa_Applications_Messages.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IApplicationMessageBus : IAsyncDisposable, 
    	IDisposable
VB __Копировать
     Public Interface IApplicationMessageBus
    	Inherits IAsyncDisposable, IDisposable
C++ __Копировать
     public interface class IApplicationMessageBus : IAsyncDisposable, 
    	IDisposable
F# __Копировать
     type IApplicationMessageBus = 
        interface
            interface IAsyncDisposable
            interface IDisposable
        end
Implements
    [IAsyncDisposable](https://learn.microsoft.com/dotnet/api/system.iasyncdisposable), [IDisposable](https://learn.microsoft.com/dotnet/api/system.idisposable)
##  __Методы
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
[ProcessMessageAsync](M_Tessa_Applications_Messages_IApplicationMessageBus_ProcessMessageAsync.htm)|
Осуществляет обработку сообщения  
[RegisterAsync](M_Tessa_Applications_Messages_IApplicationMessageBus_RegisterAsync.htm)|
Выполняет регистрацию шины обработки сообщений в Tessa Applications  
[UnregisterAsync](M_Tessa_Applications_Messages_IApplicationMessageBus_UnregisterAsync.htm)|
Выполняет отмену регистрации приложения  
## __События
[MessageReceived](E_Tessa_Applications_Messages_IApplicationMessageBus_MessageReceived.htm)|
Событие, возникающее при получении сообщения  
---|---  
## __См. также
#### Ссылки
[Tessa.Applications.Messages - пространство
имён](N_Tessa_Applications_Messages.htm)
