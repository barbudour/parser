# WorkflowEngineCompilationBuilderFactoryDelegate - делегат
##  __Definition
 **Пространство имён:**
[Tessa.Compilation.Workflow](N_Tessa_Compilation_Workflow.htm)  
 **Сборка:** Tessa.Server (в Tessa.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public delegate IWorkflowCompilationSyntaxTreeBuilder WorkflowEngineCompilationBuilderFactoryDelegate(
    	Guid sourceID,
    	ICompilationSyntaxTreeBuilder builder,
    	WorkflowCompilationDescriptionMap descriptionMap
    )
VB __Копировать
     Public Delegate Function WorkflowEngineCompilationBuilderFactoryDelegate ( 
    	sourceID As Guid,
    	builder As ICompilationSyntaxTreeBuilder,
    	descriptionMap As WorkflowCompilationDescriptionMap
    ) As IWorkflowCompilationSyntaxTreeBuilder
C++ __Копировать
     public delegate IWorkflowCompilationSyntaxTreeBuilder^ WorkflowEngineCompilationBuilderFactoryDelegate(
    	Guid sourceID, 
    	ICompilationSyntaxTreeBuilder^ builder, 
    	WorkflowCompilationDescriptionMap^ descriptionMap
    )
F# __Копировать
     type WorkflowEngineCompilationBuilderFactoryDelegate = 
        delegate of 
            sourceID : Guid * 
            builder : ICompilationSyntaxTreeBuilder * 
            descriptionMap : WorkflowCompilationDescriptionMap -> IWorkflowCompilationSyntaxTreeBuilder
#### Параметры
sourceID [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
builder
[ICompilationSyntaxTreeBuilder](T_Tessa_Compilation_ICompilationSyntaxTreeBuilder.htm)
descriptionMap
[WorkflowCompilationDescriptionMap](T_Tessa_Compilation_Workflow_WorkflowCompilationDescriptionMap.htm)
#### Возвращаемое значение
[IWorkflowCompilationSyntaxTreeBuilder](T_Tessa_Workflow_Compilation_IWorkflowCompilationSyntaxTreeBuilder.htm)
##  __См. также
#### Ссылки
[Tessa.Compilation.Workflow - пространство
имён](N_Tessa_Compilation_Workflow.htm)
