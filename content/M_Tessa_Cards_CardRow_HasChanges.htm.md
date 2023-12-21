# CardRow.HasChanges - метод
Возвращает признак того, что объект содержит изменённые поля.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public bool HasChanges(
    	CardTableType tableType
    )
VB __Копировать
     Public Function HasChanges ( 
    	tableType As CardTableType
    ) As Boolean
C++ __Копировать
     public:
    bool HasChanges(
    	CardTableType tableType
    )
F# __Копировать
     member HasChanges : 
            tableType : CardTableType -> bool 
#### Параметры
tableType [CardTableType](T_Tessa_Cards_CardTableType.htm)
    Тип секции, в которую включена строка.
#### Возвращаемое значение
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)  
true, если объект содержит изменённые поля; false в противном случае.
## __Заметки
Метод вернёт false в случае, если среди изменённых полей присутствуют только
служебные поля.
Метод не учитывает состояние строки [State](P_Tessa_Cards_CardRow_State.htm).
##  __См. также
#### Ссылки
[CardRow - ](T_Tessa_Cards_CardRow.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
