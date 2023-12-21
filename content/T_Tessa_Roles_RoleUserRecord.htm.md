# RoleUserRecord - класс
Запись о составе роли.
## __Definition
 **Пространство имён:** [Tessa.Roles](N_Tessa_Roles.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
    [DataContractAttribute]
    [TableAttribute("RoleUsers", IsColumnAttributeRequired = false)]
    public sealed class RoleUserRecord : CollectionRecord, 
    	IRoleUser
VB __Копировать
    <DataContractAttribute>
    <TableAttribute("RoleUsers", IsColumnAttributeRequired := false)>
    Public NotInheritable Class RoleUserRecord
    	Inherits CollectionRecord
    	Implements IRoleUser
C++ __Копировать
    [DataContractAttribute]
    [TableAttribute(L"RoleUsers", IsColumnAttributeRequired = false)]
    public ref class RoleUserRecord sealed : public CollectionRecord, 
    	IRoleUser
F# __Копировать
     [<SealedAttribute>]
    [<DataContractAttribute>]
    [<TableAttribute("RoleUsers", IsColumnAttributeRequired = false)>]
    type RoleUserRecord = 
        class
            inherit CollectionRecord
            interface IRoleUser
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[CollectionRecord](T_Tessa_Platform_CollectionRecord.htm) __ RoleUserRecord
Implements
    [IRoleUser](T_Tessa_Roles_IRoleUser.htm)
##  __Конструкторы
[RoleUserRecord](M_Tessa_Roles_RoleUserRecord__ctor.htm)| Инициализирует новый
экземпляр класса RoleUserRecord  
---|---  
##  __Свойства
[ID](P_Tessa_Platform_CollectionRecord_ID.htm)| Идентификатор записи.  
(Унаследован от [CollectionRecord](T_Tessa_Platform_CollectionRecord.htm))  
---|---  
[IsDeputy](P_Tessa_Roles_RoleUserRecord_IsDeputy.htm)|  Признак того, является
ли пользователь, включённый в состав роли, заместителем, или он был
непосредственно добавлен в роль.  
[Role](P_Tessa_Roles_RoleUserRecord_Role.htm)|  Роль, для которой определяется
состав.  
[RoleType](P_Tessa_Roles_RoleUserRecord_RoleType.htm)|  Тип роли.  
[RowID](P_Tessa_Platform_CollectionRecord_RowID.htm)| Идентификатор объекта,
которому соответствует запись.  
(Унаследован от [CollectionRecord](T_Tessa_Platform_CollectionRecord.htm))  
[User](P_Tessa_Roles_RoleUserRecord_User.htm)|  Пользователь, включённый в
состав роли.  
[UserID](P_Tessa_Roles_RoleUserRecord_UserID.htm)|  Идентификатор персональной
роли пользователя, включённого в состав роли.  
[UserName](P_Tessa_Roles_RoleUserRecord_UserName.htm)|  Имя пользователя,
включённого в состав роли.  
## __Методы
[Equals(ICollectionRecord)](M_Tessa_Platform_CollectionRecord_Equals_1.htm)|
Сравнивает текущий объект с заданным.  
(Унаследован от [CollectionRecord](T_Tessa_Platform_CollectionRecord.htm))  
---|---  
[Equals(Object)](M_Tessa_Platform_CollectionRecord_Equals.htm)| Сравнивает
текущий объект с заданным.  
(Унаследован от [CollectionRecord](T_Tessa_Platform_CollectionRecord.htm))  
[Finalize](https://learn.microsoft.com/dotnet/api/system.object.finalize#system-
object-finalize)| Allows an object to try to free resources and perform other
cleanup operations before it is reclaimed by garbage collection.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetHashCode](M_Tessa_Platform_CollectionRecord_GetHashCode.htm)| Возвращает
хеш-код объекта.  
(Унаследован от [CollectionRecord](T_Tessa_Platform_CollectionRecord.htm))  
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
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[UpdateFromAssociations](M_Tessa_Roles_RoleUserRecord_UpdateFromAssociations.htm)|
Обновляет значения ссылочных полей из всех объектов-ассоциаций, на которые
установлены ссылки.  
(Переопределяет
[CollectionRecord.UpdateFromAssociations()](M_Tessa_Platform_CollectionRecord_UpdateFromAssociations.htm))  
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
