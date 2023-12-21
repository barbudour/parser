# NumberHelper - класс
Вспомогательные методы для API управления номерами.
## __Definition
 **Пространство имён:** [Tessa.Cards.Numbers](N_Tessa_Cards_Numbers.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static class NumberHelper
VB __Копировать
     Public NotInheritable Class NumberHelper
C++ __Копировать
     public ref class NumberHelper abstract sealed
F# __Копировать
     [<AbstractClassAttribute>]
    [<SealedAttribute>]
    type NumberHelper = class end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ NumberHelper
##  __Методы
[GetContainer<T>](M_Tessa_Cards_Numbers_NumberHelper_GetContainer__1.htm)|
Возвращает объект-контейнер, позволяющий получить результат ссылочного типа
для заданного действия с номером.  
---|---  
[GetNumberAndSetToContextPredicateAsync](M_Tessa_Cards_Numbers_NumberHelper_GetNumberAndSetToContextPredicateAsync.htm)|
Функция предиката, передаваемая в [NotifyOnEventAsync(INumberContext,
NumberEventType, Func<INumberContext, CancellationToken, Task<Boolean>>,
Func<INumberContext, CancellationToken, Task<Boolean>>,
CancellationToken)](M_Tessa_Cards_Numbers_INumberDirectorBase_NotifyOnEventAsync.htm)
и устанавливающая в контексте номер, полученный по заданному типу numberType.  
[GetNumberFromQueueItemAsync](M_Tessa_Cards_Numbers_NumberHelper_GetNumberFromQueueItemAsync.htm)|
Возвращает номер для выполнения действия по информации, содержащейся в объекте
[NumberQueueItem](T_Tessa_Cards_Numbers_NumberQueueItem.htm). Возвращённый
номер может быть пустым, но не может быть равен null.  
[ProcessExtensionsWhileClosingOrRefreshingCardAsync](M_Tessa_Cards_Numbers_NumberHelper_ProcessExtensionsWhileClosingOrRefreshingCardAsync.htm)|
Выполняет расширения и обрабатывает очередь действий для события закрытия
вкладки карточки или обновления карточки
[ProcessingQueueWhileClosingOrRefreshingCard](F_Tessa_Cards_Numbers_NumberEventTypes_ProcessingQueueWhileClosingOrRefreshingCard.htm).
Рекомендуется вызывать метод на клиенте, где доступны клиентские зависимости и
текущий контекст UIContext.Current. Однако, это не является требованием
платформы, т.е. при использовании реализации
[INumberDirector](T_Tessa_Cards_Numbers_INumberDirector.htm) из типового
решения возможно выполнение метода и на сервере. Метод может потребоваться
вызвать вручную, например, если запросом [NewAsync(CardNewRequest,
CancellationToken)](M_Tessa_Cards_ICardRepository_NewAsync.htm) была создана
(но не сохранена) карточка, для которой в настройках указано "выделять номер
при создании". В этом случае номер будет зарезервирован, но не освобождён, и
для выполнения всех действий, связанных с освобождением номеров, требуется
вызвать этот метод, но только если карточка не будет сохранена запросом
[StoreAsync(CardStoreRequest,
CancellationToken)](M_Tessa_Cards_ICardRepository_StoreAsync.htm).  
[StoreNumberWithQueueItemAsync](M_Tessa_Cards_Numbers_NumberHelper_StoreNumberWithQueueItemAsync.htm)|
Выполняет сохранение номера в местоположение, заданное в объекте
[NumberQueueItem](T_Tessa_Cards_Numbers_NumberQueueItem.htm), если тип
местоположения отличен от
[NotAssigned](F_Tessa_Cards_Numbers_NumberLocationTypes_NotAssigned.htm).  
## __Поля
[ReleaseIfSequentialOnlyKey](F_Tessa_Cards_Numbers_NumberHelper_ReleaseIfSequentialOnlyKey.htm)|
Ключ для события
[ReleasingNumberFromControl](F_Tessa_Cards_Numbers_NumberEventTypes_ReleasingNumberFromControl.htm),
заданный в контексте действия с номером
[Info](P_Tessa_Cards_Numbers_INumberContext_Info.htm) в том случае, если номер
требуется освободить только номер из последовательности, но не номер, заданный
вручную.  
---|---  
## __См. также
#### Ссылки
[Tessa.Cards.Numbers - пространство имён](N_Tessa_Cards_Numbers.htm)
