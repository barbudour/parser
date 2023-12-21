# DeviceType - структура
Тип устройства, указанный в сессии.
## __Definition
 **Пространство имён:** [Tessa.Platform.Runtime](N_Tessa_Platform_Runtime.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public readonly struct DeviceType : IEquatable<DeviceType>
VB __Копировать
     Public Structure DeviceType
    	Implements IEquatable(Of DeviceType)
C++ __Копировать
     public value class DeviceType : IEquatable<DeviceType>
F# __Копировать
     [<SealedAttribute>]
    type DeviceType = 
        struct
            inherit ValueType
            interface IEquatable<DeviceType>
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[ValueType](https://learn.microsoft.com/dotnet/api/system.valuetype) __ DeviceType
Implements
    [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)<DeviceType>
##  __Конструкторы
[DeviceType](M_Tessa_Platform_Runtime_DeviceType__ctor.htm)|  Создаёт
экземпляр типа устройства с указанием его идентификатора.  
---|---  
## __Свойства
[ID](P_Tessa_Platform_Runtime_DeviceType_ID.htm)|  Идентификатор устройства.  
---|---  
## __Методы
[Equals(DeviceType)](M_Tessa_Platform_Runtime_DeviceType_Equals_1.htm)|
Сравнивает текущий объект с заданным.  
---|---  
[Equals(Object)](M_Tessa_Platform_Runtime_DeviceType_Equals.htm)| Сравнивает
текущий объект с заданным.  
(Переопределяет
[ValueType.Equals(Object)](https://learn.microsoft.com/dotnet/api/system.valuetype.equals#system-
valuetype-equals\(system-object\)))  
[Finalize](https://learn.microsoft.com/dotnet/api/system.object.finalize#system-
object-finalize)| Allows an object to try to free resources and perform other
cleanup operations before it is reclaimed by garbage collection.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetHashCode](M_Tessa_Platform_Runtime_DeviceType_GetHashCode.htm)| Возвращает
хеш-код объекта.  
(Переопределяет
[ValueType.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.valuetype.gethashcode#system-
valuetype-gethashcode))  
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
[ToString](M_Tessa_Platform_Runtime_DeviceType_ToString.htm)| Возвращает
строковое представление объекта.  
(Переопределяет
[ValueType.ToString()](https://learn.microsoft.com/dotnet/api/system.valuetype.tostring#system-
valuetype-tostring))  
##  __Операторы
[Equality(DeviceType,
DeviceType)](M_Tessa_Platform_Runtime_DeviceType_op_Equality.htm)| Сравнивает
заданные значения на равенство.  
---|---  
[Explicit(DeviceType to
Int32)](M_Tessa_Platform_Runtime_DeviceType_op_Explicit_1.htm)|  
[Explicit(Int32 to
DeviceType)](M_Tessa_Platform_Runtime_DeviceType_op_Explicit.htm)|  
[Inequality(DeviceType,
DeviceType)](M_Tessa_Platform_Runtime_DeviceType_op_Inequality.htm)|
Сравнивает заданные значения на неравенство.  
##  __Поля
[Desktop](F_Tessa_Platform_Runtime_DeviceType_Desktop.htm)|  Персональный
компьютер (в т.ч. ноутбук или нетбук).  
---|---  
[Other](F_Tessa_Platform_Runtime_DeviceType_Other.htm)|  Тип устройства
неизвестен.  
[Phone](F_Tessa_Platform_Runtime_DeviceType_Phone.htm)|  Смартфон (может
указываться для web-клиента).  
[Tablet](F_Tessa_Platform_Runtime_DeviceType_Tablet.htm)|  Планшет (может
указываться для web-клиента).  
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
[Tessa.Platform.Runtime - пространство имён](N_Tessa_Platform_Runtime.htm)
