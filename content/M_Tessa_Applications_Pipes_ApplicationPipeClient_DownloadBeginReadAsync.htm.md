# ApplicationPipeClient.DownloadBeginReadAsync - метод
##  __Definition
 **Пространство имён:**
[Tessa.Applications.Pipes](N_Tessa_Applications_Pipes.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public ValueTask<long> DownloadBeginReadAsync(
    	ApplicationDownloadRequest downloadRequest,
    	ApplicationHostConnectionInfo connectionInfo,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function DownloadBeginReadAsync ( 
    	downloadRequest As ApplicationDownloadRequest,
    	connectionInfo As ApplicationHostConnectionInfo,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask(Of Long)
C++ __Копировать
     public:
    virtual ValueTask<long long> DownloadBeginReadAsync(
    	ApplicationDownloadRequest^ downloadRequest, 
    	ApplicationHostConnectionInfo^ connectionInfo, 
    	CancellationToken cancellationToken = CancellationToken()
    ) sealed
F# __Копировать
     abstract DownloadBeginReadAsync : 
            downloadRequest : ApplicationDownloadRequest * 
            connectionInfo : ApplicationHostConnectionInfo * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<int64> 
    override DownloadBeginReadAsync : 
            downloadRequest : ApplicationDownloadRequest * 
            connectionInfo : ApplicationHostConnectionInfo * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<int64> 
#### Параметры
downloadRequest
[ApplicationDownloadRequest](T_Tessa_Applications_Services_TessaServer_ApplicationDownloadRequest.htm)
connectionInfo
[ApplicationHostConnectionInfo](T_Tessa_Applications_Services_TessaServer_ApplicationHostConnectionInfo.htm)
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<[Int64](https://learn.microsoft.com/dotnet/api/system.int64)>
#### Реализации
[IApplicationPipeService.DownloadBeginReadAsync(ApplicationDownloadRequest,
ApplicationHostConnectionInfo,
CancellationToken)](M_Tessa_Applications_Pipes_IApplicationPipeService_DownloadBeginReadAsync.htm)  
##  __См. также
#### Ссылки
[ApplicationPipeClient -
](T_Tessa_Applications_Pipes_ApplicationPipeClient.htm)
[Tessa.Applications.Pipes - пространство имён](N_Tessa_Applications_Pipes.htm)
