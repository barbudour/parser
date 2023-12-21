# ICardStreamStoreStrategy - интерфейс
Стратегия потокового сохранения карточки с контентом файлов.
## __Definition
 **Пространство имён:**
[Tessa.Cards.ComponentModel](N_Tessa_Cards_ComponentModel.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface ICardStreamStoreStrategy
VB __Копировать
     Public Interface ICardStreamStoreStrategy
C++ __Копировать
     public interface class ICardStreamStoreStrategy
F# __Копировать
     type ICardStreamStoreStrategy = interface end
##  __Методы
[StoreAsync(CardStoreRequest, IEnumerable<ICardFileContentProvider>,
ICardMetadata, ISession, ICardStoreStreamingContext,
CancellationToken)](M_Tessa_Cards_ComponentModel_ICardStreamStoreStrategy_StoreAsync.htm)|
Сохраняет карточку с контентом файлов, которые заданы списком объектов
[Tessa.Cards.ICardFileContentProvider].  
---|---  
[StoreAsync(CardReader, CardHeader, CardStoreRequest,
IEnumerable<ICardStreamStoreFileInfo>, ICardMetadata, ISession,
ICardStoreStreamingContext,
CancellationToken)](M_Tessa_Cards_ComponentModel_ICardStreamStoreStrategy_StoreAsync_1.htm)|
Сохраняет карточку с контентом файлов, которые упакованы в потоке карточки. К
моменту исполнения метода ожидается, что из потока карточки, доступного через
объект reader, уже были прочитаны все объекты, кроме контента файлов.  
## __См. также
#### Ссылки
[Tessa.Cards.ComponentModel - пространство
имён](N_Tessa_Cards_ComponentModel.htm)
