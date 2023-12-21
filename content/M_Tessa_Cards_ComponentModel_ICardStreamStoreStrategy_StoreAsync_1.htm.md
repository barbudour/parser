# ICardStreamStoreStrategy.StoreAsync(CardReader, CardHeader,
CardStoreRequest, IEnumerable<ICardStreamStoreFileInfo>, ICardMetadata,
ISession, ICardStoreStreamingContext, CancellationToken) - метод
Сохраняет карточку с контентом файлов, которые упакованы в потоке карточки. К
моменту исполнения метода ожидается, что из потока карточки, доступного через
объект reader, уже были прочитаны все объекты, кроме контента файлов.
## __Definition
 **Пространство имён:**
[Tessa.Cards.ComponentModel](N_Tessa_Cards_ComponentModel.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     Task<CardStoreResponse> StoreAsync(
    	CardReader reader,
    	CardHeader header,
    	CardStoreRequest request,
    	IEnumerable<ICardStreamStoreFileInfo> files,
    	ICardMetadata cardMetadata,
    	ISession session,
    	ICardStoreStreamingContext streamingContext,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Function StoreAsync ( 
    	reader As CardReader,
    	header As CardHeader,
    	request As CardStoreRequest,
    	files As IEnumerable(Of ICardStreamStoreFileInfo),
    	cardMetadata As ICardMetadata,
    	session As ISession,
    	streamingContext As ICardStoreStreamingContext,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task(Of CardStoreResponse)
C++ __Копировать
    Task<CardStoreResponse^>^ StoreAsync(
    	CardReader^ reader, 
    	CardHeader^ header, 
    	CardStoreRequest^ request, 
    	IEnumerable<ICardStreamStoreFileInfo^>^ files, 
    	ICardMetadata^ cardMetadata, 
    	ISession^ session, 
    	ICardStoreStreamingContext^ streamingContext, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     abstract StoreAsync : 
            reader : CardReader * 
            header : CardHeader * 
            request : CardStoreRequest * 
            files : IEnumerable<ICardStreamStoreFileInfo> * 
            cardMetadata : ICardMetadata * 
            session : ISession * 
            streamingContext : ICardStoreStreamingContext * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<CardStoreResponse> 
#### Параметры
reader [CardReader](T_Tessa_Cards_ComponentModel_CardReader.htm)
    Объект, осуществляющий чтение из потока карточки.
header [CardHeader](T_Tessa_Cards_ComponentModel_CardHeader.htm)
    Заголовок потока карточки.
request [CardStoreRequest](T_Tessa_Cards_CardStoreRequest.htm)
    Запрос на сохранение карточки.
files
[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)<[ICardStreamStoreFileInfo](T_Tessa_Cards_ComponentModel_ICardStreamStoreFileInfo.htm)>
    Информация о файлах, сохранённых в потоке карточки.
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
##  __См. также
#### Ссылки
[ICardStreamStoreStrategy -
](T_Tessa_Cards_ComponentModel_ICardStreamStoreStrategy.htm)
[StoreAsync -
перегрузка](Overload_Tessa_Cards_ComponentModel_ICardStreamStoreStrategy_StoreAsync.htm)
[Tessa.Cards.ComponentModel - пространство
имён](N_Tessa_Cards_ComponentModel.htm)
