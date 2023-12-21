# CardStreamServerStoreComponent.StoreAsync(CardStoreRequest,
IReadOnlyCollection<ICardFileContentProvider>, ICardMetadata, ISession,
Nullable<Guid>, CancellationToken) - метод
Сохраняет карточку и её файлы, переданные в потоке карточки.
##  __Definition
 **Пространство имён:**
[Tessa.Cards.ComponentModel](N_Tessa_Cards_ComponentModel.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public Task<CardStoreResponse> StoreAsync(
    	CardStoreRequest request,
    	IReadOnlyCollection<ICardFileContentProvider> files,
    	ICardMetadata cardMetadata,
    	ISession session,
    	Guid? operationID = null,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function StoreAsync ( 
    	request As CardStoreRequest,
    	files As IReadOnlyCollection(Of ICardFileContentProvider),
    	cardMetadata As ICardMetadata,
    	session As ISession,
    	Optional operationID As Guid? = Nothing,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task(Of CardStoreResponse)
C++ __Копировать
     public:
    virtual Task<CardStoreResponse^>^ StoreAsync(
    	CardStoreRequest^ request, 
    	IReadOnlyCollection<ICardFileContentProvider^>^ files, 
    	ICardMetadata^ cardMetadata, 
    	ISession^ session, 
    	Nullable<Guid> operationID = nullptr, 
    	CancellationToken cancellationToken = CancellationToken()
    ) sealed
F# __Копировать
     abstract StoreAsync : 
            request : CardStoreRequest * 
            files : IReadOnlyCollection<ICardFileContentProvider> * 
            cardMetadata : ICardMetadata * 
            session : ISession * 
            ?operationID : Nullable<Guid> * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _operationID = defaultArg operationID null
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<CardStoreResponse> 
    override StoreAsync : 
            request : CardStoreRequest * 
            files : IReadOnlyCollection<ICardFileContentProvider> * 
            cardMetadata : ICardMetadata * 
            session : ISession * 
            ?operationID : Nullable<Guid> * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _operationID = defaultArg operationID null
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<CardStoreResponse> 
#### Параметры
request [CardStoreRequest](T_Tessa_Cards_CardStoreRequest.htm)
files
[IReadOnlyCollection](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlycollection-1)<[ICardFileContentProvider](T_Tessa_Cards_ICardFileContentProvider.htm)>
cardMetadata [ICardMetadata](T_Tessa_Cards_ICardMetadata.htm)
    Метаинформация по типам карточек.
session [ISession](T_Tessa_Platform_Runtime_ISession.htm)
    Сессия пользователя, выполняющего сохранение карточки с контентом файлов.
operationID
[Nullable](https://learn.microsoft.com/dotnet/api/system.nullable-1)<[Guid](https://learn.microsoft.com/dotnet/api/system.guid)>
(Optional)
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<[CardStoreResponse](T_Tessa_Cards_CardStoreResponse.htm)>  
Ответ на запрос по сохранению карточки.
#### Реализации
[ICardStreamServerStoreComponent.StoreAsync(CardStoreRequest,
IReadOnlyCollection<ICardFileContentProvider>, ICardMetadata, ISession,
Nullable<Guid>,
CancellationToken)](M_Tessa_Cards_ComponentModel_ICardStreamServerStoreComponent_StoreAsync_1.htm)  
##  __См. также
#### Ссылки
[CardStreamServerStoreComponent -
](T_Tessa_Cards_ComponentModel_CardStreamServerStoreComponent.htm)
[StoreAsync -
перегрузка](Overload_Tessa_Cards_ComponentModel_CardStreamServerStoreComponent_StoreAsync.htm)
[Tessa.Cards.ComponentModel - пространство
имён](N_Tessa_Cards_ComponentModel.htm)
