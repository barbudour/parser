# CardStreamClientStoreExtendedComponent.StoreAsync - метод
Выполняет сохранение карточки с контентом файлов, которые упаковываются в
поток карточки перед отправкой на сервер.
## __Definition
 **Пространство имён:**
[Tessa.Cards.ComponentModel](N_Tessa_Cards_ComponentModel.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public ICardStoreAsyncResponse StoreAsync(
    	CardStoreRequest request,
    	CardHeader header,
    	IReadOnlyCollection<Func<CancellationToken, ValueTask<Stream>>> fileStreams,
    	long totalFileLength,
    	ICardMetadata cardMetadata,
    	ISession session,
    	ICardStoreStreamingContext streamingContext = null,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function StoreAsync ( 
    	request As CardStoreRequest,
    	header As CardHeader,
    	fileStreams As IReadOnlyCollection(Of Func(Of CancellationToken, ValueTask(Of Stream))),
    	totalFileLength As Long,
    	cardMetadata As ICardMetadata,
    	session As ISession,
    	Optional streamingContext As ICardStoreStreamingContext = Nothing,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ICardStoreAsyncResponse
C++ __Копировать
     public:
    virtual ICardStoreAsyncResponse^ StoreAsync(
    	CardStoreRequest^ request, 
    	CardHeader^ header, 
    	IReadOnlyCollection<Func<CancellationToken, ValueTask<Stream^>>^>^ fileStreams, 
    	long long totalFileLength, 
    	ICardMetadata^ cardMetadata, 
    	ISession^ session, 
    	ICardStoreStreamingContext^ streamingContext = nullptr, 
    	CancellationToken cancellationToken = CancellationToken()
    ) sealed
F# __Копировать
     abstract StoreAsync : 
            request : CardStoreRequest * 
            header : CardHeader * 
            fileStreams : IReadOnlyCollection<Func<CancellationToken, ValueTask<Stream>>> * 
            totalFileLength : int64 * 
            cardMetadata : ICardMetadata * 
            session : ISession * 
            ?streamingContext : ICardStoreStreamingContext * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _streamingContext = defaultArg streamingContext null
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ICardStoreAsyncResponse 
    override StoreAsync : 
            request : CardStoreRequest * 
            header : CardHeader * 
            fileStreams : IReadOnlyCollection<Func<CancellationToken, ValueTask<Stream>>> * 
            totalFileLength : int64 * 
            cardMetadata : ICardMetadata * 
            session : ISession * 
            ?streamingContext : ICardStoreStreamingContext * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _streamingContext = defaultArg streamingContext null
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ICardStoreAsyncResponse 
#### Параметры
request [CardStoreRequest](T_Tessa_Cards_CardStoreRequest.htm)
    Запрос на сохранение карточки.
header [CardHeader](T_Tessa_Cards_ComponentModel_CardHeader.htm)
    Заголовок потока карточки, в котором производится сохранение.
fileStreams
[IReadOnlyCollection](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlycollection-1)<[Func](https://learn.microsoft.com/dotnet/api/system.func-2)<[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken),
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<[Stream](https://learn.microsoft.com/dotnet/api/system.io.stream)>>>
     Коллекция функций, создающих потоки для сохранения каждого из файлов. Функции должны быть упорядочены в соответствии с порядком файлов в заголовке потока header. 
totalFileLength [Int64](https://learn.microsoft.com/dotnet/api/system.int64)
     Суммарная длина файлов, требуемая для расчёта процента готовности операции. Не может быть отрицательным числом. 
cardMetadata [ICardMetadata](T_Tessa_Cards_ICardMetadata.htm)
    Метаинформация по типам карточек.
session [ISession](T_Tessa_Platform_Runtime_ISession.htm)
    Сессия, в рамках которой выполняется сохранение.
streamingContext
[ICardStoreStreamingContext](T_Tessa_Cards_ComponentModel_ICardStoreStreamingContext.htm)
(Optional)
     Контекст, передаваемый от запроса на потоковое сохранение карточки с файлами до запроса на обычное сохранение карточки или null, если при сохранении не передаётся содержимое файлов. 
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[ICardStoreAsyncResponse](T_Tessa_Cards_ICardStoreAsyncResponse.htm)  
Ответ на запрос по сохранению карточки.
#### Реализации
[ICardStreamClientStoreComponent.StoreAsync(CardStoreRequest, CardHeader,
IReadOnlyCollection<Func<CancellationToken, ValueTask<Stream>>>, Int64,
ICardMetadata, ISession, ICardStoreStreamingContext,
CancellationToken)](M_Tessa_Cards_ComponentModel_ICardStreamClientStoreComponent_StoreAsync.htm)  
##  __См. также
#### Ссылки
[CardStreamClientStoreExtendedComponent -
](T_Tessa_Cards_ComponentModel_CardStreamClientStoreExtendedComponent.htm)
[Tessa.Cards.ComponentModel - пространство
имён](N_Tessa_Cards_ComponentModel.htm)
