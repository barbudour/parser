# ICardValidationLimitationManager.RowIsAllowed - метод
Возвращает признак того, что строка с заданным идентификатором в указанной
секции является доступной. При этом ограничений либо не должно быть вообще,
либо разрешено использование конкретно заданной строки в секции.
## __Definition
 **Пространство имён:** [Tessa.Cards.Validation](N_Tessa_Cards_Validation.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     bool RowIsAllowed(
    	string sectionName,
    	Guid rowID
    )
VB __Копировать
     Function RowIsAllowed ( 
    	sectionName As String,
    	rowID As Guid
    ) As Boolean
C++ __Копировать
     bool RowIsAllowed(
    	String^ sectionName, 
    	Guid rowID
    )
F# __Копировать
     abstract RowIsAllowed : 
            sectionName : string * 
            rowID : Guid -> bool 
#### Параметры
sectionName [String](https://learn.microsoft.com/dotnet/api/system.string)
    Имя секции, для строки которой требуется выполнить проверку.
rowID [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
    Идентификатор строки, который требуется проверить.
#### Возвращаемое значение
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)  
true, если строка с заданным идентификатором в указанной секции является
доступной; false в противном случае.
## __См. также
#### Ссылки
[ICardValidationLimitationManager -
](T_Tessa_Cards_Validation_ICardValidationLimitationManager.htm)
[Tessa.Cards.Validation - пространство имён](N_Tessa_Cards_Validation.htm)
