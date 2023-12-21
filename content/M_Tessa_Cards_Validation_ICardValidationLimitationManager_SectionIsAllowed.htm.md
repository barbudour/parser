# ICardValidationLimitationManager.SectionIsAllowed - метод
Возвращает признак того, что секция с заданным именем является доступной.
##  __Definition
 **Пространство имён:** [Tessa.Cards.Validation](N_Tessa_Cards_Validation.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     bool SectionIsAllowed(
    	string sectionName
    )
VB __Копировать
     Function SectionIsAllowed ( 
    	sectionName As String
    ) As Boolean
C++ __Копировать
     bool SectionIsAllowed(
    	String^ sectionName
    )
F# __Копировать
     abstract SectionIsAllowed : 
            sectionName : string -> bool 
#### Параметры
sectionName [String](https://learn.microsoft.com/dotnet/api/system.string)
    Имя секции, для которой требуется выполнить проверку.
#### Возвращаемое значение
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)  
true, если секция с заданным именем является доступной; false в противном
случае.
## __См. также
#### Ссылки
[ICardValidationLimitationManager -
](T_Tessa_Cards_Validation_ICardValidationLimitationManager.htm)
[Tessa.Cards.Validation - пространство имён](N_Tessa_Cards_Validation.htm)
