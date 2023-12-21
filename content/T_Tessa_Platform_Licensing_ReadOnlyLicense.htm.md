# ReadOnlyLicense - класс
Лицензия на платформу Tessa, доступная только для чтения.
## __Definition
 **Пространство имён:**
[Tessa.Platform.Licensing](N_Tessa_Platform_Licensing.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class ReadOnlyLicense : ILicense
VB __Копировать
     Public NotInheritable Class ReadOnlyLicense
    	Implements ILicense
C++ __Копировать
     public ref class ReadOnlyLicense sealed : ILicense
F# __Копировать
     [<SealedAttribute>]
    type ReadOnlyLicense = 
        class
            interface ILicense
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ ReadOnlyLicense
Implements
    [ILicense](T_Tessa_Platform_Licensing_ILicense.htm)
##  __Конструкторы
[ReadOnlyLicense](M_Tessa_Platform_Licensing_ReadOnlyLicense__ctor.htm)|
Создаёт экземпляр класса с указанием исходной лицензии, актуальные свойства
которой возвращаются текущим объектом.  
---|---  
## __Свойства
[CompanyAddress](P_Tessa_Platform_Licensing_ReadOnlyLicense_CompanyAddress.htm)|
Адрес компании, для которой выдана лицензия.  
---|---  
[CompanyName](P_Tessa_Platform_Licensing_ReadOnlyLicense_CompanyName.htm)| Имя
компании, для которой выдана лицензия.  
[ConcurrentCount](P_Tessa_Platform_Licensing_ReadOnlyLicense_ConcurrentCount.htm)|
Максимальное количество конкурентных сессий.  
[ID](P_Tessa_Platform_Licensing_ReadOnlyLicense_ID.htm)| Уникальный
идентификатор лицензии.  
[IssuedBy](P_Tessa_Platform_Licensing_ReadOnlyLicense_IssuedBy.htm)| Имя
компании, которая выдала лицензию.  
[Modules](P_Tessa_Platform_Licensing_ReadOnlyLicense_Modules.htm)| Коллекция
модулей, добавленных в лицензию. Каждый модуль содержит собственные настройки.  
[PersonalCount](P_Tessa_Platform_Licensing_ReadOnlyLicense_PersonalCount.htm)|
Максимальное количество персональных сессий.  
[ReceiveUpdatesTo](P_Tessa_Platform_Licensing_ReadOnlyLicense_ReceiveUpdatesTo.htm)|
Дата окончания получения обновлений платформы.  
[ValidFrom](P_Tessa_Platform_Licensing_ReadOnlyLicense_ValidFrom.htm)| Дата
выдачи лицензии.  
[ValidTo](P_Tessa_Platform_Licensing_ReadOnlyLicense_ValidTo.htm)| Дата
окончания лицензии.  
[Version](P_Tessa_Platform_Licensing_ReadOnlyLicense_Version.htm)| Версия
формата лицензии.  
##  __Методы
[AsReadOnly](M_Tessa_Platform_Licensing_ReadOnlyLicense_AsReadOnly.htm)|
Возвращает доступную только для чтения обёртку для текущего объекта. При
изменении коллекции модулей текущего объекта
[Tessa.Platform.Licensing.ILicense.Modules] коллекция в создаваемом объекте не
будет изменяться.  
---|---  
[Equals](https://learn.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\))| Determines whether the specified object is
equal to the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[Finalize](https://learn.microsoft.com/dotnet/api/system.object.finalize#system-
object-finalize)| Allows an object to try to free resources and perform other
cleanup operations before it is reclaimed by garbage collection.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetHashCode](https://learn.microsoft.com/dotnet/api/system.object.gethashcode#system-
object-gethashcode)| Serves as the default hash function.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetMobileCount](M_Tessa_Platform_Licensing_ReadOnlyLicense_GetMobileCount.htm)|
Возвращает максимальное количество лицензий для мобильного согласования.  
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
[Get](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Get.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
---|---  
[GetLicenseCount](M_Tessa_Platform_Runtime_RuntimeExtensions_GetLicenseCount.htm)|
Возвращает количество доступных лицензий для заданного типа licenseType. Для
типа [Unspecified](T_Tessa_Platform_Runtime_SessionLicenseType.htm)
возвращается -1.  
(Определяется
[RuntimeExtensions](T_Tessa_Platform_Runtime_RuntimeExtensions.htm))  
[GetValidToLastDateTime](M_Tessa_Platform_Licensing_LicensingExtensions_GetValidToLastDateTime.htm)|
Возвращает дату и время окончания лицензии. Определяется как дата в формате
UTC, указанная в лицензии, плюс время 23:59:59.  
(Определяется
[LicensingExtensions](T_Tessa_Platform_Licensing_LicensingExtensions.htm))  
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
[ToLicense](M_Tessa_Platform_Licensing_LicensingExtensions_ToLicense.htm)|
Преобразует тип объекта [ILicense](T_Tessa_Platform_Licensing_ILicense.htm) в
[License](T_Tessa_Platform_Licensing_License.htm) или создаёт новый объект
[License](T_Tessa_Platform_Licensing_License.htm), свойства которого получены
из заданного объекта.  
(Определяется
[LicensingExtensions](T_Tessa_Platform_Licensing_LicensingExtensions.htm))  
##  __См. также
#### Ссылки
[Tessa.Platform.Licensing - пространство имён](N_Tessa_Platform_Licensing.htm)
