# CompilationContext - класс
Контекст сеанса компиляции для компилятора
## __Definition
 **Пространство имён:** [Tessa.Compilation](N_Tessa_Compilation.htm)  
 **Сборка:** Tessa.Server (в Tessa.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public class CompilationContext : ICompilationContext
VB __Копировать
     Public Class CompilationContext
    	Implements ICompilationContext
C++ __Копировать
     public ref class CompilationContext : ICompilationContext
F# __Копировать
     type CompilationContext = 
        class
            interface ICompilationContext
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ CompilationContext
Implements
    [ICompilationContext](T_Tessa_Compilation_ICompilationContext.htm)
##  __Конструкторы
[CompilationContext](M_Tessa_Compilation_CompilationContext__ctor.htm)|
Создаёт экземпляр класса с параметрами по умолчанию.  
---|---  
##  __Свойства
[AssemblyID](P_Tessa_Compilation_CompilationContext_AssemblyID.htm)|
Уникальный идентификатор сеанса сборки  
---|---  
[DefaultUsings](P_Tessa_Compilation_CompilationContext_DefaultUsings.htm)|
Пространства имен, добавляемые к каждому исходнику в Sources  
[GenerateFile](P_Tessa_Compilation_CompilationContext_GenerateFile.htm)|  
[IgnoreWarnings](P_Tessa_Compilation_CompilationContext_IgnoreWarnings.htm)|  
[References](P_Tessa_Compilation_CompilationContext_References.htm)|  Внешние
зависимости. Необходимо указывать имена .dll файлов Пример: Tessa.dll,
System.dll и тд  
[Sources](P_Tessa_Compilation_CompilationContext_Sources.htm)|  Исходные коды  
## __Методы
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
[Tessa.Compilation - пространство имён](N_Tessa_Compilation.htm)