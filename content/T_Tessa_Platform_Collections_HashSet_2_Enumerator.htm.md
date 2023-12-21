# HashSet<TKey, TValue>.Enumerator - структура
Реализация энумератора.
## __Definition
 **Пространство имён:**
[Tessa.Platform.Collections](N_Tessa_Platform_Collections.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public struct Enumerator : IEnumerator<TValue>, 
    	IEnumerator, IDisposable
VB __Копировать
     Public Structure Enumerator
    	Implements IEnumerator(Of TValue), IEnumerator, IDisposable
C++ __Копировать
     public value class Enumerator : IEnumerator<TValue>, 
    	IEnumerator, IDisposable
F# __Копировать
     [<SealedAttribute>]
    type Enumerator = 
        struct
            inherit ValueType
            interface IEnumerator<'TValue>
            interface IEnumerator
            interface IDisposable
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[ValueType](https://learn.microsoft.com/dotnet/api/system.valuetype) __ HashSet<TKey, TValue>.Enumerator
Implements
    [IEnumerator](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerator-1)<[TValue](T_Tessa_Platform_Collections_HashSet_2.htm)>, [IEnumerator](https://learn.microsoft.com/dotnet/api/system.collections.ienumerator), [IDisposable](https://learn.microsoft.com/dotnet/api/system.idisposable)
##  __Свойства
[Current](P_Tessa_Platform_Collections_HashSet_2_Enumerator_Current.htm)| Gets
the element in the collection at the current position of the enumerator.  
---|---  
##  __Методы
[Dispose](M_Tessa_Platform_Collections_HashSet_2_Enumerator_Dispose.htm)|
Performs application-defined tasks associated with freeing, releasing, or
resetting unmanaged resources.  
---|---  
[Equals](https://learn.microsoft.com/dotnet/api/system.valuetype.equals#system-
valuetype-equals\(system-object\))| Indicates whether this instance and a
specified object are equal.  
(Унаследован от
[ValueType](https://learn.microsoft.com/dotnet/api/system.valuetype))  
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
[MoveNext](M_Tessa_Platform_Collections_HashSet_2_Enumerator_MoveNext.htm)|
Advances the enumerator to the next element of the collection.  
[Reset](M_Tessa_Platform_Collections_HashSet_2_Enumerator_Reset.htm)| Sets the
enumerator to its initial position, which is before the first element in the
collection.  
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
[Tessa.Platform.Collections - пространство
имён](N_Tessa_Platform_Collections.htm)
