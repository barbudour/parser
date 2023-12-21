# CardTypeVisitor - конструктор
Создаёт экземпляр класса.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     protected CardTypeVisitor(
    	IValidationResultBuilder validationResult = null
    )
VB __Копировать
     Protected Sub New ( 
    	Optional validationResult As IValidationResultBuilder = Nothing
    )
C++ __Копировать
     protected:
    CardTypeVisitor(
    	IValidationResultBuilder^ validationResult = nullptr
    )
F# __Копировать
     new : 
            ?validationResult : IValidationResultBuilder 
    (* Defaults:
            let _validationResult = defaultArg validationResult null
    *)
    -> CardTypeVisitor
#### Параметры
validationResult
[IValidationResultBuilder](T_Tessa_Platform_Validation_IValidationResultBuilder.htm)
(Optional)
     Результат валидации, полученный посредством посещения объектов типа карточки. Укажите null, чтобы был создан новый экземпляр класса [ValidationResultBuilder](T_Tessa_Platform_Validation_ValidationResultBuilder.htm). 
## __См. также
#### Ссылки
[CardTypeVisitor - ](T_Tessa_Cards_CardTypeVisitor.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
