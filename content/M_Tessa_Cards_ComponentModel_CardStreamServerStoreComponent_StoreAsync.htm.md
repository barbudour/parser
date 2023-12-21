# CardStreamServerStoreComponent.StoreAsync(Stream, ICardMetadata, ISession,
CardServiceType, CancellationToken) - метод
Сохраняет карточку с контентом файлов, которые заданы списком объектов
[Tessa.Cards.ICardFileContentProvider].
## __Definition
 **Пространство имён:**
[Tessa.Cards.ComponentModel](N_Tessa_Cards_ComponentModel.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public Task<CardStoreResponse> StoreAsync(
    	Stream cardStream,
    	ICardMetadata cardMetadata,
    	ISession session,
    	CardServiceType serviceType = CardServiceType.Default,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function StoreAsync ( 
    	cardStream As Stream,
    	cardMetadata As ICardMetadata,
    	session As ISession,
    	Optional serviceType As CardServiceType = CardServiceType.Default,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task(Of CardStoreResponse)
C++ __Копировать
     public:
    virtual Task<CardStoreResponse^>^ StoreAsync(
    	Stream^ cardStream, 
    	ICardMetadata^ cardMetadata, 
    	ISession^ session, 
    	CardServiceType serviceType = CardServiceType::Default, 
    	CancellationToken cancellationToken = CancellationToken()
    ) sealed
F# __Копировать
     abstract StoreAsync : 
            cardStream : Stream * 
            cardMetadata : ICardMetadata * 
            session : ISession * 
            ?serviceType : CardServiceType * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _serviceType = defaultArg serviceType CardServiceType.Default
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<CardStoreResponse> 
    override StoreAsync : 
            cardStream : Stream * 
            cardMetadata : ICardMetadata * 
            session : ISession * 
            ?serviceType : CardServiceType * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _serviceType = defaultArg serviceType CardServiceType.Default
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<CardStoreResponse> 
#### Параметры
cardStream [Stream](https://learn.microsoft.com/dotnet/api/system.io.stream)
cardMetadata [ICardMetadata](T_Tessa_Cards_ICardMetadata.htm)
    Метаинформация по типам карточек.
session [ISession](T_Tessa_Platform_Runtime_ISession.htm)
    Сессия с пользователем, выполняющим сохранение карточки.
serviceType [CardServiceType](T_Tessa_Cards_CardServiceType.htm) (Optional)
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<[CardStoreResponse](T_Tessa_Cards_CardStoreResponse.htm)>  
Ответ на запрос по сохранению карточки.
#### Реализации
[ICardStreamServerStoreComponent.StoreAsync(Stream, ICardMetadata, ISession,
CardServiceType,
CancellationToken)](M_Tessa_Cards_ComponentModel_ICardStreamServerStoreComponent_StoreAsync.htm)  
##  __См. также
#### Ссылки
[CardStreamServerStoreComponent -
](T_Tessa_Cards_ComponentModel_CardStreamServerStoreComponent.htm)
[StoreAsync -
перегрузка](Overload_Tessa_Cards_ComponentModel_CardStreamServerStoreComponent_StoreAsync.htm)
[Tessa.Cards.ComponentModel - пространство
имён](N_Tessa_Cards_ComponentModel.htm)
