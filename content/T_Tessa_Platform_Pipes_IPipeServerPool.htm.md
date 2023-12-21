# IPipeServerPool - интерфейс
Пул серверов, который поддерживает сразу несколько соединений
[IPipeServer](T_Tessa_Platform_Pipes_IPipeServer.htm) с автоматическим
расширением количества соединений. Объект не является синглтоном, создавайте
экземпляр объекта для каждого пула соединений.
## __Definition
 **Пространство имён:** [Tessa.Platform.Pipes](N_Tessa_Platform_Pipes.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IPipeServerPool : IAsyncDisposable, 
    	IDisposable
VB __Копировать
     Public Interface IPipeServerPool
    	Inherits IAsyncDisposable, IDisposable
C++ __Копировать
     public interface class IPipeServerPool : IAsyncDisposable, 
    	IDisposable
F# __Копировать
     type IPipeServerPool = 
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
[StartListeningAsync](M_Tessa_Platform_Pipes_IPipeServerPool_StartListeningAsync.htm)|
Запускает прослушивание в пуле серверов.  
[StopListeningAsync](M_Tessa_Platform_Pipes_IPipeServerPool_StopListeningAsync.htm)|
Останавливает прослушивание в пуле серверов.  
## __См. также
#### Ссылки
[Tessa.Platform.Pipes - пространство имён](N_Tessa_Platform_Pipes.htm)
