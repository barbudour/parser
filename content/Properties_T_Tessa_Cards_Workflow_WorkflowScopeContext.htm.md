# WorkflowScopeContext - свойства
##  __Свойства
[Current](P_Tessa_Cards_Workflow_WorkflowScopeContext_Current.htm)|  Текущий
контекст
[IWorkflowScopeContext](T_Tessa_Cards_Workflow_IWorkflowScopeContext.htm).  
---|---  
[HasCurrent](P_Tessa_Cards_Workflow_WorkflowScopeContext_HasCurrent.htm)|
Признак того, что текущий код выполняется внутри операции с контекстом
[IWorkflowScopeContext](T_Tessa_Cards_Workflow_IWorkflowScopeContext.htm), а
свойство [Current](P_Tessa_Cards_Workflow_WorkflowScopeContext_Current.htm)
ссылается на действительный контекст.  
[Parent](P_Tessa_Cards_Workflow_WorkflowScopeContext_Parent.htm)|
Родительский контекст Workflow (для нескольких вложенных сохранений,
регулируемых через Workflow). Значение может быть равно null в том случае,
если родительский или текущий объект контекста пустой.  
[StoreContext](P_Tessa_Cards_Workflow_WorkflowScopeContext_StoreContext.htm)|
Контекст по сохранению карточки, в котором было инициировано вложенное
сохранение через Workflow API. Например, в контексте содержится информация по
завершению задания, а в расширении на создание задания, отправленного через
Workflow API, возможно получить информацию по завершённому заданию. Значение
может быть равно null только в том случае, если текущий объект контекста
пустой, т.е. операция выполняется вне пределов Workflow.  
[Unknown](P_Tessa_Cards_Workflow_WorkflowScopeContext_Unknown.htm)|
Неизвестный контекст
[IWorkflowScopeContext](T_Tessa_Cards_Workflow_IWorkflowScopeContext.htm).  
[WorkflowContext](P_Tessa_Cards_Workflow_WorkflowScopeContext_WorkflowContext.htm)|
Контекст бизнес-процесса, содержащий информацию по сохраняемой карточке.
Значение может быть равно null только в том случае, если текущий объект
контекста пустой, т.е. операция выполняется вне пределов Workflow.  
[WorkflowManager](P_Tessa_Cards_Workflow_WorkflowScopeContext_WorkflowManager.htm)|
Объект, предоставляющий возможности для управления бизнес-процессом. Значение
может быть равно null только в том случае, если текущий объект контекста
пустой, т.е. операция выполняется вне пределов Workflow.  
[WorkflowWorker](P_Tessa_Cards_Workflow_WorkflowScopeContext_WorkflowWorker.htm)|
Объект, реализующий логику подпроцессов и переходов в бизнес-процессе.
Значение может быть равно null только в том случае, если текущий объект
контекста пустой, т.е. операция выполняется вне пределов Workflow.  
## __См. также
#### Ссылки
[WorkflowScopeContext - ](T_Tessa_Cards_Workflow_WorkflowScopeContext.htm)
[Tessa.Cards.Workflow - пространство имён](N_Tessa_Cards_Workflow.htm)
