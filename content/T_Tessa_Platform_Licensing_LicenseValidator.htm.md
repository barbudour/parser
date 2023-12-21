# LicenseValidator - класс
Объект, выполняющий получение фактической информации по лицензиям для её
последующей валидации. Доступен на сервере.
## __Definition
 **Пространство имён:**
[Tessa.Platform.Licensing](N_Tessa_Platform_Licensing.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class LicenseValidator : ILicenseValidator
VB __Копировать
     Public NotInheritable Class LicenseValidator
    	Implements ILicenseValidator
C++ __Копировать
     public ref class LicenseValidator sealed : ILicenseValidator
F# __Копировать
     [<SealedAttribute>]
    type LicenseValidator = 
        class
            interface ILicenseValidator
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ LicenseValidator
Implements
    [ILicenseValidator](T_Tessa_Platform_Licensing_ILicenseValidator.htm)
##  __Конструкторы
[LicenseValidator](M_Tessa_Platform_Licensing_LicenseValidator__ctor.htm)|
Создаёт экземпляр класса с указанием его зависимостей.  
---|---  
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
[GetConcurrentLicenseCountAsync](M_Tessa_Platform_Licensing_LicenseValidator_GetConcurrentLicenseCountAsync.htm)|
Получает количество задействованных конкурентных лицензий типа concurrent.  
[GetHashCode](https://learn.microsoft.com/dotnet/api/system.object.gethashcode#system-
object-gethashcode)| Serves as the default hash function.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetMobileLicenseCountAsync](M_Tessa_Platform_Licensing_LicenseValidator_GetMobileLicenseCountAsync.htm)|
Получает количество задействованных лицензий мобильного согласования.  
[GetPersonalLicenseCountAsync](M_Tessa_Platform_Licensing_LicenseValidator_GetPersonalLicenseCountAsync.htm)|
Получает количество задействованных персональных лицензий типа personal.  
[GetType](https://learn.microsoft.com/dotnet/api/system.object.gettype#system-
object-gettype)| Gets the
[Type](https://learn.microsoft.com/dotnet/api/system.type) of the current
instance.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[HasMobileLicenseAsync](M_Tessa_Platform_Licensing_LicenseValidator_HasMobileLicenseAsync.htm)|
Возвращает признак того, что пользователь с заданным идентификатором имеет
лицензию мобильного согласования.  
[HasPersonalLicenseAsync](M_Tessa_Platform_Licensing_LicenseValidator_HasPersonalLicenseAsync.htm)|
Возвращает признак того, что пользователь с заданным идентификатором имеет
персональную лицензию.  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[WillIncreaseConcurrentLicenseCountAsync](M_Tessa_Platform_Licensing_LicenseValidator_WillIncreaseConcurrentLicenseCountAsync.htm)|
Возвращает признак того, что сессия с заданными параметрами будет потреблять
на одну конкурентную лицензию больше, чем до создания сессии. Сессия может не
увеличивать количество потребляемых лицензий, если вход выполняется для того
же сотрудника и производится с того же IP адреса.  
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
