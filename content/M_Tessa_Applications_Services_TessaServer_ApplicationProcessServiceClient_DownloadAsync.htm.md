# ApplicationProcessServiceClient.DownloadAsync - метод
Операция скачивания приложения.
## __Definition
 **Пространство имён:**
[Tessa.Applications.Services.TessaServer](N_Tessa_Applications_Services_TessaServer.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public Task<Stream> DownloadAsync(
    	ApplicationDownloadRequest request,
    	ApplicationDownloadFlags flags = ApplicationDownloadFlags.None,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function DownloadAsync ( 
    	request As ApplicationDownloadRequest,
    	Optional flags As ApplicationDownloadFlags = ApplicationDownloadFlags.None,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task(Of Stream)
C++ __Копировать
     public:
    virtual Task<Stream^>^ DownloadAsync(
    	ApplicationDownloadRequest^ request, 
    	ApplicationDownloadFlags flags = ApplicationDownloadFlags::None, 
    	CancellationToken cancellationToken = CancellationToken()
    ) sealed
F# __Копировать
     abstract DownloadAsync : 
            request : ApplicationDownloadRequest * 
            ?flags : ApplicationDownloadFlags * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _flags = defaultArg flags ApplicationDownloadFlags.None
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<Stream> 
    override DownloadAsync : 
            request : ApplicationDownloadRequest * 
            ?flags : ApplicationDownloadFlags * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _flags = defaultArg flags ApplicationDownloadFlags.None
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<Stream> 
#### Параметры
request
[ApplicationDownloadRequest](T_Tessa_Applications_Services_TessaServer_ApplicationDownloadRequest.htm)
     Запрос к сервису содержащий параметры приложения запрашиваемого к загрузке на клиента. 
flags
[ApplicationDownloadFlags](T_Tessa_Applications_Services_TessaServer_ApplicationDownloadFlags.htm)
(Optional)
    Флаги, влияющие на скачивание приложений с веб-сервиса.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<[Stream](https://learn.microsoft.com/dotnet/api/system.io.stream)>  
Поток содержащий результаты обработки запроса request
#### Реализации
[IApplicationService.DownloadAsync(ApplicationDownloadRequest,
ApplicationDownloadFlags,
CancellationToken)](M_Tessa_Applications_Services_TessaServer_IApplicationService_DownloadAsync.htm)  
##  __См. также
#### Ссылки
[ApplicationProcessServiceClient -
](T_Tessa_Applications_Services_TessaServer_ApplicationProcessServiceClient.htm)
[Tessa.Applications.Services.TessaServer - пространство
имён](N_Tessa_Applications_Services_TessaServer.htm)
