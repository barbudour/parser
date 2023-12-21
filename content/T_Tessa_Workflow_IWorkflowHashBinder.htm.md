# IWorkflowHashBinder - интерфейс
Описывает объект, осуществляющего связь значений хеша со значениями в секциях
карточки.
## __Definition
 **Пространство имён:** [Tessa.Workflow](N_Tessa_Workflow.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IWorkflowHashBinder
VB __Копировать
     Public Interface IWorkflowHashBinder
C++ __Копировать
     public interface class IWorkflowHashBinder
F# __Копировать
     type IWorkflowHashBinder = interface end
##  __Методы
[AddLinkBinding(WorkflowStorageBase,
String[])](M_Tessa_Workflow_IWorkflowHashBinder_AddLinkBinding.htm)|  Создаёт
новую привязку для связи.  
---|---  
[AddLinkBinding(WorkflowStorageBase, String[],
String[])](M_Tessa_Workflow_IWorkflowHashBinder_AddLinkBinding_1.htm)|
Создаёт новую привязку для связи.  
[AttachAction](M_Tessa_Workflow_IWorkflowHashBinder_AttachAction.htm)|
Создаёт привязку для указанного действия.  
[AttachNode](M_Tessa_Workflow_IWorkflowHashBinder_AttachNode.htm)|  Создаёт
привязку для указанного узла.  
[AttachProcess](M_Tessa_Workflow_IWorkflowHashBinder_AttachProcess.htm)|
Создаёт привязку для указанного процесса.  
[CreateFieldBindingAsync](M_Tessa_Workflow_IWorkflowHashBinder_CreateFieldBindingAsync.htm)|
Создаёт привязку поля строковой секции к хешу.  
[CreateRowFieldBindingAsync](M_Tessa_Workflow_IWorkflowHashBinder_CreateRowFieldBindingAsync.htm)|
Создаёт привязку поля строки коллекционной или древовидной секции к хешу.  
[CreateTableBindingAsync](M_Tessa_Workflow_IWorkflowHashBinder_CreateTableBindingAsync.htm)|
Создаёт привязку табличной секции к хешу.  
[DetachActionAsync](M_Tessa_Workflow_IWorkflowHashBinder_DetachActionAsync.htm)|
Удаляет привязку для указанного действия.  
[DetachNodeAsync](M_Tessa_Workflow_IWorkflowHashBinder_DetachNodeAsync.htm)|
Удаляет привязку для указанного узла.  
[DetachProcessAsync](M_Tessa_Workflow_IWorkflowHashBinder_DetachProcessAsync.htm)|
Удаляет привязку для указанного процесса.  
## __См. также
#### Ссылки
[Tessa.Workflow - пространство имён](N_Tessa_Workflow.htm)
