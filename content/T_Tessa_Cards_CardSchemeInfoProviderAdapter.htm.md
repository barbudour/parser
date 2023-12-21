# CardSchemeInfoProviderAdapter - класс
Адаптер объектов
[ICardSchemeInfoProvider](T_Tessa_Cards_ICardSchemeInfoProvider.htm) для
использования в качестве [ISchemeService](T_Tessa_Scheme_ISchemeService.htm).
Имеет логику получения таблиц, для остальных методов делегирует получение
объектов для указанного объекта
[SchemeDatabase](T_Tessa_Scheme_SchemeDatabase.htm), а для прочих действий
возвращает валидные значения по умолчанию.
Посредством объекта невозможность изменить схему данных.
##  __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class CardSchemeInfoProviderAdapter : ISchemeService
VB __Копировать
     Public NotInheritable Class CardSchemeInfoProviderAdapter
    	Implements ISchemeService
C++ __Копировать
     public ref class CardSchemeInfoProviderAdapter sealed : ISchemeService
F# __Копировать
     [<SealedAttribute>]
    type CardSchemeInfoProviderAdapter = 
        class
            interface ISchemeService
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ CardSchemeInfoProviderAdapter
Implements
    [ISchemeService](T_Tessa_Scheme_ISchemeService.htm)
##  __Конструкторы
[CardSchemeInfoProviderAdapter(ICardSchemeInfoProvider,
ISchemeService)](M_Tessa_Cards_CardSchemeInfoProviderAdapter__ctor.htm)|
Создаёт экземпляр класса с указанием объекта, для которого выполняется
адаптация к интерфейсу [ISchemeService](T_Tessa_Scheme_ISchemeService.htm), и
указанием объекта [ISchemeService](T_Tessa_Scheme_ISchemeService.htm) для
получения других объектов, кроме таблиц.  
---|---  
[CardSchemeInfoProviderAdapter(ICardSchemeInfoProvider,
SchemeDatabase)](M_Tessa_Cards_CardSchemeInfoProviderAdapter__ctor_1.htm)|
Создаёт экземпляр класса с указанием объекта, для которого выполняется
адаптация к интерфейсу [ISchemeService](T_Tessa_Scheme_ISchemeService.htm), и
опциональным указанием объекта
[SchemeDatabase](T_Tessa_Scheme_SchemeDatabase.htm) для получения других
объектов, кроме таблиц.  
## __Методы
[Equals](https://learn.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\))| Determines whether the specified object is
equal to the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
---|---  
[Finalize](https://learn.microsoft.com/dotnet/api/system.object.finalize#system-
object-finalize)| Allows an object to try to free resources and perform other
cleanup operations before it is reclaimed by garbage collection.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetDatabasePropertiesAsync](M_Tessa_Cards_CardSchemeInfoProviderAdapter_GetDatabasePropertiesAsync.htm)|  
[GetFunctionAsync(Guid,
CancellationToken)](M_Tessa_Cards_CardSchemeInfoProviderAdapter_GetFunctionAsync.htm)|  
[GetFunctionAsync(String,
CancellationToken)](M_Tessa_Cards_CardSchemeInfoProviderAdapter_GetFunctionAsync_1.htm)|  
[GetFunctionsAsync](M_Tessa_Cards_CardSchemeInfoProviderAdapter_GetFunctionsAsync.htm)|  
[GetHashCode](https://learn.microsoft.com/dotnet/api/system.object.gethashcode#system-
object-gethashcode)| Serves as the default hash function.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetMigrationAsync(Guid,
CancellationToken)](M_Tessa_Cards_CardSchemeInfoProviderAdapter_GetMigrationAsync.htm)|  
[GetMigrationAsync(String,
CancellationToken)](M_Tessa_Cards_CardSchemeInfoProviderAdapter_GetMigrationAsync_1.htm)|  
[GetMigrationsAsync](M_Tessa_Cards_CardSchemeInfoProviderAdapter_GetMigrationsAsync.htm)|  
[GetPartitionAsync(Guid,
CancellationToken)](M_Tessa_Cards_CardSchemeInfoProviderAdapter_GetPartitionAsync.htm)|  
[GetPartitionAsync(String,
CancellationToken)](M_Tessa_Cards_CardSchemeInfoProviderAdapter_GetPartitionAsync_1.htm)|  
[GetPartitionsAsync](M_Tessa_Cards_CardSchemeInfoProviderAdapter_GetPartitionsAsync.htm)|  
[GetProcedureAsync(Guid,
CancellationToken)](M_Tessa_Cards_CardSchemeInfoProviderAdapter_GetProcedureAsync.htm)|  
[GetProcedureAsync(String,
CancellationToken)](M_Tessa_Cards_CardSchemeInfoProviderAdapter_GetProcedureAsync_1.htm)|  
[GetProceduresAsync](M_Tessa_Cards_CardSchemeInfoProviderAdapter_GetProceduresAsync.htm)|  
[GetTableAsync(Guid,
CancellationToken)](M_Tessa_Cards_CardSchemeInfoProviderAdapter_GetTableAsync.htm)|  
[GetTableAsync(String,
CancellationToken)](M_Tessa_Cards_CardSchemeInfoProviderAdapter_GetTableAsync_1.htm)|  
[GetTablesAsync](M_Tessa_Cards_CardSchemeInfoProviderAdapter_GetTablesAsync.htm)|  
[GetType](https://learn.microsoft.com/dotnet/api/system.object.gettype#system-
object-gettype)| Gets the
[Type](https://learn.microsoft.com/dotnet/api/system.type) of the current
instance.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[RemoveFunctionAsync](M_Tessa_Cards_CardSchemeInfoProviderAdapter_RemoveFunctionAsync.htm)|  
[RemoveMigrationAsync](M_Tessa_Cards_CardSchemeInfoProviderAdapter_RemoveMigrationAsync.htm)|  
[RemovePartitionAsync](M_Tessa_Cards_CardSchemeInfoProviderAdapter_RemovePartitionAsync.htm)|  
[RemoveProcedureAsync](M_Tessa_Cards_CardSchemeInfoProviderAdapter_RemoveProcedureAsync.htm)|  
[RemoveTableAsync](M_Tessa_Cards_CardSchemeInfoProviderAdapter_RemoveTableAsync.htm)|  
[SaveDatabasePropertiesAsync](M_Tessa_Cards_CardSchemeInfoProviderAdapter_SaveDatabasePropertiesAsync.htm)|  
[SaveFunctionAsync](M_Tessa_Cards_CardSchemeInfoProviderAdapter_SaveFunctionAsync.htm)|  
[SaveMigrationAsync](M_Tessa_Cards_CardSchemeInfoProviderAdapter_SaveMigrationAsync.htm)|  
[SavePartitionAsync](M_Tessa_Cards_CardSchemeInfoProviderAdapter_SavePartitionAsync.htm)|  
[SaveProcedureAsync](M_Tessa_Cards_CardSchemeInfoProviderAdapter_SaveProcedureAsync.htm)|  
[SaveTableAsync](M_Tessa_Cards_CardSchemeInfoProviderAdapter_SaveTableAsync.htm)|  
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
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
