# CardStoreExecutionStrategy.CheckSectionsOnInsertAsync - метод
Проверяет наличие в карточке всех строковых секций из типа карточки при её
создании. В случае отсутствия некоторых секций метод возвращает false и
добавляет сообщение в результат валидации.
## __Definition
 **Пространство имён:**
[Tessa.Cards.ComponentModel](N_Tessa_Cards_ComponentModel.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public ValueTask<bool> CheckSectionsOnInsertAsync(
    	CardStoreContext context
    )
VB __Копировать
     Public Function CheckSectionsOnInsertAsync ( 
    	context As CardStoreContext
    ) As ValueTask(Of Boolean)
C++ __Копировать
     public:
    virtual ValueTask<bool> CheckSectionsOnInsertAsync(
    	CardStoreContext^ context
    ) sealed
F# __Копировать
     abstract CheckSectionsOnInsertAsync : 
            context : CardStoreContext -> ValueTask<bool> 
    override CheckSectionsOnInsertAsync : 
            context : CardStoreContext -> ValueTask<bool> 
#### Параметры
context [CardStoreContext](T_Tessa_Cards_ComponentModel_CardStoreContext.htm)
    Контекст операции по сохранению карточки.
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)>  
true, если создаваемая карточки содержит все необходимые строковые секции;
false в противном случае.
#### Реализации
[ICardStoreExecutionStrategy.CheckSectionsOnInsertAsync(CardStoreContext)](M_Tessa_Cards_ComponentModel_ICardStoreExecutionStrategy_CheckSectionsOnInsertAsync.htm)  
##  __См. также
#### Ссылки
[CardStoreExecutionStrategy -
](T_Tessa_Cards_ComponentModel_CardStoreExecutionStrategy.htm)
[Tessa.Cards.ComponentModel - пространство
имён](N_Tessa_Cards_ComponentModel.htm)
