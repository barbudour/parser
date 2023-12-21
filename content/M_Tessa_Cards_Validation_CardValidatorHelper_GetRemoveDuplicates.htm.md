# CardValidatorHelper.GetRemoveDuplicates - метод
Возвращает признак того, что неуникальные значения (дубликаты) нужно
автоматически удалять.
## __Definition
 **Пространство имён:** [Tessa.Cards.Validation](N_Tessa_Cards_Validation.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static bool GetRemoveDuplicates(
    	CardTypeValidator validator
    )
VB __Копировать
     Public Shared Function GetRemoveDuplicates ( 
    	validator As CardTypeValidator
    ) As Boolean
C++ __Копировать
     public:
    static bool GetRemoveDuplicates(
    	CardTypeValidator^ validator
    )
F# __Копировать
     static member GetRemoveDuplicates : 
            validator : CardTypeValidator -> bool 
#### Параметры
validator [CardTypeValidator](T_Tessa_Cards_CardTypeValidator.htm)
    Объект, содержащий настройки валидатора.
#### Возвращаемое значение
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)  
Признак того, что неуникальные значения (дубликаты) нужно автоматически
удалять.
##  __См. также
#### Ссылки
[CardValidatorHelper - ](T_Tessa_Cards_Validation_CardValidatorHelper.htm)
[Tessa.Cards.Validation - пространство имён](N_Tessa_Cards_Validation.htm)
