# Card.RemoveAllButChanged - метод
Удаляет информацию о всех полях или строках всех секций карточки, которые не
были изменены посредством
[IStorageObjectStateProvider](T_Tessa_Platform_Storage_IStorageObjectStateProvider.htm).
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public void RemoveAllButChanged(
    	CardStoreMode storeMode = CardStoreMode.Update,
    	CardStoreMethod storeMethod = CardStoreMethod.Default
    )
VB __Копировать
     Public Sub RemoveAllButChanged ( 
    	Optional storeMode As CardStoreMode = CardStoreMode.Update,
    	Optional storeMethod As CardStoreMethod = CardStoreMethod.Default
    )
C++ __Копировать
     public:
    void RemoveAllButChanged(
    	CardStoreMode storeMode = CardStoreMode::Update, 
    	CardStoreMethod storeMethod = CardStoreMethod::Default
    )
F# __Копировать
     member RemoveAllButChanged : 
            ?storeMode : CardStoreMode * 
            ?storeMethod : CardStoreMethod 
    (* Defaults:
            let _storeMode = defaultArg storeMode CardStoreMode.Update
            let _storeMethod = defaultArg storeMethod CardStoreMethod.Default
    *)
    -> unit 
#### Параметры
storeMode [CardStoreMode](T_Tessa_Cards_CardStoreMode.htm) (Optional)
    Способ сохранения карточки, для которого выполняется удаление информации.
storeMethod [CardStoreMethod](T_Tessa_Cards_CardStoreMethod.htm) (Optional)
    Способ сохранения карточки, для которого выполняется удаление информации.
##  __Заметки
Метод удаляет информацию об изменённых полях, поэтому повторный его вызов
приведёт к удалению всех полей.
Для коллекционных и древовидных секций метод удаляет строки, у которых
[State](P_Tessa_Cards_CardRow_State.htm) равен
[None](T_Tessa_Cards_CardRowState.htm). Если у секций не остаётся строк, то
они удаляются. Метод удаляет всю информацию, кроме служебной, о строках, у
которых [State](P_Tessa_Cards_CardRow_State.htm) равен
[Deleted](T_Tessa_Cards_CardRowState.htm), и не удаляет информацию у строк
[Inserted](T_Tessa_Cards_CardRowState.htm).
Рекомендуется вызывать этот метод перед вызовом
[Clean()](M_Tessa_Cards_Card_Clean.htm).
##  __См. также
#### Ссылки
[Card - ](T_Tessa_Cards_Card.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
