# CardTableData.Item(String, Int32, String) - свойство
Получает или задаёт значение поля с именем fieldName, расположенного внутри
строки с индексом index, которая принадлежит коллекционной или древовидной
секции с именем sectionName.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public Object this[
    	string sectionName,
    	int index,
    	string fieldName
    ] { get; set; }
VB __Копировать
     Public Default Property Item ( 
    	sectionName As String,
    	index As Integer,
    	fieldName As String
    ) As Object
    	Get
    	Set
C++ __Копировать
     public:
    property Object^ default[String^ sectionName, int index, String^ fieldName] {
    	Object^ get (String^ sectionName, int index, String^ fieldName);
    	void set (String^ sectionName, int index, String^ fieldName, Object^ value);
    }
F# __Копировать
     member Item : Object with get, set
#### Параметры
sectionName [String](https://learn.microsoft.com/dotnet/api/system.string)
     Имя коллекционной или древовидной секции, в которой следует искать строку с индексом index. 
index [Int32](https://learn.microsoft.com/dotnet/api/system.int32)
     Отсчитываемый от нуля индекс строки, в которой следует искать поле с именем fieldName. 
fieldName [String](https://learn.microsoft.com/dotnet/api/system.string)
     Имя поля, расположенного в строке с индексом index, которая принадлежит секции с именем sectionName. 
#### Возвращаемое значение
[Object](https://learn.microsoft.com/dotnet/api/system.object)  
Значение поля с именем fieldName, расположенного в строке с индексом index,
которая принадлежит коллекционной или древовидной секции с именем sectionName.
## __См. также
#### Ссылки
[CardTableData - ](T_Tessa_Cards_CardTableData.htm)
[Item - перегрузка](Overload_Tessa_Cards_CardTableData_Item.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
