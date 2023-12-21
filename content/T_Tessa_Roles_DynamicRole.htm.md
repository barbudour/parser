# DynamicRole - класс
Динамическая роль.
## __Definition
 **Пространство имён:** [Tessa.Roles](N_Tessa_Roles.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
    [DataContractAttribute]
    [TableAttribute("DynamicRoles", IsColumnAttributeRequired = false)]
    public sealed class DynamicRole : Role, 
    	IRoleSchedulingProvider, IRoleLastErrorContainer
VB __Копировать
    <DataContractAttribute>
    <TableAttribute("DynamicRoles", IsColumnAttributeRequired := false)>
    Public NotInheritable Class DynamicRole
    	Inherits Role
    	Implements IRoleSchedulingProvider, IRoleLastErrorContainer
C++ __Копировать
    [DataContractAttribute]
    [TableAttribute(L"DynamicRoles", IsColumnAttributeRequired = false)]
    public ref class DynamicRole sealed : public Role, 
    	IRoleSchedulingProvider, IRoleLastErrorContainer
F# __Копировать
     [<SealedAttribute>]
    [<DataContractAttribute>]
    [<TableAttribute("DynamicRoles", IsColumnAttributeRequired = false)>]
    type DynamicRole = 
        class
            inherit Role
            interface IRoleSchedulingProvider
            interface IRoleLastErrorContainer
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[NamedEntry](T_Tessa_Platform_NamedEntry.htm) __[Role](T_Tessa_Roles_Role.htm) __ DynamicRole
Implements
    [IRoleLastErrorContainer](T_Tessa_Roles_IRoleLastErrorContainer.htm), [IRoleSchedulingProvider](T_Tessa_Roles_IRoleSchedulingProvider.htm)
##  __Конструкторы
[DynamicRole](M_Tessa_Roles_DynamicRole__ctor.htm)| Создаёт экземпляр класса с
параметрами по умолчанию.  
---|---  
##  __Свойства
[CronScheduling](P_Tessa_Roles_DynamicRole_CronScheduling.htm)|  Строка Cron,
определяющая расписание пересчёта состава роли, или null, если расписание
пересчёта определяется не через Cron.  
---|---  
[Deputies](P_Tessa_Roles_Role_Deputies.htm)|  Заместители на роль.  
(Унаследован от [Role](T_Tessa_Roles_Role.htm))  
[HasError](P_Tessa_Roles_DynamicRole_HasError.htm)|  Признак того, что роль
имеет сообщение о последней ошибке, возникшей при пересчёте её состава.  
[HasParent](P_Tessa_Roles_Role_HasParent.htm)|  Признак того, что заданная
роль имеет родительскую роль.  
(Унаследован от [Role](T_Tessa_Roles_Role.htm))  
[Hidden](P_Tessa_Roles_Role_Hidden.htm)|  Признак "скрывать при выборе"  
(Унаследован от [Role](T_Tessa_Roles_Role.htm))  
[ID](P_Tessa_Platform_NamedEntry_ID.htm)| Идентификатор объекта.  
(Унаследован от [NamedEntry](T_Tessa_Platform_NamedEntry.htm))  
[LastErrorDate](P_Tessa_Roles_DynamicRole_LastErrorDate.htm)|
Дата последней ошибки, возникшей при пересчёте состава роли, или null, если
ошибки не возникало.
Дата должна указываться в формате UTC (Coordinated Universal Time).  
[LastErrorText](P_Tessa_Roles_DynamicRole_LastErrorText.htm)|  Сообщение о
последней ошибке, возникшей при пересчёте состава роли, или null, если ошибки
не возникало.  
[LastException](P_Tessa_Roles_DynamicRole_LastException.htm)|  Последняя
ошибка при пересчёте состава роли, или null, если ошибки не возникало.  
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
[PeriodScheduling](P_Tessa_Roles_DynamicRole_PeriodScheduling.htm)|  Интервал
в секундах, определяющий период пересчёта состава роли, или null, если
расписание пересчёта определяется не через период.  
[RoleType](P_Tessa_Roles_Role_RoleType.htm)|  Тип роли.  
(Унаследован от [Role](T_Tessa_Roles_Role.htm))  
[ScheduleAtLaunch](P_Tessa_Roles_DynamicRole_ScheduleAtLaunch.htm)|
Запланировать пересчёт при запуске сервиса Chronos.  
[SchedulingType](P_Tessa_Roles_DynamicRole_SchedulingType.htm)|  Способ
указания расписания для пересчёта состава роли.  
[SqlText](P_Tessa_Roles_DynamicRole_SqlText.htm)|  Текст SQL-запроса
динамической роли.  
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
информация по персональной роли [PersonalRole](T_Tessa_Roles_PersonalRole.htm)
может быть не загружена.  
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
