# TransientLicenseManager - класс
Объект, управляющий временной лицензией.
## __Definition
 **Пространство имён:**
[Tessa.Platform.Licensing](N_Tessa_Platform_Licensing.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class TransientLicenseManager : ILicenseManager
VB __Копировать
     Public NotInheritable Class TransientLicenseManager
    	Implements ILicenseManager
C++ __Копировать
     public ref class TransientLicenseManager sealed : ILicenseManager
F# __Копировать
     [<SealedAttribute>]
    type TransientLicenseManager = 
        class
            interface ILicenseManager
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ TransientLicenseManager
Implements
    [ILicenseManager](T_Tessa_Platform_Licensing_ILicenseManager.htm)
##  __Конструкторы
[TransientLicenseManager](M_Tessa_Platform_Licensing_TransientLicenseManager__ctor.htm)|
Инициализирует новый экземпляр класса TransientLicenseManager  
---|---  
##  __Методы
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
[GetLicenseAsync](M_Tessa_Platform_Licensing_TransientLicenseManager_GetLicenseAsync.htm)|
Возвращает текущую используемую лицензию.  
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
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
##  __Методы расширения
[CheckChartLicense](M_Tessa_UI_Views_Charting_ChartsLicenseExtensions_CheckChartLicense.htm)|
Осуществляет проверку наличия лицензии для модуля диаграмм.  
(Определяется
[ChartsLicenseExtensions](T_Tessa_UI_Views_Charting_ChartsLicenseExtensions.htm))  
---|---  
[Get](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Get.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
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
[ValidateTypeOnClient](M_Tessa_Platform_Licensing_LicensingExtensions_ValidateTypeOnClient.htm)|
Проверяет, что тип объекта является допустимым на клиенте. Это гарантирует,
что объект не был нигде подменён злоумышленником.  
(Определяется
[LicensingExtensions](T_Tessa_Platform_Licensing_LicensingExtensions.htm))  
[ValidateTypeOnServer](M_Tessa_Platform_Licensing_LicensingExtensions_ValidateTypeOnServer.htm)|
Проверяет, что тип объекта является допустимым на сервере. Это гарантирует,
что объект не был нигде подменён злоумышленником.  
(Определяется
[LicensingExtensions](T_Tessa_Platform_Licensing_LicensingExtensions.htm))  
##  __См. также
#### Ссылки
[Tessa.Platform.Licensing - пространство имён](N_Tessa_Platform_Licensing.htm)
