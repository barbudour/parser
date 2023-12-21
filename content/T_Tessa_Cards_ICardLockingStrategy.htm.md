# ICardLockingStrategy - интерфейс
Стратегия по управлению блокировками на чтение и запись карточек. Некорректное
использование методов в этом интерфейсе может привести к "повисшим"
блокировкам, используйте с осторожностью.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface ICardLockingStrategy
VB __Копировать
     Public Interface ICardLockingStrategy
C++ __Копировать
     public interface class ICardLockingStrategy
F# __Копировать
     type ICardLockingStrategy = interface end
##  __Методы
[ObtainReaderLockAsync](M_Tessa_Cards_ICardLockingStrategy_ObtainReaderLockAsync.htm)|
Выполняет взятие блокировки на чтение карточки. Возвращает признак успешного
взятия блокировки и идентификатор типа для заданной карточки.  
---|---  
[ObtainWriterLockAsync](M_Tessa_Cards_ICardLockingStrategy_ObtainWriterLockAsync.htm)|
Выполняет взятие блокировки на запись карточки. Возвращает признак успешного
взятия блокировки.  
[ReleaseReaderLockAsync](M_Tessa_Cards_ICardLockingStrategy_ReleaseReaderLockAsync.htm)|
Выполняет снятие блокировки на чтение карточки.  
[ReleaseWriterLockAsync](M_Tessa_Cards_ICardLockingStrategy_ReleaseWriterLockAsync.htm)|
Выполняет снятие блокировки на запись карточки.  
##  __См. также
#### Ссылки
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
