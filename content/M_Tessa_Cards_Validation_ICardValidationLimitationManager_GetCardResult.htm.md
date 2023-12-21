# ICardValidationLimitationManager.GetCardResult - метод
Возвращает результат валидации для данных карточки, в котором ограничивается
набор сообщений для заданных секций и их строк.
## __Definition
 **Пространство имён:** [Tessa.Cards.Validation](N_Tessa_Cards_Validation.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     ValidationResult GetCardResult(
    	ICardValidationContext context,
    	ICardValidationResult result
    )
VB __Копировать
     Function GetCardResult ( 
    	context As ICardValidationContext,
    	result As ICardValidationResult
    ) As ValidationResult
C++ __Копировать
    ValidationResult^ GetCardResult(
    	ICardValidationContext^ context, 
    	ICardValidationResult^ result
    )
F# __Копировать
     abstract GetCardResult : 
            context : ICardValidationContext * 
            result : ICardValidationResult -> ValidationResult 
#### Параметры
context
[ICardValidationContext](T_Tessa_Cards_Validation_ICardValidationContext.htm)
    Контекст валидации карточки.
result
[ICardValidationResult](T_Tessa_Cards_Validation_ICardValidationResult.htm)
    Результат валидации карточки.
#### Возвращаемое значение
[ValidationResult](T_Tessa_Platform_Validation_ValidationResult.htm)  
Результат валидации для данных карточки, в котором ограничивается набор
сообщений для заданных секций и их строк.
## __См. также
#### Ссылки
[ICardValidationLimitationManager -
](T_Tessa_Cards_Validation_ICardValidationLimitationManager.htm)
[Tessa.Cards.Validation - пространство имён](N_Tessa_Cards_Validation.htm)
