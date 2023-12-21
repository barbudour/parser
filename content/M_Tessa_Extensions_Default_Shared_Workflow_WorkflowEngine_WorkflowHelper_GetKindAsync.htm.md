# WorkflowHelper.GetKindAsync - метод
Возвращает информацию по указанному идентификатору вида задания.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Workflow.WorkflowEngine](N_Tessa_Extensions_Default_Shared_Workflow_WorkflowEngine.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     public static Task<(bool , string )> GetKindAsync(
    	IViewService viewService,
    	Guid id,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Shared Function GetKindAsync ( 
    	viewService As IViewService,
    	id As Guid,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task(Of ( As Boolean,  As String))
C++ __Копировать
     public:
    static Task<ValueTuple<bool, String^>>^ GetKindAsync(
    	IViewService^ viewService, 
    	Guid id, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     static member GetKindAsync : 
            viewService : IViewService * 
            id : Guid * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<ValueTuple<bool, string>> 
#### Параметры
viewService [IViewService](T_Tessa_Views_IViewService.htm)
    Сервис представлений.
id [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
    Идентификатор вида задания.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить выполнения асинхронной операции.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<[ValueTuple](https://learn.microsoft.com/dotnet/api/system.valuetuple-2)<[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean),
[String](https://learn.microsoft.com/dotnet/api/system.string)>>  
Кортеж содержащий: флаг, показывающий, что вид задания имеющий указанный
идентификатор найден и название вида задания.
##  __См. также
#### Ссылки
[WorkflowHelper -
](T_Tessa_Extensions_Default_Shared_Workflow_WorkflowEngine_WorkflowHelper.htm)
[Tessa.Extensions.Default.Shared.Workflow.WorkflowEngine - пространство
имён](N_Tessa_Extensions_Default_Shared_Workflow_WorkflowEngine.htm)
