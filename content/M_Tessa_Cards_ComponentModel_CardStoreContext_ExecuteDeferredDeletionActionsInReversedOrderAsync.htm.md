# CardStoreContext.ExecuteDeferredDeletionActionsInReversedOrderAsync - метод
Осуществляет отложенное выполнение всех действий по удалению элементов
карточки в порядке, обратном их указанию.
## __Definition
 **Пространство имён:**
[Tessa.Cards.ComponentModel](N_Tessa_Cards_ComponentModel.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public Task ExecuteDeferredDeletionActionsInReversedOrderAsync()
VB __Копировать
     Public Function ExecuteDeferredDeletionActionsInReversedOrderAsync As Task
C++ __Копировать
     public:
    Task^ ExecuteDeferredDeletionActionsInReversedOrderAsync()
F# __Копировать
     member ExecuteDeferredDeletionActionsInReversedOrderAsync : unit -> Task 
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)  
Асинхронная задача.
##  __Заметки
Указание отложенных действий выполняется посредством метода
[DeferDeletionAction(Func<CardStoreContext,
Task>)](M_Tessa_Cards_ComponentModel_CardStoreContext_DeferDeletionAction.htm).
## __См. также
#### Ссылки
[CardStoreContext - ](T_Tessa_Cards_ComponentModel_CardStoreContext.htm)
[Tessa.Cards.ComponentModel - пространство
имён](N_Tessa_Cards_ComponentModel.htm)
