# EmptyInstallationProcessMonitor.FileInstallationStarting - метод
Вызывается перед началом установки файла
## __Definition
 **Пространство имён:**
[Tessa.Applications.Synchronization](N_Tessa_Applications_Synchronization.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public void FileInstallationStarting(
    	ApplicationPackageFile file
    )
VB __Копировать
     Public Sub FileInstallationStarting ( 
    	file As ApplicationPackageFile
    )
C++ __Копировать
     public:
    virtual void FileInstallationStarting(
    	ApplicationPackageFile^ file
    ) sealed
F# __Копировать
     abstract FileInstallationStarting : 
            file : ApplicationPackageFile -> unit 
    override FileInstallationStarting : 
            file : ApplicationPackageFile -> unit 
#### Параметры
file
[ApplicationPackageFile](T_Tessa_Applications_Package_ApplicationPackageFile.htm)
     Файл 
#### Реализации
[IInstallationProcessMonitor.FileInstallationStarting(ApplicationPackageFile)](M_Tessa_Applications_Synchronization_IInstallationProcessMonitor_FileInstallationStarting.htm)  
##  __См. также
#### Ссылки
[EmptyInstallationProcessMonitor -
](T_Tessa_Applications_Synchronization_EmptyInstallationProcessMonitor.htm)
[Tessa.Applications.Synchronization - пространство
имён](N_Tessa_Applications_Synchronization.htm)
