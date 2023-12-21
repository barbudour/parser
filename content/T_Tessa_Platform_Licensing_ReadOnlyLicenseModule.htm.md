# ReadOnlyLicenseModule - класс
Модуль лицензии, доступный только для чтения.
## __Definition
 **Пространство имён:**
[Tessa.Platform.Licensing](N_Tessa_Platform_Licensing.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class ReadOnlyLicenseModule : ILicenseModule, 
    	IEquatable<ILicenseModule>
VB __Копировать
     Public NotInheritable Class ReadOnlyLicenseModule
    	Implements ILicenseModule, IEquatable(Of ILicenseModule)
C++ __Копировать
     public ref class ReadOnlyLicenseModule sealed : ILicenseModule, 
    	IEquatable<ILicenseModule^>
F# __Копировать
     [<SealedAttribute>]
    type ReadOnlyLicenseModule = 
        class
            interface ILicenseModule
            interface IEquatable<ILicenseModule>
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ ReadOnlyLicenseModule
Implements
    [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)<[ILicenseModule](T_Tessa_Platform_Licensing_ILicenseModule.htm)>, [ILicenseModule](T_Tessa_Platform_Licensing_ILicenseModule.htm)
##  __Конструкторы
[ReadOnlyLicenseModule](M_Tessa_Platform_Licensing_ReadOnlyLicenseModule__ctor.htm)|
Создаёт экземпляр класса с указанием исходного модуля лицензии, актуальные
свойства которого возвращаются текущим объектом.  
---|---  
## __Свойства
[Caption](P_Tessa_Platform_Licensing_ReadOnlyLicenseModule_Caption.htm)| Имя
модуля, отображаемое пользователю.  
---|---  
[ID](P_Tessa_Platform_Licensing_ReadOnlyLicenseModule_ID.htm)| Идентификатор
модуля.  
[Settings](P_Tessa_Platform_Licensing_ReadOnlyLicenseModule_Settings.htm)|
Сериализуемые настройки модуля.  
##  __Методы
[AsReadOnly](M_Tessa_Platform_Licensing_ReadOnlyLicenseModule_AsReadOnly.htm)|
Возвращает доступную только для чтения обёртку для текущего объекта.  
---|---  
[Equals(ILicenseModule)](M_Tessa_Platform_Licensing_ReadOnlyLicenseModule_Equals_1.htm)|
Сравнивает текущий объект с заданным.  
[Equals(Object)](M_Tessa_Platform_Licensing_ReadOnlyLicenseModule_Equals.htm)|
Сравнивает текущий объект с заданным.  
(Переопределяет
[Object.Equals(Object)](https://learn.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\)))  
[Finalize](https://learn.microsoft.com/dotnet/api/system.object.finalize#system-
object-finalize)| Allows an object to try to free resources and perform other
cleanup operations before it is reclaimed by garbage collection.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetHashCode](M_Tessa_Platform_Licensing_ReadOnlyLicenseModule_GetHashCode.htm)|
Возвращает хеш-код объекта.  
(Переопределяет
[Object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode#system-
object-gethashcode))  
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
[ToString](M_Tessa_Platform_Licensing_ReadOnlyLicenseModule_ToString.htm)|
Возвращает строковое представление объекта.  
(Переопределяет
[Object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring))  
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
[ToLicenseModule](M_Tessa_Platform_Licensing_LicensingExtensions_ToLicenseModule.htm)|
Преобразует тип объекта
[ILicenseModule](T_Tessa_Platform_Licensing_ILicenseModule.htm) в
[LicenseModule](T_Tessa_Platform_Licensing_LicenseModule.htm) или создаёт
новый объект [LicenseModule](T_Tessa_Platform_Licensing_LicenseModule.htm),
свойства которого получены из заданного объекта.  
(Определяется
[LicensingExtensions](T_Tessa_Platform_Licensing_LicensingExtensions.htm))  
##  __См. также
#### Ссылки
[Tessa.Platform.Licensing - пространство имён](N_Tessa_Platform_Licensing.htm)
