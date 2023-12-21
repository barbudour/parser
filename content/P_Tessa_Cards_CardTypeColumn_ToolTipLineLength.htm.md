# CardTypeColumn.ToolTipLineLength - свойство
Предпочитаемая ширина всплывающей подсказки в символах. Если ширина превышает
это значение, то подсказка разбивается на несколько строк, где строки
переносятся по словам, которые разделены символами категории whitespace в
Unicode. По умолчанию значение равно
[DefaultToolTipLineLength](F_Tessa_Cards_CardTypeColumn_DefaultToolTipLineLength.htm).
Если значение равно 0, то используется
[DefaultToolTipLineLength](F_Tessa_Cards_CardTypeColumn_DefaultToolTipLineLength.htm).
Не должно быть отрицательным числом.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public int ToolTipLineLength { get; set; }
VB __Копировать
     Public Property ToolTipLineLength As Integer
    	Get
    	Set
C++ __Копировать
     public:
    property int ToolTipLineLength {
    	int get ();
    	void set (int value);
    }
F# __Копировать
     member ToolTipLineLength : int with get, set
#### Значение свойства
[Int32](https://learn.microsoft.com/dotnet/api/system.int32)
##  __См. также
#### Ссылки
[CardTypeColumn - ](T_Tessa_Cards_CardTypeColumn.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
