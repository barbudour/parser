# NullableObject<T> \- структура
Объект, который может быть в состоянии "недоступен", даже если значение равно
null. В этом случае свойство
[HasValue](P_Tessa_Platform_NullableObject_1_HasValue.htm) вернёт false.
## __Definition
 **Пространство имён:** [Tessa.Platform](N_Tessa_Platform.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public readonly struct NullableObject<T>
VB __Копировать
     Public Structure NullableObject(Of T)
C++ __Копировать
    generic<typename T>
    public value class NullableObject
F# __Копировать
     [<SealedAttribute>]
    type NullableObject<'T> = 
        struct
            inherit ValueType
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[ValueType](https://learn.microsoft.com/dotnet/api/system.valuetype) __ NullableObject<T>
#### Параметры типа
T
    Тип значения объекта.
##  __Конструкторы
[NullableObject<T>](M_Tessa_Platform_NullableObject_1__ctor.htm)|  Создаёт
экземпляр структуры с указанием заданного значения. Если требуется получить
объект без значения, используйте метод
[Null()](M_Tessa_Platform_NullableObject_1_Null.htm).  
---|---  
## __Свойства
[HasValue](P_Tessa_Platform_NullableObject_1_HasValue.htm)|  Признак того, что
значение объекта задано.  
---|---  
[Value](P_Tessa_Platform_NullableObject_1_Value.htm)|  Значение объекта. Имеет
смысл, если [HasValue](P_Tessa_Platform_NullableObject_1_HasValue.htm) равно
true.  
## __Методы
[Equals](https://learn.microsoft.com/dotnet/api/system.valuetype.equals#system-
valuetype-equals\(system-object\))| Indicates whether this instance and a
specified object are equal.  
(Унаследован от
[ValueType](https://learn.microsoft.com/dotnet/api/system.valuetype))  
---|---  
[Finalize](https://learn.microsoft.com/dotnet/api/system.object.finalize#system-
object-finalize)| Allows an object to try to free resources and perform other
cleanup operations before it is reclaimed by garbage collection.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetHashCode](https://learn.microsoft.com/dotnet/api/system.valuetype.gethashcode#system-
valuetype-gethashcode)| Returns the hash code for this instance.  
(Унаследован от
[ValueType](https://learn.microsoft.com/dotnet/api/system.valuetype))  
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
[Null](M_Tessa_Platform_NullableObject_1_Null.htm)|  Возвращает объект,
представляющий незаданное значение, у которого свойство
[HasValue](P_Tessa_Platform_NullableObject_1_HasValue.htm) равно false.  
[ToString](https://learn.microsoft.com/dotnet/api/system.valuetype.tostring#system-
valuetype-tostring)| Returns the fully qualified type name of this instance.  
(Унаследован от
[ValueType](https://learn.microsoft.com/dotnet/api/system.valuetype))  
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
[Tessa.Platform - пространство имён](N_Tessa_Platform.htm)
