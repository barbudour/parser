# ICardDeleteStrategy - интерфейс
Стратегия по удалению карточки.
## __Definition
 **Пространство имён:**
[Tessa.Cards.ComponentModel](N_Tessa_Cards_ComponentModel.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface ICardDeleteStrategy
VB __Копировать
     Public Interface ICardDeleteStrategy
C++ __Копировать
     public interface class ICardDeleteStrategy
F# __Копировать
     type ICardDeleteStrategy = interface end
##  __Свойства
[TransactionStrategy](P_Tessa_Cards_ComponentModel_ICardDeleteStrategy_TransactionStrategy.htm)|
Стратегия обеспечения блокировок и выполнения транзакций, используемая
сервисом.  
---|---  
##  __Методы
[DeleteAsync(CardDeleteContext)](M_Tessa_Cards_ComponentModel_ICardDeleteStrategy_DeleteAsync_1.htm)|
Удаляет карточку по данным, указанным в контексте операции.  
---|---  
[DeleteAsync(Guid, CardDeletionMode, ICardMetadata, IValidationResultBuilder,
Nullable<Guid>, String, Boolean,
CancellationToken)](M_Tessa_Cards_ComponentModel_ICardDeleteStrategy_DeleteAsync.htm)|
Удаляет карточку по заданным параметрам. Возвращает тип удаляемой карточки и
список ссылок на контенты файлов для удаления; эти объекты равны null, если
тип определить не удалось и удаление не было выполнено.  
## __См. также
#### Ссылки
[Tessa.Cards.ComponentModel - пространство
имён](N_Tessa_Cards_ComponentModel.htm)
