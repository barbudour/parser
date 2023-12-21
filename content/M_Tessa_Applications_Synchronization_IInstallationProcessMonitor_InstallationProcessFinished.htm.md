# IInstallationProcessMonitor.InstallationProcessFinished - метод
Вызывается по завершению процесса установки
## __Definition
 **Пространство имён:**
[Tessa.Applications.Synchronization](N_Tessa_Applications_Synchronization.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     void InstallationProcessFinished(
    	[NotNullAttribute] ValidationResult validationResult
    )
VB __Копировать
     Sub InstallationProcessFinished ( 
    	<NotNullAttribute> validationResult As ValidationResult
    )
C++ __Копировать
     void InstallationProcessFinished(
    	[NotNullAttribute] ValidationResult^ validationResult
    )
F# __Копировать
     abstract InstallationProcessFinished : 
            [<NotNullAttribute>] validationResult : ValidationResult -> unit 
#### Параметры
validationResult
[ValidationResult](T_Tessa_Platform_Validation_ValidationResult.htm)
    Результат выполнения
##  __См. также
#### Ссылки
[IInstallationProcessMonitor -
](T_Tessa_Applications_Synchronization_IInstallationProcessMonitor.htm)
[Tessa.Applications.Synchronization - пространство
имён](N_Tessa_Applications_Synchronization.htm)
