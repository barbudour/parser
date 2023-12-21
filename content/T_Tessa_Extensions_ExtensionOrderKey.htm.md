# ExtensionOrderKey - структура
Ключ, используемый для упорядочивания расширений по этапам.
## __Definition
 **Пространство имён:** [Tessa.Extensions](N_Tessa_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public readonly struct ExtensionOrderKey : IComparable<ExtensionOrderKey>, 
    	IEquatable<ExtensionOrderKey>
VB __Копировать
     Public Structure ExtensionOrderKey
    	Implements IComparable(Of ExtensionOrderKey), IEquatable(Of ExtensionOrderKey)
C++ __Копировать
     public value class ExtensionOrderKey : IComparable<ExtensionOrderKey>, 
    	IEquatable<ExtensionOrderKey>
F# __Копировать
     [<SealedAttribute>]
    type ExtensionOrderKey = 
        struct
            inherit ValueType
            interface IComparable<ExtensionOrderKey>
            interface IEquatable<ExtensionOrderKey>
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[ValueType](https://learn.microsoft.com/dotnet/api/system.valuetype) __ ExtensionOrderKey
Implements
    [IComparable](https://learn.microsoft.com/dotnet/api/system.icomparable-1)<ExtensionOrderKey>, [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)<ExtensionOrderKey>
##  __Конструкторы
[ExtensionOrderKey](M_Tessa_Extensions_ExtensionOrderKey__ctor.htm)|  Создаёт
экземпляр типа значения с указанием этапа выполнения расширения в цепочке
расширений и порядка выполнения расширения внутри этапа.  
---|---  
## __Свойства
[Order](P_Tessa_Extensions_ExtensionOrderKey_Order.htm)|  Порядок выполнения
расширений внутри этапа. Расширения с меньшим значением порядка выполняются
раньше.  
---|---  
[Stage](P_Tessa_Extensions_ExtensionOrderKey_Stage.htm)|  Этап выполнения
расширения в цепочке расширений.  
## __Методы
[CompareTo](M_Tessa_Extensions_ExtensionOrderKey_CompareTo.htm)| Выполняет
сравнение текущего объекта с заданным.  
---|---  
[Equals(ExtensionOrderKey)](M_Tessa_Extensions_ExtensionOrderKey_Equals_1.htm)|
Сравнивает текущий объект с заданным.  
[Equals(Object)](M_Tessa_Extensions_ExtensionOrderKey_Equals.htm)| Сравнивает
текущий объект с заданным.  
(Переопределяет
[ValueType.Equals(Object)](https://learn.microsoft.com/dotnet/api/system.valuetype.equals#system-
valuetype-equals\(system-object\)))  
[Finalize](https://learn.microsoft.com/dotnet/api/system.object.finalize#system-
object-finalize)| Allows an object to try to free resources and perform other
cleanup operations before it is reclaimed by garbage collection.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetHashCode](M_Tessa_Extensions_ExtensionOrderKey_GetHashCode.htm)|
Возвращает хеш-код объекта.  
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
[ToString](M_Tessa_Extensions_ExtensionOrderKey_ToString.htm)| Возвращает
строковое представление объекта.  
(Переопределяет
[ValueType.ToString()](https://learn.microsoft.com/dotnet/api/system.valuetype.tostring#system-
valuetype-tostring))  
##  __Операторы
[Equality(ExtensionOrderKey,
ExtensionOrderKey)](M_Tessa_Extensions_ExtensionOrderKey_op_Equality.htm)|
Сравнивает заданные значения на равенство.  
---|---  
[GreaterThan(ExtensionOrderKey,
ExtensionOrderKey)](M_Tessa_Extensions_ExtensionOrderKey_op_GreaterThan.htm)|
Возвращает признак того, что первое сравниваемое значение больше второго.  
[GreaterThanOrEqual(ExtensionOrderKey,
ExtensionOrderKey)](M_Tessa_Extensions_ExtensionOrderKey_op_GreaterThanOrEqual.htm)|
Возвращает признак того, что первое сравниваемое значение больше либо равно
второму.  
[Inequality(ExtensionOrderKey,
ExtensionOrderKey)](M_Tessa_Extensions_ExtensionOrderKey_op_Inequality.htm)|
Сравнивает заданные значения на неравенство.  
[LessThan(ExtensionOrderKey,
ExtensionOrderKey)](M_Tessa_Extensions_ExtensionOrderKey_op_LessThan.htm)|
Возвращает признак того, что первое сравниваемое значение меньше второго.  
[LessThanOrEqual(ExtensionOrderKey,
ExtensionOrderKey)](M_Tessa_Extensions_ExtensionOrderKey_op_LessThanOrEqual.htm)|
Возвращает признак того, что первое сравниваемое значение меньше либо равно
второму.  
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
[Tessa.Extensions - пространство имён](N_Tessa_Extensions.htm)
