# CardRow.SortingOrder - свойство
Порядок строки при сортировке строк для вставки, задаваемый вручную при
указании типа сортировки [Manual](T_Tessa_Cards_CardRowSortingType.htm) для
секции. Порядок строк при удалении будет обратным.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public int SortingOrder { get; set; }
VB __Копировать
     Public Property SortingOrder As Integer
    	Get
    	Set
C++ __Копировать
     public:
    property int SortingOrder {
    	int get ();
    	void set (int value);
    }
F# __Копировать
     member SortingOrder : int with get, set
#### Значение свойства
[Int32](https://learn.microsoft.com/dotnet/api/system.int32)
##  __Заметки
Значение по умолчанию 0 возвращается даже в том случае, если объект с
соответствующим ключом отсутствует в хранилище.
## __См. также
#### Ссылки
[CardRow - ](T_Tessa_Cards_CardRow.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
