# MetaRoleDmlQueryExecutor - класс
Выполняет построение DML-команд для SQL Server, изменяющих состав списка
метаролей.
## __Definition
 **Пространство имён:** [Tessa.Roles](N_Tessa_Roles.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class MetaRoleDmlQueryExecutor
VB __Копировать
     Public NotInheritable Class MetaRoleDmlQueryExecutor
C++ __Копировать
     public ref class MetaRoleDmlQueryExecutor sealed
F# __Копировать
     [<SealedAttribute>]
    type MetaRoleDmlQueryExecutor = class end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ MetaRoleDmlQueryExecutor
##  __Заметки
DML - Data Manipulation Language; это подмножество языка SQL, которое включает
команды INSERT, UPDATE и DELETE.
## __Конструкторы
[MetaRoleDmlQueryExecutor(Guid,
String)](M_Tessa_Roles_MetaRoleDmlQueryExecutor__ctor.htm)|  Создаёт экземпляр
объекта с указанием идентификатора типа карточки метароли. Для изменяемых
метаролей указывается, что изменения произвела система.  
---|---  
[MetaRoleDmlQueryExecutor(Guid, String, Guid,
String)](M_Tessa_Roles_MetaRoleDmlQueryExecutor__ctor_1.htm)|  Создаёт
экземпляр объекта с указанием идентификатора типа карточки метароли, а также
идентификатора и имени пользователя, изменившего метароли.  
## __Свойства
[CardTypeCaption](P_Tessa_Roles_MetaRoleDmlQueryExecutor_CardTypeCaption.htm)|
Отображаемое имя карточки метароли, используемое при добавлении записей о
метаролях в таблицу [Instances].  
---|---  
[CardTypeID](P_Tessa_Roles_MetaRoleDmlQueryExecutor_CardTypeID.htm)|  Тип
карточки метароли, используемый при добавлении записей о метаролях в таблицу
[Instances].  
[ItemsToDelete](P_Tessa_Roles_MetaRoleDmlQueryExecutor_ItemsToDelete.htm)|
Коллекция ролей, которые должны быть удалены.  
[ItemsToInsert](P_Tessa_Roles_MetaRoleDmlQueryExecutor_ItemsToInsert.htm)|
Коллекция ролей, которые должны быть добавлены.  
[ItemsToUpdate](P_Tessa_Roles_MetaRoleDmlQueryExecutor_ItemsToUpdate.htm)|
Коллекция ролей, которые должны быть обновлены.  
[ModifiedByID](P_Tessa_Roles_MetaRoleDmlQueryExecutor_ModifiedByID.htm)|
Идентификатор пользователя, изменяющего метароли.  
[ModifiedByName](P_Tessa_Roles_MetaRoleDmlQueryExecutor_ModifiedByName.htm)|
Имя пользователя, изменяющего метароли.  
## __Методы
[AddForDelete](M_Tessa_Roles_MetaRoleDmlQueryExecutor_AddForDelete.htm)|
Добавляет метароль к списку удаляемых метаролей.  
---|---  
[AddForInsert](M_Tessa_Roles_MetaRoleDmlQueryExecutor_AddForInsert.htm)|
Добавляет метароль к списку создаваемых метаролей.  
[AddForUpdate](M_Tessa_Roles_MetaRoleDmlQueryExecutor_AddForUpdate.htm)|
Добавляет метароль к списку обновляемых метаролей.  
[Equals](https://learn.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\))| Determines whether the specified object is
equal to the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[ExecuteDeleteAsync](M_Tessa_Roles_MetaRoleDmlQueryExecutor_ExecuteDeleteAsync.htm)|
Создаёт и выполняет SQL-команды, удаляющие метароли.  
[ExecuteInsertAndUpdateAsync](M_Tessa_Roles_MetaRoleDmlQueryExecutor_ExecuteInsertAndUpdateAsync.htm)|
Создаёт и выполняет SQL-команды, добавляющие метароли или выполняющие их
изменение.  
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
[HasDeleteData](M_Tessa_Roles_MetaRoleDmlQueryExecutor_HasDeleteData.htm)|
Определяет, содержит ли объект информацию, для которой будут созданы SQL-
запросы посредством вызова метода
[ExecuteDeleteAsync(TransactionQueryExecutor, IQueryBuilderFactory,
CancellationToken)](M_Tessa_Roles_MetaRoleDmlQueryExecutor_ExecuteDeleteAsync.htm).  
[HasInsertOrUpdateData](M_Tessa_Roles_MetaRoleDmlQueryExecutor_HasInsertOrUpdateData.htm)|
Определяет, содержит ли объект информацию, для которой будут созданы SQL-
запросы посредством вызова метода [ExecuteInsertAndUpdateAsync(IDbScope,
CancellationToken)](M_Tessa_Roles_MetaRoleDmlQueryExecutor_ExecuteInsertAndUpdateAsync.htm).  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
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
