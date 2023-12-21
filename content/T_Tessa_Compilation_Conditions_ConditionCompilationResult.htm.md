# ConditionCompilationResult - класс
Результат компиляции типов условий
## __Definition
 **Пространство имён:**
[Tessa.Compilation.Conditions](N_Tessa_Compilation_Conditions.htm)  
 **Сборка:** Tessa.Server (в Tessa.Server.dll) Версия: 3.6.0.17
C# __Копировать
    [SerializableAttribute]
    public sealed class ConditionCompilationResult : IConditionCompilationResult
VB __Копировать
    <SerializableAttribute>
    Public NotInheritable Class ConditionCompilationResult
    	Implements IConditionCompilationResult
C++ __Копировать
    [SerializableAttribute]
    public ref class ConditionCompilationResult sealed : IConditionCompilationResult
F# __Копировать
     [<SealedAttribute>]
    [<SerializableAttribute>]
    type ConditionCompilationResult = 
        class
            interface IConditionCompilationResult
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ ConditionCompilationResult
Implements
    [IConditionCompilationResult](T_Tessa_Platform_Conditions_IConditionCompilationResult.htm)
##  __Конструкторы
[ConditionCompilationResult(Byte[])](M_Tessa_Compilation_Conditions_ConditionCompilationResult__ctor.htm)|
Инициализирует новый экземпляр класса ConditionCompilationResult  
---|---  
[ConditionCompilationResult(ICompilationResult,
ValidationResult)](M_Tessa_Compilation_Conditions_ConditionCompilationResult__ctor_1.htm)|
Инициализирует новый экземпляр класса ConditionCompilationResult  
##  __Свойства
[AssemblyBytes](P_Tessa_Compilation_Conditions_ConditionCompilationResult_AssemblyBytes.htm)|
Массив байт сборки. Генерируется, если при компиляции была задана генерация
файла сборки.  
---|---  
[BuildDate](P_Tessa_Compilation_Conditions_ConditionCompilationResult_BuildDate.htm)|  
[BuildVersion](P_Tessa_Compilation_Conditions_ConditionCompilationResult_BuildVersion.htm)|  
[Conditions](P_Tessa_Compilation_Conditions_ConditionCompilationResult_Conditions.htm)|
Набор скомпилированных условий  
[ValidationResult](P_Tessa_Compilation_Conditions_ConditionCompilationResult_ValidationResult.htm)|
Результат валидации компиляции  
## __Методы
[CheckVersion](M_Tessa_Compilation_Conditions_ConditionCompilationResult_CheckVersion.htm)|
Метод для проверки версии результата процесса  
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
[Tessa.Compilation.Conditions - пространство
имён](N_Tessa_Compilation_Conditions.htm)
