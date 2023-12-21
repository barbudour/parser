# CardTableViewControlViewModel.OnUnloadingAsync - метод
Отписываемся от всех событий
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Platform.Client.UI.TableViewExtension](N_Tessa_Extensions_Platform_Client_UI_TableViewExtension.htm)  
 **Сборка:** Tessa.UI (в Tessa.UI.dll) Версия: 3.6.0.17
C# __Копировать
     protected override ValueTask OnUnloadingAsync(
    	IValidationResultBuilder validationResult
    )
VB __Копировать
     Protected Overrides Function OnUnloadingAsync ( 
    	validationResult As IValidationResultBuilder
    ) As ValueTask
C++ __Копировать
     protected:
    virtual ValueTask OnUnloadingAsync(
    	IValidationResultBuilder^ validationResult
    ) override
F# __Копировать
     abstract OnUnloadingAsync : 
            validationResult : IValidationResultBuilder -> ValueTask 
    override OnUnloadingAsync : 
            validationResult : IValidationResultBuilder -> ValueTask 
#### Параметры
validationResult
[IValidationResultBuilder](T_Tessa_Platform_Validation_IValidationResultBuilder.htm)
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask)
##  __См. также
#### Ссылки
[CardTableViewControlViewModel -
](T_Tessa_Extensions_Platform_Client_UI_TableViewExtension_CardTableViewControlViewModel.htm)
[Tessa.Extensions.Platform.Client.UI.TableViewExtension - пространство
имён](N_Tessa_Extensions_Platform_Client_UI_TableViewExtension.htm)
