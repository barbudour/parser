# PersonalRole - класс
Персональная роль (пользователь).
## __Definition
 **Пространство имён:** [Tessa.Roles](N_Tessa_Roles.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
    [DataContractAttribute]
    [TableAttribute("PersonalRoles", IsColumnAttributeRequired = false)]
    public sealed class PersonalRole : Role, 
    	IRoleUser
VB __Копировать
    <DataContractAttribute>
    <TableAttribute("PersonalRoles", IsColumnAttributeRequired := false)>
    Public NotInheritable Class PersonalRole
    	Inherits Role
    	Implements IRoleUser
C++ __Копировать
    [DataContractAttribute]
    [TableAttribute(L"PersonalRoles", IsColumnAttributeRequired = false)]
    public ref class PersonalRole sealed : public Role, 
    	IRoleUser
F# __Копировать
     [<SealedAttribute>]
    [<DataContractAttribute>]
    [<TableAttribute("PersonalRoles", IsColumnAttributeRequired = false)>]
    type PersonalRole = 
        class
            inherit Role
            interface IRoleUser
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[NamedEntry](T_Tessa_Platform_NamedEntry.htm) __[Role](T_Tessa_Roles_Role.htm) __ PersonalRole
Implements
    [IRoleUser](T_Tessa_Roles_IRoleUser.htm)
##  __Конструкторы
[PersonalRole](M_Tessa_Roles_PersonalRole__ctor.htm)| Создаёт экземпляр класса
с параметрами по умолчанию.  
---|---  
##  __Свойства
[BirthDate](P_Tessa_Roles_PersonalRole_BirthDate.htm)|  Дата рождения или
null, если дата не задана.  
---|---  
[Deputies](P_Tessa_Roles_Role_Deputies.htm)|  Заместители на роль.  
(Унаследован от [Role](T_Tessa_Roles_Role.htm))  
[Email](P_Tessa_Roles_PersonalRole_Email.htm)|  Адрес электронной почты или
null, если адрес не задан.  
[Fax](P_Tessa_Roles_PersonalRole_Fax.htm)|  Факс или null, если факс не задан.  
[FirstName](P_Tessa_Roles_PersonalRole_FirstName.htm)|  Имя или null, если имя
не задано.  
[FullName](P_Tessa_Roles_PersonalRole_FullName.htm)|  Полное имя пользователя.  
[HasParent](P_Tessa_Roles_Role_HasParent.htm)|  Признак того, что заданная
роль имеет родительскую роль.  
(Унаследован от [Role](T_Tessa_Roles_Role.htm))  
[Hidden](P_Tessa_Roles_Role_Hidden.htm)|  Признак "скрывать при выборе"  
(Унаследован от [Role](T_Tessa_Roles_Role.htm))  
[HomePhone](P_Tessa_Roles_PersonalRole_HomePhone.htm)|  Номер домашнего
телефона или null, если номер не задан.  
[ID](P_Tessa_Platform_NamedEntry_ID.htm)| Идентификатор объекта.  
(Унаследован от [NamedEntry](T_Tessa_Platform_NamedEntry.htm))  
[IPPhone](P_Tessa_Roles_PersonalRole_IPPhone.htm)|  Номер IP-телефона или
null, если номер не задан.  
[LastName](P_Tessa_Roles_PersonalRole_LastName.htm)|  Фамилия или null, если
фамилия не задана.  
[Login](P_Tessa_Roles_PersonalRole_Login.htm)|  Имя аккаунта в Active
Directory или null, если имя аккаунта не задано.  
[MiddleName](P_Tessa_Roles_PersonalRole_MiddleName.htm)|  Отчество или null,
если отчество не задано.  
[MobilePhone](P_Tessa_Roles_PersonalRole_MobilePhone.htm)|  Номер мобильного
телефона или null, если номер не задан.  
[Modified](P_Tessa_Roles_Role_Modified.htm)|  Дата и время последнего
изменения роли.  
(Унаследован от [Role](T_Tessa_Roles_Role.htm))  
[ModifiedBy](P_Tessa_Roles_Role_ModifiedBy.htm)|  Пользователь, последним
выполнивший изменение роли.  
(Унаследован от [Role](T_Tessa_Roles_Role.htm))  
[ModifiedByID](P_Tessa_Roles_Role_ModifiedByID.htm)|  Идентификатор
пользователя, последним выполнившего изменение роли. Если роль была изменена
системой, то используйте метод
[SetModifiedBySystem()](M_Tessa_Roles_Role_SetModifiedBySystem.htm).  
(Унаследован от [Role](T_Tessa_Roles_Role.htm))  
[ModifiedByName](P_Tessa_Roles_Role_ModifiedByName.htm)|  Имя пользователя,
последним выполнившего изменение роли. Если роль была изменена системой, то
используйте метод
[SetModifiedBySystem()](M_Tessa_Roles_Role_SetModifiedBySystem.htm).  
(Унаследован от [Role](T_Tessa_Roles_Role.htm))  
[Name](P_Tessa_Platform_NamedEntry_Name.htm)| Отображаемое имя объекта.  
(Унаследован от [NamedEntry](T_Tessa_Platform_NamedEntry.htm))  
[Parent](P_Tessa_Roles_Role_Parent.htm)|  Родительская роль.  
(Унаследован от [Role](T_Tessa_Roles_Role.htm))  
[ParentID](P_Tessa_Roles_Role_ParentID.htm)|  Идентификатор родительской роли
или null, если родительская роль отсутствует.  
(Унаследован от [Role](T_Tessa_Roles_Role.htm))  
[ParentName](P_Tessa_Roles_Role_ParentName.htm)|  Имя родительской роли или
null, если родительская роль отсутствует.  
(Унаследован от [Role](T_Tessa_Roles_Role.htm))  
[Phone](P_Tessa_Roles_PersonalRole_Phone.htm)|  Контактный номер телефона или
null, если номер не задан.  
[Position](P_Tessa_Roles_PersonalRole_Position.htm)|  Название должности или
null, если должность не задана.  
[RoleType](P_Tessa_Roles_Role_RoleType.htm)|  Тип роли.  
(Унаследован от [Role](T_Tessa_Roles_Role.htm))  
[TimeZoneID](P_Tessa_Roles_PersonalRole_TimeZoneID.htm)|  ID временной зоны
или null, если не задана.  
[TimeZoneUtcOffsetMinutes](P_Tessa_Roles_PersonalRole_TimeZoneUtcOffsetMinutes.htm)|
Смещение временной зоны или null, если не задано.  
[Users](P_Tessa_Roles_Role_Users.htm)|  Состав роли.  
(Унаследован от [Role](T_Tessa_Roles_Role.htm))  
##  __Методы
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
(Унаследован от [Role](T_Tessa_Roles_Role.htm))  
[ToRoleUser](M_Tessa_Roles_Role_ToRoleUser.htm)|  Возвращает информацию о
пользователе по общей информации о персональной роли. Метод следует вызывать
только в том случае, если текущая роль является персональной, при этом полная
информация по персональной роли PersonalRole может быть не загружена.  
(Унаследован от [Role](T_Tessa_Roles_Role.htm))  
[ToString](M_Tessa_Platform_NamedEntry_ToString.htm)| Возвращает строковое
представление объекта.  
(Унаследован от [NamedEntry](T_Tessa_Platform_NamedEntry.htm))  
[UpdateFromAssociations](M_Tessa_Roles_Role_UpdateFromAssociations.htm)|
Обновляет значения ссылочных полей из всех объектов-ассоциаций, на которые
установлены ссылки.  
(Унаследован от [Role](T_Tessa_Roles_Role.htm))  
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
