# HookableSchemeServiceProxy - класс
##  __Definition
 **Пространство имён:** [Tessa.Scheme](N_Tessa_Scheme.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public class HookableSchemeServiceProxy : HookableServiceProxy<ISchemeService>, 
    	ISchemeServiceWithCache, ISchemeService, ISchemeServiceWithStorage
VB __Копировать
     Public Class HookableSchemeServiceProxy
    	Inherits HookableServiceProxy(Of ISchemeService)
    	Implements ISchemeServiceWithCache, ISchemeService, ISchemeServiceWithStorage
C++ __Копировать
     public ref class HookableSchemeServiceProxy : public HookableServiceProxy<ISchemeService^>, 
    	ISchemeServiceWithCache, ISchemeService, ISchemeServiceWithStorage
F# __Копировать
     type HookableSchemeServiceProxy = 
        class
            inherit HookableServiceProxy<ISchemeService>
            interface ISchemeServiceWithCache
            interface ISchemeService
            interface ISchemeServiceWithStorage
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[HookableServiceHook](T_Tessa_Platform_HookableServiceHook_1.htm)<[ISchemeService](T_Tessa_Scheme_ISchemeService.htm)> __[HookableServiceProxy](T_Tessa_Platform_HookableServiceProxy_1.htm)<[ISchemeService](T_Tessa_Scheme_ISchemeService.htm)> __ HookableSchemeServiceProxy
Implements
    [ISchemeService](T_Tessa_Scheme_ISchemeService.htm), [ISchemeServiceWithCache](T_Tessa_Scheme_ISchemeServiceWithCache.htm), [ISchemeServiceWithStorage](T_Tessa_Scheme_ISchemeServiceWithStorage.htm)
##  __Конструкторы
[HookableSchemeServiceProxy](M_Tessa_Scheme_HookableSchemeServiceProxy__ctor.htm)|
Инициализирует новый экземпляр класса HookableSchemeServiceProxy  
---|---  
##  __Свойства
[NextHook](P_Tessa_Platform_HookableServiceHook_1_NextHook.htm)|  
(Унаследован от
[HookableServiceHook<TService>](T_Tessa_Platform_HookableServiceHook_1.htm))  
---|---  
[ProxiedService](P_Tessa_Platform_HookableServiceProxy_1_ProxiedService.htm)|  
(Унаследован от
[HookableServiceProxy<TService>](T_Tessa_Platform_HookableServiceProxy_1.htm))  
[ServiceVersion](P_Tessa_Scheme_HookableSchemeServiceProxy_ServiceVersion.htm)|  
## __Методы
[CreateStorageAsync](M_Tessa_Scheme_HookableSchemeServiceProxy_CreateStorageAsync.htm)|  
---|---  
[EnsureInvalidateCacheSubscribedAsync](M_Tessa_Scheme_HookableSchemeServiceProxy_EnsureInvalidateCacheSubscribedAsync.htm)|
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
[GetDatabasePropertiesAsync](M_Tessa_Scheme_HookableSchemeServiceProxy_GetDatabasePropertiesAsync.htm)|  
[GetFunctionAsync(Guid,
CancellationToken)](M_Tessa_Scheme_HookableSchemeServiceProxy_GetFunctionAsync.htm)|  
[GetFunctionAsync(String,
CancellationToken)](M_Tessa_Scheme_HookableSchemeServiceProxy_GetFunctionAsync_1.htm)|  
[GetFunctionsAsync](M_Tessa_Scheme_HookableSchemeServiceProxy_GetFunctionsAsync.htm)|  
[GetHashCode](https://learn.microsoft.com/dotnet/api/system.object.gethashcode#system-
object-gethashcode)| Serves as the default hash function.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetMigrationAsync(Guid,
CancellationToken)](M_Tessa_Scheme_HookableSchemeServiceProxy_GetMigrationAsync.htm)|  
[GetMigrationAsync(String,
CancellationToken)](M_Tessa_Scheme_HookableSchemeServiceProxy_GetMigrationAsync_1.htm)|  
[GetMigrationsAsync](M_Tessa_Scheme_HookableSchemeServiceProxy_GetMigrationsAsync.htm)|  
[GetPartitionAsync(Guid,
CancellationToken)](M_Tessa_Scheme_HookableSchemeServiceProxy_GetPartitionAsync.htm)|  
[GetPartitionAsync(String,
CancellationToken)](M_Tessa_Scheme_HookableSchemeServiceProxy_GetPartitionAsync_1.htm)|  
[GetPartitionsAsync](M_Tessa_Scheme_HookableSchemeServiceProxy_GetPartitionsAsync.htm)|  
[GetProcedureAsync(Guid,
CancellationToken)](M_Tessa_Scheme_HookableSchemeServiceProxy_GetProcedureAsync.htm)|  
[GetProcedureAsync(String,
CancellationToken)](M_Tessa_Scheme_HookableSchemeServiceProxy_GetProcedureAsync_1.htm)|  
[GetProceduresAsync](M_Tessa_Scheme_HookableSchemeServiceProxy_GetProceduresAsync.htm)|  
[GetStorageVersionAsync](M_Tessa_Scheme_HookableSchemeServiceProxy_GetStorageVersionAsync.htm)|  
[GetTableAsync(Guid,
CancellationToken)](M_Tessa_Scheme_HookableSchemeServiceProxy_GetTableAsync.htm)|  
[GetTableAsync(String,
CancellationToken)](M_Tessa_Scheme_HookableSchemeServiceProxy_GetTableAsync_1.htm)|  
[GetTablesAsync](M_Tessa_Scheme_HookableSchemeServiceProxy_GetTablesAsync.htm)|  
[GetType](https://learn.microsoft.com/dotnet/api/system.object.gettype#system-
object-gettype)| Gets the
[Type](https://learn.microsoft.com/dotnet/api/system.type) of the current
instance.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[InvalidateCacheAsync](M_Tessa_Scheme_HookableSchemeServiceProxy_InvalidateCacheAsync.htm)|
Инициирует сброс кэша.  
[InvalidateCacheIfChangedAsync](M_Tessa_Scheme_HookableSchemeServiceProxy_InvalidateCacheIfChangedAsync.htm)|
Инициирует сброс кэша в случае, если есть изменения.  
[IsStorageExistsAsync](M_Tessa_Scheme_HookableSchemeServiceProxy_IsStorageExistsAsync.htm)|  
[IsStorageUpToDateAsync](M_Tessa_Scheme_HookableSchemeServiceProxy_IsStorageUpToDateAsync.htm)|  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[RemoveFunctionAsync](M_Tessa_Scheme_HookableSchemeServiceProxy_RemoveFunctionAsync.htm)|  
[RemoveMigrationAsync](M_Tessa_Scheme_HookableSchemeServiceProxy_RemoveMigrationAsync.htm)|  
[RemovePartitionAsync](M_Tessa_Scheme_HookableSchemeServiceProxy_RemovePartitionAsync.htm)|  
[RemoveProcedureAsync](M_Tessa_Scheme_HookableSchemeServiceProxy_RemoveProcedureAsync.htm)|  
[RemoveTableAsync](M_Tessa_Scheme_HookableSchemeServiceProxy_RemoveTableAsync.htm)|  
[SaveDatabasePropertiesAsync](M_Tessa_Scheme_HookableSchemeServiceProxy_SaveDatabasePropertiesAsync.htm)|  
[SaveFunctionAsync](M_Tessa_Scheme_HookableSchemeServiceProxy_SaveFunctionAsync.htm)|  
[SaveMigrationAsync](M_Tessa_Scheme_HookableSchemeServiceProxy_SaveMigrationAsync.htm)|  
[SavePartitionAsync](M_Tessa_Scheme_HookableSchemeServiceProxy_SavePartitionAsync.htm)|  
[SaveProcedureAsync](M_Tessa_Scheme_HookableSchemeServiceProxy_SaveProcedureAsync.htm)|  
[SaveTableAsync](M_Tessa_Scheme_HookableSchemeServiceProxy_SaveTableAsync.htm)|  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[UpdateStorageAsync](M_Tessa_Scheme_HookableSchemeServiceProxy_UpdateStorageAsync.htm)|  
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
