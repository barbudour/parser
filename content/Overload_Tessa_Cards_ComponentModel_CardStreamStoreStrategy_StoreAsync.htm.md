# CardStreamStoreStrategy.StoreAsync - метод
##  __Список перегрузок
[StoreAsync(CardStoreRequest, IEnumerable<ICardFileContentProvider>,
ICardMetadata, ISession, ICardStoreStreamingContext,
CancellationToken)](M_Tessa_Cards_ComponentModel_CardStreamStoreStrategy_StoreAsync.htm)|
Сохраняет карточку с контентом файлов, которые заданы списком объектов
[Tessa.Cards.ICardFileContentProvider].  
---|---  
[StoreAsync(CardReader, CardHeader, CardStoreRequest,
IEnumerable<ICardStreamStoreFileInfo>, ICardMetadata, ISession,
ICardStoreStreamingContext,
CancellationToken)](M_Tessa_Cards_ComponentModel_CardStreamStoreStrategy_StoreAsync_1.htm)|
Сохраняет карточку с контентом файлов, которые упакованы в потоке карточки. К
моменту исполнения метода ожидается, что из потока карточки, доступного через
объект reader, уже были прочитаны все объекты, кроме контента файлов.  
## __См. также
#### Ссылки
[CardStreamStoreStrategy -
](T_Tessa_Cards_ComponentModel_CardStreamStoreStrategy.htm)
[Tessa.Cards.ComponentModel - пространство
имён](N_Tessa_Cards_ComponentModel.htm)
