# LicenseModuleTypeData - класс
Информация по типам, описывающим модули лицензий
[ILicenseModule](T_Tessa_Platform_Licensing_ILicenseModule.htm).
## __Definition
 **Пространство имён:**
[Tessa.Platform.Licensing](N_Tessa_Platform_Licensing.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
    [SerializableAttribute]
    [XmlRootAttribute("licenseModules", Namespace = "http://syntellect.ru/tessa")]
    public sealed class LicenseModuleTypeData : ICloneable
VB __Копировать
    <SerializableAttribute>
    <XmlRootAttribute("licenseModules", Namespace := "http://syntellect.ru/tessa")>
    Public NotInheritable Class LicenseModuleTypeData
    	Implements ICloneable
C++ __Копировать
    [SerializableAttribute]
    [XmlRootAttribute(L"licenseModules", Namespace = L"http://syntellect.ru/tessa")]
    public ref class LicenseModuleTypeData sealed : ICloneable
F# __Копировать
     [<SealedAttribute>]
    [<SerializableAttribute>]
    [<XmlRootAttribute("licenseModules", Namespace = "http://syntellect.ru/tessa")>]
    type LicenseModuleTypeData = 
        class
            interface ICloneable
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ LicenseModuleTypeData
Implements
    [ICloneable](https://learn.microsoft.com/dotnet/api/system.icloneable)
##  __Конструкторы
[LicenseModuleTypeData](M_Tessa_Platform_Licensing_LicenseModuleTypeData__ctor.htm)|
Инициализирует новый экземпляр класса LicenseModuleTypeData  
---|---  
##  __Свойства
[Types](P_Tessa_Platform_Licensing_LicenseModuleTypeData_Types.htm)|
Коллекция доступных типов модулей лицензий.  
---|---  
## __Методы
[Clone](M_Tessa_Platform_Licensing_LicenseModuleTypeData_Clone.htm)| Создаёт
полную копию объекта.  
---|---  
[DeserializeFromXml](M_Tessa_Platform_Licensing_LicenseModuleTypeData_DeserializeFromXml.htm)|
Десериализует из XML информацию по типам, описывающим модули лицензий.  
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
[Repair](M_Tessa_Platform_Licensing_LicenseModuleTypeData_Repair.htm)|
Исправляет объект и его дочерние объекты. Рекомендуется использовать перед
сериализацией.  
[SerializeToXml](M_Tessa_Platform_Licensing_LicenseModuleTypeData_SerializeToXml.htm)|
Возвращает строку, которая содержит сериализованную в XML информацию по типам,
описывающим модули лицензий.  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
##  __Методы расширения
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
