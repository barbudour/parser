# ILicenseMigrationManager - интерфейс
Объект, управляющий переходом лицензий с предыдущих версий на текущую.
## __Definition
 **Пространство имён:**
[Tessa.Platform.Licensing](N_Tessa_Platform_Licensing.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface ILicenseMigrationManager : ISealable
VB __Копировать
     Public Interface ILicenseMigrationManager
    	Inherits ISealable
C++ __Копировать
     public interface class ILicenseMigrationManager : ISealable
F# __Копировать
     type ILicenseMigrationManager = 
        interface
            interface ISealable
        end
Implements
    [ISealable](T_Tessa_Platform_ISealable.htm)
##  __Свойства
[IsSealed](P_Tessa_Platform_ISealable_IsSealed.htm)| Признак того, что объект
был защищён от изменений.  
(Унаследован от [ISealable](T_Tessa_Platform_ISealable.htm))  
---|---  
##  __Методы
[Register](M_Tessa_Platform_Licensing_ILicenseMigrationManager_Register.htm)|
Выполняет регистрацию миграции в текущем объекте.  
---|---  
[Seal](M_Tessa_Platform_ISealable_Seal.htm)| Защищает объект от изменений.  
(Унаследован от [ISealable](T_Tessa_Platform_ISealable.htm))  
[Upgrade](M_Tessa_Platform_Licensing_ILicenseMigrationManager_Upgrade.htm)|
Выполняет переход с предыдущей версии лицензии на текущую. При этом
выполняются зарегистрированные миграции в требуемом порядке.  
## __См. также
#### Ссылки
[Tessa.Platform.Licensing - пространство имён](N_Tessa_Platform_Licensing.htm)
