# IWorkflowQueueProcessor - интерфейс
Объект, выполняющий обработку действий в очереди
[WorkflowQueue](T_Tessa_Cards_Workflow_WorkflowQueue.htm).
## __Definition
 **Пространство имён:** [Tessa.Cards.Workflow](N_Tessa_Cards_Workflow.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IWorkflowQueueProcessor
VB __Копировать
     Public Interface IWorkflowQueueProcessor
C++ __Копировать
     public interface class IWorkflowQueueProcessor
F# __Копировать
     type IWorkflowQueueProcessor = interface end
##  __Методы
[ProcessAsync](M_Tessa_Cards_Workflow_IWorkflowQueueProcessor_ProcessAsync.htm)|
Выполняет действия из заданной очереди [Tessa.Cards.Workflow.WorkflowQueue].
Возвращает признак того, что во всех выполненных действиях отсутствуют ошибки.
Действия, которые были успешно выполнены, удаляются из очереди.  
---|---  
## __См. также
#### Ссылки
[Tessa.Cards.Workflow - пространство имён](N_Tessa_Cards_Workflow.htm)
