# ClientRoleManagerRequestHelper - класс
Типы стандартных запросов к сервису карточек через метод
[RequestAsync(CardRequest,
CancellationToken)](M_Tessa_Cards_ICardRepository_RequestAsync.htm) для
сервиса
[ClientRoleManagerService](T_Tessa_Extensions_Platform_Shared_Roles_ClientRoleManagerService.htm)
и другие вспомогательные константы.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Platform.Shared.Roles](N_Tessa_Extensions_Platform_Shared_Roles.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static class ClientRoleManagerRequestHelper
VB __Копировать
     Public NotInheritable Class ClientRoleManagerRequestHelper
C++ __Копировать
     public ref class ClientRoleManagerRequestHelper abstract sealed
F# __Копировать
     [<AbstractClassAttribute>]
    [<SealedAttribute>]
    type ClientRoleManagerRequestHelper = class end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ ClientRoleManagerRequestHelper
##  __Поля
[DynamicRoleID](F_Tessa_Extensions_Platform_Shared_Roles_ClientRoleManagerRequestHelper_DynamicRoleID.htm)|
Идентификатор динамической роли, передаваемый в запросе.  
---|---  
[RecalcDynamicRoles](F_Tessa_Extensions_Platform_Shared_Roles_ClientRoleManagerRequestHelper_RecalcDynamicRoles.htm)|
Пересчёт указанной динамической роли в запросе request.Info по ключу
[DynamicRoleID](F_Tessa_Extensions_Platform_Shared_Roles_ClientRoleManagerRequestHelper_DynamicRoleID.htm).
Если динамическая роль не указана, то выполняется пересчёт всех динамических
ролей.  
[RecalcRoleGenerators](F_Tessa_Extensions_Platform_Shared_Roles_ClientRoleManagerRequestHelper_RecalcRoleGenerators.htm)|
Пересчёт метаролей для указанного генератора в запросе request.Info по ключу
[RoleGeneratorID](F_Tessa_Extensions_Platform_Shared_Roles_ClientRoleManagerRequestHelper_RoleGeneratorID.htm).
Если генератор не указан, то выполняется пересчёт всех генераторов метаролей.  
[RoleGeneratorID](F_Tessa_Extensions_Platform_Shared_Roles_ClientRoleManagerRequestHelper_RoleGeneratorID.htm)|
Идентификатор генератора метароли, передаваемый в запросе.  
[SyncAllDeputies](F_Tessa_Extensions_Platform_Shared_Roles_ClientRoleManagerRequestHelper_SyncAllDeputies.htm)|
Пересчёт замещений для всех ролей, кроме динамических ролей и метаролей.  
## __См. также
#### Ссылки
[Tessa.Extensions.Platform.Shared.Roles - пространство
имён](N_Tessa_Extensions_Platform_Shared_Roles.htm)
