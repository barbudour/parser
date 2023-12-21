# IQueryExecutorResultWriter - интерфейс
Интерфейс объектов осуществляющих создание данных ITessaViewResult
## __Definition
 **Пространство имён:** [Tessa.Views](N_Tessa_Views.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IQueryExecutorResultWriter : IDisposable
VB __Копировать
     Public Interface IQueryExecutorResultWriter
    	Inherits IDisposable
C++ __Копировать
     public interface class IQueryExecutorResultWriter : IDisposable
F# __Копировать
     type IQueryExecutorResultWriter = 
        interface
            interface IDisposable
        end
Implements
    [IDisposable](https://learn.microsoft.com/dotnet/api/system.idisposable)
##  __Методы
[Dispose](https://learn.microsoft.com/dotnet/api/system.idisposable.dispose#system-
idisposable-dispose)| Performs application-defined tasks associated with
freeing, releasing, or resetting unmanaged resources.  
(Унаследован от
[IDisposable](https://learn.microsoft.com/dotnet/api/system.idisposable))  
---|---  
[WriteColumns](M_Tessa_Views_IQueryExecutorResultWriter_WriteColumns.htm)|
Осуществляет запись списка столбцов  
[WriteDataTypes](M_Tessa_Views_IQueryExecutorResultWriter_WriteDataTypes.htm)|
Осуществляет запись списка типов данных  
[WriteExpiredByTimeOut](M_Tessa_Views_IQueryExecutorResultWriter_WriteExpiredByTimeOut.htm)|
Осуществляет запись признака наличия таймаута  
[WriteRow](M_Tessa_Views_IQueryExecutorResultWriter_WriteRow.htm)|
Осуществляет запись строки данных  
## __См. также
#### Ссылки
[Tessa.Views - пространство имён](N_Tessa_Views.htm)
