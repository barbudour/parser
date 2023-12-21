# ConditionCompilationCache - класс
Кеш компиляции типов условий
## __Definition
 **Пространство имён:**
[Tessa.Compilation.Conditions](N_Tessa_Compilation_Conditions.htm)  
 **Сборка:** Tessa.Server (в Tessa.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class ConditionCompilationCache : IConditionCompilationCache, 
    	IDisposable
VB __Копировать
     Public NotInheritable Class ConditionCompilationCache
    	Implements IConditionCompilationCache, IDisposable
C++ __Копировать
     public ref class ConditionCompilationCache sealed : IConditionCompilationCache, 
    	IDisposable
F# __Копировать
     [<SealedAttribute>]
    type ConditionCompilationCache = 
        class
            interface IConditionCompilationCache
            interface IDisposable
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ ConditionCompilationCache
Implements
    [IDisposable](https://learn.microsoft.com/dotnet/api/system.idisposable), [IConditionCompilationCache](T_Tessa_Platform_Conditions_IConditionCompilationCache.htm)
##  __Конструкторы
[ConditionCompilationCache](M_Tessa_Compilation_Conditions_ConditionCompilationCache__ctor.htm)|
Инициализирует новый экземпляр класса ConditionCompilationCache  
---|---  
##  __Методы
[Dispose](M_Tessa_Compilation_Conditions_ConditionCompilationCache_Dispose.htm)|
Освобождает все ресурсы, используемые объектом ConditionCompilationCache  
---|---  
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
[GetAsync](M_Tessa_Compilation_Conditions_ConditionCompilationCache_GetAsync.htm)|
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
[InvalidateAsync](M_Tessa_Compilation_Conditions_ConditionCompilationCache_InvalidateAsync.htm)|
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
[Tessa.Compilation.Conditions - пространство
имён](N_Tessa_Compilation_Conditions.htm)
