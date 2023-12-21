# FileSourceForCard.GetContentCoreAsync - метод
Загружает контент версии файла из внешней подсистемы.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     protected override ValueTask<IFileContentResponse> GetContentCoreAsync(
    	IFileContentRequest request,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Protected Overrides Function GetContentCoreAsync ( 
    	request As IFileContentRequest,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask(Of IFileContentResponse)
C++ __Копировать
     protected:
    virtual ValueTask<IFileContentResponse^> GetContentCoreAsync(
    	IFileContentRequest^ request, 
    	CancellationToken cancellationToken = CancellationToken()
    ) override
F# __Копировать
     abstract GetContentCoreAsync : 
            request : IFileContentRequest * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<IFileContentResponse> 
    override GetContentCoreAsync : 
            request : IFileContentRequest * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<IFileContentResponse> 
#### Параметры
request [IFileContentRequest](T_Tessa_Files_IFileContentRequest.htm)
    Запрос на загрузку содержимого.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<[IFileContentResponse](T_Tessa_Files_IFileContentResponse.htm)>  
Ответ на запрос с контентом версии файла из внешней подсистемы (например, из
карточки), если контент существует, или null, если контент версии неизвестен.
## __Заметки
По умолчанию создаётся ответ на запрос без указания результата, а метод
[ProcessContentActionAsync](P_Tessa_Files_IFileContentRequest_ProcessContentActionAsync.htm)
вызывается с передачей ему пустого потока.
## __См. также
#### Ссылки
[FileSourceForCard - ](T_Tessa_Cards_FileSourceForCard.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
