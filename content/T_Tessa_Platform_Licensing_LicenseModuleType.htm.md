# LicenseModuleType - класс
Информация, описывающая модуль лицензии
[ILicenseModule](T_Tessa_Platform_Licensing_ILicenseModule.htm), т.е.
дополнительную подключаемую функциональность платформы.
## __Definition
 **Пространство имён:**
[Tessa.Platform.Licensing](N_Tessa_Platform_Licensing.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
    [SerializableAttribute]
    public sealed class LicenseModuleType : ICloneable, 
    	IEquatable<LicenseModuleType>
VB __Копировать
    <SerializableAttribute>
    Public NotInheritable Class LicenseModuleType
    	Implements ICloneable, IEquatable(Of LicenseModuleType)
C++ __Копировать
    [SerializableAttribute]
    public ref class LicenseModuleType sealed : ICloneable, 
    	IEquatable<LicenseModuleType^>
F# __Копировать
     [<SealedAttribute>]
    [<SerializableAttribute>]
    type LicenseModuleType = 
        class
            interface ICloneable
            interface IEquatable<LicenseModuleType>
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ LicenseModuleType
Implements
    [ICloneable](https://learn.microsoft.com/dotnet/api/system.icloneable), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)<LicenseModuleType>
##  __Конструкторы
[LicenseModuleType](M_Tessa_Platform_Licensing_LicenseModuleType__ctor.htm)|
Инициализирует новый экземпляр класса LicenseModuleType  
---|---  
##  __Свойства
[Caption](P_Tessa_Platform_Licensing_LicenseModuleType_Caption.htm)|
Отображаемое пользователю имя создаваемого модуля.  
---|---  
[Enterprise](P_Tessa_Platform_Licensing_LicenseModuleType_Enterprise.htm)|
Признак того, что модуль входит в корпоративную лицензию. По умолчанию равен
true.  
[ID](P_Tessa_Platform_Licensing_LicenseModuleType_ID.htm)|  Идентификатор
создаваемого модуля.  
[Settings](P_Tessa_Platform_Licensing_LicenseModuleType_Settings.htm)|
Информация по настройкам модуля, описывающая, каким образом модуль будет
отредактирован.  
## __Методы
[Clone](M_Tessa_Platform_Licensing_LicenseModuleType_Clone.htm)| Создаёт
полную копию объекта.  
---|---  
[Equals(LicenseModuleType)](M_Tessa_Platform_Licensing_LicenseModuleType_Equals_1.htm)|
Сравнивает текущий объект с заданным.  
[Equals(Object)](M_Tessa_Platform_Licensing_LicenseModuleType_Equals.htm)|
Сравнивает текущий объект с заданным.  
(Переопределяет
[Object.Equals(Object)](https://learn.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\)))  
[Finalize](https://learn.microsoft.com/dotnet/api/system.object.finalize#system-
object-finalize)| Allows an object to try to free resources and perform other
cleanup operations before it is reclaimed by garbage collection.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetHashCode](M_Tessa_Platform_Licensing_LicenseModuleType_GetHashCode.htm)|
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
[Repair](M_Tessa_Platform_Licensing_LicenseModuleType_Repair.htm)|  Исправляет
объект и его дочерние объекты. Рекомендуется использовать перед сериализацией.  
[ToString](M_Tessa_Platform_Licensing_LicenseModuleType_ToString.htm)|
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
##  __См. также
#### Ссылки
[Tessa.Platform.Licensing - пространство имён](N_Tessa_Platform_Licensing.htm)
