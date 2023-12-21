# ICardStoreExecutionStrategy.CheckSectionsOnInsertAsync - метод
Проверяет наличие в карточке всех строковых секций из типа карточки при её
создании. В случае отсутствия некоторых секций метод возвращает false и
добавляет сообщение в результат валидации.
## __Definition
 **Пространство имён:**
[Tessa.Cards.ComponentModel](N_Tessa_Cards_ComponentModel.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     ValueTask<bool> CheckSectionsOnInsertAsync(
    	CardStoreContext context
    )
VB __Копировать
     Function CheckSectionsOnInsertAsync ( 
    	context As CardStoreContext
    ) As ValueTask(Of Boolean)
C++ __Копировать
     ValueTask<bool> CheckSectionsOnInsertAsync(
    	CardStoreContext^ context
    )
F# __Копировать
     abstract CheckSectionsOnInsertAsync : 
            context : CardStoreContext -> ValueTask<bool> 
#### Параметры
context [CardStoreContext](T_Tessa_Cards_ComponentModel_CardStoreContext.htm)
    Контекст операции по сохранению карточки.
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)>  
true, если создаваемая карточки содержит все необходимые строковые секции;
false в противном случае.
## __См. также
#### Ссылки
[ICardStoreExecutionStrategy -
](T_Tessa_Cards_ComponentModel_ICardStoreExecutionStrategy.htm)
[Tessa.Cards.ComponentModel - пространство
имён](N_Tessa_Cards_ComponentModel.htm)
