# LicenseMigrationManager - класс
Объект, управляющий переходом лицензий с предыдущих версий на текущую. В
объекте должны быть зарегистрированы миграции при переходе не более, чем на
одну версию вперёд, иначе миграции запущены не будут.
## __Definition
 **Пространство имён:**
[Tessa.Platform.Licensing](N_Tessa_Platform_Licensing.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class LicenseMigrationManager : ILicenseMigrationManager, 
    	ISealable
VB __Копировать
     Public NotInheritable Class LicenseMigrationManager
    	Implements ILicenseMigrationManager, ISealable
C++ __Копировать
     public ref class LicenseMigrationManager sealed : ILicenseMigrationManager, 
    	ISealable
F# __Копировать
     [<SealedAttribute>]
    type LicenseMigrationManager = 
        class
            interface ILicenseMigrationManager
            interface ISealable
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ LicenseMigrationManager
Implements
    [ISealable](T_Tessa_Platform_ISealable.htm), [ILicenseMigrationManager](T_Tessa_Platform_Licensing_ILicenseMigrationManager.htm)
##  __Конструкторы
[LicenseMigrationManager](M_Tessa_Platform_Licensing_LicenseMigrationManager__ctor.htm)|
Инициализирует новый экземпляр класса LicenseMigrationManager  
---|---  
##  __Свойства
[Editor](P_Tessa_Platform_Licensing_LicenseMigrationManager_Editor.htm)|
Объект по умолчанию, управляющий переходом лицензий с предыдущих версий на
текущую для использования в редакторе лицензий.  
---|---  
[IsSealed](P_Tessa_Platform_Licensing_LicenseMigrationManager_IsSealed.htm)|
Признак того, что объект был защищён от изменений.  
[Service](P_Tessa_Platform_Licensing_LicenseMigrationManager_Service.htm)|
Объект по умолчанию, управляющий переходом лицензий с предыдущих версий на
текущую для использования в веб-сервисе.  
## __Методы
[Equals](https://learn.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\))| Determines whether the specified object is
equal to the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
---|---  
[Finalize](https://learn.microsoft.com/dotnet/api/system.object.finalize#system-
object-finalize)| Allows an object to try to free resources and perform other
cleanup operations before it is reclaimed by garbage collection.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetHashCode](https://learn.microsoft.com/dotnet/api/system.object.gethashcode#system-
object-gethashcode)| Serves as the default hash function.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetType](https://learn.microsoft.com/dotnet/api/system.object.gettype#system-
object-gettype)| Gets the
[Type](https://learn.microsoft.com/dotnet/api/system.type) of the current
instance.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[Register](M_Tessa_Platform_Licensing_LicenseMigrationManager_Register.htm)|
Выполняет регистрацию миграции в текущем объекте.  
[Seal](M_Tessa_Platform_Licensing_LicenseMigrationManager_Seal.htm)| Защищает
объект от изменений.  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[Upgrade](M_Tessa_Platform_Licensing_LicenseMigrationManager_Upgrade.htm)|
Выполняет переход с предыдущей версии лицензии на текущую. При этом
выполняются зарегистрированные миграции в требуемом порядке.  
## __Методы расширения
[Get](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Get.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
---|---  
[InternalMarkerCanvas](M_Tessa_UI_Views_Charting_Annotations_AnnotationInternalsAccessor_InternalMarkerCanvas.htm)|
Возвращает маркер аннотации  
(Определяется
[AnnotationInternalsAccessor](T_Tessa_UI_Views_Charting_Annotations_AnnotationInternalsAccessor.htm))  
[Invoke](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Invoke.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
[Set](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Set.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
##  __См. также
#### Ссылки
[Tessa.Platform.Licensing - пространство имён](N_Tessa_Platform_Licensing.htm)
