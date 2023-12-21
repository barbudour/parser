# KrRoleTypePermissionsManager.RoleTypeUseCustomPermissionsAsync - метод
##  __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Workflow.KrPermissions](N_Tessa_Extensions_Default_Shared_Workflow_KrPermissions.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     public ValueTask<bool> RoleTypeUseCustomPermissionsAsync(
    	Guid roleTypeID,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function RoleTypeUseCustomPermissionsAsync ( 
    	roleTypeID As Guid,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask(Of Boolean)
C++ __Копировать
     public:
    virtual ValueTask<bool> RoleTypeUseCustomPermissionsAsync(
    	Guid roleTypeID, 
    	CancellationToken cancellationToken = CancellationToken()
    ) sealed
F# __Копировать
     abstract RoleTypeUseCustomPermissionsAsync : 
            roleTypeID : Guid * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<bool> 
    override RoleTypeUseCustomPermissionsAsync : 
            roleTypeID : Guid * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<bool> 
#### Параметры
roleTypeID [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)>
#### Реализации
[IRoleTypePermissionsManager.RoleTypeUseCustomPermissionsAsync(Guid,
CancellationToken)](M_Tessa_Roles_IRoleTypePermissionsManager_RoleTypeUseCustomPermissionsAsync.htm)  
##  __См. также
#### Ссылки
[KrRoleTypePermissionsManager -
](T_Tessa_Extensions_Default_Shared_Workflow_KrPermissions_KrRoleTypePermissionsManager.htm)
[Tessa.Extensions.Default.Shared.Workflow.KrPermissions - пространство
имён](N_Tessa_Extensions_Default_Shared_Workflow_KrPermissions.htm)
