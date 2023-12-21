# Card.Tables - свойство
Объект, позволяющий обратиться напрямую от коллекционной или древовидной
секции карточки к значению поля строки с заданным номером и автоматически
устанавливающий системную информацию об изменённых полях и строках.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public CardTableData Tables { get; }
VB __Копировать
     Public ReadOnly Property Tables As CardTableData
    	Get
C++ __Копировать
     public:
    property CardTableData^ Tables {
    	CardTableData^ get ();
    }
F# __Копировать
     member Tables : CardTableData with get
#### Значение свойства
[CardTableData](T_Tessa_Cards_CardTableData.htm)
##  __Заметки
Использование Tables позволяет не устанавливать информацию об изменённых полях
и строках вручную, т.к. любое поле, значение которого изменяется, заносится в
список изменённых, а строка, в котором расположено поле, переходит в состояние
[Modified](T_Tessa_Cards_CardRowState.htm), если она была в состоянии
[None](T_Tessa_Cards_CardRowState.htm).
## __См. также
#### Ссылки
[Card - ](T_Tessa_Cards_Card.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
