# PlaceholderCompilationResult - класс
Результат компиляции текста с плейсхолдерами
## __Definition
 **Пространство имён:**
[Tessa.Compilation.Placeholders](N_Tessa_Compilation_Placeholders.htm)  
 **Сборка:** Tessa.Server (в Tessa.Server.dll) Версия: 3.6.0.17
C# __Копировать
    [SerializableAttribute]
    public sealed class PlaceholderCompilationResult : IPlaceholderCompilationResult
VB __Копировать
    <SerializableAttribute>
    Public NotInheritable Class PlaceholderCompilationResult
    	Implements IPlaceholderCompilationResult
C++ __Копировать
    [SerializableAttribute]
    public ref class PlaceholderCompilationResult sealed : IPlaceholderCompilationResult
F# __Копировать
     [<SealedAttribute>]
    [<SerializableAttribute>]
    type PlaceholderCompilationResult = 
        class
            interface IPlaceholderCompilationResult
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ PlaceholderCompilationResult
Implements
    [IPlaceholderCompilationResult](T_Tessa_Platform_Placeholders_Compilation_IPlaceholderCompilationResult.htm)
##  __Конструкторы
[PlaceholderCompilationResult](M_Tessa_Compilation_Placeholders_PlaceholderCompilationResult__ctor.htm)|
Инициализирует новый экземпляр класса PlaceholderCompilationResult  
---|---  
##  __Свойства
[AssemblyBytes](P_Tessa_Compilation_Placeholders_PlaceholderCompilationResult_AssemblyBytes.htm)|
Массив байт сборки. Генерируется, если при компиляции была задана генерация
файла сборки.  
---|---  
[Created](P_Tessa_Compilation_Placeholders_PlaceholderCompilationResult_Created.htm)|
Дата создания результата компиляции  
[IsValid](P_Tessa_Compilation_Placeholders_PlaceholderCompilationResult_IsValid.htm)|
Определяет, является ли результат компиляции валидным  
[ValidationResult](P_Tessa_Compilation_Placeholders_PlaceholderCompilationResult_ValidationResult.htm)|
Результат валидации компиляции  
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
[GetPlaceholderScript](M_Tessa_Compilation_Placeholders_PlaceholderCompilationResult_GetPlaceholderScript.htm)|
Метод для получения объекта скрипта из результата компиляции  
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
[Tessa.Compilation.Placeholders - пространство
имён](N_Tessa_Compilation_Placeholders.htm)
