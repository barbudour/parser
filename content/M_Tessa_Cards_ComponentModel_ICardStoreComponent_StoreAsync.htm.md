# ICardStoreComponent.StoreAsync - метод
Выполняет сохранение карточки.
##  __Definition
 **Пространство имён:**
[Tessa.Cards.ComponentModel](N_Tessa_Cards_ComponentModel.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     Task<CardStoreResponse> StoreAsync(
    	CardStoreRequest request,
    	ICardMetadata cardMetadata,
    	ISession session,
    	ICardStoreStreamingContext streamingContext = null,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Function StoreAsync ( 
    	request As CardStoreRequest,
    	cardMetadata As ICardMetadata,
    	session As ISession,
    	Optional streamingContext As ICardStoreStreamingContext = Nothing,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task(Of CardStoreResponse)
C++ __Копировать
    Task<CardStoreResponse^>^ StoreAsync(
    	CardStoreRequest^ request, 
    	ICardMetadata^ cardMetadata, 
    	ISession^ session, 
    	ICardStoreStreamingContext^ streamingContext = nullptr, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     abstract StoreAsync : 
            request : CardStoreRequest * 
            cardMetadata : ICardMetadata * 
            session : ISession * 
            ?streamingContext : ICardStoreStreamingContext * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _streamingContext = defaultArg streamingContext null
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<CardStoreResponse> 
#### Параметры
request [CardStoreRequest](T_Tessa_Cards_CardStoreRequest.htm)
    Запрос на сохранение карточки.
cardMetadata [ICardMetadata](T_Tessa_Cards_ICardMetadata.htm)
    Метаинформация по типам карточек.
session [ISession](T_Tessa_Platform_Runtime_ISession.htm)
    Сессия пользователя, выполняющего сохранение карточки.
streamingContext
[ICardStoreStreamingContext](T_Tessa_Cards_ComponentModel_ICardStoreStreamingContext.htm)
(Optional)
     Контекст, передаваемый от запроса на потоковое сохранение карточки с файлами до запроса на обычное сохранение карточки, или null, если контекст не задан. 
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<[CardStoreResponse](T_Tessa_Cards_CardStoreResponse.htm)>  
Асинхронная операция, возвращающая ответ на запрос по сохранению карточки.
##  __См. также
#### Ссылки
[ICardStoreComponent - ](T_Tessa_Cards_ComponentModel_ICardStoreComponent.htm)
[Tessa.Cards.ComponentModel - пространство
имён](N_Tessa_Cards_ComponentModel.htm)
