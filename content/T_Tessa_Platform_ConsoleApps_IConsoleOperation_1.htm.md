# IConsoleOperation<TOperationContext> \- интерфейс
Описание интерфейса операции в консоли
## __Definition
 **Пространство имён:**
[Tessa.Platform.ConsoleApps](N_Tessa_Platform_ConsoleApps.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IConsoleOperation<in TOperationContext> : IAsyncDisposable
VB __Копировать
     Public Interface IConsoleOperation(Of In TOperationContext)
    	Inherits IAsyncDisposable
C++ __Копировать
    generic<typename TOperationContext>
    public interface class IConsoleOperation : IAsyncDisposable
F# __Копировать
     type IConsoleOperation<'TOperationContext> = 
        interface
            interface IAsyncDisposable
        end
Implements
    [IAsyncDisposable](https://learn.microsoft.com/dotnet/api/system.iasyncdisposable)
#### Параметры типа
TOperationContext
     Тип контекста операции 
## __Методы
[CloseAsync](M_Tessa_Platform_ConsoleApps_IConsoleOperation_1_CloseAsync.htm)|
Закрывает соединение с сервисом.  
---|---  
[DisposeAsync](https://learn.microsoft.com/dotnet/api/system.iasyncdisposable.disposeasync#system-
iasyncdisposable-disposeasync)| Performs application-defined tasks associated
with freeing, releasing, or resetting unmanaged resources asynchronously.  
(Унаследован от
[IAsyncDisposable](https://learn.microsoft.com/dotnet/api/system.iasyncdisposable))  
[ExecuteAsync](M_Tessa_Platform_ConsoleApps_IConsoleOperation_1_ExecuteAsync.htm)|
Осуществляет выполнение операции.  
[LoginAsync](M_Tessa_Platform_ConsoleApps_IConsoleOperation_1_LoginAsync.htm)|
Устанавливает соединение с сервисом.  
## __См. также
#### Ссылки
[Tessa.Platform.ConsoleApps - пространство
имён](N_Tessa_Platform_ConsoleApps.htm)
