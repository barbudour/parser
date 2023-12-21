# IInstallationProcessMonitor.FileInstallationStarting - метод
Вызывается перед началом установки файла
## __Definition
 **Пространство имён:**
[Tessa.Applications.Synchronization](N_Tessa_Applications_Synchronization.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     void FileInstallationStarting(
    	[NotNullAttribute] ApplicationPackageFile file
    )
VB __Копировать
     Sub FileInstallationStarting ( 
    	<NotNullAttribute> file As ApplicationPackageFile
    )
C++ __Копировать
     void FileInstallationStarting(
    	[NotNullAttribute] ApplicationPackageFile^ file
    )
F# __Копировать
     abstract FileInstallationStarting : 
            [<NotNullAttribute>] file : ApplicationPackageFile -> unit 
#### Параметры
file
[ApplicationPackageFile](T_Tessa_Applications_Package_ApplicationPackageFile.htm)
    Файл
##  __См. также
#### Ссылки
[IInstallationProcessMonitor -
](T_Tessa_Applications_Synchronization_IInstallationProcessMonitor.htm)
[Tessa.Applications.Synchronization - пространство
имён](N_Tessa_Applications_Synchronization.htm)
