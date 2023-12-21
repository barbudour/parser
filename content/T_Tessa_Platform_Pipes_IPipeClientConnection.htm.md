# IPipeClientConnection - интерфейс
Объект соединения клиента с сервером по каналу, по которому клиент может
отправлять сообщения серверу.
## __Definition
 **Пространство имён:** [Tessa.Platform.Pipes](N_Tessa_Platform_Pipes.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IPipeClientConnection : IAsyncDisposable, 
    	IDisposable
VB __Копировать
     Public Interface IPipeClientConnection
    	Inherits IAsyncDisposable, IDisposable
C++ __Копировать
     public interface class IPipeClientConnection : IAsyncDisposable, 
    	IDisposable
F# __Копировать
     type IPipeClientConnection = 
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
[SendAsync](M_Tessa_Platform_Pipes_IPipeClientConnection_SendAsync.htm)|
Отправляет сообщение серверу и получает ответ. Возвращаемый объект не равен
null.  
## __См. также
#### Ссылки
[Tessa.Platform.Pipes - пространство имён](N_Tessa_Platform_Pipes.htm)
