# ICardDeleteStrategy.DeleteAsync(CardDeleteContext) - метод
Удаляет карточку по данным, указанным в контексте операции.
##  __Definition
 **Пространство имён:**
[Tessa.Cards.ComponentModel](N_Tessa_Cards_ComponentModel.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     Task DeleteAsync(
    	CardDeleteContext context
    )
VB __Копировать
     Function DeleteAsync ( 
    	context As CardDeleteContext
    ) As Task
C++ __Копировать
    Task^ DeleteAsync(
    	CardDeleteContext^ context
    )
F# __Копировать
     abstract DeleteAsync : 
            context : CardDeleteContext -> Task 
#### Параметры
context
[CardDeleteContext](T_Tessa_Cards_ComponentModel_CardDeleteContext.htm)
    Контекст операции по удалению карточки.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)
##  __См. также
#### Ссылки
[ICardDeleteStrategy - ](T_Tessa_Cards_ComponentModel_ICardDeleteStrategy.htm)
[DeleteAsync -
перегрузка](Overload_Tessa_Cards_ComponentModel_ICardDeleteStrategy_DeleteAsync.htm)
[Tessa.Cards.ComponentModel - пространство
имён](N_Tessa_Cards_ComponentModel.htm)
