# HookableSchemeService - класс
##  __Definition
 **Пространство имён:** [Tessa.Scheme](N_Tessa_Scheme.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class HookableSchemeService : HookableService<ISchemeService>, 
    	ISchemeServiceWithCache, ISchemeService, ISchemeServiceWithStorage
VB __Копировать
     Public NotInheritable Class HookableSchemeService
    	Inherits HookableService(Of ISchemeService)
    	Implements ISchemeServiceWithCache, ISchemeService, ISchemeServiceWithStorage
C++ __Копировать
     public ref class HookableSchemeService sealed : public HookableService<ISchemeService^>, 
    	ISchemeServiceWithCache, ISchemeService, ISchemeServiceWithStorage
F# __Копировать
     [<SealedAttribute>]
    type HookableSchemeService = 
        class
            inherit HookableService<ISchemeService>
            interface ISchemeServiceWithCache
            interface ISchemeService
            interface ISchemeServiceWithStorage
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[HookableService](T_Tessa_Platform_HookableService_1.htm)<[ISchemeService](T_Tessa_Scheme_ISchemeService.htm)> __ HookableSchemeService
Implements
    [ISchemeService](T_Tessa_Scheme_ISchemeService.htm), [ISchemeServiceWithCache](T_Tessa_Scheme_ISchemeServiceWithCache.htm), [ISchemeServiceWithStorage](T_Tessa_Scheme_ISchemeServiceWithStorage.htm)
##  __Конструкторы
[HookableSchemeService](M_Tessa_Scheme_HookableSchemeService__ctor.htm)|
Инициализирует новый экземпляр класса HookableSchemeService  
---|---  
##  __Свойства
[FirstHook](P_Tessa_Platform_HookableService_1_FirstHook.htm)|  
(Унаследован от
[HookableService<TService>](T_Tessa_Platform_HookableService_1.htm))  
---|---  
[ServiceVersion](P_Tessa_Scheme_HookableSchemeService_ServiceVersion.htm)|  
## __Методы
[AddHook](M_Tessa_Platform_HookableService_1_AddHook.htm)|  
(Унаследован от
[HookableService<TService>](T_Tessa_Platform_HookableService_1.htm))  
---|---  
[CreateStorageAsync](M_Tessa_Scheme_HookableSchemeService_CreateStorageAsync.htm)|  
[EnsureInvalidateCacheSubscribedAsync](M_Tessa_Scheme_HookableSchemeService_EnsureInvalidateCacheSubscribedAsync.htm)|
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
[GetDatabasePropertiesAsync](M_Tessa_Scheme_HookableSchemeService_GetDatabasePropertiesAsync.htm)|  
[GetFunctionAsync(Guid,
CancellationToken)](M_Tessa_Scheme_HookableSchemeService_GetFunctionAsync.htm)|  
[GetFunctionAsync(String,
CancellationToken)](M_Tessa_Scheme_HookableSchemeService_GetFunctionAsync_1.htm)|  
[GetFunctionsAsync](M_Tessa_Scheme_HookableSchemeService_GetFunctionsAsync.htm)|  
[GetHashCode](https://learn.microsoft.com/dotnet/api/system.object.gethashcode#system-
object-gethashcode)| Serves as the default hash function.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetMigrationAsync(Guid,
CancellationToken)](M_Tessa_Scheme_HookableSchemeService_GetMigrationAsync.htm)|  
[GetMigrationAsync(String,
CancellationToken)](M_Tessa_Scheme_HookableSchemeService_GetMigrationAsync_1.htm)|  
[GetMigrationsAsync](M_Tessa_Scheme_HookableSchemeService_GetMigrationsAsync.htm)|  
[GetPartitionAsync(Guid,
CancellationToken)](M_Tessa_Scheme_HookableSchemeService_GetPartitionAsync.htm)|  
[GetPartitionAsync(String,
CancellationToken)](M_Tessa_Scheme_HookableSchemeService_GetPartitionAsync_1.htm)|  
[GetPartitionsAsync](M_Tessa_Scheme_HookableSchemeService_GetPartitionsAsync.htm)|  
[GetProcedureAsync(Guid,
CancellationToken)](M_Tessa_Scheme_HookableSchemeService_GetProcedureAsync.htm)|  
[GetProcedureAsync(String,
CancellationToken)](M_Tessa_Scheme_HookableSchemeService_GetProcedureAsync_1.htm)|  
[GetProceduresAsync](M_Tessa_Scheme_HookableSchemeService_GetProceduresAsync.htm)|  
[GetStorageVersionAsync](M_Tessa_Scheme_HookableSchemeService_GetStorageVersionAsync.htm)|  
[GetTableAsync(Guid,
CancellationToken)](M_Tessa_Scheme_HookableSchemeService_GetTableAsync.htm)|  
[GetTableAsync(String,
CancellationToken)](M_Tessa_Scheme_HookableSchemeService_GetTableAsync_1.htm)|  
[GetTablesAsync](M_Tessa_Scheme_HookableSchemeService_GetTablesAsync.htm)|  
[GetType](https://learn.microsoft.com/dotnet/api/system.object.gettype#system-
object-gettype)| Gets the
[Type](https://learn.microsoft.com/dotnet/api/system.type) of the current
instance.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[InvalidateCacheAsync](M_Tessa_Scheme_HookableSchemeService_InvalidateCacheAsync.htm)|
Инициирует сброс кэша.  
[InvalidateCacheIfChangedAsync](M_Tessa_Scheme_HookableSchemeService_InvalidateCacheIfChangedAsync.htm)|
Инициирует сброс кэша в случае, если есть изменения.  
[IsStorageExistsAsync](M_Tessa_Scheme_HookableSchemeService_IsStorageExistsAsync.htm)|  
[IsStorageUpToDateAsync](M_Tessa_Scheme_HookableSchemeService_IsStorageUpToDateAsync.htm)|  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[RemoveFunctionAsync](M_Tessa_Scheme_HookableSchemeService_RemoveFunctionAsync.htm)|  
[RemoveHook](M_Tessa_Platform_HookableService_1_RemoveHook.htm)|  
(Унаследован от
[HookableService<TService>](T_Tessa_Platform_HookableService_1.htm))  
[RemoveMigrationAsync](M_Tessa_Scheme_HookableSchemeService_RemoveMigrationAsync.htm)|  
[RemovePartitionAsync](M_Tessa_Scheme_HookableSchemeService_RemovePartitionAsync.htm)|  
[RemoveProcedureAsync](M_Tessa_Scheme_HookableSchemeService_RemoveProcedureAsync.htm)|  
[RemoveTableAsync](M_Tessa_Scheme_HookableSchemeService_RemoveTableAsync.htm)|  
[SaveDatabasePropertiesAsync](M_Tessa_Scheme_HookableSchemeService_SaveDatabasePropertiesAsync.htm)|  
[SaveFunctionAsync](M_Tessa_Scheme_HookableSchemeService_SaveFunctionAsync.htm)|  
[SaveMigrationAsync](M_Tessa_Scheme_HookableSchemeService_SaveMigrationAsync.htm)|  
[SavePartitionAsync](M_Tessa_Scheme_HookableSchemeService_SavePartitionAsync.htm)|  
[SaveProcedureAsync](M_Tessa_Scheme_HookableSchemeService_SaveProcedureAsync.htm)|  
[SaveTableAsync](M_Tessa_Scheme_HookableSchemeService_SaveTableAsync.htm)|  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[UpdateStorageAsync](M_Tessa_Scheme_HookableSchemeService_UpdateStorageAsync.htm)|  
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
