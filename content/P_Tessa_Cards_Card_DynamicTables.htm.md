# Card.DynamicTables - свойство
Объект, позволяющий обратиться напрямую от строковой секции карточки к
значению поля через позднее связывание и автоматически устанавливающий
системную информацию об изменённых полях.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public Object DynamicTables { get; }
VB __Копировать
     Public ReadOnly Property DynamicTables As Object
    	Get
C++ __Копировать
     public:
    property Object^ DynamicTables {
    	Object^ get ();
    }
F# __Копировать
     member DynamicTables : Object with get
#### Значение свойства
[Object](https://learn.microsoft.com/dotnet/api/system.object)
##  __Заметки
Обращение к DynamicTables немного быстрее, чем к Dynamic.Tables за счёт
кэширования выражений средой DLR.
Также использование DynamicTables позволяет не устанавливать информацию об
изменённых полях и строках вручную, т.к. любое поле, значение которого
изменяется, заносится в список изменённых, а строка, в котором расположено
поле, переходит в состояние [Modified](T_Tessa_Cards_CardRowState.htm), если
она была в состоянии [None](T_Tessa_Cards_CardRowState.htm).
##  __См. также
#### Ссылки
[Card - ](T_Tessa_Cards_Card.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
