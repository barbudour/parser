# IWorkflowEngineLogger - интерфейс
Логгер процессов в Workflow Engine
## __Definition
 **Пространство имён:** [Tessa.Workflow](N_Tessa_Workflow.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IWorkflowEngineLogger : IAsyncDisposable
VB __Копировать
     Public Interface IWorkflowEngineLogger
    	Inherits IAsyncDisposable
C++ __Копировать
     public interface class IWorkflowEngineLogger : IAsyncDisposable
F# __Копировать
     type IWorkflowEngineLogger = 
        interface
            interface IAsyncDisposable
        end
Implements
    [IAsyncDisposable](https://learn.microsoft.com/dotnet/api/system.iasyncdisposable)
##  __Методы
[DisposeAsync](https://learn.microsoft.com/dotnet/api/system.iasyncdisposable.disposeasync#system-
iasyncdisposable-disposeasync)| Performs application-defined tasks associated
with freeing, releasing, or resetting unmanaged resources asynchronously.  
(Унаследован от
[IAsyncDisposable](https://learn.microsoft.com/dotnet/api/system.iasyncdisposable))  
---|---  
[LogAsync](M_Tessa_Workflow_IWorkflowEngineLogger_LogAsync.htm)|  Метод для
записи лога WorkflowEngine  
## __См. также
#### Ссылки
[Tessa.Workflow - пространство имён](N_Tessa_Workflow.htm)
