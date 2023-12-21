# CardValidationLimitationManager.SectionIsAllowed - метод
Возвращает признак того, что секция с заданным именем является доступной.
##  __Definition
 **Пространство имён:** [Tessa.Cards.Validation](N_Tessa_Cards_Validation.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public bool SectionIsAllowed(
    	string sectionName
    )
VB __Копировать
     Public Function SectionIsAllowed ( 
    	sectionName As String
    ) As Boolean
C++ __Копировать
     public:
    virtual bool SectionIsAllowed(
    	String^ sectionName
    ) sealed
F# __Копировать
     abstract SectionIsAllowed : 
            sectionName : string -> bool 
    override SectionIsAllowed : 
            sectionName : string -> bool 
#### Параметры
sectionName [String](https://learn.microsoft.com/dotnet/api/system.string)
    Имя секции, для которой требуется выполнить проверку.
#### Возвращаемое значение
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)  
true, если секция с заданным именем является доступной; false в противном
случае.
#### Реализации
[ICardValidationLimitationManager.SectionIsAllowed(String)](M_Tessa_Cards_Validation_ICardValidationLimitationManager_SectionIsAllowed.htm)  
##  __См. также
#### Ссылки
[CardValidationLimitationManager -
](T_Tessa_Cards_Validation_CardValidationLimitationManager.htm)
[Tessa.Cards.Validation - пространство имён](N_Tessa_Cards_Validation.htm)
