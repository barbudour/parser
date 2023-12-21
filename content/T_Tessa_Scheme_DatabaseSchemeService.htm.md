# DatabaseSchemeService - класс
##  __Definition
 **Пространство имён:** [Tessa.Scheme](N_Tessa_Scheme.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class DatabaseSchemeService : SystemSchemeService
VB __Копировать
     Public NotInheritable Class DatabaseSchemeService
    	Inherits SystemSchemeService
C++ __Копировать
     public ref class DatabaseSchemeService sealed : public SystemSchemeService
F# __Копировать
     [<SealedAttribute>]
    type DatabaseSchemeService = 
        class
            inherit SystemSchemeService
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[SystemSchemeService](T_Tessa_Scheme_SystemSchemeService.htm) __ DatabaseSchemeService
##  __Конструкторы
[DatabaseSchemeService](M_Tessa_Scheme_DatabaseSchemeService__ctor.htm)|
Инициализирует новый экземпляр класса DatabaseSchemeService  
---|---  
##  __Свойства
[DbScope](P_Tessa_Scheme_DatabaseSchemeService_DbScope.htm)|  Объект для
взаимодействия с базой данных, используемый текущим сервисом.  
---|---  
[Options](P_Tessa_Scheme_SystemSchemeService_Options.htm)|  
(Унаследован от [SystemSchemeService](T_Tessa_Scheme_SystemSchemeService.htm))  
[ServiceVersion](P_Tessa_Scheme_SystemSchemeService_ServiceVersion.htm)|  
(Унаследован от [SystemSchemeService](T_Tessa_Scheme_SystemSchemeService.htm))  
##  __Методы
[CheckIsNotNull](M_Tessa_Scheme_SystemSchemeService_CheckIsNotNull.htm)|  
(Унаследован от [SystemSchemeService](T_Tessa_Scheme_SystemSchemeService.htm))  
---|---  
[CheckIsNotReadOnly](M_Tessa_Scheme_SystemSchemeService_CheckIsNotReadOnly.htm)|  
(Унаследован от [SystemSchemeService](T_Tessa_Scheme_SystemSchemeService.htm))  
[CreateException](M_Tessa_Scheme_SystemSchemeService_CreateException.htm)|  
(Унаследован от [SystemSchemeService](T_Tessa_Scheme_SystemSchemeService.htm))  
[CreateOperationScope](M_Tessa_Scheme_SystemSchemeService_CreateOperationScope.htm)|  
(Унаследован от [SystemSchemeService](T_Tessa_Scheme_SystemSchemeService.htm))  
[CreateOperationScopeOverride](M_Tessa_Scheme_DatabaseSchemeService_CreateOperationScopeOverride.htm)|  
(Переопределяет [SystemSchemeService.CreateOperationScopeOverride(String,
SchemeObject)](M_Tessa_Scheme_SystemSchemeService_CreateOperationScopeOverride.htm))  
[CreateStorageAsync](M_Tessa_Scheme_SystemSchemeService_CreateStorageAsync.htm)|  
(Унаследован от [SystemSchemeService](T_Tessa_Scheme_SystemSchemeService.htm))  
[CreateStorageOverrideAsync](M_Tessa_Scheme_DatabaseSchemeService_CreateStorageOverrideAsync.htm)|  
(Переопределяет
[SystemSchemeService.CreateStorageOverrideAsync(CancellationToken)](M_Tessa_Scheme_SystemSchemeService_CreateStorageOverrideAsync.htm))  
[EnsureInvalidateCacheSubscribedAsync](M_Tessa_Scheme_DatabaseSchemeService_EnsureInvalidateCacheSubscribedAsync.htm)|
Производит подписку на событие сброса кэша, если необходимо.  
(Переопределяет
[SystemSchemeService.EnsureInvalidateCacheSubscribedAsync(CancellationToken)](M_Tessa_Scheme_SystemSchemeService_EnsureInvalidateCacheSubscribedAsync.htm))  
[Equals](https://learn.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\))| Determines whether the specified object is
equal to the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[Finalize](https://learn.microsoft.com/dotnet/api/system.object.finalize#system-
object-finalize)| Allows an object to try to free resources and perform other
cleanup operations before it is reclaimed by garbage collection.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetDatabasePropertiesAsync](M_Tessa_Scheme_SystemSchemeService_GetDatabasePropertiesAsync.htm)|  
(Унаследован от [SystemSchemeService](T_Tessa_Scheme_SystemSchemeService.htm))  
[GetDatabasePropertiesOverrideAsync](M_Tessa_Scheme_DatabaseSchemeService_GetDatabasePropertiesOverrideAsync.htm)|  
(Переопределяет
[SystemSchemeService.GetDatabasePropertiesOverrideAsync(CancellationToken)](M_Tessa_Scheme_SystemSchemeService_GetDatabasePropertiesOverrideAsync.htm))  
[GetDbmsVersionQuery](M_Tessa_Scheme_DatabaseSchemeService_GetDbmsVersionQuery.htm)|  
[GetFunctionAsync(Guid,
CancellationToken)](M_Tessa_Scheme_SystemSchemeService_GetFunctionAsync.htm)|  
(Унаследован от [SystemSchemeService](T_Tessa_Scheme_SystemSchemeService.htm))  
[GetFunctionAsync(String,
CancellationToken)](M_Tessa_Scheme_SystemSchemeService_GetFunctionAsync_1.htm)|  
(Унаследован от [SystemSchemeService](T_Tessa_Scheme_SystemSchemeService.htm))  
[GetFunctionOverrideAsync(Guid,
CancellationToken)](M_Tessa_Scheme_DatabaseSchemeService_GetFunctionOverrideAsync.htm)|  
(Переопределяет [SystemSchemeService.GetFunctionOverrideAsync(Guid,
CancellationToken)](M_Tessa_Scheme_SystemSchemeService_GetFunctionOverrideAsync.htm))  
[GetFunctionOverrideAsync(String,
CancellationToken)](M_Tessa_Scheme_DatabaseSchemeService_GetFunctionOverrideAsync_1.htm)|  
(Переопределяет [SystemSchemeService.GetFunctionOverrideAsync(String,
CancellationToken)](M_Tessa_Scheme_SystemSchemeService_GetFunctionOverrideAsync_1.htm))  
[GetFunctionsAsync](M_Tessa_Scheme_SystemSchemeService_GetFunctionsAsync.htm)|  
(Унаследован от [SystemSchemeService](T_Tessa_Scheme_SystemSchemeService.htm))  
[GetFunctionsOverrideAsync](M_Tessa_Scheme_DatabaseSchemeService_GetFunctionsOverrideAsync.htm)|  
(Переопределяет
[SystemSchemeService.GetFunctionsOverrideAsync(CancellationToken)](M_Tessa_Scheme_SystemSchemeService_GetFunctionsOverrideAsync.htm))  
[GetFunctionsQuery](M_Tessa_Scheme_DatabaseSchemeService_GetFunctionsQuery.htm)|  
[GetHashCode](https://learn.microsoft.com/dotnet/api/system.object.gethashcode#system-
object-gethashcode)| Serves as the default hash function.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetMigrationAsync(Guid,
CancellationToken)](M_Tessa_Scheme_SystemSchemeService_GetMigrationAsync.htm)|  
(Унаследован от [SystemSchemeService](T_Tessa_Scheme_SystemSchemeService.htm))  
[GetMigrationAsync(String,
CancellationToken)](M_Tessa_Scheme_SystemSchemeService_GetMigrationAsync_1.htm)|  
(Унаследован от [SystemSchemeService](T_Tessa_Scheme_SystemSchemeService.htm))  
[GetMigrationOverrideAsync(Guid,
CancellationToken)](M_Tessa_Scheme_DatabaseSchemeService_GetMigrationOverrideAsync.htm)|  
(Переопределяет [SystemSchemeService.GetMigrationOverrideAsync(Guid,
CancellationToken)](M_Tessa_Scheme_SystemSchemeService_GetMigrationOverrideAsync.htm))  
[GetMigrationOverrideAsync(String,
CancellationToken)](M_Tessa_Scheme_DatabaseSchemeService_GetMigrationOverrideAsync_1.htm)|  
(Переопределяет [SystemSchemeService.GetMigrationOverrideAsync(String,
CancellationToken)](M_Tessa_Scheme_SystemSchemeService_GetMigrationOverrideAsync_1.htm))  
[GetMigrationsAsync](M_Tessa_Scheme_SystemSchemeService_GetMigrationsAsync.htm)|  
(Унаследован от [SystemSchemeService](T_Tessa_Scheme_SystemSchemeService.htm))  
[GetMigrationsOverrideAsync](M_Tessa_Scheme_DatabaseSchemeService_GetMigrationsOverrideAsync.htm)|  
(Переопределяет
[SystemSchemeService.GetMigrationsOverrideAsync(CancellationToken)](M_Tessa_Scheme_SystemSchemeService_GetMigrationsOverrideAsync.htm))  
[GetMigrationsQuery](M_Tessa_Scheme_DatabaseSchemeService_GetMigrationsQuery.htm)|  
[GetPartitionAsync(Guid,
CancellationToken)](M_Tessa_Scheme_SystemSchemeService_GetPartitionAsync.htm)|  
(Унаследован от [SystemSchemeService](T_Tessa_Scheme_SystemSchemeService.htm))  
[GetPartitionAsync(String,
CancellationToken)](M_Tessa_Scheme_SystemSchemeService_GetPartitionAsync_1.htm)|  
(Унаследован от [SystemSchemeService](T_Tessa_Scheme_SystemSchemeService.htm))  
[GetPartitionOverrideAsync(Guid,
CancellationToken)](M_Tessa_Scheme_DatabaseSchemeService_GetPartitionOverrideAsync.htm)|  
(Переопределяет [SystemSchemeService.GetPartitionOverrideAsync(Guid,
CancellationToken)](M_Tessa_Scheme_SystemSchemeService_GetPartitionOverrideAsync.htm))  
[GetPartitionOverrideAsync(String,
CancellationToken)](M_Tessa_Scheme_DatabaseSchemeService_GetPartitionOverrideAsync_1.htm)|  
(Переопределяет [SystemSchemeService.GetPartitionOverrideAsync(String,
CancellationToken)](M_Tessa_Scheme_SystemSchemeService_GetPartitionOverrideAsync_1.htm))  
[GetPartitionsAsync](M_Tessa_Scheme_SystemSchemeService_GetPartitionsAsync.htm)|  
(Унаследован от [SystemSchemeService](T_Tessa_Scheme_SystemSchemeService.htm))  
[GetPartitionsOverrideAsync](M_Tessa_Scheme_DatabaseSchemeService_GetPartitionsOverrideAsync.htm)|  
(Переопределяет
[SystemSchemeService.GetPartitionsOverrideAsync(CancellationToken)](M_Tessa_Scheme_SystemSchemeService_GetPartitionsOverrideAsync.htm))  
[GetPartitionsQuery](M_Tessa_Scheme_DatabaseSchemeService_GetPartitionsQuery.htm)|  
[GetProcedureAsync(Guid,
CancellationToken)](M_Tessa_Scheme_SystemSchemeService_GetProcedureAsync.htm)|  
(Унаследован от [SystemSchemeService](T_Tessa_Scheme_SystemSchemeService.htm))  
[GetProcedureAsync(String,
CancellationToken)](M_Tessa_Scheme_SystemSchemeService_GetProcedureAsync_1.htm)|  
(Унаследован от [SystemSchemeService](T_Tessa_Scheme_SystemSchemeService.htm))  
[GetProcedureOverrideAsync(Guid,
CancellationToken)](M_Tessa_Scheme_DatabaseSchemeService_GetProcedureOverrideAsync.htm)|  
(Переопределяет [SystemSchemeService.GetProcedureOverrideAsync(Guid,
CancellationToken)](M_Tessa_Scheme_SystemSchemeService_GetProcedureOverrideAsync.htm))  
[GetProcedureOverrideAsync(String,
CancellationToken)](M_Tessa_Scheme_DatabaseSchemeService_GetProcedureOverrideAsync_1.htm)|  
(Переопределяет [SystemSchemeService.GetProcedureOverrideAsync(String,
CancellationToken)](M_Tessa_Scheme_SystemSchemeService_GetProcedureOverrideAsync_1.htm))  
[GetProceduresAsync](M_Tessa_Scheme_SystemSchemeService_GetProceduresAsync.htm)|  
(Унаследован от [SystemSchemeService](T_Tessa_Scheme_SystemSchemeService.htm))  
[GetProceduresOverrideAsync](M_Tessa_Scheme_DatabaseSchemeService_GetProceduresOverrideAsync.htm)|  
(Переопределяет
[SystemSchemeService.GetProceduresOverrideAsync(CancellationToken)](M_Tessa_Scheme_SystemSchemeService_GetProceduresOverrideAsync.htm))  
[GetProceduresQuery](M_Tessa_Scheme_DatabaseSchemeService_GetProceduresQuery.htm)|  
[GetStorageVersionAsync](M_Tessa_Scheme_DatabaseSchemeService_GetStorageVersionAsync.htm)|  
(Переопределяет
[SystemSchemeService.GetStorageVersionAsync(CancellationToken)](M_Tessa_Scheme_SystemSchemeService_GetStorageVersionAsync.htm))  
[GetTableAsync(Guid,
CancellationToken)](M_Tessa_Scheme_SystemSchemeService_GetTableAsync.htm)|  
(Унаследован от [SystemSchemeService](T_Tessa_Scheme_SystemSchemeService.htm))  
[GetTableAsync(String,
CancellationToken)](M_Tessa_Scheme_SystemSchemeService_GetTableAsync_1.htm)|  
(Унаследован от [SystemSchemeService](T_Tessa_Scheme_SystemSchemeService.htm))  
[GetTableOverrideAsync(Guid,
CancellationToken)](M_Tessa_Scheme_DatabaseSchemeService_GetTableOverrideAsync.htm)|  
(Переопределяет [SystemSchemeService.GetTableOverrideAsync(Guid,
CancellationToken)](M_Tessa_Scheme_SystemSchemeService_GetTableOverrideAsync.htm))  
[GetTableOverrideAsync(String,
CancellationToken)](M_Tessa_Scheme_DatabaseSchemeService_GetTableOverrideAsync_1.htm)|  
(Переопределяет [SystemSchemeService.GetTableOverrideAsync(String,
CancellationToken)](M_Tessa_Scheme_SystemSchemeService_GetTableOverrideAsync_1.htm))  
[GetTablesAsync](M_Tessa_Scheme_SystemSchemeService_GetTablesAsync.htm)|  
(Унаследован от [SystemSchemeService](T_Tessa_Scheme_SystemSchemeService.htm))  
[GetTablesOverrideAsync](M_Tessa_Scheme_DatabaseSchemeService_GetTablesOverrideAsync.htm)|  
(Переопределяет
[SystemSchemeService.GetTablesOverrideAsync(CancellationToken)](M_Tessa_Scheme_SystemSchemeService_GetTablesOverrideAsync.htm))  
[GetTablesQuery](M_Tessa_Scheme_DatabaseSchemeService_GetTablesQuery.htm)|  
[GetType](https://learn.microsoft.com/dotnet/api/system.object.gettype#system-
object-gettype)| Gets the
[Type](https://learn.microsoft.com/dotnet/api/system.type) of the current
instance.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[InitializeAsync](M_Tessa_Scheme_SystemSchemeService_InitializeAsync.htm)|  
(Унаследован от [SystemSchemeService](T_Tessa_Scheme_SystemSchemeService.htm))  
[InitializeOverrideAsync](M_Tessa_Scheme_DatabaseSchemeService_InitializeOverrideAsync.htm)|  
(Переопределяет
[SystemSchemeService.InitializeOverrideAsync(CancellationToken)](M_Tessa_Scheme_SystemSchemeService_InitializeOverrideAsync.htm))  
[InvalidateCacheAsync](M_Tessa_Scheme_DatabaseSchemeService_InvalidateCacheAsync.htm)|
Инициирует сброс кэша.  
(Переопределяет
[SystemSchemeService.InvalidateCacheAsync(CancellationToken)](M_Tessa_Scheme_SystemSchemeService_InvalidateCacheAsync.htm))  
[InvalidateCacheIfChangedAsync](M_Tessa_Scheme_DatabaseSchemeService_InvalidateCacheIfChangedAsync.htm)|
Инициирует сброс кэша в случае, если есть изменения.  
(Переопределяет
[SystemSchemeService.InvalidateCacheIfChangedAsync(CancellationToken)](M_Tessa_Scheme_SystemSchemeService_InvalidateCacheIfChangedAsync.htm))  
[IsStorageExistsAsync](M_Tessa_Scheme_DatabaseSchemeService_IsStorageExistsAsync.htm)|  
(Переопределяет
[SystemSchemeService.IsStorageExistsAsync(CancellationToken)](M_Tessa_Scheme_SystemSchemeService_IsStorageExistsAsync.htm))  
[IsStorageUpToDateAsync](M_Tessa_Scheme_SystemSchemeService_IsStorageUpToDateAsync.htm)|  
(Унаследован от [SystemSchemeService](T_Tessa_Scheme_SystemSchemeService.htm))  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[ParsePostgresFunctionParameters](M_Tessa_Scheme_DatabaseSchemeService_ParsePostgresFunctionParameters.htm)|
Метод для парсинга параметров функции postgres из скрипта создания функции.
Взвращает параметры без определений значений по умолчанию.  
[PopulateConfigurationQuery](M_Tessa_Scheme_DatabaseSchemeService_PopulateConfigurationQuery.htm)|  
[PopulateStorageQuery](M_Tessa_Scheme_DatabaseSchemeService_PopulateStorageQuery.htm)|  
[ReadDatabasePropertiesQuery](M_Tessa_Scheme_DatabaseSchemeService_ReadDatabasePropertiesQuery.htm)|  
[ReadDatabasePropertiesQuery2](M_Tessa_Scheme_DatabaseSchemeService_ReadDatabasePropertiesQuery2.htm)|  
[ReadDatabasePropertiesQuery3](M_Tessa_Scheme_DatabaseSchemeService_ReadDatabasePropertiesQuery3.htm)|  
[ReadSchemeVersionQuery](M_Tessa_Scheme_DatabaseSchemeService_ReadSchemeVersionQuery.htm)|  
[ReadSchemeVersionQuery2](M_Tessa_Scheme_DatabaseSchemeService_ReadSchemeVersionQuery2.htm)|  
[RemoveFunctionAsync](M_Tessa_Scheme_SystemSchemeService_RemoveFunctionAsync.htm)|  
(Унаследован от [SystemSchemeService](T_Tessa_Scheme_SystemSchemeService.htm))  
[RemoveFunctionOverrideAsync](M_Tessa_Scheme_DatabaseSchemeService_RemoveFunctionOverrideAsync.htm)|  
(Переопределяет
[SystemSchemeService.RemoveFunctionOverrideAsync(SchemeFunction,
CancellationToken)](M_Tessa_Scheme_SystemSchemeService_RemoveFunctionOverrideAsync.htm))  
[RemoveFunctionQuery](M_Tessa_Scheme_DatabaseSchemeService_RemoveFunctionQuery.htm)|  
[RemoveMigrationAsync](M_Tessa_Scheme_SystemSchemeService_RemoveMigrationAsync.htm)|  
(Унаследован от [SystemSchemeService](T_Tessa_Scheme_SystemSchemeService.htm))  
[RemoveMigrationOverrideAsync](M_Tessa_Scheme_DatabaseSchemeService_RemoveMigrationOverrideAsync.htm)|  
(Переопределяет
[SystemSchemeService.RemoveMigrationOverrideAsync(SchemeMigration,
CancellationToken)](M_Tessa_Scheme_SystemSchemeService_RemoveMigrationOverrideAsync.htm))  
[RemoveMigrationQuery](M_Tessa_Scheme_DatabaseSchemeService_RemoveMigrationQuery.htm)|  
[RemovePartitionAsync](M_Tessa_Scheme_SystemSchemeService_RemovePartitionAsync.htm)|  
(Унаследован от [SystemSchemeService](T_Tessa_Scheme_SystemSchemeService.htm))  
[RemovePartitionOverrideAsync](M_Tessa_Scheme_DatabaseSchemeService_RemovePartitionOverrideAsync.htm)|  
(Переопределяет
[SystemSchemeService.RemovePartitionOverrideAsync(SchemePartition,
CancellationToken)](M_Tessa_Scheme_SystemSchemeService_RemovePartitionOverrideAsync.htm))  
[RemovePartitionQuery](M_Tessa_Scheme_DatabaseSchemeService_RemovePartitionQuery.htm)|  
[RemoveProcedureAsync](M_Tessa_Scheme_SystemSchemeService_RemoveProcedureAsync.htm)|  
(Унаследован от [SystemSchemeService](T_Tessa_Scheme_SystemSchemeService.htm))  
[RemoveProcedureOverrideAsync](M_Tessa_Scheme_DatabaseSchemeService_RemoveProcedureOverrideAsync.htm)|  
(Переопределяет
[SystemSchemeService.RemoveProcedureOverrideAsync(SchemeProcedure,
CancellationToken)](M_Tessa_Scheme_SystemSchemeService_RemoveProcedureOverrideAsync.htm))  
[RemoveProcedureQuery](M_Tessa_Scheme_DatabaseSchemeService_RemoveProcedureQuery.htm)|  
[RemoveTableAsync](M_Tessa_Scheme_SystemSchemeService_RemoveTableAsync.htm)|  
(Унаследован от [SystemSchemeService](T_Tessa_Scheme_SystemSchemeService.htm))  
[RemoveTableOverrideAsync](M_Tessa_Scheme_DatabaseSchemeService_RemoveTableOverrideAsync.htm)|  
(Переопределяет [SystemSchemeService.RemoveTableOverrideAsync(SchemeTable,
CancellationToken)](M_Tessa_Scheme_SystemSchemeService_RemoveTableOverrideAsync.htm))  
[RemoveTableQuery](M_Tessa_Scheme_DatabaseSchemeService_RemoveTableQuery.htm)|  
[SaveDatabasePropertiesAsync](M_Tessa_Scheme_SystemSchemeService_SaveDatabasePropertiesAsync.htm)|  
(Унаследован от [SystemSchemeService](T_Tessa_Scheme_SystemSchemeService.htm))  
[SaveDatabasePropertiesOverrideAsync](M_Tessa_Scheme_DatabaseSchemeService_SaveDatabasePropertiesOverrideAsync.htm)|  
(Переопределяет
[SystemSchemeService.SaveDatabasePropertiesOverrideAsync(SchemeDatabaseProperties,
CancellationToken)](M_Tessa_Scheme_SystemSchemeService_SaveDatabasePropertiesOverrideAsync.htm))  
[SaveFunctionAsync](M_Tessa_Scheme_SystemSchemeService_SaveFunctionAsync.htm)|  
(Унаследован от [SystemSchemeService](T_Tessa_Scheme_SystemSchemeService.htm))  
[SaveFunctionOverrideAsync](M_Tessa_Scheme_DatabaseSchemeService_SaveFunctionOverrideAsync.htm)|  
(Переопределяет [SystemSchemeService.SaveFunctionOverrideAsync(SchemeFunction,
CancellationToken)](M_Tessa_Scheme_SystemSchemeService_SaveFunctionOverrideAsync.htm))  
[SaveFunctionQuery](M_Tessa_Scheme_DatabaseSchemeService_SaveFunctionQuery.htm)|  
[SaveMigrationAsync](M_Tessa_Scheme_SystemSchemeService_SaveMigrationAsync.htm)|  
(Унаследован от [SystemSchemeService](T_Tessa_Scheme_SystemSchemeService.htm))  
[SaveMigrationOverrideAsync](M_Tessa_Scheme_DatabaseSchemeService_SaveMigrationOverrideAsync.htm)|  
(Переопределяет
[SystemSchemeService.SaveMigrationOverrideAsync(SchemeMigration,
CancellationToken)](M_Tessa_Scheme_SystemSchemeService_SaveMigrationOverrideAsync.htm))  
[SaveMigrationQuery](M_Tessa_Scheme_DatabaseSchemeService_SaveMigrationQuery.htm)|  
[SavePartitionAsync](M_Tessa_Scheme_SystemSchemeService_SavePartitionAsync.htm)|  
(Унаследован от [SystemSchemeService](T_Tessa_Scheme_SystemSchemeService.htm))  
[SavePartitionOverrideAsync](M_Tessa_Scheme_DatabaseSchemeService_SavePartitionOverrideAsync.htm)|  
(Переопределяет
[SystemSchemeService.SavePartitionOverrideAsync(SchemePartition,
CancellationToken)](M_Tessa_Scheme_SystemSchemeService_SavePartitionOverrideAsync.htm))  
[SavePartitionQuery](M_Tessa_Scheme_DatabaseSchemeService_SavePartitionQuery.htm)|  
[SaveProcedureAsync](M_Tessa_Scheme_SystemSchemeService_SaveProcedureAsync.htm)|  
(Унаследован от [SystemSchemeService](T_Tessa_Scheme_SystemSchemeService.htm))  
[SaveProcedureOverrideAsync](M_Tessa_Scheme_DatabaseSchemeService_SaveProcedureOverrideAsync.htm)|  
(Переопределяет
[SystemSchemeService.SaveProcedureOverrideAsync(SchemeProcedure,
CancellationToken)](M_Tessa_Scheme_SystemSchemeService_SaveProcedureOverrideAsync.htm))  
[SaveProcedureQuery](M_Tessa_Scheme_DatabaseSchemeService_SaveProcedureQuery.htm)|  
[SaveTableAsync](M_Tessa_Scheme_SystemSchemeService_SaveTableAsync.htm)|  
(Унаследован от [SystemSchemeService](T_Tessa_Scheme_SystemSchemeService.htm))  
[SaveTableOverrideAsync](M_Tessa_Scheme_DatabaseSchemeService_SaveTableOverrideAsync.htm)|  
(Переопределяет [SystemSchemeService.SaveTableOverrideAsync(SchemeTable,
CancellationToken)](M_Tessa_Scheme_SystemSchemeService_SaveTableOverrideAsync.htm))  
[SaveTableQuery](M_Tessa_Scheme_DatabaseSchemeService_SaveTableQuery.htm)|  
[ShouldInvalidateCacheQuery](M_Tessa_Scheme_DatabaseSchemeService_ShouldInvalidateCacheQuery.htm)|  
[TableExistsQuery](M_Tessa_Scheme_DatabaseSchemeService_TableExistsQuery.htm)|  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[UpdateModifiedByQuery](M_Tessa_Scheme_DatabaseSchemeService_UpdateModifiedByQuery.htm)|  
[UpdateStorageAsync](M_Tessa_Scheme_SystemSchemeService_UpdateStorageAsync.htm)|  
(Унаследован от [SystemSchemeService](T_Tessa_Scheme_SystemSchemeService.htm))  
[UpdateStorageOverrideAsync](M_Tessa_Scheme_DatabaseSchemeService_UpdateStorageOverrideAsync.htm)|  
(Переопределяет
[SystemSchemeService.UpdateStorageOverrideAsync(CancellationToken)](M_Tessa_Scheme_SystemSchemeService_UpdateStorageOverrideAsync.htm))  
[WriteDatabasePropertiesQuery](M_Tessa_Scheme_DatabaseSchemeService_WriteDatabasePropertiesQuery.htm)|  
[WriteSchemeVersionQuery](M_Tessa_Scheme_DatabaseSchemeService_WriteSchemeVersionQuery.htm)|  
## __Поля
[GetSchemeServiceVersionName](F_Tessa_Scheme_DatabaseSchemeService_GetSchemeServiceVersionName.htm)|  
---|---  
[GetStoragePropertiesName](F_Tessa_Scheme_DatabaseSchemeService_GetStoragePropertiesName.htm)|  
[PostgresGetFunctionsQuery](F_Tessa_Scheme_DatabaseSchemeService_PostgresGetFunctionsQuery.htm)|  
[PostgresGetMigrationsQuery](F_Tessa_Scheme_DatabaseSchemeService_PostgresGetMigrationsQuery.htm)|  
[PostgresGetPartitionsQuery](F_Tessa_Scheme_DatabaseSchemeService_PostgresGetPartitionsQuery.htm)|  
[PostgresGetProceduresQuery](F_Tessa_Scheme_DatabaseSchemeService_PostgresGetProceduresQuery.htm)|  
[PostgresGetTablesQuery](F_Tessa_Scheme_DatabaseSchemeService_PostgresGetTablesQuery.htm)|  
[PostgresRemoveFunctionQuery](F_Tessa_Scheme_DatabaseSchemeService_PostgresRemoveFunctionQuery.htm)|  
[PostgresRemoveMigrationQuery](F_Tessa_Scheme_DatabaseSchemeService_PostgresRemoveMigrationQuery.htm)|  
[PostgresRemovePartitionQuery](F_Tessa_Scheme_DatabaseSchemeService_PostgresRemovePartitionQuery.htm)|  
[PostgresRemoveProcedureQuery](F_Tessa_Scheme_DatabaseSchemeService_PostgresRemoveProcedureQuery.htm)|  
[PostgresRemoveTableQuery](F_Tessa_Scheme_DatabaseSchemeService_PostgresRemoveTableQuery.htm)|  
[PostgresSaveFunctionViaInsertQuery](F_Tessa_Scheme_DatabaseSchemeService_PostgresSaveFunctionViaInsertQuery.htm)|  
[PostgresSaveFunctionViaUpdateQuery](F_Tessa_Scheme_DatabaseSchemeService_PostgresSaveFunctionViaUpdateQuery.htm)|  
[PostgresSaveMigrationViaInsertQuery](F_Tessa_Scheme_DatabaseSchemeService_PostgresSaveMigrationViaInsertQuery.htm)|  
[PostgresSaveMigrationViaUpdateQuery](F_Tessa_Scheme_DatabaseSchemeService_PostgresSaveMigrationViaUpdateQuery.htm)|  
[PostgresSavePartitionViaInsertQuery](F_Tessa_Scheme_DatabaseSchemeService_PostgresSavePartitionViaInsertQuery.htm)|  
[PostgresSavePartitionViaUpdateQuery](F_Tessa_Scheme_DatabaseSchemeService_PostgresSavePartitionViaUpdateQuery.htm)|  
[PostgresSaveProcedureViaInsertQuery](F_Tessa_Scheme_DatabaseSchemeService_PostgresSaveProcedureViaInsertQuery.htm)|  
[PostgresSaveProcedureViaUpdateQuery](F_Tessa_Scheme_DatabaseSchemeService_PostgresSaveProcedureViaUpdateQuery.htm)|  
[PostgresSaveTableViaInsertQuery](F_Tessa_Scheme_DatabaseSchemeService_PostgresSaveTableViaInsertQuery.htm)|  
[PostgresSaveTableViaUpdateQuery](F_Tessa_Scheme_DatabaseSchemeService_PostgresSaveTableViaUpdateQuery.htm)|  
[SqlGetFunctionsQuery](F_Tessa_Scheme_DatabaseSchemeService_SqlGetFunctionsQuery.htm)|  
[SqlGetMigrationsQuery](F_Tessa_Scheme_DatabaseSchemeService_SqlGetMigrationsQuery.htm)|  
[SqlGetPartitionsQuery](F_Tessa_Scheme_DatabaseSchemeService_SqlGetPartitionsQuery.htm)|  
[SqlGetProceduresQuery](F_Tessa_Scheme_DatabaseSchemeService_SqlGetProceduresQuery.htm)|  
[SqlGetTablesQuery](F_Tessa_Scheme_DatabaseSchemeService_SqlGetTablesQuery.htm)|  
[SqlRemoveFunctionQuery](F_Tessa_Scheme_DatabaseSchemeService_SqlRemoveFunctionQuery.htm)|  
[SqlRemoveMigrationQuery](F_Tessa_Scheme_DatabaseSchemeService_SqlRemoveMigrationQuery.htm)|  
[SqlRemovePartitionQuery](F_Tessa_Scheme_DatabaseSchemeService_SqlRemovePartitionQuery.htm)|  
[SqlRemoveProcedureQuery](F_Tessa_Scheme_DatabaseSchemeService_SqlRemoveProcedureQuery.htm)|  
[SqlRemoveTableQuery](F_Tessa_Scheme_DatabaseSchemeService_SqlRemoveTableQuery.htm)|  
[SqlSaveFunctionViaInsertQuery](F_Tessa_Scheme_DatabaseSchemeService_SqlSaveFunctionViaInsertQuery.htm)|  
[SqlSaveFunctionViaUpdateQuery](F_Tessa_Scheme_DatabaseSchemeService_SqlSaveFunctionViaUpdateQuery.htm)|  
[SqlSaveMigrationViaInsertQuery](F_Tessa_Scheme_DatabaseSchemeService_SqlSaveMigrationViaInsertQuery.htm)|  
[SqlSaveMigrationViaUpdateQuery](F_Tessa_Scheme_DatabaseSchemeService_SqlSaveMigrationViaUpdateQuery.htm)|  
[SqlSavePartitionViaInsertQuery](F_Tessa_Scheme_DatabaseSchemeService_SqlSavePartitionViaInsertQuery.htm)|  
[SqlSavePartitionViaUpdateQuery](F_Tessa_Scheme_DatabaseSchemeService_SqlSavePartitionViaUpdateQuery.htm)|  
[SqlSaveProcedureViaInsertQuery](F_Tessa_Scheme_DatabaseSchemeService_SqlSaveProcedureViaInsertQuery.htm)|  
[SqlSaveProcedureViaUpdateQuery](F_Tessa_Scheme_DatabaseSchemeService_SqlSaveProcedureViaUpdateQuery.htm)|  
[SqlSaveTableViaInsertQuery](F_Tessa_Scheme_DatabaseSchemeService_SqlSaveTableViaInsertQuery.htm)|  
[SqlSaveTableViaUpdateQuery](F_Tessa_Scheme_DatabaseSchemeService_SqlSaveTableViaUpdateQuery.htm)|  
## __Методы расширения
[Get](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Get.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
---|---  
[InternalMarkerCanvas](M_Tessa_UI_Views_Charting_Annotations_AnnotationInternalsAccessor_InternalMarkerCanvas.htm)|
Возвращает маркер аннотации  
(Определяется
[AnnotationInternalsAccessor](T_Tessa_UI_Views_Charting_Annotations_AnnotationInternalsAccessor.htm))  
[Invoke](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Invoke.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
[Set](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Set.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
##  __См. также
#### Ссылки
[Tessa.Scheme - пространство имён](N_Tessa_Scheme.htm)
