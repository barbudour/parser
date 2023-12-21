# IApplicationDownloader.GetApplicationStreamAsync - метод
Создает и возвращает поток содержащий неизменные файлы приложения
## __Definition
 **Пространство имён:**
[Tessa.Applications.Services.TessaServer](N_Tessa_Applications_Services_TessaServer.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     Task<Stream> GetApplicationStreamAsync(
    	[NotNullAttribute] ApplicationDownloadRequest request,
    	ApplicationDownloadFlags flags = ApplicationDownloadFlags.None,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Function GetApplicationStreamAsync ( 
    	<NotNullAttribute> request As ApplicationDownloadRequest,
    	Optional flags As ApplicationDownloadFlags = ApplicationDownloadFlags.None,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task(Of Stream)
C++ __Копировать
    Task<Stream^>^ GetApplicationStreamAsync(
    	[NotNullAttribute] ApplicationDownloadRequest^ request, 
    	ApplicationDownloadFlags flags = ApplicationDownloadFlags::None, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     abstract GetApplicationStreamAsync : 
            [<NotNullAttribute>] request : ApplicationDownloadRequest * 
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
     Запрос на загрузку приложения 
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
Поток содержащий обновленные файлы приложения
## __См. также
#### Ссылки
[IApplicationDownloader -
](T_Tessa_Applications_Services_TessaServer_IApplicationDownloader.htm)
[Tessa.Applications.Services.TessaServer - пространство
имён](N_Tessa_Applications_Services_TessaServer.htm)
