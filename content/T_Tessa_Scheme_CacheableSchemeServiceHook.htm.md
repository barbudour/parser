# CacheableSchemeServiceHook - класс
##  __Definition
 **Пространство имён:** [Tessa.Scheme](N_Tessa_Scheme.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class CacheableSchemeServiceHook : HookableSchemeServiceHook, 
    	IDisposable
VB __Копировать
     Public NotInheritable Class CacheableSchemeServiceHook
    	Inherits HookableSchemeServiceHook
    	Implements IDisposable
C++ __Копировать
     public ref class CacheableSchemeServiceHook sealed : public HookableSchemeServiceHook, 
    	IDisposable
F# __Копировать
     [<SealedAttribute>]
    type CacheableSchemeServiceHook = 
        class
            inherit HookableSchemeServiceHook
            interface IDisposable
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[HookableServiceHook](T_Tessa_Platform_HookableServiceHook_1.htm)<[ISchemeService](T_Tessa_Scheme_ISchemeService.htm)> __[HookableSchemeServiceHook](T_Tessa_Scheme_HookableSchemeServiceHook.htm) __ CacheableSchemeServiceHook
Implements
    [IDisposable](https://learn.microsoft.com/dotnet/api/system.idisposable)
##  __Конструкторы
[CacheableSchemeServiceHook](M_Tessa_Scheme_CacheableSchemeServiceHook__ctor.htm)|
Инициализирует новый экземпляр класса CacheableSchemeServiceHook  
---|---  
##  __Свойства
[NextHook](P_Tessa_Platform_HookableServiceHook_1_NextHook.htm)|  
(Унаследован от
[HookableServiceHook<TService>](T_Tessa_Platform_HookableServiceHook_1.htm))  
---|---  
[ServiceVersion](P_Tessa_Scheme_HookableSchemeServiceHook_ServiceVersion.htm)|  
(Унаследован от
[HookableSchemeServiceHook](T_Tessa_Scheme_HookableSchemeServiceHook.htm))  
##  __Методы
[CreateStorageAsync](M_Tessa_Scheme_HookableSchemeServiceHook_CreateStorageAsync.htm)|  
(Унаследован от
[HookableSchemeServiceHook](T_Tessa_Scheme_HookableSchemeServiceHook.htm))  
---|---  
[Dispose](M_Tessa_Scheme_CacheableSchemeServiceHook_Dispose.htm)| Освобождает
все ресурсы, используемые объектом CacheableSchemeServiceHook  
[EnsureInvalidateCacheSubscribedAsync](M_Tessa_Scheme_HookableSchemeServiceHook_EnsureInvalidateCacheSubscribedAsync.htm)|
Производит подписку на событие сброса кэша, если необходимо.  
(Унаследован от
[HookableSchemeServiceHook](T_Tessa_Scheme_HookableSchemeServiceHook.htm))  
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
[GetDatabasePropertiesAsync](M_Tessa_Scheme_CacheableSchemeServiceHook_GetDatabasePropertiesAsync.htm)|  
(Переопределяет
[HookableSchemeServiceHook.GetDatabasePropertiesAsync(CancellationToken)](M_Tessa_Scheme_HookableSchemeServiceHook_GetDatabasePropertiesAsync.htm))  
[GetFunctionAsync(Guid,
CancellationToken)](M_Tessa_Scheme_CacheableSchemeServiceHook_GetFunctionAsync.htm)|  
(Переопределяет [HookableSchemeServiceHook.GetFunctionAsync(Guid,
CancellationToken)](M_Tessa_Scheme_HookableSchemeServiceHook_GetFunctionAsync.htm))  
[GetFunctionAsync(String,
CancellationToken)](M_Tessa_Scheme_CacheableSchemeServiceHook_GetFunctionAsync_1.htm)|  
(Переопределяет [HookableSchemeServiceHook.GetFunctionAsync(String,
CancellationToken)](M_Tessa_Scheme_HookableSchemeServiceHook_GetFunctionAsync_1.htm))  
[GetFunctionsAsync](M_Tessa_Scheme_CacheableSchemeServiceHook_GetFunctionsAsync.htm)|  
(Переопределяет
[HookableSchemeServiceHook.GetFunctionsAsync(CancellationToken)](M_Tessa_Scheme_HookableSchemeServiceHook_GetFunctionsAsync.htm))  
[GetHashCode](https://learn.microsoft.com/dotnet/api/system.object.gethashcode#system-
object-gethashcode)| Serves as the default hash function.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetMigrationAsync(Guid,
CancellationToken)](M_Tessa_Scheme_CacheableSchemeServiceHook_GetMigrationAsync.htm)|  
(Переопределяет [HookableSchemeServiceHook.GetMigrationAsync(Guid,
CancellationToken)](M_Tessa_Scheme_HookableSchemeServiceHook_GetMigrationAsync.htm))  
[GetMigrationAsync(String,
CancellationToken)](M_Tessa_Scheme_CacheableSchemeServiceHook_GetMigrationAsync_1.htm)|  
(Переопределяет [HookableSchemeServiceHook.GetMigrationAsync(String,
CancellationToken)](M_Tessa_Scheme_HookableSchemeServiceHook_GetMigrationAsync_1.htm))  
[GetMigrationsAsync](M_Tessa_Scheme_CacheableSchemeServiceHook_GetMigrationsAsync.htm)|  
(Переопределяет
[HookableSchemeServiceHook.GetMigrationsAsync(CancellationToken)](M_Tessa_Scheme_HookableSchemeServiceHook_GetMigrationsAsync.htm))  
[GetPartitionAsync(Guid,
CancellationToken)](M_Tessa_Scheme_CacheableSchemeServiceHook_GetPartitionAsync.htm)|  
(Переопределяет [HookableSchemeServiceHook.GetPartitionAsync(Guid,
CancellationToken)](M_Tessa_Scheme_HookableSchemeServiceHook_GetPartitionAsync.htm))  
[GetPartitionAsync(String,
CancellationToken)](M_Tessa_Scheme_CacheableSchemeServiceHook_GetPartitionAsync_1.htm)|  
(Переопределяет [HookableSchemeServiceHook.GetPartitionAsync(String,
CancellationToken)](M_Tessa_Scheme_HookableSchemeServiceHook_GetPartitionAsync_1.htm))  
[GetPartitionsAsync](M_Tessa_Scheme_CacheableSchemeServiceHook_GetPartitionsAsync.htm)|  
(Переопределяет
[HookableSchemeServiceHook.GetPartitionsAsync(CancellationToken)](M_Tessa_Scheme_HookableSchemeServiceHook_GetPartitionsAsync.htm))  
[GetProcedureAsync(Guid,
CancellationToken)](M_Tessa_Scheme_CacheableSchemeServiceHook_GetProcedureAsync.htm)|  
(Переопределяет [HookableSchemeServiceHook.GetProcedureAsync(Guid,
CancellationToken)](M_Tessa_Scheme_HookableSchemeServiceHook_GetProcedureAsync.htm))  
[GetProcedureAsync(String,
CancellationToken)](M_Tessa_Scheme_CacheableSchemeServiceHook_GetProcedureAsync_1.htm)|  
(Переопределяет [HookableSchemeServiceHook.GetProcedureAsync(String,
CancellationToken)](M_Tessa_Scheme_HookableSchemeServiceHook_GetProcedureAsync_1.htm))  
[GetProceduresAsync](M_Tessa_Scheme_CacheableSchemeServiceHook_GetProceduresAsync.htm)|  
(Переопределяет
[HookableSchemeServiceHook.GetProceduresAsync(CancellationToken)](M_Tessa_Scheme_HookableSchemeServiceHook_GetProceduresAsync.htm))  
[GetStorageVersionAsync](M_Tessa_Scheme_HookableSchemeServiceHook_GetStorageVersionAsync.htm)|  
(Унаследован от
[HookableSchemeServiceHook](T_Tessa_Scheme_HookableSchemeServiceHook.htm))  
[GetTableAsync(Guid,
CancellationToken)](M_Tessa_Scheme_CacheableSchemeServiceHook_GetTableAsync.htm)|  
(Переопределяет [HookableSchemeServiceHook.GetTableAsync(Guid,
CancellationToken)](M_Tessa_Scheme_HookableSchemeServiceHook_GetTableAsync.htm))  
[GetTableAsync(String,
CancellationToken)](M_Tessa_Scheme_CacheableSchemeServiceHook_GetTableAsync_1.htm)|  
(Переопределяет [HookableSchemeServiceHook.GetTableAsync(String,
CancellationToken)](M_Tessa_Scheme_HookableSchemeServiceHook_GetTableAsync_1.htm))  
[GetTablesAsync](M_Tessa_Scheme_CacheableSchemeServiceHook_GetTablesAsync.htm)|  
(Переопределяет
[HookableSchemeServiceHook.GetTablesAsync(CancellationToken)](M_Tessa_Scheme_HookableSchemeServiceHook_GetTablesAsync.htm))  
[GetType](https://learn.microsoft.com/dotnet/api/system.object.gettype#system-
object-gettype)| Gets the
[Type](https://learn.microsoft.com/dotnet/api/system.type) of the current
instance.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[InvalidateCacheAsync](M_Tessa_Scheme_CacheableSchemeServiceHook_InvalidateCacheAsync.htm)|
Инициирует сброс кэша.  
(Переопределяет
[HookableSchemeServiceHook.InvalidateCacheAsync(CancellationToken)](M_Tessa_Scheme_HookableSchemeServiceHook_InvalidateCacheAsync.htm))  
[InvalidateCacheIfChangedAsync](M_Tessa_Scheme_CacheableSchemeServiceHook_InvalidateCacheIfChangedAsync.htm)|
Инициирует сброс кэша в случае, если есть изменения.  
(Переопределяет
[HookableSchemeServiceHook.InvalidateCacheIfChangedAsync(CancellationToken)](M_Tessa_Scheme_HookableSchemeServiceHook_InvalidateCacheIfChangedAsync.htm))  
[IsStorageExistsAsync](M_Tessa_Scheme_HookableSchemeServiceHook_IsStorageExistsAsync.htm)|  
(Унаследован от
[HookableSchemeServiceHook](T_Tessa_Scheme_HookableSchemeServiceHook.htm))  
[IsStorageUpToDateAsync](M_Tessa_Scheme_HookableSchemeServiceHook_IsStorageUpToDateAsync.htm)|  
(Унаследован от
[HookableSchemeServiceHook](T_Tessa_Scheme_HookableSchemeServiceHook.htm))  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[RemoveFunctionAsync](M_Tessa_Scheme_CacheableSchemeServiceHook_RemoveFunctionAsync.htm)|  
(Переопределяет [HookableSchemeServiceHook.RemoveFunctionAsync(SchemeFunction,
CancellationToken)](M_Tessa_Scheme_HookableSchemeServiceHook_RemoveFunctionAsync.htm))  
[RemoveMigrationAsync](M_Tessa_Scheme_CacheableSchemeServiceHook_RemoveMigrationAsync.htm)|  
(Переопределяет
[HookableSchemeServiceHook.RemoveMigrationAsync(SchemeMigration,
CancellationToken)](M_Tessa_Scheme_HookableSchemeServiceHook_RemoveMigrationAsync.htm))  
[RemovePartitionAsync](M_Tessa_Scheme_CacheableSchemeServiceHook_RemovePartitionAsync.htm)|  
(Переопределяет
[HookableSchemeServiceHook.RemovePartitionAsync(SchemePartition,
CancellationToken)](M_Tessa_Scheme_HookableSchemeServiceHook_RemovePartitionAsync.htm))  
[RemoveProcedureAsync](M_Tessa_Scheme_CacheableSchemeServiceHook_RemoveProcedureAsync.htm)|  
(Переопределяет
[HookableSchemeServiceHook.RemoveProcedureAsync(SchemeProcedure,
CancellationToken)](M_Tessa_Scheme_HookableSchemeServiceHook_RemoveProcedureAsync.htm))  
[RemoveTableAsync](M_Tessa_Scheme_CacheableSchemeServiceHook_RemoveTableAsync.htm)|  
(Переопределяет [HookableSchemeServiceHook.RemoveTableAsync(SchemeTable,
CancellationToken)](M_Tessa_Scheme_HookableSchemeServiceHook_RemoveTableAsync.htm))  
[SaveDatabasePropertiesAsync](M_Tessa_Scheme_CacheableSchemeServiceHook_SaveDatabasePropertiesAsync.htm)|  
(Переопределяет
[HookableSchemeServiceHook.SaveDatabasePropertiesAsync(SchemeDatabaseProperties,
CancellationToken)](M_Tessa_Scheme_HookableSchemeServiceHook_SaveDatabasePropertiesAsync.htm))  
[SaveFunctionAsync](M_Tessa_Scheme_CacheableSchemeServiceHook_SaveFunctionAsync.htm)|  
(Переопределяет [HookableSchemeServiceHook.SaveFunctionAsync(SchemeFunction,
CancellationToken)](M_Tessa_Scheme_HookableSchemeServiceHook_SaveFunctionAsync.htm))  
[SaveMigrationAsync](M_Tessa_Scheme_CacheableSchemeServiceHook_SaveMigrationAsync.htm)|  
(Переопределяет [HookableSchemeServiceHook.SaveMigrationAsync(SchemeMigration,
CancellationToken)](M_Tessa_Scheme_HookableSchemeServiceHook_SaveMigrationAsync.htm))  
[SavePartitionAsync](M_Tessa_Scheme_CacheableSchemeServiceHook_SavePartitionAsync.htm)|  
(Переопределяет [HookableSchemeServiceHook.SavePartitionAsync(SchemePartition,
CancellationToken)](M_Tessa_Scheme_HookableSchemeServiceHook_SavePartitionAsync.htm))  
[SaveProcedureAsync](M_Tessa_Scheme_CacheableSchemeServiceHook_SaveProcedureAsync.htm)|  
(Переопределяет [HookableSchemeServiceHook.SaveProcedureAsync(SchemeProcedure,
CancellationToken)](M_Tessa_Scheme_HookableSchemeServiceHook_SaveProcedureAsync.htm))  
[SaveTableAsync](M_Tessa_Scheme_CacheableSchemeServiceHook_SaveTableAsync.htm)|  
(Переопределяет [HookableSchemeServiceHook.SaveTableAsync(SchemeTable,
CancellationToken)](M_Tessa_Scheme_HookableSchemeServiceHook_SaveTableAsync.htm))  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[UpdateStorageAsync](M_Tessa_Scheme_HookableSchemeServiceHook_UpdateStorageAsync.htm)|  
(Унаследован от
[HookableSchemeServiceHook](T_Tessa_Scheme_HookableSchemeServiceHook.htm))  
##  __Методы расширения
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
