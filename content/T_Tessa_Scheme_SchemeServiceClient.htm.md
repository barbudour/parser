# SchemeServiceClient - класс
##  __Definition
 **Пространство имён:** [Tessa.Scheme](N_Tessa_Scheme.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class SchemeServiceClient : ISchemeServiceWithCache, 
    	ISchemeService
VB __Копировать
     Public NotInheritable Class SchemeServiceClient
    	Implements ISchemeServiceWithCache, ISchemeService
C++ __Копировать
     public ref class SchemeServiceClient sealed : ISchemeServiceWithCache, 
    	ISchemeService
F# __Копировать
     [<SealedAttribute>]
    type SchemeServiceClient = 
        class
            interface ISchemeServiceWithCache
            interface ISchemeService
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ SchemeServiceClient
Implements
    [ISchemeService](T_Tessa_Scheme_ISchemeService.htm), [ISchemeServiceWithCache](T_Tessa_Scheme_ISchemeServiceWithCache.htm)
##  __Конструкторы
[SchemeServiceClient](M_Tessa_Scheme_SchemeServiceClient__ctor.htm)|  Создаёт
экземпляр класса с указанием его зависимостей.  
---|---  
## __Методы
[EnsureInvalidateCacheSubscribedAsync](M_Tessa_Scheme_SchemeServiceClient_EnsureInvalidateCacheSubscribedAsync.htm)|
Производит подписку на событие сброса кэша, если необходимо.  
---|---  
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
[GetDatabasePropertiesAsync](M_Tessa_Scheme_SchemeServiceClient_GetDatabasePropertiesAsync.htm)|  
[GetFunctionAsync(Guid,
CancellationToken)](M_Tessa_Scheme_SchemeServiceClient_GetFunctionAsync.htm)|  
[GetFunctionAsync(String,
CancellationToken)](M_Tessa_Scheme_SchemeServiceClient_GetFunctionAsync_1.htm)|  
[GetFunctionsAsync](M_Tessa_Scheme_SchemeServiceClient_GetFunctionsAsync.htm)|  
[GetHashCode](https://learn.microsoft.com/dotnet/api/system.object.gethashcode#system-
object-gethashcode)| Serves as the default hash function.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetMigrationAsync(Guid,
CancellationToken)](M_Tessa_Scheme_SchemeServiceClient_GetMigrationAsync.htm)|  
[GetMigrationAsync(String,
CancellationToken)](M_Tessa_Scheme_SchemeServiceClient_GetMigrationAsync_1.htm)|  
[GetMigrationsAsync](M_Tessa_Scheme_SchemeServiceClient_GetMigrationsAsync.htm)|  
[GetPartitionAsync(Guid,
CancellationToken)](M_Tessa_Scheme_SchemeServiceClient_GetPartitionAsync.htm)|  
[GetPartitionAsync(String,
CancellationToken)](M_Tessa_Scheme_SchemeServiceClient_GetPartitionAsync_1.htm)|  
[GetPartitionsAsync](M_Tessa_Scheme_SchemeServiceClient_GetPartitionsAsync.htm)|  
[GetProcedureAsync(Guid,
CancellationToken)](M_Tessa_Scheme_SchemeServiceClient_GetProcedureAsync.htm)|  
[GetProcedureAsync(String,
CancellationToken)](M_Tessa_Scheme_SchemeServiceClient_GetProcedureAsync_1.htm)|  
[GetProceduresAsync](M_Tessa_Scheme_SchemeServiceClient_GetProceduresAsync.htm)|  
[GetTableAsync(Guid,
CancellationToken)](M_Tessa_Scheme_SchemeServiceClient_GetTableAsync.htm)|  
[GetTableAsync(String,
CancellationToken)](M_Tessa_Scheme_SchemeServiceClient_GetTableAsync_1.htm)|  
[GetTablesAsync](M_Tessa_Scheme_SchemeServiceClient_GetTablesAsync.htm)|  
[GetType](https://learn.microsoft.com/dotnet/api/system.object.gettype#system-
object-gettype)| Gets the
[Type](https://learn.microsoft.com/dotnet/api/system.type) of the current
instance.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[InvalidateCacheAsync](M_Tessa_Scheme_SchemeServiceClient_InvalidateCacheAsync.htm)|
Инициирует сброс кэша.  
[InvalidateCacheIfChangedAsync](M_Tessa_Scheme_SchemeServiceClient_InvalidateCacheIfChangedAsync.htm)|
Инициирует сброс кэша в случае, если есть изменения.  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[RemoveFunctionAsync](M_Tessa_Scheme_SchemeServiceClient_RemoveFunctionAsync.htm)|  
[RemoveMigrationAsync](M_Tessa_Scheme_SchemeServiceClient_RemoveMigrationAsync.htm)|  
[RemovePartitionAsync](M_Tessa_Scheme_SchemeServiceClient_RemovePartitionAsync.htm)|  
[RemoveProcedureAsync](M_Tessa_Scheme_SchemeServiceClient_RemoveProcedureAsync.htm)|  
[RemoveTableAsync](M_Tessa_Scheme_SchemeServiceClient_RemoveTableAsync.htm)|  
[SaveDatabasePropertiesAsync](M_Tessa_Scheme_SchemeServiceClient_SaveDatabasePropertiesAsync.htm)|  
[SaveFunctionAsync](M_Tessa_Scheme_SchemeServiceClient_SaveFunctionAsync.htm)|  
[SaveMigrationAsync](M_Tessa_Scheme_SchemeServiceClient_SaveMigrationAsync.htm)|  
[SavePartitionAsync](M_Tessa_Scheme_SchemeServiceClient_SavePartitionAsync.htm)|  
[SaveProcedureAsync](M_Tessa_Scheme_SchemeServiceClient_SaveProcedureAsync.htm)|  
[SaveTableAsync](M_Tessa_Scheme_SchemeServiceClient_SaveTableAsync.htm)|  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
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
