# CardStoreExecutionStrategy.StoreSectionsAsync - метод
Выполняет сохранение секций карточки.
##  __Definition
 **Пространство имён:**
[Tessa.Cards.ComponentModel](N_Tessa_Cards_ComponentModel.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public Task StoreSectionsAsync(
    	CardStoreContext context
    )
VB __Копировать
     Public Function StoreSectionsAsync ( 
    	context As CardStoreContext
    ) As Task
C++ __Копировать
     public:
    virtual Task^ StoreSectionsAsync(
    	CardStoreContext^ context
    ) sealed
F# __Копировать
     abstract StoreSectionsAsync : 
            context : CardStoreContext -> Task 
    override StoreSectionsAsync : 
            context : CardStoreContext -> Task 
#### Параметры
context [CardStoreContext](T_Tessa_Cards_ComponentModel_CardStoreContext.htm)
    Контекст операции по сохранению карточки.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)  
Асинхронная задача.
#### Реализации
[ICardStoreExecutionStrategy.StoreSectionsAsync(CardStoreContext)](M_Tessa_Cards_ComponentModel_ICardStoreExecutionStrategy_StoreSectionsAsync.htm)  
##  __См. также
#### Ссылки
[CardStoreExecutionStrategy -
](T_Tessa_Cards_ComponentModel_CardStoreExecutionStrategy.htm)
[Tessa.Cards.ComponentModel - пространство
имён](N_Tessa_Cards_ComponentModel.htm)
