# FileConverterFormat.RegisterExtensions - метод
Регистрирует информацию по входным расширениям для заданного формата выходного
файла. Если заданы null или пустые массивы для обоих параметров, то
конвертация будет допустима для любых входных файлов.
## __Definition
 **Пространство имён:** [Tessa.FileConverters](N_Tessa_FileConverters.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static void RegisterExtensions(
    	FileConverterFormat outputFormat,
    	string outputExtension,
    	IEnumerable<string> recommendedInputExtensions = null,
    	IEnumerable<string> additionalInputExtensions = null
    )
VB __Копировать
     Public Shared Sub RegisterExtensions ( 
    	outputFormat As FileConverterFormat,
    	outputExtension As String,
    	Optional recommendedInputExtensions As IEnumerable(Of String) = Nothing,
    	Optional additionalInputExtensions As IEnumerable(Of String) = Nothing
    )
C++ __Копировать
     public:
    static void RegisterExtensions(
    	FileConverterFormat outputFormat, 
    	String^ outputExtension, 
    	IEnumerable<String^>^ recommendedInputExtensions = nullptr, 
    	IEnumerable<String^>^ additionalInputExtensions = nullptr
    )
F# __Копировать
     static member RegisterExtensions : 
            outputFormat : FileConverterFormat * 
            outputExtension : string * 
            ?recommendedInputExtensions : IEnumerable<string> * 
            ?additionalInputExtensions : IEnumerable<string> 
    (* Defaults:
            let _recommendedInputExtensions = defaultArg recommendedInputExtensions null
            let _additionalInputExtensions = defaultArg additionalInputExtensions null
    *)
    -> unit 
#### Параметры
outputFormat
[FileConverterFormat](T_Tessa_FileConverters_FileConverterFormat.htm)
    Формат выходного файла, для которого выполняется регистрация.
outputExtension [String](https://learn.microsoft.com/dotnet/api/system.string)
     Расширение выходного файла без точки в нижнем регистре. Не должно быть равно null. 
recommendedInputExtensions
[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)<[String](https://learn.microsoft.com/dotnet/api/system.string)>
(Optional)
     Рекомендуемые поддерживаемые типы файлов для конвертации. Указываются расширения файлов в нижнем регистре без ведущей точки. 
additionalInputExtensions
[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)<[String](https://learn.microsoft.com/dotnet/api/system.string)>
(Optional)
     Дополнительные поддерживаемые типы файлов для конвертации. Не рекомендуется выполнять конвертацию с использованием этого формата, но конвертация возможна, если возникла необходимость. Указываются расширения файлов в нижнем регистре без ведущей точки. 
## __См. также
#### Ссылки
[FileConverterFormat - ](T_Tessa_FileConverters_FileConverterFormat.htm)
[Tessa.FileConverters - пространство имён](N_Tessa_FileConverters.htm)
