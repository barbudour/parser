# WorkflowHelper.IsWorkflowEngineTaskAsync - метод
Возвращает значение, показывающее, что указанное задание task из карточки card
было отправлено из Workflow Engine.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Workflow.WorkflowEngine](N_Tessa_Extensions_Default_Shared_Workflow_WorkflowEngine.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     public static Task<bool> IsWorkflowEngineTaskAsync(
    	CardTask task,
    	Card card,
    	IDbScope dbScope,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Shared Function IsWorkflowEngineTaskAsync ( 
    	task As CardTask,
    	card As Card,
    	dbScope As IDbScope,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task(Of Boolean)
C++ __Копировать
     public:
    static Task<bool>^ IsWorkflowEngineTaskAsync(
    	CardTask^ task, 
    	Card^ card, 
    	IDbScope^ dbScope, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     static member IsWorkflowEngineTaskAsync : 
            task : CardTask * 
            card : Card * 
            dbScope : IDbScope * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<bool> 
#### Параметры
task [CardTask](T_Tessa_Cards_CardTask.htm)
    Проверяемое задание.
card [Card](T_Tessa_Cards_Card.htm)
    Карточка содержащая проверяемое задание или значение null, если она не доступна.
dbScope [IDbScope](T_Tessa_Platform_Data_IDbScope.htm)
    Объект для взаимодействия с базой данных.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)>  
Значение true, если задание было отправлено из Workflow Engine, иначе - false.
##  __Заметки
Проверка основана на том, что при отправке задания, стандартным способом,
посредством метода [SendTaskAsync(Guid, String, Nullable<DateTime>,
Nullable<Int32>, Guid, String, Nullable<Guid>, Nullable<Guid>,
Action<CardTask>,
CancellationToken)](M_Tessa_Workflow_WorkflowEngineContext_SendTaskAsync.htm)
задаётся значение [ProcessKind](P_Tessa_Cards_CardTask_ProcessKind.htm) равное
[WorkflowEngineProcessName](F_Tessa_Workflow_Helpful_WorkflowEngineHelper_WorkflowEngineProcessName.htm),
если задание не содержит информации об
[ProcessKind](P_Tessa_Cards_CardTask_ProcessKind.htm) и card задан, то
выполняется её поиск в истории заданий в
[ProcessKind](P_Tessa_Cards_CardTaskHistoryItem_ProcessKind.htm), если и там
отсутствует информация или не задано значение card, то проверяется наличие
подписки на задание в таблице **WorkflowEngineTaskSubscriptions**.
## __См. также
#### Ссылки
[WorkflowHelper -
](T_Tessa_Extensions_Default_Shared_Workflow_WorkflowEngine_WorkflowHelper.htm)
[Tessa.Extensions.Default.Shared.Workflow.WorkflowEngine - пространство
имён](N_Tessa_Extensions_Default_Shared_Workflow_WorkflowEngine.htm)
