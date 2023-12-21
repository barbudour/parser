# PlaceholderCompilationStorage - класс
Объект, который производит сохранение, получение и удаление кешей сборок из
базы
## __Definition
 **Пространство имён:**
[Tessa.Compilation.Placeholders](N_Tessa_Compilation_Placeholders.htm)  
 **Сборка:** Tessa.Server (в Tessa.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class PlaceholderCompilationStorage : IPlaceholderCompilationStorage
VB __Копировать
     Public NotInheritable Class PlaceholderCompilationStorage
    	Implements IPlaceholderCompilationStorage
C++ __Копировать
     public ref class PlaceholderCompilationStorage sealed : IPlaceholderCompilationStorage
F# __Копировать
     [<SealedAttribute>]
    type PlaceholderCompilationStorage = 
        class
            interface IPlaceholderCompilationStorage
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ PlaceholderCompilationStorage
Implements
    [IPlaceholderCompilationStorage](T_Tessa_Platform_Placeholders_Compilation_IPlaceholderCompilationStorage.htm)
##  __Конструкторы
[PlaceholderCompilationStorage](M_Tessa_Compilation_Placeholders_PlaceholderCompilationStorage__ctor.htm)|
Инициализирует новый экземпляр класса PlaceholderCompilationStorage  
---|---  
##  __Методы
[CheckIsActualAsync](M_Tessa_Compilation_Placeholders_PlaceholderCompilationStorage_CheckIsActualAsync.htm)|
Метод для првоерки актуальности данных в кеше  
---|---  
[DeleteAsync](M_Tessa_Compilation_Placeholders_PlaceholderCompilationStorage_DeleteAsync.htm)|
Удаление объекта с информацией о результате компиляции по его идентификатору  
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
[GetAsync<T>](M_Tessa_Compilation_Placeholders_PlaceholderCompilationStorage_GetAsync__1.htm)|
Получение объекта с информацией о результате компиляции из базы  
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
[StoreAsync<T>](M_Tessa_Compilation_Placeholders_PlaceholderCompilationStorage_StoreAsync__1.htm)|
Сохранение объекта с информацией о результате компиляции в базе  
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
