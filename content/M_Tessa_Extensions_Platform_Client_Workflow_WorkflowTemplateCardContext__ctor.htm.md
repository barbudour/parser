# WorkflowTemplateCardContext - конструктор
Инициализирует новый экземпляр класса
[WorkflowTemplateCardContext](T_Tessa_Extensions_Platform_Client_Workflow_WorkflowTemplateCardContext.htm)
##  __Definition
 **Пространство имён:**
[Tessa.Extensions.Platform.Client.Workflow](N_Tessa_Extensions_Platform_Client_Workflow.htm)  
 **Сборка:** Tessa.UI (в Tessa.UI.dll) Версия: 3.6.0.17
C# __Копировать
     public WorkflowTemplateCardContext(
    	ISession session,
    	ICardDialogManager dialogManager,
    	Func<INodeProcessor> createNodeProcessorFunc,
    	CreateCardModelWithMetadataFuncAsync createModelWithMetadataFuncAsync,
    	ICardRepository cardRepository,
    	IWorkflowService workflowService,
    	IWorkflowEngineCompiler workflowCompiler,
    	ICardMetadata cardMetadata,
    	Func<ICardEditorModel> createEditorFunc,
    	CreateFileSourceForCardModelFuncAsync createFileSourceForCardModelFuncAsync,
    	CreateFileUIContainerFuncAsync createFileUIContainerFuncAsync,
    	IWorkflowEngineBPMNConverter workflowEngineBPMNConverter,
    	IUnityContainer container
    )
VB __Копировать
     Public Sub New ( 
    	session As ISession,
    	dialogManager As ICardDialogManager,
    	createNodeProcessorFunc As Func(Of INodeProcessor),
    	createModelWithMetadataFuncAsync As CreateCardModelWithMetadataFuncAsync,
    	cardRepository As ICardRepository,
    	workflowService As IWorkflowService,
    	workflowCompiler As IWorkflowEngineCompiler,
    	cardMetadata As ICardMetadata,
    	createEditorFunc As Func(Of ICardEditorModel),
    	createFileSourceForCardModelFuncAsync As CreateFileSourceForCardModelFuncAsync,
    	createFileUIContainerFuncAsync As CreateFileUIContainerFuncAsync,
    	workflowEngineBPMNConverter As IWorkflowEngineBPMNConverter,
    	container As IUnityContainer
    )
C++ __Копировать
     public:
    WorkflowTemplateCardContext(
    	ISession^ session, 
    	ICardDialogManager^ dialogManager, 
    	Func<INodeProcessor^>^ createNodeProcessorFunc, 
    	CreateCardModelWithMetadataFuncAsync^ createModelWithMetadataFuncAsync, 
    	ICardRepository^ cardRepository, 
    	IWorkflowService^ workflowService, 
    	IWorkflowEngineCompiler^ workflowCompiler, 
    	ICardMetadata^ cardMetadata, 
    	Func<ICardEditorModel^>^ createEditorFunc, 
    	CreateFileSourceForCardModelFuncAsync^ createFileSourceForCardModelFuncAsync, 
    	CreateFileUIContainerFuncAsync^ createFileUIContainerFuncAsync, 
    	IWorkflowEngineBPMNConverter^ workflowEngineBPMNConverter, 
    	IUnityContainer^ container
    )
F# __Копировать
     new : 
            session : ISession * 
            dialogManager : ICardDialogManager * 
            createNodeProcessorFunc : Func<INodeProcessor> * 
            createModelWithMetadataFuncAsync : CreateCardModelWithMetadataFuncAsync * 
            cardRepository : ICardRepository * 
            workflowService : IWorkflowService * 
            workflowCompiler : IWorkflowEngineCompiler * 
            cardMetadata : ICardMetadata * 
            createEditorFunc : Func<ICardEditorModel> * 
            createFileSourceForCardModelFuncAsync : CreateFileSourceForCardModelFuncAsync * 
            createFileUIContainerFuncAsync : CreateFileUIContainerFuncAsync * 
            workflowEngineBPMNConverter : IWorkflowEngineBPMNConverter * 
            container : IUnityContainer -> WorkflowTemplateCardContext
#### Параметры
session [ISession](T_Tessa_Platform_Runtime_ISession.htm)
dialogManager [ICardDialogManager](T_Tessa_UI_Cards_ICardDialogManager.htm)
createNodeProcessorFunc
[Func](https://learn.microsoft.com/dotnet/api/system.func-1)<[INodeProcessor](T_Tessa_UI_WorkflowViewer_Processors_INodeProcessor.htm)>
createModelWithMetadataFuncAsync
[CreateCardModelWithMetadataFuncAsync](T_Tessa_UI_Cards_CreateCardModelWithMetadataFuncAsync.htm)
cardRepository [ICardRepository](T_Tessa_Cards_ICardRepository.htm)
workflowService [IWorkflowService](T_Tessa_Workflow_IWorkflowService.htm)
workflowCompiler
[IWorkflowEngineCompiler](T_Tessa_Workflow_Compilation_IWorkflowEngineCompiler.htm)
cardMetadata [ICardMetadata](T_Tessa_Cards_ICardMetadata.htm)
createEditorFunc
[Func](https://learn.microsoft.com/dotnet/api/system.func-1)<[ICardEditorModel](T_Tessa_UI_Cards_ICardEditorModel.htm)>
createFileSourceForCardModelFuncAsync
[CreateFileSourceForCardModelFuncAsync](T_Tessa_UI_Cards_CreateFileSourceForCardModelFuncAsync.htm)
createFileUIContainerFuncAsync
[CreateFileUIContainerFuncAsync](T_Tessa_UI_Files_CreateFileUIContainerFuncAsync.htm)
workflowEngineBPMNConverter
[IWorkflowEngineBPMNConverter](T_Tessa_Workflow_BPMN_IWorkflowEngineBPMNConverter.htm)
container IUnityContainer
## __См. также
#### Ссылки
[WorkflowTemplateCardContext -
](T_Tessa_Extensions_Platform_Client_Workflow_WorkflowTemplateCardContext.htm)
[Tessa.Extensions.Platform.Client.Workflow - пространство
имён](N_Tessa_Extensions_Platform_Client_Workflow.htm)
