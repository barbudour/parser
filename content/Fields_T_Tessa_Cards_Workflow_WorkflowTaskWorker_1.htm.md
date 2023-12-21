# WorkflowTaskWorker<TManager> \- поля
##  __Поля
[TaskHistoryGroupsKey](F_Tessa_Cards_Workflow_WorkflowTaskWorker_1_TaskHistoryGroupsKey.htm)|
Ключ, по которому в контексте Manager.Info будет содержаться коллекция групп
для истории заданий IReadOnlyCollection<CardTaskHistoryGroup>, если она была
предварительно загружена методом
[GetTaskHistoryGroupsAsync(IValidationResultBuilder,
CancellationToken)](M_Tessa_Cards_Workflow_WorkflowTaskWorker_1_GetTaskHistoryGroupsAsync.htm)
Используйте метод [GetTaskHistoryGroupsAsync(IValidationResultBuilder,
CancellationToken)](M_Tessa_Cards_Workflow_WorkflowTaskWorker_1_GetTaskHistoryGroupsAsync.htm)
для получения полного списка групп в истории заданий. Используйте метод
[ResolveTaskHistoryGroupAsync(Guid, Nullable<Guid>, Boolean,
IValidationResultBuilder,
CancellationToken)](M_Tessa_Cards_Workflow_WorkflowTaskWorker_1_ResolveTaskHistoryGroupAsync.htm)
для упрощённого поиска/создания группы в истории заданий.  
---|---  
## __См. также
#### Ссылки
[WorkflowTaskWorker<TManager> \-
](T_Tessa_Cards_Workflow_WorkflowTaskWorker_1.htm)
[Tessa.Cards.Workflow - пространство имён](N_Tessa_Cards_Workflow.htm)
