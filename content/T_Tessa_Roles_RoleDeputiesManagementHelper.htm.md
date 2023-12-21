# RoleDeputiesManagementHelper - класс
##  __Definition
 **Пространство имён:** [Tessa.Roles](N_Tessa_Roles.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static class RoleDeputiesManagementHelper
VB __Копировать
     Public NotInheritable Class RoleDeputiesManagementHelper
C++ __Копировать
     public ref class RoleDeputiesManagementHelper abstract sealed
F# __Копировать
     [<AbstractClassAttribute>]
    [<SealedAttribute>]
    type RoleDeputiesManagementHelper = class end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ RoleDeputiesManagementHelper
##  __Методы
[GenerateCardIDFromUserID](M_Tessa_Roles_RoleDeputiesManagementHelper_GenerateCardIDFromUserID.htm)|  
---|---  
[GetUserIDFromCardID](M_Tessa_Roles_RoleDeputiesManagementHelper_GetUserIDFromCardID.htm)|  
[RecalcContextRoleDeputiesAsync](M_Tessa_Roles_RoleDeputiesManagementHelper_RecalcContextRoleDeputiesAsync.htm)|
Пересчитывает замещения для всех временных ролей с учетом замещений на
контекстные роли.  
[RecalcDynamicFakeRolesAsync](M_Tessa_Roles_RoleDeputiesManagementHelper_RecalcDynamicFakeRolesAsync.htm)|
Перерасчитывает записи по фейковым ролям и добавляет записи в RoleDeputies
если необходимо.  
[RecalcDynamicRoleDeputiesAsync](M_Tessa_Roles_RoleDeputiesManagementHelper_RecalcDynamicRoleDeputiesAsync.htm)|
Пересчитывает состав роли с учетом замещений на динамические роли.  
[RecalcFakeAllDepartmentsAsync](M_Tessa_Roles_RoleDeputiesManagementHelper_RecalcFakeAllDepartmentsAsync.htm)|
Пересчитывает фейковую роль "Все департаменты".  
[RecalcFakeAllRolesAsync](M_Tessa_Roles_RoleDeputiesManagementHelper_RecalcFakeAllRolesAsync.htm)|
Пересчитывает фейковую роль "Все роли и департаменты".  
[RecalcFakeAllStaticRolesAsync](M_Tessa_Roles_RoleDeputiesManagementHelper_RecalcFakeAllStaticRolesAsync.htm)|
Пересчитывает фейковую роль "Все статичные роли".  
[RecalcFakeOnlyMeAsync](M_Tessa_Roles_RoleDeputiesManagementHelper_RecalcFakeOnlyMeAsync.htm)|
Пересчитывает фейковую роль "Лично я".  
[RecalcMetaRoleDeputiesAsync](M_Tessa_Roles_RoleDeputiesManagementHelper_RecalcMetaRoleDeputiesAsync.htm)|
Пересчитывает состав роли с учетом замещений на мета роли.  
[RecalcStaticFakeRolesAsync](M_Tessa_Roles_RoleDeputiesManagementHelper_RecalcStaticFakeRolesAsync.htm)|
Перерасчитывает записи по фейковым ролям и добавляет записи в RoleDeputies
если необходимо.  
## __Поля
[FakeAllDepartments](F_Tessa_Roles_RoleDeputiesManagementHelper_FakeAllDepartments.htm)|
Все подразделения.  
---|---  
[FakeAllRoles](F_Tessa_Roles_RoleDeputiesManagementHelper_FakeAllRoles.htm)|
Все роли и подразделения.  
[FakeAllStaticRoles](F_Tessa_Roles_RoleDeputiesManagementHelper_FakeAllStaticRoles.htm)|
Все статичные роли.  
[FakeOnlyMe](F_Tessa_Roles_RoleDeputiesManagementHelper_FakeOnlyMe.htm)|
Лично я.  
[FakeRoles](F_Tessa_Roles_RoleDeputiesManagementHelper_FakeRoles.htm)|  Все
фейковые роли для замещений, такие как: "Все роли и подразделения", "Все
подразделения", "Все статические роли", "Лично я"  
## __См. также
#### Ссылки
[Tessa.Roles - пространство имён](N_Tessa_Roles.htm)
