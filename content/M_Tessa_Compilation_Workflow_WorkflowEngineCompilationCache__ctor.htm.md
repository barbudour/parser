# WorkflowEngineCompilationCache - конструктор
Инициализирует новый экземпляр класса
[WorkflowEngineCompilationCache](T_Tessa_Compilation_Workflow_WorkflowEngineCompilationCache.htm)
##  __Definition
 **Пространство имён:**
[Tessa.Compilation.Workflow](N_Tessa_Compilation_Workflow.htm)  
 **Сборка:** Tessa.Server (в Tessa.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public WorkflowEngineCompilationCache(
    	IWorkflowService workflowService,
    	IWorkflowEngineCache workflowCache,
    	ICardCache cardCache,
    	IWorkflowEngineCompiler compiler,
    	IWorkflowEngineTilesCompiler tilesCompiler,
    	IDbScope dbScope,
    	[OptionalDependencyAttribute] IUnityDisposableContainer unityDisposableContainer = null
    )
VB __Копировать
     Public Sub New ( 
    	workflowService As IWorkflowService,
    	workflowCache As IWorkflowEngineCache,
    	cardCache As ICardCache,
    	compiler As IWorkflowEngineCompiler,
    	tilesCompiler As IWorkflowEngineTilesCompiler,
    	dbScope As IDbScope,
    	<OptionalDependencyAttribute> Optional unityDisposableContainer As IUnityDisposableContainer = Nothing
    )
C++ __Копировать
     public:
    WorkflowEngineCompilationCache(
    	IWorkflowService^ workflowService, 
    	IWorkflowEngineCache^ workflowCache, 
    	ICardCache^ cardCache, 
    	IWorkflowEngineCompiler^ compiler, 
    	IWorkflowEngineTilesCompiler^ tilesCompiler, 
    	IDbScope^ dbScope, 
    	[OptionalDependencyAttribute] IUnityDisposableContainer^ unityDisposableContainer = nullptr
    )
F# __Копировать
     new : 
            workflowService : IWorkflowService * 
            workflowCache : IWorkflowEngineCache * 
            cardCache : ICardCache * 
            compiler : IWorkflowEngineCompiler * 
            tilesCompiler : IWorkflowEngineTilesCompiler * 
            dbScope : IDbScope * 
            [<OptionalDependencyAttribute>] ?unityDisposableContainer : IUnityDisposableContainer 
    (* Defaults:
            let _unityDisposableContainer = defaultArg unityDisposableContainer null
    *)
    -> WorkflowEngineCompilationCache
#### Параметры
workflowService [IWorkflowService](T_Tessa_Workflow_IWorkflowService.htm)
workflowCache
[IWorkflowEngineCache](T_Tessa_Workflow_IWorkflowEngineCache.htm)
cardCache [ICardCache](T_Tessa_Cards_Caching_ICardCache.htm)
compiler
[IWorkflowEngineCompiler](T_Tessa_Workflow_Compilation_IWorkflowEngineCompiler.htm)
tilesCompiler
[IWorkflowEngineTilesCompiler](T_Tessa_Workflow_Compilation_IWorkflowEngineTilesCompiler.htm)
dbScope [IDbScope](T_Tessa_Platform_Data_IDbScope.htm)
unityDisposableContainer
[IUnityDisposableContainer](T_Tessa_Platform_IUnityDisposableContainer.htm)
(Optional)
## __См. также
#### Ссылки
[WorkflowEngineCompilationCache -
](T_Tessa_Compilation_Workflow_WorkflowEngineCompilationCache.htm)
[Tessa.Compilation.Workflow - пространство
имён](N_Tessa_Compilation_Workflow.htm)
