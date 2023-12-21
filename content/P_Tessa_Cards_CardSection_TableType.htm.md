# CardSection.TableType - свойство
Тип коллекционной или древовидной секции. Для строковой секции всегда
возвращается значение Unspecified.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public CardTableType TableType { get; set; }
VB __Копировать
     Public Property TableType As CardTableType
    	Get
    	Set
C++ __Копировать
     public:
    property CardTableType TableType {
    	CardTableType get ();
    	void set (CardTableType value);
    }
F# __Копировать
     member TableType : CardTableType with get, set
#### Значение свойства
[CardTableType](T_Tessa_Cards_CardTableType.htm)
##  __Заметки
Значение по умолчанию Unspecified возвращается даже в том случае, если объект
с соответствующим ключом отсутствует в хранилище.
## __См. также
#### Ссылки
[CardSection - ](T_Tessa_Cards_CardSection.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
