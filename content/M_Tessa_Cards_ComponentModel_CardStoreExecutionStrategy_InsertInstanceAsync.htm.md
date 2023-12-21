# CardStoreExecutionStrategy.InsertInstanceAsync - метод
Вставляет запись в таблицу экземпляров карточек Instances. В момент создания
открывается блокировка на запись, которая должна быть закрыта по завершению.
## __Definition
 **Пространство имён:**
[Tessa.Cards.ComponentModel](N_Tessa_Cards_ComponentModel.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public Task InsertInstanceAsync(
    	CardStoreContext context
    )
VB __Копировать
     Public Function InsertInstanceAsync ( 
    	context As CardStoreContext
    ) As Task
C++ __Копировать
     public:
    virtual Task^ InsertInstanceAsync(
    	CardStoreContext^ context
    ) sealed
F# __Копировать
     abstract InsertInstanceAsync : 
            context : CardStoreContext -> Task 
    override InsertInstanceAsync : 
            context : CardStoreContext -> Task 
#### Параметры
context [CardStoreContext](T_Tessa_Cards_ComponentModel_CardStoreContext.htm)
    Контекст операции по сохранению карточки.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)  
Асинхронная задача.
#### Реализации
[ICardStoreExecutionStrategy.InsertInstanceAsync(CardStoreContext)](M_Tessa_Cards_ComponentModel_ICardStoreExecutionStrategy_InsertInstanceAsync.htm)  
##  __См. также
#### Ссылки
[CardStoreExecutionStrategy -
](T_Tessa_Cards_ComponentModel_CardStoreExecutionStrategy.htm)
[Tessa.Cards.ComponentModel - пространство
имён](N_Tessa_Cards_ComponentModel.htm)
