# CardTypeColumn.AggregationFormat - свойство
Формат агрегации дочерних строк. Если значение равно null, то строки выводятся
как есть. Если количество дочерних строк равно нулю, то результирующая строка
должна быть равна null. В противном случае соединённые сепараторами
[Separator](P_Tessa_Cards_CardTypeColumn_Separator.htm) дочерние строки
приходят в качестве параметра {0}, а количество строк - в параметре {1}. Таким
образом, например, можно поставить точку в конце списка строк, разделённые
запятыми.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public string AggregationFormat { get; set; }
VB __Копировать
     Public Property AggregationFormat As String
    	Get
    	Set
C++ __Копировать
     public:
    property String^ AggregationFormat {
    	String^ get ();
    	void set (String^ value);
    }
F# __Копировать
     member AggregationFormat : string with get, set
#### Значение свойства
[String](https://learn.microsoft.com/dotnet/api/system.string)
##  __См. также
#### Ссылки
[CardTypeColumn - ](T_Tessa_Cards_CardTypeColumn.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
