# CardTableData.Get<T> \- метод
Возвращает строго типизированное значение поля с именем fieldName,
расположенного внутри строки с индексом index, которая принадлежит
коллекционной или древовидной секции с именем sectionName.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public T Get<T>(
    	string sectionName,
    	int index,
    	string fieldName
    )
VB __Копировать
     Public Function Get(Of T) ( 
    	sectionName As String,
    	index As Integer,
    	fieldName As String
    ) As T
C++ __Копировать
     public:
    generic<typename T>
    T Get(
    	String^ sectionName, 
    	int index, 
    	String^ fieldName
    )
F# __Копировать
     member Get : 
            sectionName : string * 
            index : int * 
            fieldName : string -> 'T 
#### Параметры
sectionName [String](https://learn.microsoft.com/dotnet/api/system.string)
     Имя коллекционной или древовидной секции, в которой следует искать строку с индексом index. 
index [Int32](https://learn.microsoft.com/dotnet/api/system.int32)
     Отсчитываемый от нуля индекс строки, в которой следует искать поле с именем fieldName. 
fieldName [String](https://learn.microsoft.com/dotnet/api/system.string)
     Имя поля, расположенного в строке с индексом index, которая принадлежит секции с именем sectionName. 
#### Параметры типа
T
    Тип значения возвращаемого поля.
#### Возвращаемое значение
T  
Строго типизированное значение поля с именем fieldName, расположенного в
строке с индексом index, которая принадлежит коллекционной или древовидной
секции с именем sectionName.
## __См. также
#### Ссылки
[CardTableData - ](T_Tessa_Cards_CardTableData.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
