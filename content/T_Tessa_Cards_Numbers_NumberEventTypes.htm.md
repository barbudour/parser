# NumberEventTypes - класс
Стандартные типы действий с номерами.
## __Definition
 **Пространство имён:** [Tessa.Cards.Numbers](N_Tessa_Cards_Numbers.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static class NumberEventTypes
VB __Копировать
     Public NotInheritable Class NumberEventTypes
C++ __Копировать
     public ref class NumberEventTypes abstract sealed
F# __Копировать
     [<AbstractClassAttribute>]
    [<SealedAttribute>]
    type NumberEventTypes = class end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ NumberEventTypes
##  __Методы
[IsKnown](M_Tessa_Cards_Numbers_NumberEventTypes_IsKnown.htm)|  Возвращает
признак того, что тип события, происходящего с номером, является известным для
стандартного API.  
---|---  
## __Поля
[All](F_Tessa_Cards_Numbers_NumberEventTypes_All.htm)|  Список всех типов
событий, происходящих с номерами, которые являются частью стандартного API.  
---|---  
[ClosingTab](F_Tessa_Cards_Numbers_NumberEventTypes_ClosingTab.htm)|
Закрывается вкладка с карточкой на стороне клиента. При этом может
потребоваться освободить номер, если он был зарезервирован и ещё не был занят.
Обычно выполняется на клиенте.  
[CreatingCard](F_Tessa_Cards_Numbers_NumberEventTypes_CreatingCard.htm)|
Создаётся карточка (обычным способом или по шаблону). При этом может
потребоваться зарезервировать номер. Обычно выполняется на сервере на этапе
AfterRequest после создания карточки методом [NewAsync(CardNewRequest,
CancellationToken)](M_Tessa_Cards_ICardRepository_NewAsync.htm).  
[CustomAction](F_Tessa_Cards_Numbers_NumberEventTypes_CustomAction.htm)|
Произвольное действие с номерами, которое можно использовать в расширениях,
где не принципиально место возникновения события с номерами.  
[CustomActionFromControl](F_Tessa_Cards_Numbers_NumberEventTypes_CustomActionFromControl.htm)|
Другое действие, специфичное для элемента управления. Выполняется на клиенте.  
[DeletingBackupCard](F_Tessa_Cards_Numbers_NumberEventTypes_DeletingBackupCard.htm)|
Карточка окончательно удаляется, т.е. удаляется её удалённая карточка
[DeletedTypeName](F_Tessa_Cards_CardHelper_DeletedTypeName.htm). При этом
может потребоваться освободить занятый номер. Обычно выполняется на сервере на
этапе BeforeCommitTransaction при удалении удалённой карточки методом
[DeleteAsync(CardDeleteRequest,
CancellationToken)](M_Tessa_Cards_ICardRepository_DeleteAsync.htm).  
[DeletingCardWithoutBackup](F_Tessa_Cards_Numbers_NumberEventTypes_DeletingCardWithoutBackup.htm)|
Карточка удаляется без возможности восстановления. При этом может
потребоваться освободить занятый номер. Обычно выполняется на сервере на этапе
BeforeCommitTransaction при удалении карточки без возможности восстановления
методом [DeleteAsync(CardDeleteRequest,
CancellationToken)](M_Tessa_Cards_ICardRepository_DeleteAsync.htm).  
[DeregisteringCard](F_Tessa_Cards_Numbers_NumberEventTypes_DeregisteringCard.htm)|
Выполняется дерегистрация карточки. При этом может потребоваться освободить
регистрационный номер. Обычно выполняется на сервере на этапе BeforeRequest
перед сохранением карточки методом [StoreAsync(CardStoreRequest,
CancellationToken)](M_Tessa_Cards_ICardRepository_StoreAsync.htm).  
[GettingDigest](F_Tessa_Cards_Numbers_NumberEventTypes_GettingDigest.htm)|
Производится вычисление Digest карточки на основании её номера. Может
выполняться на клиенте или на сервере.  
[ImportingCard](F_Tessa_Cards_Numbers_NumberEventTypes_ImportingCard.htm)|
Карточка импортируется. При этом может потребоваться занять номер, который был
ранее занят. Обычно выполняется на сервере на этапе BeforeCommitTransaction в
транзакции на сохранение карточки методом [StoreAsync(CardStoreRequest,
CancellationToken)](M_Tessa_Cards_ICardRepository_StoreAsync.htm).  
[PreparingTemplate](F_Tessa_Cards_Numbers_NumberEventTypes_PreparingTemplate.htm)|
Карточка шаблона подготавливается к созданию. При этом может потребоваться
очистить поля номеров, заданных в шаблоне.. Обычно выполняется на сервере на
этапе AfterRequest после создания карточки методом [NewAsync(CardNewRequest,
CancellationToken)](M_Tessa_Cards_ICardRepository_NewAsync.htm), но перед
событием
[CreatingCard](F_Tessa_Cards_Numbers_NumberEventTypes_CreatingCard.htm).  
[ProcessingQueueWhileClosingOrRefreshingCard](F_Tessa_Cards_Numbers_NumberEventTypes_ProcessingQueueWhileClosingOrRefreshingCard.htm)|
Выполняется обработка действий с номерами в очереди при закрытии вкладки
карточки, а также при обновлении карточки, в т.ч. после успешного сохранения.
Обычно выполняется на клиенте.  
[ProcessingQueueWhileStoringCard](F_Tessa_Cards_Numbers_NumberEventTypes_ProcessingQueueWhileStoringCard.htm)|
Выполняется обработка действий с номерами в очереди при сохранении карточки.
Обычно выполняется на сервере.  
[RegisteringCard](F_Tessa_Cards_Numbers_NumberEventTypes_RegisteringCard.htm)|
Выполняется регистрация карточки. При этом может потребоваться выделить
регистрационный номер. Обычно выполняется на сервере на этапе BeforeRequest
перед сохранением карточки методом [StoreAsync(CardStoreRequest,
CancellationToken)](M_Tessa_Cards_ICardRepository_StoreAsync.htm).  
[ReleasingNumberFromControl](F_Tessa_Cards_Numbers_NumberEventTypes_ReleasingNumberFromControl.htm)|
Освобождение номера из элемента управления. Выполняется и на клиенте, и на
сервере, причём клиентская реализация обычно вызывает серверную.  
[ReservingNumberFromControl](F_Tessa_Cards_Numbers_NumberEventTypes_ReservingNumberFromControl.htm)|
Резервирование номера из элемента управления. Выполняется и на клиенте, и на
сервере, причём клиентская реализация обычно вызывает серверную.  
[SavingNewCard](F_Tessa_Cards_Numbers_NumberEventTypes_SavingNewCard.htm)|
Карточка впервые сохраняется. При этом может потребоваться выделить номер.
Обычно выполняется на сервере на этапе BeforeRequest перед сохранением
карточки методом [StoreAsync(CardStoreRequest,
CancellationToken)](M_Tessa_Cards_ICardRepository_StoreAsync.htm).  
[Unknown](F_Tessa_Cards_Numbers_NumberEventTypes_Unknown.htm)|  Неизвестное
событие, происходящее с номером. Обычно в этом случае событие ещё не было
установлено. Тип не является зарегистрированным в стандартном API, поэтому
вызов
[IsKnown(NumberEventType)](M_Tessa_Cards_Numbers_NumberEventTypes_IsKnown.htm)
вернёт false.  
## __См. также
#### Ссылки
[Tessa.Cards.Numbers - пространство имён](N_Tessa_Cards_Numbers.htm)
