# CardHeaderFile.ValidateInternal - метод
Выполняет валидацию текущего объекта и всех его дочерних объектов.
##  __Definition
 **Пространство имён:**
[Tessa.Cards.ComponentModel](N_Tessa_Cards_ComponentModel.htm)  
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
[CardHeaderFile - ](T_Tessa_Cards_ComponentModel_CardHeaderFile.htm)
[Tessa.Cards.ComponentModel - пространство
имён](N_Tessa_Cards_ComponentModel.htm)
