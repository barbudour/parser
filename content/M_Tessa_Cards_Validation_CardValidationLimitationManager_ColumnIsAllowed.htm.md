# CardValidationLimitationManager.ColumnIsAllowed - метод
Возвращает признак того, что колонка из указанной секции является доступной.
##  __Definition
 **Пространство имён:** [Tessa.Cards.Validation](N_Tessa_Cards_Validation.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public bool ColumnIsAllowed(
    	string sectionName,
    	string columnName
    )
VB __Копировать
     Public Function ColumnIsAllowed ( 
    	sectionName As String,
    	columnName As String
    ) As Boolean
C++ __Копировать
     public:
    virtual bool ColumnIsAllowed(
    	String^ sectionName, 
    	String^ columnName
    ) sealed
F# __Копировать
     abstract ColumnIsAllowed : 
            sectionName : string * 
            columnName : string -> bool 
    override ColumnIsAllowed : 
            sectionName : string * 
            columnName : string -> bool 
#### Параметры
sectionName [String](https://learn.microsoft.com/dotnet/api/system.string)
    Имя секции, для которой требуется выполнить проверку.
columnName [String](https://learn.microsoft.com/dotnet/api/system.string)
#### Возвращаемое значение
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)  
true, если колонка с заданным именем является доступной; false в противном
случае.
#### Реализации
[ICardValidationLimitationManager.ColumnIsAllowed(String,
String)](M_Tessa_Cards_Validation_ICardValidationLimitationManager_ColumnIsAllowed.htm)  
##  __См. также
#### Ссылки
[CardValidationLimitationManager -
](T_Tessa_Cards_Validation_CardValidationLimitationManager.htm)
[Tessa.Cards.Validation - пространство имён](N_Tessa_Cards_Validation.htm)
