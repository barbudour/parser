# DefaultTypeReflectionSerializer - класс
Объект, выполняющий сериализацию в
[SerializationInfo](https://learn.microsoft.com/dotnet/api/system.runtime.serialization.serializationinfo)
для объекта заданного типа. Сериализация производится посредством рефлексии.
## __Definition
 **Пространство имён:**
[Tessa.Platform.Reflection](N_Tessa_Platform_Reflection.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class DefaultTypeReflectionSerializer
VB __Копировать
     Public NotInheritable Class DefaultTypeReflectionSerializer
C++ __Копировать
     public ref class DefaultTypeReflectionSerializer sealed
F# __Копировать
     [<SealedAttribute>]
    type DefaultTypeReflectionSerializer = class end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ DefaultTypeReflectionSerializer
##  __Конструкторы
[DefaultTypeReflectionSerializer](M_Tessa_Platform_Reflection_DefaultTypeReflectionSerializer__ctor.htm)|
Создаёт экземпляр класса с указанием типа и правил сериализации.  
---|---  
## __Методы
[CreateLazy<T>](M_Tessa_Platform_Reflection_DefaultTypeReflectionSerializer_CreateLazy__1.htm)|
Создаёт объект с ленивой инициализацией для указанного типа и заданных
настроек. Результат может быть записан в статическое поле и безопасно
использован из разных потоков для разных экземпляров.  
---|---  
[Deserialize](M_Tessa_Platform_Reflection_DefaultTypeReflectionSerializer_Deserialize.htm)|
Десериализует заданный экземпляр по правилам текущего объекта.  
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
[Serialize](M_Tessa_Platform_Reflection_DefaultTypeReflectionSerializer_Serialize.htm)|
Сериализует заданный экземпляр по правилам текущего объекта.  
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
[Tessa.Platform.Reflection - пространство
имён](N_Tessa_Platform_Reflection.htm)
