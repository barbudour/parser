# CardRequestClientComponent.RequestAsync - метод
Выполняет универсальный запрос к сервису карточек.
##  __Definition
 **Пространство имён:**
[Tessa.Cards.ComponentModel](N_Tessa_Cards_ComponentModel.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public Task<CardResponse> RequestAsync(
    	CardRequest request,
    	ICardMetadata cardMetadata,
    	ISession session,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function RequestAsync ( 
    	request As CardRequest,
    	cardMetadata As ICardMetadata,
    	session As ISession,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task(Of CardResponse)
C++ __Копировать
     public:
    virtual Task<CardResponse^>^ RequestAsync(
    	CardRequest^ request, 
    	ICardMetadata^ cardMetadata, 
    	ISession^ session, 
    	CancellationToken cancellationToken = CancellationToken()
    ) sealed
F# __Копировать
     abstract RequestAsync : 
            request : CardRequest * 
            cardMetadata : ICardMetadata * 
            session : ISession * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<CardResponse> 
    override RequestAsync : 
            request : CardRequest * 
            cardMetadata : ICardMetadata * 
            session : ISession * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<CardResponse> 
#### Параметры
request [CardRequest](T_Tessa_Cards_CardRequest.htm)
    Универсальный запрос к сервису карточек.
cardMetadata [ICardMetadata](T_Tessa_Cards_ICardMetadata.htm)
    Метаинформация по типам карточек.
session [ISession](T_Tessa_Platform_Runtime_ISession.htm)
    Сессия пользователя, выполняющего запрос.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<[CardResponse](T_Tessa_Cards_CardResponse.htm)>  
Ответ на универсальный запрос к сервису карточек.
#### Реализации
[ICardRequestComponent.RequestAsync(CardRequest, ICardMetadata, ISession,
CancellationToken)](M_Tessa_Cards_ComponentModel_ICardRequestComponent_RequestAsync.htm)  
##  __См. также
#### Ссылки
[CardRequestClientComponent -
](T_Tessa_Cards_ComponentModel_CardRequestClientComponent.htm)
[Tessa.Cards.ComponentModel - пространство
имён](N_Tessa_Cards_ComponentModel.htm)
