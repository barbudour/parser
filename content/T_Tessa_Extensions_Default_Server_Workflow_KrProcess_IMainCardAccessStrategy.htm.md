# IMainCardAccessStrategy - интерфейс
Описывает стратегию доступа к карточке.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Server.Workflow.KrProcess](N_Tessa_Extensions_Default_Server_Workflow_KrProcess.htm)  
 **Сборка:** Tessa.Extensions.Default.Server (в
Tessa.Extensions.Default.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IMainCardAccessStrategy : IAsyncDisposable
VB __Копировать
     Public Interface IMainCardAccessStrategy
    	Inherits IAsyncDisposable
C++ __Копировать
     public interface class IMainCardAccessStrategy : IAsyncDisposable
F# __Копировать
     type IMainCardAccessStrategy = 
        interface
            interface IAsyncDisposable
        end
Implements
    [IAsyncDisposable](https://learn.microsoft.com/dotnet/api/system.iasyncdisposable)
##  __Свойства
[WasFileContainerUsed](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_IMainCardAccessStrategy_WasFileContainerUsed.htm)|
Возвращает признак использования файлового контейнера.  
---|---  
[WasUsed](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_IMainCardAccessStrategy_WasUsed.htm)|
Признак того, что стратегия использовалась, т.е. вызывались методы доступа к
карточке.  
## __Методы
[DisposeAsync](https://learn.microsoft.com/dotnet/api/system.iasyncdisposable.disposeasync#system-
iasyncdisposable-disposeasync)| Performs application-defined tasks associated
with freeing, releasing, or resetting unmanaged resources asynchronously.  
(Унаследован от
[IAsyncDisposable](https://learn.microsoft.com/dotnet/api/system.iasyncdisposable))  
---|---  
[EnsureTaskHistoryLoadedAsync](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_IMainCardAccessStrategy_EnsureTaskHistoryLoadedAsync.htm)|
Загрузка (при необходимости) истории заданий в карточку в соответствии с
правилами стратегии.  
[GetCardAsync](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_IMainCardAccessStrategy_GetCardAsync.htm)|
Получение объекта карточки в соответствии с правилами стратегии.  
[GetFileContainerAsync](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_IMainCardAccessStrategy_GetFileContainerAsync.htm)|
Возвращает файловый контейнер карточки полученный в соответствии с правилами
стратегии.  
## __См. также
#### Ссылки
[Tessa.Extensions.Default.Server.Workflow.KrProcess - пространство
имён](N_Tessa_Extensions_Default_Server_Workflow_KrProcess.htm)
