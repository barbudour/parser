# CardEntryData.Item - свойство
Получает или задаёт значение поля с именем fieldName, расположенного внутри
строковой секции с именем sectionName.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public Object this[
    	string sectionName,
    	string fieldName
    ] { get; set; }
VB __Копировать
     Public Default Property Item ( 
    	sectionName As String,
    	fieldName As String
    ) As Object
    	Get
    	Set
C++ __Копировать
     public:
    property Object^ default[String^ sectionName, String^ fieldName] {
    	Object^ get (String^ sectionName, String^ fieldName);
    	void set (String^ sectionName, String^ fieldName, Object^ value);
    }
F# __Копировать
     member Item : Object with get, set
#### Параметры
sectionName [String](https://learn.microsoft.com/dotnet/api/system.string)
     Имя строковой секции, в которой следует искать поле с именем fieldName. 
fieldName [String](https://learn.microsoft.com/dotnet/api/system.string)
     Имя поля, расположенного в строковой секции с именем sectionName. 
#### Возвращаемое значение
[Object](https://learn.microsoft.com/dotnet/api/system.object)  
Значение поля с именем fieldName, расположенного в строковой секции с именем
sectionName.
## __См. также
#### Ссылки
[CardEntryData - ](T_Tessa_Cards_CardEntryData.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
