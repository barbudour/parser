# CardValidatorType.IsAllowed(CardValidationMode) - метод
Возвращает признак того, что валидатор разрешён для заданного способа
выполнения валидации.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public bool IsAllowed(
    	CardValidationMode validationMode
    )
VB __Копировать
     Public Function IsAllowed ( 
    	validationMode As CardValidationMode
    ) As Boolean
C++ __Копировать
     public:
    bool IsAllowed(
    	CardValidationMode validationMode
    )
F# __Копировать
     member IsAllowed : 
            validationMode : CardValidationMode -> bool 
#### Параметры
validationMode
[CardValidationMode](T_Tessa_Cards_Validation_CardValidationMode.htm)
    Способ выполнения валидации, который требуется проверить.
#### Возвращаемое значение
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)  
true, если валидатор разрешён для заданного способа выполнения валидации;
false в противном случае.
## __См. также
#### Ссылки
[CardValidatorType - ](T_Tessa_Cards_CardValidatorType.htm)
[IsAllowed - перегрузка](Overload_Tessa_Cards_CardValidatorType_IsAllowed.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
