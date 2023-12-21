# WorkflowEngineBaseTessaView.GetDataAsync - метод
##  __Definition
 **Пространство имён:**
[Tessa.Extensions.Platform.Client.Workflow](N_Tessa_Extensions_Platform_Client_Workflow.htm)  
 **Сборка:** Tessa.UI (в Tessa.UI.dll) Версия: 3.6.0.17
C# __Копировать
     public abstract Task<ITessaViewResult> GetDataAsync(
    	ITessaViewRequest request,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public MustOverride Function GetDataAsync ( 
    	request As ITessaViewRequest,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task(Of ITessaViewResult)
C++ __Копировать
     public:
    virtual Task<ITessaViewResult^>^ GetDataAsync(
    	ITessaViewRequest^ request, 
    	CancellationToken cancellationToken = CancellationToken()
    ) abstract
F# __Копировать
     abstract GetDataAsync : 
            request : ITessaViewRequest * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<ITessaViewResult> 
#### Параметры
request [ITessaViewRequest](T_Tessa_Views_ITessaViewRequest.htm)
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<[ITessaViewResult](T_Tessa_Views_ITessaViewResult.htm)>
#### Реализации
[ITessaView.GetDataAsync(ITessaViewRequest,
CancellationToken)](M_Tessa_Views_ITessaView_GetDataAsync.htm)  
##  __См. также
#### Ссылки
[WorkflowEngineBaseTessaView -
](T_Tessa_Extensions_Platform_Client_Workflow_WorkflowEngineBaseTessaView.htm)
[Tessa.Extensions.Platform.Client.Workflow - пространство
имён](N_Tessa_Extensions_Platform_Client_Workflow.htm)
