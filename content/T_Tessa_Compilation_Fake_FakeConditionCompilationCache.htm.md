# FakeConditionCompilationCache - класс
Фейковая реализация для
[IConditionCompilationCache](T_Tessa_Platform_Conditions_IConditionCompilationCache.htm).
## __Definition
 **Пространство имён:** [Tessa.Compilation.Fake](N_Tessa_Compilation_Fake.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class FakeConditionCompilationCache : IConditionCompilationCache
VB __Копировать
     Public NotInheritable Class FakeConditionCompilationCache
    	Implements IConditionCompilationCache
C++ __Копировать
     public ref class FakeConditionCompilationCache sealed : IConditionCompilationCache
F# __Копировать
     [<SealedAttribute>]
    type FakeConditionCompilationCache = 
        class
            interface IConditionCompilationCache
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ FakeConditionCompilationCache
Implements
    [IConditionCompilationCache](T_Tessa_Platform_Conditions_IConditionCompilationCache.htm)
##  __Конструкторы
[FakeConditionCompilationCache](M_Tessa_Compilation_Fake_FakeConditionCompilationCache__ctor.htm)|
Инициализирует новый экземпляр класса FakeConditionCompilationCache  
---|---  
##  __Методы
[Equals](https://learn.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\))| Determines whether the specified object is
equal to the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
---|---  
[Finalize](https://learn.microsoft.com/dotnet/api/system.object.finalize#system-
object-finalize)| Allows an object to try to free resources and perform other
cleanup operations before it is reclaimed by garbage collection.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetAsync](M_Tessa_Compilation_Fake_FakeConditionCompilationCache_GetAsync.htm)|
Метод для получения результата компиляции из кеша. Если результата еще нет в
кеше, то произведется компиляция.  
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
[InvalidateAsync](M_Tessa_Compilation_Fake_FakeConditionCompilationCache_InvalidateAsync.htm)|
Сбрасывает кэш условий.  
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
[Tessa.Compilation.Fake - пространство имён](N_Tessa_Compilation_Fake.htm)
