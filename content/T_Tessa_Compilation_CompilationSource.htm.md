# CompilationSource - класс
Инкапсуляция элемента компиляции.
## __Definition
 **Пространство имён:** [Tessa.Compilation](N_Tessa_Compilation.htm)  
 **Сборка:** Tessa.Server (в Tessa.Server.dll) Версия: 3.6.0.17
C# __Копировать
    [SerializableAttribute]
    public sealed class CompilationSource : ICompilationSource
VB __Копировать
    <SerializableAttribute>
    Public NotInheritable Class CompilationSource
    	Implements ICompilationSource
C++ __Копировать
    [SerializableAttribute]
    public ref class CompilationSource sealed : ICompilationSource
F# __Копировать
     [<SealedAttribute>]
    [<SerializableAttribute>]
    type CompilationSource = 
        class
            interface ICompilationSource
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ CompilationSource
Implements
    [ICompilationSource](T_Tessa_Compilation_ICompilationSource.htm)
##  __Конструкторы
[CompilationSource(String, CompilationUnitSyntax,
IEnumerable<String>)](M_Tessa_Compilation_CompilationSource__ctor_1.htm)|
Создаёт экземпляр класса с указанными параметрами.  
---|---  
[CompilationSource(Guid, String, CompilationUnitSyntax,
IEnumerable<String>)](M_Tessa_Compilation_CompilationSource__ctor.htm)|
Создаёт экземпляр класса с указанными параметрами.  
## __Свойства
[CompilationUnit](P_Tessa_Compilation_CompilationSource_CompilationUnit.htm)|
Исходный код  
---|---  
[ID](P_Tessa_Compilation_CompilationSource_ID.htm)|  Идентификатор исходного
кода. Устанавливается в объекте и прописывается комментарием в исходном коде
для установления соответствия.  
[Name](P_Tessa_Compilation_CompilationSource_Name.htm)|  Имя  
[RequiredReferences](P_Tessa_Compilation_CompilationSource_RequiredReferences.htm)|
Требуемые референсы  
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
[AppendUsings](M_Tessa_Compilation_CompilationSourceExtensions_AppendUsings.htm)|  
(Определяется
[CompilationSourceExtensions](T_Tessa_Compilation_CompilationSourceExtensions.htm))  
---|---  
[Get](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Get.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
[InternalMarkerCanvas](M_Tessa_UI_Views_Charting_Annotations_AnnotationInternalsAccessor_InternalMarkerCanvas.htm)|
Возвращает маркер аннотации  
(Определяется
[AnnotationInternalsAccessor](T_Tessa_UI_Views_Charting_Annotations_AnnotationInternalsAccessor.htm))  
[Invoke](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Invoke.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
[Normalize](M_Tessa_Compilation_CompilationSourceExtensions_Normalize.htm)|  
(Определяется
[CompilationSourceExtensions](T_Tessa_Compilation_CompilationSourceExtensions.htm))  
[Set](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Set.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
[SetSourceID](M_Tessa_Compilation_CompilationSourceExtensions_SetSourceID.htm)|  
(Определяется
[CompilationSourceExtensions](T_Tessa_Compilation_CompilationSourceExtensions.htm))  
[WithCompilationUnit](M_Tessa_Compilation_CompilationSourceExtensions_WithCompilationUnit.htm)|  
(Определяется
[CompilationSourceExtensions](T_Tessa_Compilation_CompilationSourceExtensions.htm))  
##  __См. также
#### Ссылки
[Tessa.Compilation - пространство имён](N_Tessa_Compilation.htm)
