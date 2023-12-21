# ICardValidationLimitationManager.ColumnIsAllowed - метод
Возвращает признак того, что колонка из указанной секции является доступной.
##  __Definition
 **Пространство имён:** [Tessa.Cards.Validation](N_Tessa_Cards_Validation.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     bool ColumnIsAllowed(
    	string sectionName,
    	string columnName
    )
VB __Копировать
     Function ColumnIsAllowed ( 
    	sectionName As String,
    	columnName As String
    ) As Boolean
C++ __Копировать
     bool ColumnIsAllowed(
    	String^ sectionName, 
    	String^ columnName
    )
F# __Копировать
     abstract ColumnIsAllowed : 
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
## __См. также
#### Ссылки
[ICardValidationLimitationManager -
](T_Tessa_Cards_Validation_ICardValidationLimitationManager.htm)
[Tessa.Cards.Validation - пространство имён](N_Tessa_Cards_Validation.htm)
