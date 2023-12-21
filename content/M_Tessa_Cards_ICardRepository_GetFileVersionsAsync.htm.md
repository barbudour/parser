# ICardRepository.GetFileVersionsAsync - метод
Возвращает информацию о версиях файла по заданному запросу.
##  __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     Task<CardGetFileVersionsResponse> GetFileVersionsAsync(
    	CardGetFileVersionsRequest request,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Function GetFileVersionsAsync ( 
    	request As CardGetFileVersionsRequest,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task(Of CardGetFileVersionsResponse)
C++ __Копировать
    Task<CardGetFileVersionsResponse^>^ GetFileVersionsAsync(
    	CardGetFileVersionsRequest^ request, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     abstract GetFileVersionsAsync : 
            request : CardGetFileVersionsRequest * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<CardGetFileVersionsResponse> 
#### Параметры
request
[CardGetFileVersionsRequest](T_Tessa_Cards_CardGetFileVersionsRequest.htm)
    Запрос, содержащий информацию о версиях файла, которые должны быть возвращены.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<[CardGetFileVersionsResponse](T_Tessa_Cards_CardGetFileVersionsResponse.htm)>  
Ответ на запрос, содержащий данные запрашиваемых версий файла.
##  __См. также
#### Ссылки
[ICardRepository - ](T_Tessa_Cards_ICardRepository.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
