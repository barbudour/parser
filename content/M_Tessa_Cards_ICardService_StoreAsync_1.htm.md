# ICardService.StoreAsync(CardStoreRequest, CancellationToken) - метод
Сохраняет карточку, переданную в запросе.
##  __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     Task<CardStoreResponse> StoreAsync(
    	CardStoreRequest request,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Function StoreAsync ( 
    	request As CardStoreRequest,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task(Of CardStoreResponse)
C++ __Копировать
    Task<CardStoreResponse^>^ StoreAsync(
    	CardStoreRequest^ request, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     abstract StoreAsync : 
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
##  __См. также
#### Ссылки
[ICardService - ](T_Tessa_Cards_ICardService.htm)
[StoreAsync - перегрузка](Overload_Tessa_Cards_ICardService_StoreAsync.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
