# FileSystemSynchronizationSource.CreateSynchronizationEnumerable - метод
Возвращает перечислитель файлов для пакета приложения
## __Definition
 **Пространство имён:**
[Tessa.Applications.Synchronization](N_Tessa_Applications_Synchronization.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public IApplicationPackageFileEnumerable CreateSynchronizationEnumerable(
    	ApplicationPackage currentState
    )
VB __Копировать
     Public Function CreateSynchronizationEnumerable ( 
    	currentState As ApplicationPackage
    ) As IApplicationPackageFileEnumerable
C++ __Копировать
     public:
    IApplicationPackageFileEnumerable^ CreateSynchronizationEnumerable(
    	ApplicationPackage^ currentState
    )
F# __Копировать
     member CreateSynchronizationEnumerable : 
            currentState : ApplicationPackage -> IApplicationPackageFileEnumerable 
#### Параметры
currentState
[ApplicationPackage](T_Tessa_Applications_Package_ApplicationPackage.htm)
     Пакет приложения 
#### Возвращаемое значение
[IApplicationPackageFileEnumerable](T_Tessa_Applications_Synchronization_IApplicationPackageFileEnumerable.htm)  
Перечислитель файлов
## __См. также
#### Ссылки
[FileSystemSynchronizationSource -
](T_Tessa_Applications_Synchronization_FileSystemSynchronizationSource.htm)
[Tessa.Applications.Synchronization - пространство
имён](N_Tessa_Applications_Synchronization.htm)
