# WorkflowEngineCompiler - конструктор
Инициализирует новый экземпляр класса
[WorkflowEngineCompiler](T_Tessa_Compilation_Workflow_WorkflowEngineCompiler.htm)
##  __Definition
 **Пространство имён:**
[Tessa.Compilation.Workflow](N_Tessa_Compilation_Workflow.htm)  
 **Сборка:** Tessa.Server (в Tessa.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public WorkflowEngineCompiler(
    	ICompiler compiler,
    	IPreprocessor preprocessor,
    	ICompilationSourceProvider compilationProvider,
    	IWorkflowEngineCompiledBaseRegistry compiledRegistry,
    	ICardRepository cardRepository,
    	ICardServerPermissionsProvider permissionsProvider,
    	IWorkflowActionRegistry workflowActionRegistry,
    	[DependencyAttribute("CompilationBuilderName")] WorkflowEngineCompilationBuilderFactoryDelegate compilationBuilderFactory,
    	[DependencyAttribute("SourceBuilderName")] WorkflowEngineCompilationBuilderFactoryDelegate sourceBuilderFactory
    )
VB __Копировать
     Public Sub New ( 
    	compiler As ICompiler,
    	preprocessor As IPreprocessor,
    	compilationProvider As ICompilationSourceProvider,
    	compiledRegistry As IWorkflowEngineCompiledBaseRegistry,
    	cardRepository As ICardRepository,
    	permissionsProvider As ICardServerPermissionsProvider,
    	workflowActionRegistry As IWorkflowActionRegistry,
    	<DependencyAttribute("CompilationBuilderName")> compilationBuilderFactory As WorkflowEngineCompilationBuilderFactoryDelegate,
    	<DependencyAttribute("SourceBuilderName")> sourceBuilderFactory As WorkflowEngineCompilationBuilderFactoryDelegate
    )
C++ __Копировать
     public:
    WorkflowEngineCompiler(
    	ICompiler^ compiler, 
    	IPreprocessor^ preprocessor, 
    	ICompilationSourceProvider^ compilationProvider, 
    	IWorkflowEngineCompiledBaseRegistry^ compiledRegistry, 
    	ICardRepository^ cardRepository, 
    	ICardServerPermissionsProvider^ permissionsProvider, 
    	IWorkflowActionRegistry^ workflowActionRegistry, 
    	[DependencyAttribute(L"CompilationBuilderName")] WorkflowEngineCompilationBuilderFactoryDelegate^ compilationBuilderFactory, 
    	[DependencyAttribute(L"SourceBuilderName")] WorkflowEngineCompilationBuilderFactoryDelegate^ sourceBuilderFactory
    )
F# __Копировать
     new : 
            compiler : ICompiler * 
            preprocessor : IPreprocessor * 
            compilationProvider : ICompilationSourceProvider * 
            compiledRegistry : IWorkflowEngineCompiledBaseRegistry * 
            cardRepository : ICardRepository * 
            permissionsProvider : ICardServerPermissionsProvider * 
            workflowActionRegistry : IWorkflowActionRegistry * 
            [<DependencyAttribute("CompilationBuilderName")>] compilationBuilderFactory : WorkflowEngineCompilationBuilderFactoryDelegate * 
            [<DependencyAttribute("SourceBuilderName")>] sourceBuilderFactory : WorkflowEngineCompilationBuilderFactoryDelegate -> WorkflowEngineCompiler
#### Параметры
compiler [ICompiler](T_Tessa_Compilation_ICompiler.htm)
preprocessor [IPreprocessor](T_Tessa_Compilation_IPreprocessor.htm)
compilationProvider
[ICompilationSourceProvider](T_Tessa_Compilation_ICompilationSourceProvider.htm)
compiledRegistry
[IWorkflowEngineCompiledBaseRegistry](T_Tessa_Workflow_Compilation_IWorkflowEngineCompiledBaseRegistry.htm)
cardRepository [ICardRepository](T_Tessa_Cards_ICardRepository.htm)
permissionsProvider
[ICardServerPermissionsProvider](T_Tessa_Cards_ICardServerPermissionsProvider.htm)
workflowActionRegistry
[IWorkflowActionRegistry](T_Tessa_Workflow_Actions_IWorkflowActionRegistry.htm)
compilationBuilderFactory
[WorkflowEngineCompilationBuilderFactoryDelegate](T_Tessa_Compilation_Workflow_WorkflowEngineCompilationBuilderFactoryDelegate.htm)
sourceBuilderFactory
[WorkflowEngineCompilationBuilderFactoryDelegate](T_Tessa_Compilation_Workflow_WorkflowEngineCompilationBuilderFactoryDelegate.htm)
## __См. также
#### Ссылки
[WorkflowEngineCompiler -
](T_Tessa_Compilation_Workflow_WorkflowEngineCompiler.htm)
[Tessa.Compilation.Workflow - пространство
имён](N_Tessa_Compilation_Workflow.htm)
