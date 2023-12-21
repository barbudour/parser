# ICardGetCachingStrategy - интерфейс
Стратегия кэширования объектов для операции по загрузке карточки.
## __Definition
 **Пространство имён:**
[Tessa.Cards.ComponentModel](N_Tessa_Cards_ComponentModel.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface ICardGetCachingStrategy
VB __Копировать
     Public Interface ICardGetCachingStrategy
C++ __Копировать
     public interface class ICardGetCachingStrategy
F# __Копировать
     type ICardGetCachingStrategy = interface end
##  __Методы
[AddLoader](M_Tessa_Cards_ComponentModel_ICardGetCachingStrategy_AddLoader.htm)|
Добавляет в кэш объект, выполняющий загрузку данных карточки. Если к кэшу в
момент добавления осуществляется параллельный доступ, то фактическое
добавление не гарантируется.  
---|---  
[TryGetLoader](M_Tessa_Cards_ComponentModel_ICardGetCachingStrategy_TryGetLoader.htm)|
Возвращает из кэша объект, выполняющий загрузку данных карточки заданного
типа, или null, если объект не найден в кэше.  
## __См. также
#### Ссылки
[Tessa.Cards.ComponentModel - пространство
имён](N_Tessa_Cards_ComponentModel.htm)
