# ICardStreamServerStoreComponent - интерфейс
Компонент, выполняющий потоковое сохранение карточки с контентом файлов на
сервере.
## __Definition
 **Пространство имён:**
[Tessa.Cards.ComponentModel](N_Tessa_Cards_ComponentModel.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface ICardStreamServerStoreComponent
VB __Копировать
     Public Interface ICardStreamServerStoreComponent
C++ __Копировать
     public interface class ICardStreamServerStoreComponent
F# __Копировать
     type ICardStreamServerStoreComponent = interface end
##  __Методы
[StoreAsync(Stream, ICardMetadata, ISession, CardServiceType,
CancellationToken)](M_Tessa_Cards_ComponentModel_ICardStreamServerStoreComponent_StoreAsync.htm)|
Сохраняет карточку с контентом файлов, которые заданы списком объектов
[Tessa.Cards.ICardFileContentProvider].  
---|---  
[StoreAsync(CardStoreRequest, IReadOnlyCollection<ICardFileContentProvider>,
ICardMetadata, ISession, Nullable<Guid>,
CancellationToken)](M_Tessa_Cards_ComponentModel_ICardStreamServerStoreComponent_StoreAsync_1.htm)|
Сохраняет карточку и её файлы, переданные в потоке карточки.  
##  __См. также
#### Ссылки
[Tessa.Cards.ComponentModel - пространство
имён](N_Tessa_Cards_ComponentModel.htm)
