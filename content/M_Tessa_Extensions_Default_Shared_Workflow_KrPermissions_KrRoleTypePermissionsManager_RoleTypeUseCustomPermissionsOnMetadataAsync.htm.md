# KrRoleTypePermissionsManager.RoleTypeUseCustomPermissionsOnMetadataAsync -
метод
##  __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Workflow.KrPermissions](N_Tessa_Extensions_Default_Shared_Workflow_KrPermissions.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     public ValueTask<bool> RoleTypeUseCustomPermissionsOnMetadataAsync(
    	Guid roleTypeID,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function RoleTypeUseCustomPermissionsOnMetadataAsync ( 
    	roleTypeID As Guid,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask(Of Boolean)
C++ __Копировать
     public:
    virtual ValueTask<bool> RoleTypeUseCustomPermissionsOnMetadataAsync(
    	Guid roleTypeID, 
    	CancellationToken cancellationToken = CancellationToken()
    ) sealed
F# __Копировать
     abstract RoleTypeUseCustomPermissionsOnMetadataAsync : 
            roleTypeID : Guid * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<bool> 
    override RoleTypeUseCustomPermissionsOnMetadataAsync : 
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
[IRoleTypePermissionsManager.RoleTypeUseCustomPermissionsOnMetadataAsync(Guid,
CancellationToken)](M_Tessa_Roles_IRoleTypePermissionsManager_RoleTypeUseCustomPermissionsOnMetadataAsync.htm)  
##  __См. также
#### Ссылки
[KrRoleTypePermissionsManager -
](T_Tessa_Extensions_Default_Shared_Workflow_KrPermissions_KrRoleTypePermissionsManager.htm)
[Tessa.Extensions.Default.Shared.Workflow.KrPermissions - пространство
имён](N_Tessa_Extensions_Default_Shared_Workflow_KrPermissions.htm)
