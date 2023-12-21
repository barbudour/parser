# ExtensionExecutionKey - структура
Ключ, используемый для идентификации выполняемого метода.
## __Definition
 **Пространство имён:** [Tessa.Extensions](N_Tessa_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public readonly struct ExtensionExecutionKey : IEquatable<ExtensionExecutionKey>
VB __Копировать
     Public Structure ExtensionExecutionKey
    	Implements IEquatable(Of ExtensionExecutionKey)
C++ __Копировать
     public value class ExtensionExecutionKey : IEquatable<ExtensionExecutionKey>
F# __Копировать
     [<SealedAttribute>]
    type ExtensionExecutionKey = 
        struct
            inherit ValueType
            interface IEquatable<ExtensionExecutionKey>
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[ValueType](https://learn.microsoft.com/dotnet/api/system.valuetype) __ ExtensionExecutionKey
Implements
    [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)<ExtensionExecutionKey>
##  __Конструкторы
[ExtensionExecutionKey](M_Tessa_Extensions_ExtensionExecutionKey__ctor.htm)|
Создаёт экземпляр типа значения с указанием имени выполняемого метода.  
---|---  
## __Свойства
[IsEmpty](P_Tessa_Extensions_ExtensionExecutionKey_IsEmpty.htm)|  Признак
того, что значение не содержит полезных данных.  
---|---  
[MethodName](P_Tessa_Extensions_ExtensionExecutionKey_MethodName.htm)|  Имя
выполняемого метода.  
## __Методы
[Equals(ExtensionExecutionKey)](M_Tessa_Extensions_ExtensionExecutionKey_Equals_1.htm)|
Сравнивает текущий объект с заданным.  
---|---  
[Equals(Object)](M_Tessa_Extensions_ExtensionExecutionKey_Equals.htm)|
Сравнивает текущий объект с заданным.  
(Переопределяет
[ValueType.Equals(Object)](https://learn.microsoft.com/dotnet/api/system.valuetype.equals#system-
valuetype-equals\(system-object\)))  
[Finalize](https://learn.microsoft.com/dotnet/api/system.object.finalize#system-
object-finalize)| Allows an object to try to free resources and perform other
cleanup operations before it is reclaimed by garbage collection.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetHashCode](M_Tessa_Extensions_ExtensionExecutionKey_GetHashCode.htm)|
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
[ToString](M_Tessa_Extensions_ExtensionExecutionKey_ToString.htm)| Возвращает
строковое представление объекта.  
(Переопределяет
[ValueType.ToString()](https://learn.microsoft.com/dotnet/api/system.valuetype.tostring#system-
valuetype-tostring))  
##  __Операторы
[Equality(ExtensionExecutionKey,
ExtensionExecutionKey)](M_Tessa_Extensions_ExtensionExecutionKey_op_Equality.htm)|
Сравнивает заданные значения на равенство.  
---|---  
[Inequality(ExtensionExecutionKey,
ExtensionExecutionKey)](M_Tessa_Extensions_ExtensionExecutionKey_op_Inequality.htm)|
Сравнивает заданные значения на неравенство.  
##  __Поля
[Empty](F_Tessa_Extensions_ExtensionExecutionKey_Empty.htm)|  Ключ, который не
содержит полезных данных.  
---|---  
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
[Tessa.Extensions - пространство имён](N_Tessa_Extensions.htm)
