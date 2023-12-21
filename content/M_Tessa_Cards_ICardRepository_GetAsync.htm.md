# ICardRepository.GetAsync - метод
Возвращает данные карточки по заданному запросу.
##  __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     Task<CardGetResponse> GetAsync(
    	CardGetRequest request,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Function GetAsync ( 
    	request As CardGetRequest,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task(Of CardGetResponse)
C++ __Копировать
    Task<CardGetResponse^>^ GetAsync(
    	CardGetRequest^ request, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     abstract GetAsync : 
            request : CardGetRequest * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<CardGetResponse> 
#### Параметры
request [CardGetRequest](T_Tessa_Cards_CardGetRequest.htm)
    Запрос, содержащий информацию по карточке, которая должна быть возвращена.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<[CardGetResponse](T_Tessa_Cards_CardGetResponse.htm)>  
Ответ на запрос, содержащий данные запрашиваемой карточки.
##  __См. также
#### Ссылки
[ICardRepository - ](T_Tessa_Cards_ICardRepository.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
