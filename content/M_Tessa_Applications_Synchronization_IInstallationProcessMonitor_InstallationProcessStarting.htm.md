# IInstallationProcessMonitor.InstallationProcessStarting - метод
Вызывается перед началом процесса установки
## __Definition
 **Пространство имён:**
[Tessa.Applications.Synchronization](N_Tessa_Applications_Synchronization.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     void InstallationProcessStarting(
    	[NotNullAttribute] ApplicationPackage package,
    	long totalBytes
    )
VB __Копировать
     Sub InstallationProcessStarting ( 
    	<NotNullAttribute> package As ApplicationPackage,
    	totalBytes As Long
    )
C++ __Копировать
     void InstallationProcessStarting(
    	[NotNullAttribute] ApplicationPackage^ package, 
    	long long totalBytes
    )
F# __Копировать
     abstract InstallationProcessStarting : 
            [<NotNullAttribute>] package : ApplicationPackage * 
            totalBytes : int64 -> unit 
#### Параметры
package
[ApplicationPackage](T_Tessa_Applications_Package_ApplicationPackage.htm)
    Пакет приложения
totalBytes [Int64](https://learn.microsoft.com/dotnet/api/system.int64)
    Общий размер файлов
##  __См. также
#### Ссылки
[IInstallationProcessMonitor -
](T_Tessa_Applications_Synchronization_IInstallationProcessMonitor.htm)
[Tessa.Applications.Synchronization - пространство
имён](N_Tessa_Applications_Synchronization.htm)
