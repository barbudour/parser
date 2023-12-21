# IHostOperation<T> \- интерфейс
Описание интерфейса операции приложения Tessa Host
##  __Definition
 **Пространство имён:** [Tessa.Host](N_Tessa_Host.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IHostOperation<in T> : IDisposable
    where T : IHostOperationContext
VB __Копировать
     Public Interface IHostOperation(Of In T As IHostOperationContext)
    	Inherits IDisposable
C++ __Копировать
    generic<typename T>
    where T : IHostOperationContext
    public interface class IHostOperation : IDisposable
F# __Копировать
     type IHostOperation<'T when 'T : IHostOperationContext> = 
        interface
            interface IDisposable
        end
Implements
    [IDisposable](https://learn.microsoft.com/dotnet/api/system.idisposable)
#### Параметры типа
T
     Тип контекста выполнения операции 
## __Методы
[Dispose](https://learn.microsoft.com/dotnet/api/system.idisposable.dispose#system-
idisposable-dispose)| Performs application-defined tasks associated with
freeing, releasing, or resetting unmanaged resources.  
(Унаследован от
[IDisposable](https://learn.microsoft.com/dotnet/api/system.idisposable))  
---|---  
[Execute](M_Tessa_Host_IHostOperation_1_Execute.htm)|  Осуществляет выполнение
операции  
## __См. также
#### Ссылки
[Tessa.Host - пространство имён](N_Tessa_Host.htm)
