# RoleDeputyIsActiveQueryExecutor - класс
Выполняет построение команд для активации и деактивации записей о замещении.
Активация подразумевает установленный бит в колонке IsActive.
## __Definition
 **Пространство имён:** [Tessa.Roles](N_Tessa_Roles.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class RoleDeputyIsActiveQueryExecutor
VB __Копировать
     Public NotInheritable Class RoleDeputyIsActiveQueryExecutor
C++ __Копировать
     public ref class RoleDeputyIsActiveQueryExecutor sealed
F# __Копировать
     [<SealedAttribute>]
    type RoleDeputyIsActiveQueryExecutor = class end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ RoleDeputyIsActiveQueryExecutor
##  __Конструкторы
[RoleDeputyIsActiveQueryExecutor](M_Tessa_Roles_RoleDeputyIsActiveQueryExecutor__ctor.htm)|
Инициализирует новый экземпляр класса RoleDeputyIsActiveQueryExecutor  
---|---  
##  __Свойства
[Count](P_Tessa_Roles_RoleDeputyIsActiveQueryExecutor_Count.htm)|  Общее
количество записей с замещением, которые требуется активировать и
деактивировать. Значение равно количество запросов, которое будет
сгенерировано при обращении к методу [ExecuteAsync(IQueryExecutor,
IQueryBuilderFactory,
CancellationToken)](M_Tessa_Roles_RoleDeputyIsActiveQueryExecutor_ExecuteAsync.htm).  
---|---  
## __Методы
[Activate](M_Tessa_Roles_RoleDeputyIsActiveQueryExecutor_Activate.htm)|
Добавляет идентификатор строки с замещением в список на активацию. Если
идентификатор был добавлен в список на деактивацию, то он удаляется оттуда.  
---|---  
[Deactivate](M_Tessa_Roles_RoleDeputyIsActiveQueryExecutor_Deactivate.htm)|
Добавляет идентификатор строки с замещением в список на деактивацию. Если
идентификатор был добавлен в список на активацию, то он удаляется оттуда.  
[Equals](https://learn.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\))| Determines whether the specified object is
equal to the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[ExecuteAsync](M_Tessa_Roles_RoleDeputyIsActiveQueryExecutor_ExecuteAsync.htm)|
Выполняет команды на активацию и деактивацию записей на замещение. Не очищает
списки на активацию и деактивацию.  
[Finalize](https://learn.microsoft.com/dotnet/api/system.object.finalize#system-
object-finalize)| Allows an object to try to free resources and perform other
cleanup operations before it is reclaimed by garbage collection.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetHashCode](https://learn.microsoft.com/dotnet/api/system.object.gethashcode#system-
object-gethashcode)| Serves as the default hash function.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
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
[Reset](M_Tessa_Roles_RoleDeputyIsActiveQueryExecutor_Reset.htm)|  Очищает все
списки на активацию и деактивацию. Позволяет повторно наполнить списки и
выполнить активацию и деактивацию.  
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
##  __См. также
#### Ссылки
[Tessa.Roles - пространство имён](N_Tessa_Roles.htm)
