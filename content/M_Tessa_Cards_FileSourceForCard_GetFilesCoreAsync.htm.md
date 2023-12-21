# FileSourceForCard.GetFilesCoreAsync - метод
Возвращает коллекцию доступных файлов.
##  __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     protected override ValueTask<IFileResponse> GetFilesCoreAsync(
    	IFileRequest request,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Protected Overrides Function GetFilesCoreAsync ( 
    	request As IFileRequest,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask(Of IFileResponse)
C++ __Копировать
     protected:
    virtual ValueTask<IFileResponse^> GetFilesCoreAsync(
    	IFileRequest^ request, 
    	CancellationToken cancellationToken = CancellationToken()
    ) override
F# __Копировать
     abstract GetFilesCoreAsync : 
            request : IFileRequest * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<IFileResponse> 
    override GetFilesCoreAsync : 
            request : IFileRequest * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<IFileResponse> 
#### Параметры
request [IFileRequest](T_Tessa_Files_IFileRequest.htm)
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<[IFileResponse](T_Tessa_Files_IFileResponse.htm)>  
Ответ на запрос на получение коллекции доступных файлов.
##  __См. также
#### Ссылки
[FileSourceForCard - ](T_Tessa_Cards_FileSourceForCard.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
