# AssemblySynchronizationSource.Validate - метод
Выполняет валидацию текущего объекта и всех его дочерних объектов.
##  __Definition
 **Пространство имён:**
[Tessa.Applications.Synchronization](N_Tessa_Applications_Synchronization.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public void Validate(
    	IValidationResultBuilder validationResult
    )
VB __Копировать
     Public Sub Validate ( 
    	validationResult As IValidationResultBuilder
    )
C++ __Копировать
     public:
    virtual void Validate(
    	IValidationResultBuilder^ validationResult
    ) sealed
F# __Копировать
     abstract Validate : 
            validationResult : IValidationResultBuilder -> unit 
    override Validate : 
            validationResult : IValidationResultBuilder -> unit 
#### Параметры
validationResult
[IValidationResultBuilder](T_Tessa_Platform_Validation_IValidationResultBuilder.htm)
    Объект, выполняющий построение результата валидации.
#### Реализации
[IValidationObject.Validate(IValidationResultBuilder)](M_Tessa_Platform_Validation_IValidationObject_Validate.htm)  
##  __См. также
#### Ссылки
[AssemblySynchronizationSource -
](T_Tessa_Applications_Synchronization_AssemblySynchronizationSource.htm)
[Tessa.Applications.Synchronization - пространство
имён](N_Tessa_Applications_Synchronization.htm)
