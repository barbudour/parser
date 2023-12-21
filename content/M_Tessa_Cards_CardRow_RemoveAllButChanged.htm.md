# CardRow.RemoveAllButChanged - метод
Удаляет информацию о всех полях строки, которые не были изменены посредством
[IStorageObjectStateProvider](T_Tessa_Platform_Storage_IStorageObjectStateProvider.htm)
и не являются служебными.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public void RemoveAllButChanged(
    	CardTableType tableType
    )
VB __Копировать
     Public Sub RemoveAllButChanged ( 
    	tableType As CardTableType
    )
C++ __Копировать
     public:
    void RemoveAllButChanged(
    	CardTableType tableType
    )
F# __Копировать
     member RemoveAllButChanged : 
            tableType : CardTableType -> unit 
#### Параметры
tableType [CardTableType](T_Tessa_Cards_CardTableType.htm)
    Тип коллекционной или древовидной секции карточки, в которую включена строка.
##  __Заметки
Метод удаляет информацию об изменённых полях, поэтому повторный его вызов
приведёт к удалению всех полей. Метод не удаляет поля
[RowID](P_Tessa_Cards_CardRow_RowID.htm) и
[State](P_Tessa_Cards_CardRow_State.htm) для любой секции, а также
[ParentRowID](P_Tessa_Cards_CardRow_ParentRowID.htm) для древовидной секции.
Метод удаляет всю информацию, кроме служебной, о строках, у которых
[State](P_Tessa_Cards_CardRow_State.htm) равен
[Deleted](T_Tessa_Cards_CardRowState.htm), и не удаляет информацию у строк
[Inserted](T_Tessa_Cards_CardRowState.htm).
Рекомендуется вызывать этот метод перед вызовом
[Clean()](M_Tessa_Cards_CardRow_Clean.htm).
##  __См. также
#### Ссылки
[CardRow - ](T_Tessa_Cards_CardRow.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
