# ICardStoreExecutionStrategy.InsertTaskHistoryAsync(CardStoreContext,
CardTask) - метод
Вставляет запись о завершённом задании в таблицу с историей заданий
TaskHistory.
## __Definition
 **Пространство имён:**
[Tessa.Cards.ComponentModel](N_Tessa_Cards_ComponentModel.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     Task InsertTaskHistoryAsync(
    	CardStoreContext context,
    	CardTask task
    )
VB __Копировать
     Function InsertTaskHistoryAsync ( 
    	context As CardStoreContext,
    	task As CardTask
    ) As Task
C++ __Копировать
    Task^ InsertTaskHistoryAsync(
    	CardStoreContext^ context, 
    	CardTask^ task
    )
F# __Копировать
     abstract InsertTaskHistoryAsync : 
            context : CardStoreContext * 
            task : CardTask -> Task 
#### Параметры
context [CardStoreContext](T_Tessa_Cards_ComponentModel_CardStoreContext.htm)
    Контекст операции по сохранению карточки, для которой назначено задание.
task [CardTask](T_Tessa_Cards_CardTask.htm)
    Задание, для которого создаётся запись о завершённом задании.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)  
Асинхронная задача.
##  __См. также
#### Ссылки
[ICardStoreExecutionStrategy -
](T_Tessa_Cards_ComponentModel_ICardStoreExecutionStrategy.htm)
[InsertTaskHistoryAsync -
перегрузка](Overload_Tessa_Cards_ComponentModel_ICardStoreExecutionStrategy_InsertTaskHistoryAsync.htm)
[Tessa.Cards.ComponentModel - пространство
имён](N_Tessa_Cards_ComponentModel.htm)
