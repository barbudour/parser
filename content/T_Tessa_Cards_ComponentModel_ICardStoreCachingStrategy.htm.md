# ICardStoreCachingStrategy - интерфейс
Стратегия кэширования объектов для операции по сохранению карточки.
## __Definition
 **Пространство имён:**
[Tessa.Cards.ComponentModel](N_Tessa_Cards_ComponentModel.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface ICardStoreCachingStrategy
VB __Копировать
     Public Interface ICardStoreCachingStrategy
C++ __Копировать
     public interface class ICardStoreCachingStrategy
F# __Копировать
     type ICardStoreCachingStrategy = interface end
##  __Методы
[AddRowRemover](M_Tessa_Cards_ComponentModel_ICardStoreCachingStrategy_AddRowRemover.htm)|
Добавляет в кэш объект, выполняющий удаление строк из заданной коллекционной
или древовидной секции. Если к кэшу в момент добавления осуществляется
параллельный доступ, то фактическое добавление не гарантируется.  
---|---  
[TryGetRowRemover](M_Tessa_Cards_ComponentModel_ICardStoreCachingStrategy_TryGetRowRemover.htm)|
Возвращает из кэша объект, выполняющий удаление строк из заданной
коллекционной или древовидной секции, или null, если объект не найден в кэше.  
## __См. также
#### Ссылки
[Tessa.Cards.ComponentModel - пространство
имён](N_Tessa_Cards_ComponentModel.htm)
