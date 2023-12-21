# RoleUserDmlQueryExecutor - класс
Выполняет построение DML-команды для SQL Server, управляющей содержимым
состава указанной роли.
## __Definition
 **Пространство имён:** [Tessa.Roles](N_Tessa_Roles.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class RoleUserDmlQueryExecutor
VB __Копировать
     Public NotInheritable Class RoleUserDmlQueryExecutor
C++ __Копировать
     public ref class RoleUserDmlQueryExecutor sealed
F# __Копировать
     [<SealedAttribute>]
    type RoleUserDmlQueryExecutor = class end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ RoleUserDmlQueryExecutor
##  __Заметки
DML - Data Manipulation Language; это подмножество языка SQL, которое включает
команды INSERT, UPDATE и DELETE.
## __Конструкторы
[RoleUserDmlQueryExecutor](M_Tessa_Roles_RoleUserDmlQueryExecutor__ctor.htm)|
Создаёт экземпляр объекта с указанием идентификатора роли, состав которой
должен быть изменён, типа роли и признака замещения.  
---|---  
## __Свойства
[IsDeputy](P_Tessa_Roles_RoleUserDmlQueryExecutor_IsDeputy.htm)|  Признак
того, являются ли все изменяемые записи записями о замещении или нет.  
---|---  
[ItemsToDelete](P_Tessa_Roles_RoleUserDmlQueryExecutor_ItemsToDelete.htm)|
Коллекция записей о пользователях, которые должны быть удалены.  
[ItemsToInsert](P_Tessa_Roles_RoleUserDmlQueryExecutor_ItemsToInsert.htm)|
Коллекция записей о пользователях, которые должны быть добавлены.  
[ItemsToUpdate](P_Tessa_Roles_RoleUserDmlQueryExecutor_ItemsToUpdate.htm)|
Коллекция записей о пользователях, которые должны быть обновлены.  
[RoleID](P_Tessa_Roles_RoleUserDmlQueryExecutor_RoleID.htm)|  Идентификатор
роли, состав которой должен быть изменён, или null, если объект используется
для изменения нескольких ролей.  
[RoleType](P_Tessa_Roles_RoleUserDmlQueryExecutor_RoleType.htm)|  Тип роли,
состав которой должен быть изменён, или null, если тип роли определяется
индивидуально для каждой записи о составе.  
## __Методы
[AddForDelete](M_Tessa_Roles_RoleUserDmlQueryExecutor_AddForDelete.htm)|
Добавляет запись о пользователе, который входит в состав роли, к списку
удаляемых записей.  
---|---  
[AddForInsert](M_Tessa_Roles_RoleUserDmlQueryExecutor_AddForInsert.htm)|
Добавляет запись о пользователе, который входит в состав роли, к списку
создаваемых записей.  
[AddForUpdate](M_Tessa_Roles_RoleUserDmlQueryExecutor_AddForUpdate.htm)|
Добавляет запись о пользователе, который входит в состав роли, к списку
обновляемых записей.  
[Equals](https://learn.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\))| Determines whether the specified object is
equal to the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[ExecuteAsync](M_Tessa_Roles_RoleUserDmlQueryExecutor_ExecuteAsync.htm)|
Создаёт и выполняет SQL-команды, изменяющие состав роли.  
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
[HasData](M_Tessa_Roles_RoleUserDmlQueryExecutor_HasData.htm)|  Определяет,
содержит ли объект информацию, для которой будут созданы SQL-запросы.  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[RemoveForDelete](M_Tessa_Roles_RoleUserDmlQueryExecutor_RemoveForDelete.htm)|
Удаляет записи о составе роли из списка удаляемых записей для пользователя с
идентификатором userID, находящимся в составе роли с идентификатором roleID, и
возвращает количество удалённых записей.  
[RemoveForInsert](M_Tessa_Roles_RoleUserDmlQueryExecutor_RemoveForInsert.htm)|
Удаляет записи о составе роли из списка создаваемых записей для пользователя с
идентификатором userID, находящимся в составе роли с идентификатором roleID, и
возвращает количество удалённых записей.  
[RemoveForUpdate](M_Tessa_Roles_RoleUserDmlQueryExecutor_RemoveForUpdate.htm)|
Удаляет записи о составе роли из списка изменяемых записей для пользователя с
идентификатором userID, находящимся в составе роли с идентификатором roleID, и
возвращает количество удалённых записей.  
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
