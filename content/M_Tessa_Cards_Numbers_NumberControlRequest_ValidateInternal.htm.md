# NumberControlRequest.ValidateInternal - метод
Выполняет валидацию текущего объекта и всех его дочерних объектов.
##  __Definition
 **Пространство имён:** [Tessa.Cards.Numbers](N_Tessa_Cards_Numbers.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     protected override void ValidateInternal(
    	IValidationResultBuilder validationResult
    )
VB __Копировать
     Protected Overrides Sub ValidateInternal ( 
    	validationResult As IValidationResultBuilder
    )
C++ __Копировать
     protected:
    virtual void ValidateInternal(
    	IValidationResultBuilder^ validationResult
    ) override
F# __Копировать
     abstract ValidateInternal : 
            validationResult : IValidationResultBuilder -> unit 
    override ValidateInternal : 
            validationResult : IValidationResultBuilder -> unit 
#### Параметры
validationResult
[IValidationResultBuilder](T_Tessa_Platform_Validation_IValidationResultBuilder.htm)
    Объект, выполняющий построение результата валидации.
##  __См. также
#### Ссылки
[NumberControlRequest - ](T_Tessa_Cards_Numbers_NumberControlRequest.htm)
[Tessa.Cards.Numbers - пространство имён](N_Tessa_Cards_Numbers.htm)
