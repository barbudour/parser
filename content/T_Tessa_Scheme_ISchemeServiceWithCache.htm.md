# ISchemeServiceWithCache - интерфейс
##  __Definition
 **Пространство имён:** [Tessa.Scheme](N_Tessa_Scheme.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface ISchemeServiceWithCache : ISchemeService
VB __Копировать
     Public Interface ISchemeServiceWithCache
    	Inherits ISchemeService
C++ __Копировать
     public interface class ISchemeServiceWithCache : ISchemeService
F# __Копировать
     type ISchemeServiceWithCache = 
        interface
            interface ISchemeService
        end
Implements
    [ISchemeService](T_Tessa_Scheme_ISchemeService.htm)
##  __Методы
[EnsureInvalidateCacheSubscribedAsync](M_Tessa_Scheme_ISchemeServiceWithCache_EnsureInvalidateCacheSubscribedAsync.htm)|
Производит подписку на событие сброса кэша, если необходимо.  
---|---  
[GetDatabasePropertiesAsync](M_Tessa_Scheme_ISchemeService_GetDatabasePropertiesAsync.htm)|  
(Унаследован от [ISchemeService](T_Tessa_Scheme_ISchemeService.htm))  
[GetFunctionAsync(Guid,
CancellationToken)](M_Tessa_Scheme_ISchemeService_GetFunctionAsync.htm)|  
(Унаследован от [ISchemeService](T_Tessa_Scheme_ISchemeService.htm))  
[GetFunctionAsync(String,
CancellationToken)](M_Tessa_Scheme_ISchemeService_GetFunctionAsync_1.htm)|  
(Унаследован от [ISchemeService](T_Tessa_Scheme_ISchemeService.htm))  
[GetFunctionsAsync](M_Tessa_Scheme_ISchemeService_GetFunctionsAsync.htm)|  
(Унаследован от [ISchemeService](T_Tessa_Scheme_ISchemeService.htm))  
[GetMigrationAsync(Guid,
CancellationToken)](M_Tessa_Scheme_ISchemeService_GetMigrationAsync.htm)|  
(Унаследован от [ISchemeService](T_Tessa_Scheme_ISchemeService.htm))  
[GetMigrationAsync(String,
CancellationToken)](M_Tessa_Scheme_ISchemeService_GetMigrationAsync_1.htm)|  
(Унаследован от [ISchemeService](T_Tessa_Scheme_ISchemeService.htm))  
[GetMigrationsAsync](M_Tessa_Scheme_ISchemeService_GetMigrationsAsync.htm)|  
(Унаследован от [ISchemeService](T_Tessa_Scheme_ISchemeService.htm))  
[GetPartitionAsync(Guid,
CancellationToken)](M_Tessa_Scheme_ISchemeService_GetPartitionAsync.htm)|  
(Унаследован от [ISchemeService](T_Tessa_Scheme_ISchemeService.htm))  
[GetPartitionAsync(String,
CancellationToken)](M_Tessa_Scheme_ISchemeService_GetPartitionAsync_1.htm)|  
(Унаследован от [ISchemeService](T_Tessa_Scheme_ISchemeService.htm))  
[GetPartitionsAsync](M_Tessa_Scheme_ISchemeService_GetPartitionsAsync.htm)|  
(Унаследован от [ISchemeService](T_Tessa_Scheme_ISchemeService.htm))  
[GetProcedureAsync(Guid,
CancellationToken)](M_Tessa_Scheme_ISchemeService_GetProcedureAsync.htm)|  
(Унаследован от [ISchemeService](T_Tessa_Scheme_ISchemeService.htm))  
[GetProcedureAsync(String,
CancellationToken)](M_Tessa_Scheme_ISchemeService_GetProcedureAsync_1.htm)|  
(Унаследован от [ISchemeService](T_Tessa_Scheme_ISchemeService.htm))  
[GetProceduresAsync](M_Tessa_Scheme_ISchemeService_GetProceduresAsync.htm)|  
(Унаследован от [ISchemeService](T_Tessa_Scheme_ISchemeService.htm))  
[GetTableAsync(Guid,
CancellationToken)](M_Tessa_Scheme_ISchemeService_GetTableAsync.htm)|  
(Унаследован от [ISchemeService](T_Tessa_Scheme_ISchemeService.htm))  
[GetTableAsync(String,
CancellationToken)](M_Tessa_Scheme_ISchemeService_GetTableAsync_1.htm)|  
(Унаследован от [ISchemeService](T_Tessa_Scheme_ISchemeService.htm))  
[GetTablesAsync](M_Tessa_Scheme_ISchemeService_GetTablesAsync.htm)|  
(Унаследован от [ISchemeService](T_Tessa_Scheme_ISchemeService.htm))  
[InvalidateCacheAsync](M_Tessa_Scheme_ISchemeServiceWithCache_InvalidateCacheAsync.htm)|
Инициирует сброс кэша.  
[InvalidateCacheIfChangedAsync](M_Tessa_Scheme_ISchemeServiceWithCache_InvalidateCacheIfChangedAsync.htm)|
Инициирует сброс кэша в случае, если есть изменения.  
[RemoveFunctionAsync](M_Tessa_Scheme_ISchemeService_RemoveFunctionAsync.htm)|  
(Унаследован от [ISchemeService](T_Tessa_Scheme_ISchemeService.htm))  
[RemoveMigrationAsync](M_Tessa_Scheme_ISchemeService_RemoveMigrationAsync.htm)|  
(Унаследован от [ISchemeService](T_Tessa_Scheme_ISchemeService.htm))  
[RemovePartitionAsync](M_Tessa_Scheme_ISchemeService_RemovePartitionAsync.htm)|  
(Унаследован от [ISchemeService](T_Tessa_Scheme_ISchemeService.htm))  
[RemoveProcedureAsync](M_Tessa_Scheme_ISchemeService_RemoveProcedureAsync.htm)|  
(Унаследован от [ISchemeService](T_Tessa_Scheme_ISchemeService.htm))  
[RemoveTableAsync](M_Tessa_Scheme_ISchemeService_RemoveTableAsync.htm)|  
(Унаследован от [ISchemeService](T_Tessa_Scheme_ISchemeService.htm))  
[SaveDatabasePropertiesAsync](M_Tessa_Scheme_ISchemeService_SaveDatabasePropertiesAsync.htm)|  
(Унаследован от [ISchemeService](T_Tessa_Scheme_ISchemeService.htm))  
[SaveFunctionAsync](M_Tessa_Scheme_ISchemeService_SaveFunctionAsync.htm)|  
(Унаследован от [ISchemeService](T_Tessa_Scheme_ISchemeService.htm))  
[SaveMigrationAsync](M_Tessa_Scheme_ISchemeService_SaveMigrationAsync.htm)|  
(Унаследован от [ISchemeService](T_Tessa_Scheme_ISchemeService.htm))  
[SavePartitionAsync](M_Tessa_Scheme_ISchemeService_SavePartitionAsync.htm)|  
(Унаследован от [ISchemeService](T_Tessa_Scheme_ISchemeService.htm))  
[SaveProcedureAsync](M_Tessa_Scheme_ISchemeService_SaveProcedureAsync.htm)|  
(Унаследован от [ISchemeService](T_Tessa_Scheme_ISchemeService.htm))  
[SaveTableAsync](M_Tessa_Scheme_ISchemeService_SaveTableAsync.htm)|  
(Унаследован от [ISchemeService](T_Tessa_Scheme_ISchemeService.htm))  
##  __Методы расширения
[ValidateAsync](M_Tessa_UI_Cards_CardUIExtensions_ValidateAsync_3.htm)|
Выполняет проверку наличия таблицы с идентификатором tableID в схеме.  
(Определяется [CardUIExtensions](T_Tessa_UI_Cards_CardUIExtensions.htm))  
---|---  
[ValidateAsync](M_Tessa_UI_Cards_CardUIExtensions_ValidateAsync_2.htm)|
Выполняет проверку наличия колонки с идентификатором columnID в таблице с
идентификатором tableID.  
(Определяется [CardUIExtensions](T_Tessa_UI_Cards_CardUIExtensions.htm))  
##  __См. также
#### Ссылки
[Tessa.Scheme - пространство имён](N_Tessa_Scheme.htm)
