# BusinessProcessUIExtension - конструктор
Инициализирует новый экземпляр класса
[BusinessProcessUIExtension](T_Tessa_Extensions_Platform_Client_UI_BusinessProcessUIExtension.htm)
##  __Definition
 **Пространство имён:**
[Tessa.Extensions.Platform.Client.UI](N_Tessa_Extensions_Platform_Client_UI.htm)  
 **Сборка:** Tessa.UI (в Tessa.UI.dll) Версия: 3.6.0.17
C# __Копировать
     public BusinessProcessUIExtension(
    	IWorkflowEngineCompiler workflowCompiler,
    	IWorkflowEngineTilesCompiler workflowTilesCompiler,
    	Func<WorkflowTemplateCardContext> contextBuilder
    )
VB __Копировать
     Public Sub New ( 
    	workflowCompiler As IWorkflowEngineCompiler,
    	workflowTilesCompiler As IWorkflowEngineTilesCompiler,
    	contextBuilder As Func(Of WorkflowTemplateCardContext)
    )
C++ __Копировать
     public:
    BusinessProcessUIExtension(
    	IWorkflowEngineCompiler^ workflowCompiler, 
    	IWorkflowEngineTilesCompiler^ workflowTilesCompiler, 
    	Func<WorkflowTemplateCardContext^>^ contextBuilder
    )
F# __Копировать
     new : 
            workflowCompiler : IWorkflowEngineCompiler * 
            workflowTilesCompiler : IWorkflowEngineTilesCompiler * 
            contextBuilder : Func<WorkflowTemplateCardContext> -> BusinessProcessUIExtension
#### Параметры
workflowCompiler
[IWorkflowEngineCompiler](T_Tessa_Workflow_Compilation_IWorkflowEngineCompiler.htm)
workflowTilesCompiler
[IWorkflowEngineTilesCompiler](T_Tessa_Workflow_Compilation_IWorkflowEngineTilesCompiler.htm)
contextBuilder
[Func](https://learn.microsoft.com/dotnet/api/system.func-1)<[WorkflowTemplateCardContext](T_Tessa_Extensions_Platform_Client_Workflow_WorkflowTemplateCardContext.htm)>
## __См. также
#### Ссылки
[BusinessProcessUIExtension -
](T_Tessa_Extensions_Platform_Client_UI_BusinessProcessUIExtension.htm)
[Tessa.Extensions.Platform.Client.UI - пространство
имён](N_Tessa_Extensions_Platform_Client_UI.htm)
