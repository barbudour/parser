# SystemSchemeService - класс
##  __Definition
 **Пространство имён:** [Tessa.Scheme](N_Tessa_Scheme.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public abstract class SystemSchemeService : ISchemeServiceWithStorage, 
    	ISchemeService, ISchemeServiceWithCache
VB __Копировать
     Public MustInherit Class SystemSchemeService
    	Implements ISchemeServiceWithStorage, ISchemeService, ISchemeServiceWithCache
C++ __Копировать
     public ref class SystemSchemeService abstract : ISchemeServiceWithStorage, 
    	ISchemeService, ISchemeServiceWithCache
F# __Копировать
     [<AbstractClassAttribute>]
    type SystemSchemeService = 
        class
            interface ISchemeServiceWithStorage
            interface ISchemeService
            interface ISchemeServiceWithCache
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ SystemSchemeService
Derived
[Tessa.Extensions.Default.Console.SchemeScript.FakeSchemeService](T_Tessa_Extensions_Default_Console_SchemeScript_FakeSchemeService.htm)
[Tessa.Scheme.DatabaseSchemeService](T_Tessa_Scheme_DatabaseSchemeService.htm)
[Tessa.Scheme.FileSchemeService](T_Tessa_Scheme_FileSchemeService.htm)
Implements
    [ISchemeService](T_Tessa_Scheme_ISchemeService.htm), [ISchemeServiceWithCache](T_Tessa_Scheme_ISchemeServiceWithCache.htm), [ISchemeServiceWithStorage](T_Tessa_Scheme_ISchemeServiceWithStorage.htm)
##  __Конструкторы
[SystemSchemeService](M_Tessa_Scheme_SystemSchemeService__ctor.htm)|
Инициализирует новый экземпляр класса SystemSchemeService  
---|---  
##  __Свойства
[Options](P_Tessa_Scheme_SystemSchemeService_Options.htm)|  
---|---  
[ServiceVersion](P_Tessa_Scheme_SystemSchemeService_ServiceVersion.htm)|  
## __Методы
[CheckIsNotNull](M_Tessa_Scheme_SystemSchemeService_CheckIsNotNull.htm)|  
---|---  
[CheckIsNotReadOnly](M_Tessa_Scheme_SystemSchemeService_CheckIsNotReadOnly.htm)|  
[CreateException](M_Tessa_Scheme_SystemSchemeService_CreateException.htm)|  
[CreateOperationScope](M_Tessa_Scheme_SystemSchemeService_CreateOperationScope.htm)|  
[CreateOperationScopeOverride](M_Tessa_Scheme_SystemSchemeService_CreateOperationScopeOverride.htm)|  
[CreateStorageAsync](M_Tessa_Scheme_SystemSchemeService_CreateStorageAsync.htm)|  
[CreateStorageOverrideAsync](M_Tessa_Scheme_SystemSchemeService_CreateStorageOverrideAsync.htm)|  
[EnsureInvalidateCacheSubscribedAsync](M_Tessa_Scheme_SystemSchemeService_EnsureInvalidateCacheSubscribedAsync.htm)|
Производит подписку на событие сброса кэша, если необходимо.  
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
[GetDatabasePropertiesOverrideAsync](M_Tessa_Scheme_SystemSchemeService_GetDatabasePropertiesOverrideAsync.htm)|  
[GetFunctionAsync(Guid,
CancellationToken)](M_Tessa_Scheme_SystemSchemeService_GetFunctionAsync.htm)|  
[GetFunctionAsync(String,
CancellationToken)](M_Tessa_Scheme_SystemSchemeService_GetFunctionAsync_1.htm)|  
[GetFunctionOverrideAsync(Guid,
CancellationToken)](M_Tessa_Scheme_SystemSchemeService_GetFunctionOverrideAsync.htm)|  
[GetFunctionOverrideAsync(String,
CancellationToken)](M_Tessa_Scheme_SystemSchemeService_GetFunctionOverrideAsync_1.htm)|  
[GetFunctionsAsync](M_Tessa_Scheme_SystemSchemeService_GetFunctionsAsync.htm)|  
[GetFunctionsOverrideAsync](M_Tessa_Scheme_SystemSchemeService_GetFunctionsOverrideAsync.htm)|  
[GetHashCode](https://learn.microsoft.com/dotnet/api/system.object.gethashcode#system-
object-gethashcode)| Serves as the default hash function.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetMigrationAsync(Guid,
CancellationToken)](M_Tessa_Scheme_SystemSchemeService_GetMigrationAsync.htm)|  
[GetMigrationAsync(String,
CancellationToken)](M_Tessa_Scheme_SystemSchemeService_GetMigrationAsync_1.htm)|  
[GetMigrationOverrideAsync(Guid,
CancellationToken)](M_Tessa_Scheme_SystemSchemeService_GetMigrationOverrideAsync.htm)|  
[GetMigrationOverrideAsync(String,
CancellationToken)](M_Tessa_Scheme_SystemSchemeService_GetMigrationOverrideAsync_1.htm)|  
[GetMigrationsAsync](M_Tessa_Scheme_SystemSchemeService_GetMigrationsAsync.htm)|  
[GetMigrationsOverrideAsync](M_Tessa_Scheme_SystemSchemeService_GetMigrationsOverrideAsync.htm)|  
[GetPartitionAsync(Guid,
CancellationToken)](M_Tessa_Scheme_SystemSchemeService_GetPartitionAsync.htm)|  
[GetPartitionAsync(String,
CancellationToken)](M_Tessa_Scheme_SystemSchemeService_GetPartitionAsync_1.htm)|  
[GetPartitionOverrideAsync(Guid,
CancellationToken)](M_Tessa_Scheme_SystemSchemeService_GetPartitionOverrideAsync.htm)|  
[GetPartitionOverrideAsync(String,
CancellationToken)](M_Tessa_Scheme_SystemSchemeService_GetPartitionOverrideAsync_1.htm)|  
[GetPartitionsAsync](M_Tessa_Scheme_SystemSchemeService_GetPartitionsAsync.htm)|  
[GetPartitionsOverrideAsync](M_Tessa_Scheme_SystemSchemeService_GetPartitionsOverrideAsync.htm)|  
[GetProcedureAsync(Guid,
CancellationToken)](M_Tessa_Scheme_SystemSchemeService_GetProcedureAsync.htm)|  
[GetProcedureAsync(String,
CancellationToken)](M_Tessa_Scheme_SystemSchemeService_GetProcedureAsync_1.htm)|  
[GetProcedureOverrideAsync(Guid,
CancellationToken)](M_Tessa_Scheme_SystemSchemeService_GetProcedureOverrideAsync.htm)|  
[GetProcedureOverrideAsync(String,
CancellationToken)](M_Tessa_Scheme_SystemSchemeService_GetProcedureOverrideAsync_1.htm)|  
[GetProceduresAsync](M_Tessa_Scheme_SystemSchemeService_GetProceduresAsync.htm)|  
[GetProceduresOverrideAsync](M_Tessa_Scheme_SystemSchemeService_GetProceduresOverrideAsync.htm)|  
[GetStorageVersionAsync](M_Tessa_Scheme_SystemSchemeService_GetStorageVersionAsync.htm)|  
[GetTableAsync(Guid,
CancellationToken)](M_Tessa_Scheme_SystemSchemeService_GetTableAsync.htm)|  
[GetTableAsync(String,
CancellationToken)](M_Tessa_Scheme_SystemSchemeService_GetTableAsync_1.htm)|  
[GetTableOverrideAsync(Guid,
CancellationToken)](M_Tessa_Scheme_SystemSchemeService_GetTableOverrideAsync.htm)|  
[GetTableOverrideAsync(String,
CancellationToken)](M_Tessa_Scheme_SystemSchemeService_GetTableOverrideAsync_1.htm)|  
[GetTablesAsync](M_Tessa_Scheme_SystemSchemeService_GetTablesAsync.htm)|  
[GetTablesOverrideAsync](M_Tessa_Scheme_SystemSchemeService_GetTablesOverrideAsync.htm)|  
[GetType](https://learn.microsoft.com/dotnet/api/system.object.gettype#system-
object-gettype)| Gets the
[Type](https://learn.microsoft.com/dotnet/api/system.type) of the current
instance.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[InitializeAsync](M_Tessa_Scheme_SystemSchemeService_InitializeAsync.htm)|  
[InitializeOverrideAsync](M_Tessa_Scheme_SystemSchemeService_InitializeOverrideAsync.htm)|  
[InvalidateCacheAsync](M_Tessa_Scheme_SystemSchemeService_InvalidateCacheAsync.htm)|
Инициирует сброс кэша.  
[InvalidateCacheIfChangedAsync](M_Tessa_Scheme_SystemSchemeService_InvalidateCacheIfChangedAsync.htm)|
Инициирует сброс кэша в случае, если есть изменения.  
[IsStorageExistsAsync](M_Tessa_Scheme_SystemSchemeService_IsStorageExistsAsync.htm)|  
[IsStorageUpToDateAsync](M_Tessa_Scheme_SystemSchemeService_IsStorageUpToDateAsync.htm)|  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[ReadSql<T>](M_Tessa_Scheme_SystemSchemeService_ReadSql__1.htm)|  
[RemoveFunctionAsync](M_Tessa_Scheme_SystemSchemeService_RemoveFunctionAsync.htm)|  
[RemoveFunctionOverrideAsync](M_Tessa_Scheme_SystemSchemeService_RemoveFunctionOverrideAsync.htm)|  
[RemoveMigrationAsync](M_Tessa_Scheme_SystemSchemeService_RemoveMigrationAsync.htm)|  
[RemoveMigrationOverrideAsync](M_Tessa_Scheme_SystemSchemeService_RemoveMigrationOverrideAsync.htm)|  
[RemovePartitionAsync](M_Tessa_Scheme_SystemSchemeService_RemovePartitionAsync.htm)|  
[RemovePartitionOverrideAsync](M_Tessa_Scheme_SystemSchemeService_RemovePartitionOverrideAsync.htm)|  
[RemoveProcedureAsync](M_Tessa_Scheme_SystemSchemeService_RemoveProcedureAsync.htm)|  
[RemoveProcedureOverrideAsync](M_Tessa_Scheme_SystemSchemeService_RemoveProcedureOverrideAsync.htm)|  
[RemoveTableAsync](M_Tessa_Scheme_SystemSchemeService_RemoveTableAsync.htm)|  
[RemoveTableOverrideAsync](M_Tessa_Scheme_SystemSchemeService_RemoveTableOverrideAsync.htm)|  
[SaveDatabasePropertiesAsync](M_Tessa_Scheme_SystemSchemeService_SaveDatabasePropertiesAsync.htm)|  
[SaveDatabasePropertiesOverrideAsync](M_Tessa_Scheme_SystemSchemeService_SaveDatabasePropertiesOverrideAsync.htm)|  
[SaveFunctionAsync](M_Tessa_Scheme_SystemSchemeService_SaveFunctionAsync.htm)|  
[SaveFunctionOverrideAsync](M_Tessa_Scheme_SystemSchemeService_SaveFunctionOverrideAsync.htm)|  
[SaveMigrationAsync](M_Tessa_Scheme_SystemSchemeService_SaveMigrationAsync.htm)|  
[SaveMigrationOverrideAsync](M_Tessa_Scheme_SystemSchemeService_SaveMigrationOverrideAsync.htm)|  
[SavePartitionAsync](M_Tessa_Scheme_SystemSchemeService_SavePartitionAsync.htm)|  
[SavePartitionOverrideAsync](M_Tessa_Scheme_SystemSchemeService_SavePartitionOverrideAsync.htm)|  
[SaveProcedureAsync](M_Tessa_Scheme_SystemSchemeService_SaveProcedureAsync.htm)|  
[SaveProcedureOverrideAsync](M_Tessa_Scheme_SystemSchemeService_SaveProcedureOverrideAsync.htm)|  
[SaveTableAsync](M_Tessa_Scheme_SystemSchemeService_SaveTableAsync.htm)|  
[SaveTableOverrideAsync](M_Tessa_Scheme_SystemSchemeService_SaveTableOverrideAsync.htm)|  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[UpdateStorageAsync](M_Tessa_Scheme_SystemSchemeService_UpdateStorageAsync.htm)|  
[UpdateStorageOverrideAsync](M_Tessa_Scheme_SystemSchemeService_UpdateStorageOverrideAsync.htm)|  
## __Поля
[SchemeVersion](F_Tessa_Scheme_SystemSchemeService_SchemeVersion.htm)|  
---|---  
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
[ValidateAsync](M_Tessa_UI_Cards_CardUIExtensions_ValidateAsync_3.htm)|
Выполняет проверку наличия таблицы с идентификатором tableID в схеме.  
(Определяется [CardUIExtensions](T_Tessa_UI_Cards_CardUIExtensions.htm))  
[ValidateAsync](M_Tessa_UI_Cards_CardUIExtensions_ValidateAsync_2.htm)|
Выполняет проверку наличия колонки с идентификатором columnID в таблице с
идентификатором tableID.  
(Определяется [CardUIExtensions](T_Tessa_UI_Cards_CardUIExtensions.htm))  
##  __См. также
#### Ссылки
[Tessa.Scheme - пространство имён](N_Tessa_Scheme.htm)
