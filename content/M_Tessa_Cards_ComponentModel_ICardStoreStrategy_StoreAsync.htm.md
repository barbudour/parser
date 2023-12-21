# ICardStoreStrategy.StoreAsync - метод
Сохраняет карточку, данные её секций, файлы и задания.
##  __Definition
 **Пространство имён:**
[Tessa.Cards.ComponentModel](N_Tessa_Cards_ComponentModel.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     Task StoreAsync(
    	CardStoreContext context
    )
VB __Копировать
     Function StoreAsync ( 
    	context As CardStoreContext
    ) As Task
C++ __Копировать
    Task^ StoreAsync(
    	CardStoreContext^ context
    )
F# __Копировать
     abstract StoreAsync : 
            context : CardStoreContext -> Task 
#### Параметры
context [CardStoreContext](T_Tessa_Cards_ComponentModel_CardStoreContext.htm)
    Контекст операции по сохранению карточки.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)  
Асинхронная задача.
##  __См. также
#### Ссылки
[ICardStoreStrategy - ](T_Tessa_Cards_ComponentModel_ICardStoreStrategy.htm)
[Tessa.Cards.ComponentModel - пространство
имён](N_Tessa_Cards_ComponentModel.htm)
