# WorkflowScopeContext - конструктор
Создаёт экземпляр класса с указанием значений его свойств.
## __Definition
 **Пространство имён:** [Tessa.Cards.Workflow](N_Tessa_Cards_Workflow.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public WorkflowScopeContext(
    	ICardStoreExtensionContext storeContext,
    	IWorkflowContext workflowContext,
    	IWorkflowManager workflowManager,
    	IWorkflowWorker workflowWorker
    )
VB __Копировать
     Public Sub New ( 
    	storeContext As ICardStoreExtensionContext,
    	workflowContext As IWorkflowContext,
    	workflowManager As IWorkflowManager,
    	workflowWorker As IWorkflowWorker
    )
C++ __Копировать
     public:
    WorkflowScopeContext(
    	ICardStoreExtensionContext^ storeContext, 
    	IWorkflowContext^ workflowContext, 
    	IWorkflowManager^ workflowManager, 
    	IWorkflowWorker^ workflowWorker
    )
F# __Копировать
     new : 
            storeContext : ICardStoreExtensionContext * 
            workflowContext : IWorkflowContext * 
            workflowManager : IWorkflowManager * 
            workflowWorker : IWorkflowWorker -> WorkflowScopeContext
#### Параметры
storeContext
[ICardStoreExtensionContext](T_Tessa_Cards_Extensions_ICardStoreExtensionContext.htm)
     Контекст по сохранению карточки, в котором было инициировано вложенное сохранение через Workflow API. Например, в контексте содержится информация по завершению задания, а в расширении на создание задания, отправленного через Workflow API, возможно получить информацию по завершённому заданию. Значение не должно быть равно null. 
workflowContext
[IWorkflowContext](T_Tessa_Cards_Workflow_IWorkflowContext.htm)
     Контекст бизнес-процесса, содержащий информацию по сохраняемой карточке. Значение не должно быть равно null. 
workflowManager
[IWorkflowManager](T_Tessa_Cards_Workflow_IWorkflowManager.htm)
     Объект, предоставляющий возможности для управления бизнес-процессом. Значение не должно быть равно null. 
workflowWorker [IWorkflowWorker](T_Tessa_Cards_Workflow_IWorkflowWorker.htm)
     Объект, реализующий логику подпроцессов и переходов в бизнес-процессе. Значение не должно быть равно null. 
## __См. также
#### Ссылки
[WorkflowScopeContext - ](T_Tessa_Cards_Workflow_WorkflowScopeContext.htm)
[Tessa.Cards.Workflow - пространство имён](N_Tessa_Cards_Workflow.htm)
