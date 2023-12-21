# WorkflowEngineBaseTessaView.GetMetadataAsync - метод
##  __Definition
 **Пространство имён:**
[Tessa.Extensions.Platform.Client.Workflow](N_Tessa_Extensions_Platform_Client_Workflow.htm)  
 **Сборка:** Tessa.UI (в Tessa.UI.dll) Версия: 3.6.0.17
C# __Копировать
     public ValueTask<IViewMetadata> GetMetadataAsync(
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function GetMetadataAsync ( 
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask(Of IViewMetadata)
C++ __Копировать
     public:
    virtual ValueTask<IViewMetadata^> GetMetadataAsync(
    	CancellationToken cancellationToken = CancellationToken()
    ) sealed
F# __Копировать
     abstract GetMetadataAsync : 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<IViewMetadata> 
    override GetMetadataAsync : 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<IViewMetadata> 
#### Параметры
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<[IViewMetadata](T_Tessa_Views_Metadata_IViewMetadata.htm)>
#### Реализации
[ITessaView.GetMetadataAsync(CancellationToken)](M_Tessa_Views_ITessaView_GetMetadataAsync.htm)  
##  __См. также
#### Ссылки
[WorkflowEngineBaseTessaView -
](T_Tessa_Extensions_Platform_Client_Workflow_WorkflowEngineBaseTessaView.htm)
[Tessa.Extensions.Platform.Client.Workflow - пространство
имён](N_Tessa_Extensions_Platform_Client_Workflow.htm)
