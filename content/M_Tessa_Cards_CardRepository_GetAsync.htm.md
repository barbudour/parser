# CardRepository.GetAsync - метод
Возвращает данные карточки по заданному запросу.
##  __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public Task<CardGetResponse> GetAsync(
    	CardGetRequest request,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function GetAsync ( 
    	request As CardGetRequest,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task(Of CardGetResponse)
C++ __Копировать
     public:
    virtual Task<CardGetResponse^>^ GetAsync(
    	CardGetRequest^ request, 
    	CancellationToken cancellationToken = CancellationToken()
    ) sealed
F# __Копировать
     abstract GetAsync : 
            request : CardGetRequest * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<CardGetResponse> 
    override GetAsync : 
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
#### Реализации
[ICardRepository.GetAsync(CardGetRequest,
CancellationToken)](M_Tessa_Cards_ICardRepository_GetAsync.htm)  
##  __См. также
#### Ссылки
[CardRepository - ](T_Tessa_Cards_CardRepository.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
