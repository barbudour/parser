# CardStreamStoreStrategy.StoreAsync(CardStoreRequest,
IEnumerable<ICardFileContentProvider>, ICardMetadata, ISession,
ICardStoreStreamingContext, CancellationToken) - метод
Сохраняет карточку с контентом файлов, которые заданы списком объектов
[Tessa.Cards.ICardFileContentProvider].
## __Definition
 **Пространство имён:**
[Tessa.Cards.ComponentModel](N_Tessa_Cards_ComponentModel.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public Task<CardStoreResponse> StoreAsync(
    	CardStoreRequest request,
    	IEnumerable<ICardFileContentProvider> files,
    	ICardMetadata cardMetadata,
    	ISession session,
    	ICardStoreStreamingContext streamingContext,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function StoreAsync ( 
    	request As CardStoreRequest,
    	files As IEnumerable(Of ICardFileContentProvider),
    	cardMetadata As ICardMetadata,
    	session As ISession,
    	streamingContext As ICardStoreStreamingContext,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task(Of CardStoreResponse)
C++ __Копировать
     public:
    virtual Task<CardStoreResponse^>^ StoreAsync(
    	CardStoreRequest^ request, 
    	IEnumerable<ICardFileContentProvider^>^ files, 
    	ICardMetadata^ cardMetadata, 
    	ISession^ session, 
    	ICardStoreStreamingContext^ streamingContext, 
    	CancellationToken cancellationToken = CancellationToken()
    ) sealed
F# __Копировать
     abstract StoreAsync : 
            request : CardStoreRequest * 
            files : IEnumerable<ICardFileContentProvider> * 
            cardMetadata : ICardMetadata * 
            session : ISession * 
            streamingContext : ICardStoreStreamingContext * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<CardStoreResponse> 
    override StoreAsync : 
            request : CardStoreRequest * 
            files : IEnumerable<ICardFileContentProvider> * 
            cardMetadata : ICardMetadata * 
            session : ISession * 
            streamingContext : ICardStoreStreamingContext * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<CardStoreResponse> 
#### Параметры
request [CardStoreRequest](T_Tessa_Cards_CardStoreRequest.htm)
    Запрос на сохранение карточки.
files
[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)<[ICardFileContentProvider](T_Tessa_Cards_ICardFileContentProvider.htm)>
    Список объектов, обеспечивающих получение контента файла по его идентификатору.
cardMetadata [ICardMetadata](T_Tessa_Cards_ICardMetadata.htm)
    Метаинформация по типам карточек.
session [ISession](T_Tessa_Platform_Runtime_ISession.htm)
    Сессия с пользователем, выполняющим сохранение карточки.
streamingContext
[ICardStoreStreamingContext](T_Tessa_Cards_ComponentModel_ICardStoreStreamingContext.htm)
     Контекст, передаваемый от запроса на потоковое сохранение карточки с файлами до запроса на обычное сохранение карточки. Значение не равно null. 
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<[CardStoreResponse](T_Tessa_Cards_CardStoreResponse.htm)>  
Ответ на запрос по сохранению карточки.
#### Реализации
[ICardStreamStoreStrategy.StoreAsync(CardStoreRequest,
IEnumerable<ICardFileContentProvider>, ICardMetadata, ISession,
ICardStoreStreamingContext,
CancellationToken)](M_Tessa_Cards_ComponentModel_ICardStreamStoreStrategy_StoreAsync.htm)  
##  __См. также
#### Ссылки
[CardStreamStoreStrategy -
](T_Tessa_Cards_ComponentModel_CardStreamStoreStrategy.htm)
[StoreAsync -
перегрузка](Overload_Tessa_Cards_ComponentModel_CardStreamStoreStrategy_StoreAsync.htm)
[Tessa.Cards.ComponentModel - пространство
имён](N_Tessa_Cards_ComponentModel.htm)
