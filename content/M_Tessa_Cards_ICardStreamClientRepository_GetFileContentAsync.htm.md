# ICardStreamClientRepository.GetFileContentAsync - метод
Получает контент версии файла.
##  __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     Task<CardGetFileContentResponse> GetFileContentAsync(
    	CardGetFileContentRequest request,
    	Func<Stream, CancellationToken, ValueTask> processContentActionAsync,
    	Func<CardGetFileContentResponse, CancellationToken, ValueTask> processResponseActionAsync = null,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Function GetFileContentAsync ( 
    	request As CardGetFileContentRequest,
    	processContentActionAsync As Func(Of Stream, CancellationToken, ValueTask),
    	Optional processResponseActionAsync As Func(Of CardGetFileContentResponse, CancellationToken, ValueTask) = Nothing,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task(Of CardGetFileContentResponse)
C++ __Копировать
    Task<CardGetFileContentResponse^>^ GetFileContentAsync(
    	CardGetFileContentRequest^ request, 
    	Func<Stream^, CancellationToken, ValueTask>^ processContentActionAsync, 
    	Func<CardGetFileContentResponse^, CancellationToken, ValueTask>^ processResponseActionAsync = nullptr, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     abstract GetFileContentAsync : 
            request : CardGetFileContentRequest * 
            processContentActionAsync : Func<Stream, CancellationToken, ValueTask> * 
            ?processResponseActionAsync : Func<CardGetFileContentResponse, CancellationToken, ValueTask> * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _processResponseActionAsync = defaultArg processResponseActionAsync null
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
(Optional)
     Метод, выполняющий операции с полученным ответом сервиса до запуска чтения и обработки контента. 
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
     Объект, посредством которого можно отменить выполнение запроса с клиента на сервер. Укажите CancellationToken.None, если отмена не требуется. 
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<[CardGetFileContentResponse](T_Tessa_Cards_CardGetFileContentResponse.htm)>  
Ответ на запрос по получению контента версии файла.
##  __См. также
#### Ссылки
[ICardStreamClientRepository -
](T_Tessa_Cards_ICardStreamClientRepository.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
