# CardValidationLimitationManager.RowIsAllowed - метод
Возвращает признак того, что строка с заданным идентификатором в указанной
секции является доступной. При этом ограничений либо не должно быть вообще,
либо разрешено использование конкретно заданной строки в секции.
## __Definition
 **Пространство имён:** [Tessa.Cards.Validation](N_Tessa_Cards_Validation.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public bool RowIsAllowed(
    	string sectionName,
    	Guid rowID
    )
VB __Копировать
     Public Function RowIsAllowed ( 
    	sectionName As String,
    	rowID As Guid
    ) As Boolean
C++ __Копировать
     public:
    virtual bool RowIsAllowed(
    	String^ sectionName, 
    	Guid rowID
    ) sealed
F# __Копировать
     abstract RowIsAllowed : 
            sectionName : string * 
            rowID : Guid -> bool 
    override RowIsAllowed : 
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
#### Реализации
[ICardValidationLimitationManager.RowIsAllowed(String,
Guid)](M_Tessa_Cards_Validation_ICardValidationLimitationManager_RowIsAllowed.htm)  
##  __См. также
#### Ссылки
[CardValidationLimitationManager -
](T_Tessa_Cards_Validation_CardValidationLimitationManager.htm)
[Tessa.Cards.Validation - пространство имён](N_Tessa_Cards_Validation.htm)
