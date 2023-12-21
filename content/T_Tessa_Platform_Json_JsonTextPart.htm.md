# JsonTextPart - структура
Контейнер для сериализации/десериализации в JSON, позволяющий разбить
multiline строку на 2 части \-
[Alias](P_Tessa_Platform_Json_JsonTextPart_Alias.htm), который запишется в
значение по ключу, и Content, который должен быть дописан после конца JSON
(после закрывающей скобки).
Для корректного использования при сериализации/десериализации с помощью
[TypedJsonConverter](T_Tessa_Platform_Json_TypedJsonConverter.htm) нужно
создать область операции для контекста
[ITessaJsonSerializationContext](T_Tessa_Platform_Json_ITessaJsonSerializationContext.htm),
в который будут помещены все найденные JsonTextPart.
Запись происходит в формате:  
[TEXTPART Alias]  
Content
##  __Definition
 **Пространство имён:** [Tessa.Platform.Json](N_Tessa_Platform_Json.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public readonly struct JsonTextPart : IEquatable<JsonTextPart>
VB __Копировать
     Public Structure JsonTextPart
    	Implements IEquatable(Of JsonTextPart)
C++ __Копировать
     public value class JsonTextPart : IEquatable<JsonTextPart>
F# __Копировать
     [<SealedAttribute>]
    type JsonTextPart = 
        struct
            inherit ValueType
            interface IEquatable<JsonTextPart>
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[ValueType](https://learn.microsoft.com/dotnet/api/system.valuetype) __ JsonTextPart
Implements
    [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)<JsonTextPart>
##  __Конструкторы
[JsonTextPart](M_Tessa_Platform_Json_JsonTextPart__ctor.htm)|  Создаёт
экземпляр структуры с указанием значений её свойств.  
---|---  
## __Свойства
[Alias](P_Tessa_Platform_Json_JsonTextPart_Alias.htm)|  Алиас textpart, будет
записан в хранилище по ключу.  
---|---  
[Content](P_Tessa_Platform_Json_JsonTextPart_Content.htm)|  Содержимое
textpart, должно быть дописано после окончания блока JSON с сохранением
форматирования.  
## __Методы
[Equals(JsonTextPart)](M_Tessa_Platform_Json_JsonTextPart_Equals_1.htm)|
Indicates whether the current object is equal to another object of the same
type.  
---|---  
[Equals(Object)](M_Tessa_Platform_Json_JsonTextPart_Equals.htm)| Indicates
whether this instance and a specified object are equal.  
(Переопределяет
[ValueType.Equals(Object)](https://learn.microsoft.com/dotnet/api/system.valuetype.equals#system-
valuetype-equals\(system-object\)))  
[Finalize](https://learn.microsoft.com/dotnet/api/system.object.finalize#system-
object-finalize)| Allows an object to try to free resources and perform other
cleanup operations before it is reclaimed by garbage collection.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetHashCode](M_Tessa_Platform_Json_JsonTextPart_GetHashCode.htm)| Returns the
hash code for this instance.  
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
[ToString](M_Tessa_Platform_Json_JsonTextPart_ToString.htm)| Returns the fully
qualified type name of this instance.  
(Переопределяет
[ValueType.ToString()](https://learn.microsoft.com/dotnet/api/system.valuetype.tostring#system-
valuetype-tostring))  
##  __Операторы
[Equality(JsonTextPart,
JsonTextPart)](M_Tessa_Platform_Json_JsonTextPart_op_Equality.htm)|  
---|---  
[Implicit(JsonTextPart to
String)](M_Tessa_Platform_Json_JsonTextPart_op_Implicit.htm)|  
[Inequality(JsonTextPart,
JsonTextPart)](M_Tessa_Platform_Json_JsonTextPart_op_Inequality.htm)|  
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
[Tessa.Platform.Json - пространство имён](N_Tessa_Platform_Json.htm)
