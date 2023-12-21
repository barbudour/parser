# CardTask.TryGetOrCreateCardForStore - метод
Возвращает карточку для сохранения задания или null, если карточка ещё не была
задана. В отличие от метода
[TryGetCard()](M_Tessa_Cards_CardTask_TryGetCard.htm), этот метод может
создать копию основной карточки и удалить из неё все поля, кроме изменяемых,
если выполняется завершение задания без удаления, т.е. свойство
[State](P_Tessa_Cards_CardTask_State.htm) равно
[Modified](T_Tessa_Cards_CardRowState.htm), а свойство
[Action](P_Tessa_Cards_CardTask_Action.htm) равно
[Complete](T_Tessa_Cards_CardTaskAction.htm).
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public Card TryGetOrCreateCardForStore(
    	CardStoreMethod storeMethod = CardStoreMethod.Default
    )
VB __Копировать
     Public Function TryGetOrCreateCardForStore ( 
    	Optional storeMethod As CardStoreMethod = CardStoreMethod.Default
    ) As Card
C++ __Копировать
     public:
    Card^ TryGetOrCreateCardForStore(
    	CardStoreMethod storeMethod = CardStoreMethod::Default
    )
F# __Копировать
     member TryGetOrCreateCardForStore : 
            ?storeMethod : CardStoreMethod 
    (* Defaults:
            let _storeMethod = defaultArg storeMethod CardStoreMethod.Default
    *)
    -> Card 
#### Параметры
storeMethod [CardStoreMethod](T_Tessa_Cards_CardStoreMethod.htm) (Optional)
#### Возвращаемое значение
[Card](T_Tessa_Cards_Card.htm)  
Карточка для сохранения задания или null, если карточка ещё не была задана.
## __См. также
#### Ссылки
[CardTask - ](T_Tessa_Cards_CardTask.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
