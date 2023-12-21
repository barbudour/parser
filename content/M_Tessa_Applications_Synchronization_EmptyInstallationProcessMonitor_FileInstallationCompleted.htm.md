# EmptyInstallationProcessMonitor.FileInstallationCompleted - метод
Вызывается по завершению установки файла
## __Definition
 **Пространство имён:**
[Tessa.Applications.Synchronization](N_Tessa_Applications_Synchronization.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public void FileInstallationCompleted(
    	ApplicationPackageFile file
    )
VB __Копировать
     Public Sub FileInstallationCompleted ( 
    	file As ApplicationPackageFile
    )
C++ __Копировать
     public:
    virtual void FileInstallationCompleted(
    	ApplicationPackageFile^ file
    ) sealed
F# __Копировать
     abstract FileInstallationCompleted : 
            file : ApplicationPackageFile -> unit 
    override FileInstallationCompleted : 
            file : ApplicationPackageFile -> unit 
#### Параметры
file
[ApplicationPackageFile](T_Tessa_Applications_Package_ApplicationPackageFile.htm)
     Файл 
#### Реализации
[IInstallationProcessMonitor.FileInstallationCompleted(ApplicationPackageFile)](M_Tessa_Applications_Synchronization_IInstallationProcessMonitor_FileInstallationCompleted.htm)  
##  __См. также
#### Ссылки
[EmptyInstallationProcessMonitor -
](T_Tessa_Applications_Synchronization_EmptyInstallationProcessMonitor.htm)
[Tessa.Applications.Synchronization - пространство
имён](N_Tessa_Applications_Synchronization.htm)
