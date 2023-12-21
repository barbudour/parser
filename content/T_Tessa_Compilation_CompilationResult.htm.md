# CompilationResult - класс
Результат компиляции.
## __Definition
 **Пространство имён:** [Tessa.Compilation](N_Tessa_Compilation.htm)  
 **Сборка:** Tessa.Server (в Tessa.Server.dll) Версия: 3.6.0.17
C# __Копировать
    [SerializableAttribute]
    public sealed class CompilationResult : ICompilationResult
VB __Копировать
    <SerializableAttribute>
    Public NotInheritable Class CompilationResult
    	Implements ICompilationResult
C++ __Копировать
    [SerializableAttribute]
    public ref class CompilationResult sealed : ICompilationResult
F# __Копировать
     [<SealedAttribute>]
    [<SerializableAttribute>]
    type CompilationResult = 
        class
            interface ICompilationResult
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ CompilationResult
Implements
    [ICompilationResult](T_Tessa_Compilation_ICompilationResult.htm)
##  __Конструкторы
[CompilationResult](M_Tessa_Compilation_CompilationResult__ctor.htm)|  Создаёт
экземпляр класса с указанием значений его свойств. Объект после создания
является неизменяемым (immutable).  
---|---  
## __Свойства
[Assembly](P_Tessa_Compilation_CompilationResult_Assembly.htm)|  Исполняемая
сборка, результат компиляции. В случае неудачной компиляции равно null  
---|---  
[AssemblyBytes](P_Tessa_Compilation_CompilationResult_AssemblyBytes.htm)|  
[AssemblyID](P_Tessa_Compilation_CompilationResult_AssemblyID.htm)|
Уникальный идентификатор сборки  
[BuildDate](P_Tessa_Compilation_CompilationResult_BuildDate.htm)|  Дата сборки
версии платформы, при которой выполнялась компиляция  
[BuildVersion](P_Tessa_Compilation_CompilationResult_BuildVersion.htm)|
Версия платформы, при которой выполнялась компиляция  
[CompilationDateTime](P_Tessa_Compilation_CompilationResult_CompilationDateTime.htm)|
Дата/время сборки  
[CompilerOutput](P_Tessa_Compilation_CompilationResult_CompilerOutput.htm)|
Вывод компилятора  
[CompilerReturnValue](P_Tessa_Compilation_CompilationResult_CompilerReturnValue.htm)|
Возвращаемое значение процесса компилятора  
[Info](P_Tessa_Compilation_CompilationResult_Info.htm)|  Дополнительная
информация  
[RawOutput](P_Tessa_Compilation_CompilationResult_RawOutput.htm)|
Неформатированный вывод компилятора  
[ValidationResult](P_Tessa_Compilation_CompilationResult_ValidationResult.htm)|
Ошибки и предупреждения выполненной сборки  
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
[Resolve<T>](M_Tessa_Compilation_CompilationExtensions_Resolve__1.htm)|  Найти
в результате сборки тип, реализующий интерфейс T и создать его экземпляр В
случае отсутствия хотя бы одного типа в сборке будет выброшено
System.InvalidOperationException  
(Определяется
[CompilationExtensions](T_Tessa_Compilation_CompilationExtensions.htm))  
[ResolveAll<T>](M_Tessa_Compilation_CompilationExtensions_ResolveAll__1.htm)|
Найти в результате сборки все типы, реализующие интерфейс T и создать их
экземпляры  
(Определяется
[CompilationExtensions](T_Tessa_Compilation_CompilationExtensions.htm))  
[Set](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Set.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
##  __См. также
#### Ссылки
[Tessa.Compilation - пространство имён](N_Tessa_Compilation.htm)
