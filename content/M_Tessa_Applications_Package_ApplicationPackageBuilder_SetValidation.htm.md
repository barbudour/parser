# ApplicationPackageBuilder.SetValidation - метод
Устанавливает объект осуществляющий валидацию построения пакета приложения
## __Definition
 **Пространство имён:**
[Tessa.Applications.Package](N_Tessa_Applications_Package.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
    [NotNullAttribute]
    public ApplicationPackageBuilder SetValidation(
    	[NotNullAttribute] IValidationResultBuilder validationResultBuilder
    )
VB __Копировать
    <NotNullAttribute>
    Public Function SetValidation ( 
    	<NotNullAttribute> validationResultBuilder As IValidationResultBuilder
    ) As ApplicationPackageBuilder
C++ __Копировать
     public:
    [NotNullAttribute]
    ApplicationPackageBuilder^ SetValidation(
    	[NotNullAttribute] IValidationResultBuilder^ validationResultBuilder
    )
F# __Копировать
     [<NotNullAttribute>]
    member SetValidation : 
            [<NotNullAttribute>] validationResultBuilder : IValidationResultBuilder -> ApplicationPackageBuilder 
#### Параметры
validationResultBuilder
[IValidationResultBuilder](T_Tessa_Platform_Validation_IValidationResultBuilder.htm)
     Построитель результатов валидиции 
#### Возвращаемое значение
[ApplicationPackageBuilder](T_Tessa_Applications_Package_ApplicationPackageBuilder.htm)  
Ссылку на себя
## __См. также
#### Ссылки
[ApplicationPackageBuilder -
](T_Tessa_Applications_Package_ApplicationPackageBuilder.htm)
[Tessa.Applications.Package - пространство
имён](N_Tessa_Applications_Package.htm)
