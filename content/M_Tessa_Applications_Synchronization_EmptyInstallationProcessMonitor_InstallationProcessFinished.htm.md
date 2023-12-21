# EmptyInstallationProcessMonitor.InstallationProcessFinished - метод
Вызывается по завершению процесса установки
## __Definition
 **Пространство имён:**
[Tessa.Applications.Synchronization](N_Tessa_Applications_Synchronization.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public void InstallationProcessFinished(
    	ValidationResult validationResult
    )
VB __Копировать
     Public Sub InstallationProcessFinished ( 
    	validationResult As ValidationResult
    )
C++ __Копировать
     public:
    virtual void InstallationProcessFinished(
    	ValidationResult^ validationResult
    ) sealed
F# __Копировать
     abstract InstallationProcessFinished : 
            validationResult : ValidationResult -> unit 
    override InstallationProcessFinished : 
            validationResult : ValidationResult -> unit 
#### Параметры
validationResult
[ValidationResult](T_Tessa_Platform_Validation_ValidationResult.htm)
     Результат выполнения 
#### Реализации
[IInstallationProcessMonitor.InstallationProcessFinished(ValidationResult)](M_Tessa_Applications_Synchronization_IInstallationProcessMonitor_InstallationProcessFinished.htm)  
##  __См. также
#### Ссылки
[EmptyInstallationProcessMonitor -
](T_Tessa_Applications_Synchronization_EmptyInstallationProcessMonitor.htm)
[Tessa.Applications.Synchronization - пространство
имён](N_Tessa_Applications_Synchronization.htm)
