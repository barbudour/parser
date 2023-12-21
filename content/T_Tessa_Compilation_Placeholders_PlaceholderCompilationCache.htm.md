# PlaceholderCompilationCache - класс
Кеш результатов компиляции текстов с плейсхолдерами и скриптами
## __Definition
 **Пространство имён:**
[Tessa.Compilation.Placeholders](N_Tessa_Compilation_Placeholders.htm)  
 **Сборка:** Tessa.Server (в Tessa.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class PlaceholderCompilationCache : IPlaceholderCompilationCache
VB __Копировать
     Public NotInheritable Class PlaceholderCompilationCache
    	Implements IPlaceholderCompilationCache
C++ __Копировать
     public ref class PlaceholderCompilationCache sealed : IPlaceholderCompilationCache
F# __Копировать
     [<SealedAttribute>]
    type PlaceholderCompilationCache = 
        class
            interface IPlaceholderCompilationCache
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ PlaceholderCompilationCache
Implements
    [IPlaceholderCompilationCache](T_Tessa_Platform_Placeholders_Compilation_IPlaceholderCompilationCache.htm)
##  __Конструкторы
[PlaceholderCompilationCache](M_Tessa_Compilation_Placeholders_PlaceholderCompilationCache__ctor.htm)|
Инициализирует новый экземпляр класса PlaceholderCompilationCache  
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
[GetAsync](M_Tessa_Compilation_Placeholders_PlaceholderCompilationCache_GetAsync.htm)|
Метод для получения результата компиляции текста с плейсхолдерами из кеша по
его ID  
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
[InvalidateAsync](M_Tessa_Compilation_Placeholders_PlaceholderCompilationCache_InvalidateAsync.htm)|
Производит удаление результата компиляции из кеша по его ID  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[StoreAsync](M_Tessa_Compilation_Placeholders_PlaceholderCompilationCache_StoreAsync.htm)|
Производит сохранение результата компиляции в кеше с его ID  
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
[Tessa.Compilation.Placeholders - пространство
имён](N_Tessa_Compilation_Placeholders.htm)
