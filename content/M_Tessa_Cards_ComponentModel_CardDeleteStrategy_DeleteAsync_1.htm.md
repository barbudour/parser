# CardDeleteStrategy.DeleteAsync(CardDeleteContext) - метод
Удаляет карточку по данным, указанным в контексте операции.
##  __Definition
 **Пространство имён:**
[Tessa.Cards.ComponentModel](N_Tessa_Cards_ComponentModel.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public Task DeleteAsync(
    	CardDeleteContext context
    )
VB __Копировать
     Public Function DeleteAsync ( 
    	context As CardDeleteContext
    ) As Task
C++ __Копировать
     public:
    virtual Task^ DeleteAsync(
    	CardDeleteContext^ context
    ) sealed
F# __Копировать
     abstract DeleteAsync : 
            context : CardDeleteContext -> Task 
    override DeleteAsync : 
            context : CardDeleteContext -> Task 
#### Параметры
context
[CardDeleteContext](T_Tessa_Cards_ComponentModel_CardDeleteContext.htm)
    Контекст операции по удалению карточки.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)
#### Реализации
[ICardDeleteStrategy.DeleteAsync(CardDeleteContext)](M_Tessa_Cards_ComponentModel_ICardDeleteStrategy_DeleteAsync_1.htm)  
##  __См. также
#### Ссылки
[CardDeleteStrategy - ](T_Tessa_Cards_ComponentModel_CardDeleteStrategy.htm)
[DeleteAsync -
перегрузка](Overload_Tessa_Cards_ComponentModel_CardDeleteStrategy_DeleteAsync.htm)
[Tessa.Cards.ComponentModel - пространство
имён](N_Tessa_Cards_ComponentModel.htm)
