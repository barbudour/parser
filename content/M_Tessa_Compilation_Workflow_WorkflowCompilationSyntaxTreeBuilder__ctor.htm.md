# WorkflowCompilationSyntaxTreeBuilder - конструктор
Инициализирует новый экземпляр класса
[WorkflowCompilationSyntaxTreeBuilder](T_Tessa_Compilation_Workflow_WorkflowCompilationSyntaxTreeBuilder.htm)
##  __Definition
 **Пространство имён:**
[Tessa.Compilation.Workflow](N_Tessa_Compilation_Workflow.htm)  
 **Сборка:** Tessa.Server (в Tessa.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public WorkflowCompilationSyntaxTreeBuilder(
    	Guid sourceID,
    	ICompilationSyntaxTreeBuilder innerBuilder,
    	WorkflowCompilationDescriptionMap descriptionMap,
    	IWorkflowEnginePreprocessorProvider preprocessorProvider
    )
VB __Копировать
     Public Sub New ( 
    	sourceID As Guid,
    	innerBuilder As ICompilationSyntaxTreeBuilder,
    	descriptionMap As WorkflowCompilationDescriptionMap,
    	preprocessorProvider As IWorkflowEnginePreprocessorProvider
    )
C++ __Копировать
     public:
    WorkflowCompilationSyntaxTreeBuilder(
    	Guid sourceID, 
    	ICompilationSyntaxTreeBuilder^ innerBuilder, 
    	WorkflowCompilationDescriptionMap^ descriptionMap, 
    	IWorkflowEnginePreprocessorProvider^ preprocessorProvider
    )
F# __Копировать
     new : 
            sourceID : Guid * 
            innerBuilder : ICompilationSyntaxTreeBuilder * 
            descriptionMap : WorkflowCompilationDescriptionMap * 
            preprocessorProvider : IWorkflowEnginePreprocessorProvider -> WorkflowCompilationSyntaxTreeBuilder
#### Параметры
sourceID [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
innerBuilder
[ICompilationSyntaxTreeBuilder](T_Tessa_Compilation_ICompilationSyntaxTreeBuilder.htm)
descriptionMap
[WorkflowCompilationDescriptionMap](T_Tessa_Compilation_Workflow_WorkflowCompilationDescriptionMap.htm)
preprocessorProvider
[IWorkflowEnginePreprocessorProvider](T_Tessa_Workflow_Compilation_IWorkflowEnginePreprocessorProvider.htm)
## __См. также
#### Ссылки
[WorkflowCompilationSyntaxTreeBuilder -
](T_Tessa_Compilation_Workflow_WorkflowCompilationSyntaxTreeBuilder.htm)
[Tessa.Compilation.Workflow - пространство
имён](N_Tessa_Compilation_Workflow.htm)
