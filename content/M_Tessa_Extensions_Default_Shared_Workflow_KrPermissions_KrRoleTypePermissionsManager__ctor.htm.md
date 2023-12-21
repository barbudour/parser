# KrRoleTypePermissionsManager - конструктор
Инициализирует новый экземпляр класса
[KrRoleTypePermissionsManager](T_Tessa_Extensions_Default_Shared_Workflow_KrPermissions_KrRoleTypePermissionsManager.htm)
##  __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Workflow.KrPermissions](N_Tessa_Extensions_Default_Shared_Workflow_KrPermissions.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     public KrRoleTypePermissionsManager(
    	[OptionalDependencyAttribute] IKrTypesCache krTypesCache = null,
    	[OptionalDependencyAttribute] IDbScope dbScope = null
    )
VB __Копировать
     Public Sub New ( 
    	<OptionalDependencyAttribute> Optional krTypesCache As IKrTypesCache = Nothing,
    	<OptionalDependencyAttribute> Optional dbScope As IDbScope = Nothing
    )
C++ __Копировать
     public:
    KrRoleTypePermissionsManager(
    	[OptionalDependencyAttribute] IKrTypesCache^ krTypesCache = nullptr, 
    	[OptionalDependencyAttribute] IDbScope^ dbScope = nullptr
    )
F# __Копировать
     new : 
            [<OptionalDependencyAttribute>] ?krTypesCache : IKrTypesCache * 
            [<OptionalDependencyAttribute>] ?dbScope : IDbScope 
    (* Defaults:
            let _krTypesCache = defaultArg krTypesCache null
            let _dbScope = defaultArg dbScope null
    *)
    -> KrRoleTypePermissionsManager
#### Параметры
krTypesCache
[IKrTypesCache](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_IKrTypesCache.htm)
(Optional)
dbScope [IDbScope](T_Tessa_Platform_Data_IDbScope.htm) (Optional)
## __См. также
#### Ссылки
[KrRoleTypePermissionsManager -
](T_Tessa_Extensions_Default_Shared_Workflow_KrPermissions_KrRoleTypePermissionsManager.htm)
[Tessa.Extensions.Default.Shared.Workflow.KrPermissions - пространство
имён](N_Tessa_Extensions_Default_Shared_Workflow_KrPermissions.htm)
