# CardServiceClient.StoreAsync(CardStoreRequest, CancellationToken) - метод
Сохраняет карточку, переданную в запросе.
##  __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public Task<CardStoreResponse> StoreAsync(
    	CardStoreRequest request,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function StoreAsync ( 
    	request As CardStoreRequest,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task(Of CardStoreResponse)
C++ __Копировать
     public:
    virtual Task<CardStoreResponse^>^ StoreAsync(
    	CardStoreRequest^ request, 
    	CancellationToken cancellationToken = CancellationToken()
    ) sealed
F# __Копировать
     abstract StoreAsync : 
            request : CardStoreRequest * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<CardStoreResponse> 
    override StoreAsync : 
            request : CardStoreRequest * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<CardStoreResponse> 
#### Параметры
request [CardStoreRequest](T_Tessa_Cards_CardStoreRequest.htm)
    Запрос на сохранение карточки, содержащий изменённую информацию о карточке.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<[CardStoreResponse](T_Tessa_Cards_CardStoreResponse.htm)>  
Ответ на запрос, содержащий информацию о валидации процесса сохранения
карточки, включая сообщения об ошибках.
#### Реализации
[ICardService.StoreAsync(CardStoreRequest,
CancellationToken)](M_Tessa_Cards_ICardService_StoreAsync_1.htm)  
##  __См. также
#### Ссылки
[CardServiceClient - ](T_Tessa_Cards_CardServiceClient.htm)
[StoreAsync -
перегрузка](Overload_Tessa_Cards_CardServiceClient_StoreAsync.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
