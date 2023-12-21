# BusinessProcessCardStoreExtension - конструктор
Инициализирует новый экземпляр класса
[BusinessProcessCardStoreExtension](T_Tessa_Extensions_Platform_Server_Cards_BusinessProcessCardStoreExtension.htm)
##  __Definition
 **Пространство имён:**
[Tessa.Extensions.Platform.Server.Cards](N_Tessa_Extensions_Platform_Server_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public BusinessProcessCardStoreExtension(
    	IWorkflowService workflowService,
    	IWorkflowEngineCompilationCache compilationCache,
    	IWorkflowEngineCache workflowCache,
    	IWorkflowEnginePermissionManager permissionManager,
    	IConfigurationInfoProvider configurationInfoProvider,
    	IWorkflowActionRegistry workflowActionRegistry,
    	IWorkflowEngineTileCache workflowTileCache
    )
VB __Копировать
     Public Sub New ( 
    	workflowService As IWorkflowService,
    	compilationCache As IWorkflowEngineCompilationCache,
    	workflowCache As IWorkflowEngineCache,
    	permissionManager As IWorkflowEnginePermissionManager,
    	configurationInfoProvider As IConfigurationInfoProvider,
    	workflowActionRegistry As IWorkflowActionRegistry,
    	workflowTileCache As IWorkflowEngineTileCache
    )
C++ __Копировать
     public:
    BusinessProcessCardStoreExtension(
    	IWorkflowService^ workflowService, 
    	IWorkflowEngineCompilationCache^ compilationCache, 
    	IWorkflowEngineCache^ workflowCache, 
    	IWorkflowEnginePermissionManager^ permissionManager, 
    	IConfigurationInfoProvider^ configurationInfoProvider, 
    	IWorkflowActionRegistry^ workflowActionRegistry, 
    	IWorkflowEngineTileCache^ workflowTileCache
    )
F# __Копировать
     new : 
            workflowService : IWorkflowService * 
            compilationCache : IWorkflowEngineCompilationCache * 
            workflowCache : IWorkflowEngineCache * 
            permissionManager : IWorkflowEnginePermissionManager * 
            configurationInfoProvider : IConfigurationInfoProvider * 
            workflowActionRegistry : IWorkflowActionRegistry * 
            workflowTileCache : IWorkflowEngineTileCache -> BusinessProcessCardStoreExtension
#### Параметры
workflowService [IWorkflowService](T_Tessa_Workflow_IWorkflowService.htm)
compilationCache
[IWorkflowEngineCompilationCache](T_Tessa_Workflow_Compilation_IWorkflowEngineCompilationCache.htm)
workflowCache
[IWorkflowEngineCache](T_Tessa_Workflow_IWorkflowEngineCache.htm)
permissionManager
[IWorkflowEnginePermissionManager](T_Tessa_Workflow_IWorkflowEnginePermissionManager.htm)
configurationInfoProvider
[IConfigurationInfoProvider](T_Tessa_Platform_Runtime_IConfigurationInfoProvider.htm)
workflowActionRegistry
[IWorkflowActionRegistry](T_Tessa_Workflow_Actions_IWorkflowActionRegistry.htm)
workflowTileCache
[IWorkflowEngineTileCache](T_Tessa_Workflow_IWorkflowEngineTileCache.htm)
## __См. также
#### Ссылки
[BusinessProcessCardStoreExtension -
](T_Tessa_Extensions_Platform_Server_Cards_BusinessProcessCardStoreExtension.htm)
[Tessa.Extensions.Platform.Server.Cards - пространство
имён](N_Tessa_Extensions_Platform_Server_Cards.htm)
