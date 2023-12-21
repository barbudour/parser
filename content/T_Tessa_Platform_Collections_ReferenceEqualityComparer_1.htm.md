# ReferenceEqualityComparer<T> \- класс
Сравнивает объекты на равенство ссылок. Методы [Equals(T,
T)](M_Tessa_Platform_Collections_ReferenceEqualityComparer_1_Equals.htm) и
[GetHashCode(T)](M_Tessa_Platform_Collections_ReferenceEqualityComparer_1_GetHashCode.htm)
компаратора игнорируют любые определённые в объектах способы сравнения и
вычисления хеш-кода.
## __Definition
 **Пространство имён:**
[Tessa.Platform.Collections](N_Tessa_Platform_Collections.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class ReferenceEqualityComparer<T> : IEqualityComparer<T>
    where T : class
VB __Копировать
     Public NotInheritable Class ReferenceEqualityComparer(Of T As Class)
    	Implements IEqualityComparer(Of T)
C++ __Копировать
    generic<typename T>
    where T : ref class
    public ref class ReferenceEqualityComparer sealed : IEqualityComparer<T>
F# __Копировать
     [<SealedAttribute>]
    type ReferenceEqualityComparer<'T when 'T : not struct> = 
        class
            interface IEqualityComparer<'T>
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ ReferenceEqualityComparer<T>
Implements
    [IEqualityComparer](https://learn.microsoft.com/dotnet/api/system.collections.generic.iequalitycomparer-1)<T>
#### Параметры типа
T
    Ссылочный тип сравниваемых объектов.
##  __Конструкторы
[ReferenceEqualityComparer<T>](M_Tessa_Platform_Collections_ReferenceEqualityComparer_1__ctor.htm)|
Инициализирует новый экземпляр класса ReferenceEqualityComparer<T>  
---|---  
##  __Свойства
[Instance](P_Tessa_Platform_Collections_ReferenceEqualityComparer_1_Instance.htm)|
Экземпляр класса.  
---|---  
##  __Методы
[Equals(Object)](https://learn.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\))| Determines whether the specified object is
equal to the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
---|---  
[Equals(T,
T)](M_Tessa_Platform_Collections_ReferenceEqualityComparer_1_Equals.htm)|
Сравнивает объекты на равенство ссылок.  
[Finalize](https://learn.microsoft.com/dotnet/api/system.object.finalize#system-
object-finalize)| Allows an object to try to free resources and perform other
cleanup operations before it is reclaimed by garbage collection.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode#system-
object-gethashcode)| Serves as the default hash function.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetHashCode(T)](M_Tessa_Platform_Collections_ReferenceEqualityComparer_1_GetHashCode.htm)|
Возвращает хеш-код объекта.  
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
