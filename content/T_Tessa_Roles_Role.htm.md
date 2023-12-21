# Role - класс
Роль.
## __Definition
 **Пространство имён:** [Tessa.Roles](N_Tessa_Roles.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
    [DataContractAttribute]
    [TableAttribute("Roles", IsColumnAttributeRequired = false)]
    public class Role : NamedEntry
VB __Копировать
    <DataContractAttribute>
    <TableAttribute("Roles", IsColumnAttributeRequired := false)>
    Public Class Role
    	Inherits NamedEntry
C++ __Копировать
    [DataContractAttribute]
    [TableAttribute(L"Roles", IsColumnAttributeRequired = false)]
    public ref class Role : public NamedEntry
F# __Копировать
     [<DataContractAttribute>]
    [<TableAttribute("Roles", IsColumnAttributeRequired = false)>]
    type Role = 
        class
            inherit NamedEntry
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[NamedEntry](T_Tessa_Platform_NamedEntry.htm) __ Role
Derived
[Tessa.Roles.ContextRole](T_Tessa_Roles_ContextRole.htm)
[Tessa.Roles.DepartmentRole](T_Tessa_Roles_DepartmentRole.htm)
[Tessa.Roles.DynamicRole](T_Tessa_Roles_DynamicRole.htm)
[Tessa.Roles.MetaRole](T_Tessa_Roles_MetaRole.htm)
[Tessa.Roles.PersonalRole](T_Tessa_Roles_PersonalRole.htm)
[Tessa.Roles.StaticRole](T_Tessa_Roles_StaticRole.htm)
[Tessa.Roles.TaskRole](T_Tessa_Roles_TaskRole.htm)
Подробнее __Less __
##  __Конструкторы
[Role](M_Tessa_Roles_Role__ctor.htm)| Инициализирует новый экземпляр класса
Role  
---|---  
##  __Свойства
[Deputies](P_Tessa_Roles_Role_Deputies.htm)|  Заместители на роль.  
---|---  
[HasParent](P_Tessa_Roles_Role_HasParent.htm)|  Признак того, что заданная
роль имеет родительскую роль.  
[Hidden](P_Tessa_Roles_Role_Hidden.htm)|  Признак "скрывать при выборе"  
[ID](P_Tessa_Platform_NamedEntry_ID.htm)| Идентификатор объекта.  
(Унаследован от [NamedEntry](T_Tessa_Platform_NamedEntry.htm))  
[Modified](P_Tessa_Roles_Role_Modified.htm)|  Дата и время последнего
изменения роли.  
[ModifiedBy](P_Tessa_Roles_Role_ModifiedBy.htm)|  Пользователь, последним
выполнивший изменение роли.  
[ModifiedByID](P_Tessa_Roles_Role_ModifiedByID.htm)|  Идентификатор
пользователя, последним выполнившего изменение роли. Если роль была изменена
системой, то используйте метод
[SetModifiedBySystem()](M_Tessa_Roles_Role_SetModifiedBySystem.htm).  
[ModifiedByName](P_Tessa_Roles_Role_ModifiedByName.htm)|  Имя пользователя,
последним выполнившего изменение роли. Если роль была изменена системой, то
используйте метод
[SetModifiedBySystem()](M_Tessa_Roles_Role_SetModifiedBySystem.htm).  
[Name](P_Tessa_Platform_NamedEntry_Name.htm)| Отображаемое имя объекта.  
(Унаследован от [NamedEntry](T_Tessa_Platform_NamedEntry.htm))  
[Parent](P_Tessa_Roles_Role_Parent.htm)|  Родительская роль.  
[ParentID](P_Tessa_Roles_Role_ParentID.htm)|  Идентификатор родительской роли
или null, если родительская роль отсутствует.  
[ParentName](P_Tessa_Roles_Role_ParentName.htm)|  Имя родительской роли или
null, если родительская роль отсутствует.  
[RoleType](P_Tessa_Roles_Role_RoleType.htm)|  Тип роли.  
[Users](P_Tessa_Roles_Role_Users.htm)|  Состав роли.  
## __Методы
[Equals(INamedEntry)](M_Tessa_Platform_NamedEntry_Equals_1.htm)| Сравнивает
текущий объект с заданным.  
(Унаследован от [NamedEntry](T_Tessa_Platform_NamedEntry.htm))  
---|---  
[Equals(Object)](M_Tessa_Platform_NamedEntry_Equals.htm)| Сравнивает текущий
объект с заданным.  
(Унаследован от [NamedEntry](T_Tessa_Platform_NamedEntry.htm))  
[Finalize](https://learn.microsoft.com/dotnet/api/system.object.finalize#system-
object-finalize)| Allows an object to try to free resources and perform other
cleanup operations before it is reclaimed by garbage collection.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetHashCode](M_Tessa_Platform_NamedEntry_GetHashCode.htm)| Возвращает хеш-код
объекта.  
(Унаследован от [NamedEntry](T_Tessa_Platform_NamedEntry.htm))  
[GetName](M_Tessa_Platform_NamedEntry_GetName.htm)|  Возвращает имя объекта.  
(Унаследован от [NamedEntry](T_Tessa_Platform_NamedEntry.htm))  
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
[SetModifiedBySystem](M_Tessa_Roles_Role_SetModifiedBySystem.htm)|
Устанавливает свойства [ModifiedByID](P_Tessa_Roles_Role_ModifiedByID.htm) и
[ModifiedByName](P_Tessa_Roles_Role_ModifiedByName.htm) таким образом, чтобы
установить, что роль была изменена системой.  
[ToRoleUser](M_Tessa_Roles_Role_ToRoleUser.htm)|  Возвращает информацию о
пользователе по общей информации о персональной роли. Метод следует вызывать
только в том случае, если текущая роль является персональной, при этом полная
информация по персональной роли [PersonalRole](T_Tessa_Roles_PersonalRole.htm)
может быть не загружена.  
[ToString](M_Tessa_Platform_NamedEntry_ToString.htm)| Возвращает строковое
представление объекта.  
(Унаследован от [NamedEntry](T_Tessa_Platform_NamedEntry.htm))  
[UpdateFromAssociations](M_Tessa_Roles_Role_UpdateFromAssociations.htm)|
Обновляет значения ссылочных полей из всех объектов-ассоциаций, на которые
установлены ссылки.  
(Переопределяет
[NamedEntry.UpdateFromAssociations()](M_Tessa_Platform_NamedEntry_UpdateFromAssociations.htm))  
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
