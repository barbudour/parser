# ICardStreamClientGetComponent.GetFileContentAsync - метод
Получает контент версии файла.
##  __Definition
 **Пространство имён:**
[Tessa.Cards.ComponentModel](N_Tessa_Cards_ComponentModel.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     Task<CardGetFileContentResponse> GetFileContentAsync(
    	CardGetFileContentRequest request,
    	Func<Stream, CancellationToken, ValueTask> processContentActionAsync,
    	Func<CardGetFileContentResponse, CancellationToken, ValueTask> processResponseActionAsync,
    	ICardMetadata cardMetadata,
    	ISession session,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Function GetFileContentAsync ( 
    	request As CardGetFileContentRequest,
    	processContentActionAsync As Func(Of Stream, CancellationToken, ValueTask),
    	processResponseActionAsync As Func(Of CardGetFileContentResponse, CancellationToken, ValueTask),
    	cardMetadata As ICardMetadata,
    	session As ISession,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task(Of CardGetFileContentResponse)
C++ __Копировать
    Task<CardGetFileContentResponse^>^ GetFileContentAsync(
    	CardGetFileContentRequest^ request, 
    	Func<Stream^, CancellationToken, ValueTask>^ processContentActionAsync, 
    	Func<CardGetFileContentResponse^, CancellationToken, ValueTask>^ processResponseActionAsync, 
    	ICardMetadata^ cardMetadata, 
    	ISession^ session, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     abstract GetFileContentAsync : 
            request : CardGetFileContentRequest * 
            processContentActionAsync : Func<Stream, CancellationToken, ValueTask> * 
            processResponseActionAsync : Func<CardGetFileContentResponse, CancellationToken, ValueTask> * 
            cardMetadata : ICardMetadata * 
            session : ISession * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<CardGetFileContentResponse> 
#### Параметры
request
[CardGetFileContentRequest](T_Tessa_Cards_CardGetFileContentRequest.htm)
    Запрос на получение контента версии файла.
processContentActionAsync
[Func](https://learn.microsoft.com/dotnet/api/system.func-3)<[Stream](https://learn.microsoft.com/dotnet/api/system.io.stream),
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken),
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask)>
     Метод, выполняющий чтение и обработку контента версии файла. Метод не вызывается, если контент файла не был передан. 
processResponseActionAsync
[Func](https://learn.microsoft.com/dotnet/api/system.func-3)<[CardGetFileContentResponse](T_Tessa_Cards_CardGetFileContentResponse.htm),
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken),
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask)>
     Метод, выполняющий операции с полученным ответом сервиса до запуска чтения и обработки контента. 
cardMetadata [ICardMetadata](T_Tessa_Cards_ICardMetadata.htm)
    Метаинформация по типам карточек.
session [ISession](T_Tessa_Platform_Runtime_ISession.htm)
    Сессия пользователя, выполняющего получение контента файла.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
     Объект, посредством которого можно отменить выполнение запроса с клиента на сервер. Укажите CancellationToken.None, если отмена не требуется. 
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<[CardGetFileContentResponse](T_Tessa_Cards_CardGetFileContentResponse.htm)>  
Ответ на запрос по получению контента версии файла.
##  __См. также
#### Ссылки
[ICardStreamClientGetComponent -
](T_Tessa_Cards_ComponentModel_ICardStreamClientGetComponent.htm)
[Tessa.Cards.ComponentModel - пространство
имён](N_Tessa_Cards_ComponentModel.htm)
