# IActionCompletionOptionsProvider.GetActionCompletionOptionsAsync - метод
Возвращает доступный только для чтения словарь с вариантами завершения
действий.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Workflow.WorkflowEngine](N_Tessa_Extensions_Default_Shared_Workflow_WorkflowEngine.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
    ValueTask<ReadOnlyDictionary<Guid, ActionCompletionOption>> GetActionCompletionOptionsAsync(
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Function GetActionCompletionOptionsAsync ( 
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask(Of ReadOnlyDictionary(Of Guid, ActionCompletionOption))
C++ __Копировать
    ValueTask<ReadOnlyDictionary<Guid, ActionCompletionOption^>^> GetActionCompletionOptionsAsync(
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     abstract GetActionCompletionOptionsAsync : 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<ReadOnlyDictionary<Guid, ActionCompletionOption>> 
#### Параметры
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить выполнение асинхронной задачи.
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<[ReadOnlyDictionary](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.readonlydictionary-2)<[Guid](https://learn.microsoft.com/dotnet/api/system.guid),
[ActionCompletionOption](T_Tessa_Extensions_Default_Shared_Workflow_WorkflowEngine_ActionCompletionOption.htm)>>  
Доступный только для чтения словарь с вариантами завершения действий.
##  __См. также
#### Ссылки
[IActionCompletionOptionsProvider -
](T_Tessa_Extensions_Default_Shared_Workflow_WorkflowEngine_IActionCompletionOptionsProvider.htm)
[Tessa.Extensions.Default.Shared.Workflow.WorkflowEngine - пространство
имён](N_Tessa_Extensions_Default_Shared_Workflow_WorkflowEngine.htm)
