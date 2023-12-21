# CompilationResult - конструктор
Создаёт экземпляр класса с указанием значений его свойств. Объект после
создания является неизменяемым (immutable).
## __Definition
 **Пространство имён:** [Tessa.Compilation](N_Tessa_Compilation.htm)  
 **Сборка:** Tessa.Server (в Tessa.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public CompilationResult(
    	Guid assemblyID,
    	byte[] assemblyBytes = null,
    	string buildVersion = null,
    	DateTime? buildDate = null,
    	Assembly assembly = null,
    	ValidationResult result = null,
    	IList<ICompilerOutputItem> output = null,
    	string rawOutput = null,
    	int compilerReturnValue = 0,
    	Dictionary<string, Object> info = null
    )
VB __Копировать
     Public Sub New ( 
    	assemblyID As Guid,
    	Optional assemblyBytes As Byte() = Nothing,
    	Optional buildVersion As String = Nothing,
    	Optional buildDate As DateTime? = Nothing,
    	Optional assembly As Assembly = Nothing,
    	Optional result As ValidationResult = Nothing,
    	Optional output As IList(Of ICompilerOutputItem) = Nothing,
    	Optional rawOutput As String = Nothing,
    	Optional compilerReturnValue As Integer = 0,
    	Optional info As Dictionary(Of String, Object) = Nothing
    )
C++ __Копировать
     public:
    CompilationResult(
    	Guid assemblyID, 
    	array<unsigned char>^ assemblyBytes = nullptr, 
    	String^ buildVersion = nullptr, 
    	Nullable<DateTime> buildDate = nullptr, 
    	Assembly^ assembly = nullptr, 
    	ValidationResult^ result = nullptr, 
    	IList<ICompilerOutputItem^>^ output = nullptr, 
    	String^ rawOutput = nullptr, 
    	int compilerReturnValue = 0, 
    	Dictionary<String^, Object^>^ info = nullptr
    )
F# __Копировать
     new : 
            assemblyID : Guid * 
            ?assemblyBytes : byte[] * 
            ?buildVersion : string * 
            ?buildDate : Nullable<DateTime> * 
            ?assembly : Assembly * 
            ?result : ValidationResult * 
            ?output : IList<ICompilerOutputItem> * 
            ?rawOutput : string * 
            ?compilerReturnValue : int * 
            ?info : Dictionary<string, Object> 
    (* Defaults:
            let _assemblyBytes = defaultArg assemblyBytes null
            let _buildVersion = defaultArg buildVersion null
            let _buildDate = defaultArg buildDate null
            let _assembly = defaultArg assembly null
            let _result = defaultArg result null
            let _output = defaultArg output null
            let _rawOutput = defaultArg rawOutput null
            let _compilerReturnValue = defaultArg compilerReturnValue 0
            let _info = defaultArg info null
    *)
    -> CompilationResult
#### Параметры
assemblyID [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
     Идентификатор сборки из [Tessa.Platform.Compilers.ICompilationContext]. 
assemblyBytes [Byte](https://learn.microsoft.com/dotnet/api/system.byte)[]
(Optional)
     Массив байт, соответствующий сборке, или null, если массив байт не задан. Позволяет загрузить сборку посредством метода Assembly.Load(bytes). 
buildVersion [String](https://learn.microsoft.com/dotnet/api/system.string)
(Optional)
buildDate
[Nullable](https://learn.microsoft.com/dotnet/api/system.nullable-1)<[DateTime](https://learn.microsoft.com/dotnet/api/system.datetime)>
(Optional)
assembly
[Assembly](https://learn.microsoft.com/dotnet/api/system.reflection.assembly)
(Optional)
     Объект сборки [System.Reflection.Assembly]. 
result [ValidationResult](T_Tessa_Platform_Validation_ValidationResult.htm)
(Optional)
     Результат компиляции, указанный через [Tessa.Platform.Validation.ValidationResult]. 
output
[IList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ilist-1)<[ICompilerOutputItem](T_Tessa_Compilation_ICompilerOutputItem.htm)>
(Optional)
    Список строк вывода компилятора.
rawOutput [String](https://learn.microsoft.com/dotnet/api/system.string)
(Optional)
    Полный вывод компилятора в виде строки текста (аналогичен выводу на консоль при компиляции).
compilerReturnValue
[Int32](https://learn.microsoft.com/dotnet/api/system.int32) (Optional)
    Возвращаемое значение компилятора.
info
[Dictionary](https://learn.microsoft.com/dotnet/api/system.collections.generic.dictionary-2)<[String](https://learn.microsoft.com/dotnet/api/system.string),
[Object](https://learn.microsoft.com/dotnet/api/system.object)> (Optional)
    Дополнительная информация.
##  __См. также
#### Ссылки
[CompilationResult - ](T_Tessa_Compilation_CompilationResult.htm)
[Tessa.Compilation - пространство имён](N_Tessa_Compilation.htm)
