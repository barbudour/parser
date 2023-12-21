# CardStoreStrategy.StoreAsync - метод
Сохраняет карточку, данные её секций, файлы и задания.
##  __Definition
 **Пространство имён:**
[Tessa.Cards.ComponentModel](N_Tessa_Cards_ComponentModel.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public Task StoreAsync(
    	CardStoreContext context
    )
VB __Копировать
     Public Function StoreAsync ( 
    	context As CardStoreContext
    ) As Task
C++ __Копировать
     public:
    virtual Task^ StoreAsync(
    	CardStoreContext^ context
    ) sealed
F# __Копировать
     abstract StoreAsync : 
            context : CardStoreContext -> Task 
    override StoreAsync : 
            context : CardStoreContext -> Task 
#### Параметры
context [CardStoreContext](T_Tessa_Cards_ComponentModel_CardStoreContext.htm)
    Контекст операции по сохранению карточки.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)  
Асинхронная задача.
#### Реализации
[ICardStoreStrategy.StoreAsync(CardStoreContext)](M_Tessa_Cards_ComponentModel_ICardStoreStrategy_StoreAsync.htm)  
##  __См. также
#### Ссылки
[CardStoreStrategy - ](T_Tessa_Cards_ComponentModel_CardStoreStrategy.htm)
[Tessa.Cards.ComponentModel - пространство
имён](N_Tessa_Cards_ComponentModel.htm)
