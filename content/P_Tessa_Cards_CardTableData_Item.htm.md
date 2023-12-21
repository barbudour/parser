# CardTableData.Item(String, Int32) - свойство
Получает коллекцию пар ключ / значение, которая соответствует свойствам строки
с индексом index, расположенной в пределах секции с именем sectionName. При
изменении такой коллекции автоматически изменяется информация об изменённых
полях и строках.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public IDictionary<string, Object> this[
    	string sectionName,
    	int index
    ] { get; }
VB __Копировать
     Public ReadOnly Default Property Item ( 
    	sectionName As String,
    	index As Integer
    ) As IDictionary(Of String, Object)
    	Get
C++ __Копировать
     public:
    property IDictionary<String^, Object^>^ default[String^ sectionName, int index] {
    	IDictionary<String^, Object^>^ get (String^ sectionName, int index);
    }
F# __Копировать
     member Item : IDictionary<string, Object> with get
#### Параметры
sectionName [String](https://learn.microsoft.com/dotnet/api/system.string)
     Имя коллекционной или древовидной секции, в которой следует искать строку с индексом index. 
index [Int32](https://learn.microsoft.com/dotnet/api/system.int32)
     Отсчитываемый от нуля индекс строки, коллекцию пар ключ / значение которой требуется вернуть. 
#### Возвращаемое значение
[IDictionary](https://learn.microsoft.com/dotnet/api/system.collections.generic.idictionary-2)<[String](https://learn.microsoft.com/dotnet/api/system.string),
[Object](https://learn.microsoft.com/dotnet/api/system.object)>  
Коллекция пар ключ / значение, которая соответствует свойствам строки с
индексом index, расположенной в пределах секции с именем sectionName.
## __См. также
#### Ссылки
[CardTableData - ](T_Tessa_Cards_CardTableData.htm)
[Item - перегрузка](Overload_Tessa_Cards_CardTableData_Item.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
