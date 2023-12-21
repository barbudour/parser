# MetaRoleItem - класс
Запись о метароли и одном из пользователей, входящих в её состав.
## __Definition
 **Пространство имён:** [Tessa.Roles](N_Tessa_Roles.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class MetaRoleItem
VB __Копировать
     Public NotInheritable Class MetaRoleItem
C++ __Копировать
     public ref class MetaRoleItem sealed
F# __Копировать
     [<SealedAttribute>]
    type MetaRoleItem = class end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ MetaRoleItem
##  __Конструкторы
[MetaRoleItem](M_Tessa_Roles_MetaRoleItem__ctor.htm)|  Создаёт экземпляр
записи о метароли и одном из пользователей, входящих в её состав, с указанием
полного списка необходимых свойств такой записи.  
---|---  
## __Свойства
[RoleIDGuid](P_Tessa_Roles_MetaRoleItem_RoleIDGuid.htm)|  Свойство
[IDGuid](P_Tessa_Roles_MetaRole_IDGuid.htm) метароли.  
---|---  
[RoleIDInteger](P_Tessa_Roles_MetaRoleItem_RoleIDInteger.htm)|  Свойство
[IDInteger](P_Tessa_Roles_MetaRole_IDInteger.htm) метароли.  
[RoleIDString](P_Tessa_Roles_MetaRoleItem_RoleIDString.htm)|  Свойство
[IDString](P_Tessa_Roles_MetaRole_IDString.htm) метароли.  
[RoleName](P_Tessa_Roles_MetaRoleItem_RoleName.htm)|  Свойство
[Name](P_Tessa_Platform_NamedEntry_Name.htm) метароли.  
[TimeZoneID](P_Tessa_Roles_MetaRoleItem_TimeZoneID.htm)|
Свойство [TimeZoneID](P_Tessa_Roles_MetaRole_TimeZoneID.htm) метароли.  
[UserID](P_Tessa_Roles_MetaRoleItem_UserID.htm)|  Свойство
[UserID](P_Tessa_Roles_RoleUserRecord_UserID.htm) пользователя, входящего в
роль, или null, если метароль создаётся без пользователей.  
[UserName](P_Tessa_Roles_MetaRoleItem_UserName.htm)|
Свойство [UserName](P_Tessa_Roles_RoleUserRecord_UserName.htm) пользователя,
входящего в роль.
Может быть равно null.  
##  __Методы
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
[GetHashCode](https://learn.microsoft.com/dotnet/api/system.object.gethashcode#system-
object-gethashcode)| Serves as the default hash function.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetMetaRoleType](M_Tessa_Roles_MetaRoleItem_GetMetaRoleType.htm)|  Получает
свойство [MetaRoleType](P_Tessa_Roles_MetaRole_MetaRoleType.htm) метароли,
определяемое значениями свойств
[RoleIDGuid](P_Tessa_Roles_MetaRoleItem_RoleIDGuid.htm),
[RoleIDInteger](P_Tessa_Roles_MetaRoleItem_RoleIDInteger.htm) и
[RoleIDString](P_Tessa_Roles_MetaRoleItem_RoleIDString.htm).  
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
