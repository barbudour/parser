# ApplicationsBinaryWebProxy.DownloadAsync - метод
Операция скачивания приложения.
## __Definition
 **Пространство имён:**
[Tessa.Applications.Services.TessaServer](N_Tessa_Applications_Services_TessaServer.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public Task<Stream> DownloadAsync(
    	ApplicationDownloadRequest request,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function DownloadAsync ( 
    	request As ApplicationDownloadRequest,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task(Of Stream)
C++ __Копировать
     public:
    Task<Stream^>^ DownloadAsync(
    	ApplicationDownloadRequest^ request, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     member DownloadAsync : 
            request : ApplicationDownloadRequest * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<Stream> 
#### Параметры
request
[ApplicationDownloadRequest](T_Tessa_Applications_Services_TessaServer_ApplicationDownloadRequest.htm)
     Запрос к сервису содержащий параметры приложения запрашиваемого к загрузке на клиента. 
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<[Stream](https://learn.microsoft.com/dotnet/api/system.io.stream)>  
Поток содержащий результаты обработки запроса request
##  __См. также
#### Ссылки
[ApplicationsBinaryWebProxy -
](T_Tessa_Applications_Services_TessaServer_ApplicationsBinaryWebProxy.htm)
[Tessa.Applications.Services.TessaServer - пространство
имён](N_Tessa_Applications_Services_TessaServer.htm)
