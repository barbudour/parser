# ICardStoreExecutionStrategy.InsertInstanceAsync - метод
Вставляет запись в таблицу экземпляров карточек Instances. В момент создания
открывается блокировка на запись, которая должна быть закрыта по завершению.
## __Definition
 **Пространство имён:**
[Tessa.Cards.ComponentModel](N_Tessa_Cards_ComponentModel.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     Task InsertInstanceAsync(
    	CardStoreContext context
    )
VB __Копировать
     Function InsertInstanceAsync ( 
    	context As CardStoreContext
    ) As Task
C++ __Копировать
    Task^ InsertInstanceAsync(
    	CardStoreContext^ context
    )
F# __Копировать
     abstract InsertInstanceAsync : 
            context : CardStoreContext -> Task 
#### Параметры
context [CardStoreContext](T_Tessa_Cards_ComponentModel_CardStoreContext.htm)
    Контекст операции по сохранению карточки.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)  
Асинхронная задача.
##  __См. также
#### Ссылки
[ICardStoreExecutionStrategy -
](T_Tessa_Cards_ComponentModel_ICardStoreExecutionStrategy.htm)
[Tessa.Cards.ComponentModel - пространство
имён](N_Tessa_Cards_ComponentModel.htm)
