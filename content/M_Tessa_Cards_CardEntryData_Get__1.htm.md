# CardEntryData.Get<T> \- метод
Возвращает строго типизированное значение поля с именем fieldName,
расположенного внутри строковой секции с именем sectionName.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public T Get<T>(
    	string sectionName,
    	string fieldName
    )
VB __Копировать
     Public Function Get(Of T) ( 
    	sectionName As String,
    	fieldName As String
    ) As T
C++ __Копировать
     public:
    generic<typename T>
    T Get(
    	String^ sectionName, 
    	String^ fieldName
    )
F# __Копировать
     member Get : 
            sectionName : string * 
            fieldName : string -> 'T 
#### Параметры
sectionName [String](https://learn.microsoft.com/dotnet/api/system.string)
     Имя строковой секции, в которой следует искать поле с именем fieldName. 
fieldName [String](https://learn.microsoft.com/dotnet/api/system.string)
     Имя поля, расположенного в строковой секции с именем sectionName. 
#### Параметры типа
T
    Тип значения возвращаемого поля.
#### Возвращаемое значение
T  
Строго типизированное значение поля с именем fieldName, расположенного внутри
строковой секции с именем sectionName.
## __См. также
#### Ссылки
[CardEntryData - ](T_Tessa_Cards_CardEntryData.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
