# EmptyInstallationProcessMonitor.InstallationProcessStarting - метод
Вызывается перед началом процесса установки
## __Definition
 **Пространство имён:**
[Tessa.Applications.Synchronization](N_Tessa_Applications_Synchronization.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public void InstallationProcessStarting(
    	ApplicationPackage package,
    	long totalBytes
    )
VB __Копировать
     Public Sub InstallationProcessStarting ( 
    	package As ApplicationPackage,
    	totalBytes As Long
    )
C++ __Копировать
     public:
    virtual void InstallationProcessStarting(
    	ApplicationPackage^ package, 
    	long long totalBytes
    ) sealed
F# __Копировать
     abstract InstallationProcessStarting : 
            package : ApplicationPackage * 
            totalBytes : int64 -> unit 
    override InstallationProcessStarting : 
            package : ApplicationPackage * 
            totalBytes : int64 -> unit 
#### Параметры
package
[ApplicationPackage](T_Tessa_Applications_Package_ApplicationPackage.htm)
     Пакет приложения 
totalBytes [Int64](https://learn.microsoft.com/dotnet/api/system.int64)
     Общий размер файлов 
#### Реализации
[IInstallationProcessMonitor.InstallationProcessStarting(ApplicationPackage,
Int64)](M_Tessa_Applications_Synchronization_IInstallationProcessMonitor_InstallationProcessStarting.htm)  
##  __См. также
#### Ссылки
[EmptyInstallationProcessMonitor -
](T_Tessa_Applications_Synchronization_EmptyInstallationProcessMonitor.htm)
[Tessa.Applications.Synchronization - пространство
имён](N_Tessa_Applications_Synchronization.htm)
