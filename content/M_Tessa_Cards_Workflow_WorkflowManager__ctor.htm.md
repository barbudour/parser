# WorkflowManager - конструктор
Создаёт экземпляр класса с указанием значений его свойств.
## __Definition
 **Пространство имён:** [Tessa.Cards.Workflow](N_Tessa_Cards_Workflow.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public WorkflowManager(
    	IWorkflowContext context,
    	IWorkflowQueueProcessor queueProcessor
    )
VB __Копировать
     Public Sub New ( 
    	context As IWorkflowContext,
    	queueProcessor As IWorkflowQueueProcessor
    )
C++ __Копировать
     public:
    WorkflowManager(
    	IWorkflowContext^ context, 
    	IWorkflowQueueProcessor^ queueProcessor
    )
F# __Копировать
     new : 
            context : IWorkflowContext * 
            queueProcessor : IWorkflowQueueProcessor -> WorkflowManager
#### Параметры
context [IWorkflowContext](T_Tessa_Cards_Workflow_IWorkflowContext.htm)
     Контекст бизнес-процесса, содержащий информацию по сохраняемой карточке. 
queueProcessor
[IWorkflowQueueProcessor](T_Tessa_Cards_Workflow_IWorkflowQueueProcessor.htm)
     Объект, выполняющий обработку действий в очереди [WorkflowQueue](T_Tessa_Cards_Workflow_WorkflowQueue.htm). 
## __См. также
#### Ссылки
[WorkflowManager - ](T_Tessa_Cards_Workflow_WorkflowManager.htm)
[Tessa.Cards.Workflow - пространство имён](N_Tessa_Cards_Workflow.htm)
