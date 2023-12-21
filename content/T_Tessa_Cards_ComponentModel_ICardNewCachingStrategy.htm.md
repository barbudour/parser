# ICardNewCachingStrategy - интерфейс
Стратегия кэширования объектов для операции по созданию карточки.
## __Definition
 **Пространство имён:**
[Tessa.Cards.ComponentModel](N_Tessa_Cards_ComponentModel.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface ICardNewCachingStrategy
VB __Копировать
     Public Interface ICardNewCachingStrategy
C++ __Копировать
     public interface class ICardNewCachingStrategy
F# __Копировать
     type ICardNewCachingStrategy = interface end
##  __Методы
[AddResponse](M_Tessa_Cards_ComponentModel_ICardNewCachingStrategy_AddResponse.htm)|
Добавляет в кэш объект, выполняющий создание структуры карточки. Если к кэшу в
момент добавления осуществляется параллельный доступ, то фактическое
добавление не гарантируется.  
---|---  
[TryGetResponse](M_Tessa_Cards_ComponentModel_ICardNewCachingStrategy_TryGetResponse.htm)|
Возвращает из кэша объект, выполняющий создание структуры карточки заданного
типа, или null, если объект не найден в кэше.  
## __См. также
#### Ссылки
[Tessa.Cards.ComponentModel - пространство
имён](N_Tessa_Cards_ComponentModel.htm)
