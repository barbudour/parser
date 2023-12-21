# FileConverterContext(String, String, String, String, IFileConverterRequest,
IOperation, CancellationToken) - конструктор
Создаёт экземпляр класса с указанием значений его свойств.
## __Definition
 **Пространство имён:** [Tessa.FileConverters](N_Tessa_FileConverters.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public FileConverterContext(
    	string inputFilePath,
    	string inputExtension,
    	string outputFilePath,
    	string outputExtension,
    	IFileConverterRequest request = null,
    	IOperation operation = null,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Sub New ( 
    	inputFilePath As String,
    	inputExtension As String,
    	outputFilePath As String,
    	outputExtension As String,
    	Optional request As IFileConverterRequest = Nothing,
    	Optional operation As IOperation = Nothing,
    	Optional cancellationToken As CancellationToken = Nothing
    )
C++ __Копировать
     public:
    FileConverterContext(
    	String^ inputFilePath, 
    	String^ inputExtension, 
    	String^ outputFilePath, 
    	String^ outputExtension, 
    	IFileConverterRequest^ request = nullptr, 
    	IOperation^ operation = nullptr, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     new : 
            inputFilePath : string * 
            inputExtension : string * 
            outputFilePath : string * 
            outputExtension : string * 
            ?request : IFileConverterRequest * 
            ?operation : IOperation * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _request = defaultArg request null
            let _operation = defaultArg operation null
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> FileConverterContext
#### Параметры
inputFilePath [String](https://learn.microsoft.com/dotnet/api/system.string)
    Путь к файлу для пребразования.
inputExtension [String](https://learn.microsoft.com/dotnet/api/system.string)
     Расширение для конвертируемого файла. Задаётся как расширение файла в нижнем регистре без ведущей точки. Преобразуется к нижнему регистру при необходимости. Может быть равно null или пустой строке, если у файла нет расширения. 
outputFilePath [String](https://learn.microsoft.com/dotnet/api/system.string)
    Путь к выходному файлу.
outputExtension [String](https://learn.microsoft.com/dotnet/api/system.string)
     Расширение для выходного формата файла. Задаётся как расширение файла в нижнем регистре без ведущей точки. Преобразуется к нижнему регистру при необходимости. Может быть равно null или пустой строке, если у файла нет расширения. 
request
[IFileConverterRequest](T_Tessa_FileConverters_IFileConverterRequest.htm)
(Optional)
     Запрос на выполнение операции, в рамках которого выполняется конвертация, или null, если запрос неизвестен или отсутствует. 
operation [IOperation](T_Tessa_Platform_Operations_IOperation.htm) (Optional)
     Операция, в рамках которой выполняется конвертация, или null, если операция неизвестна или отсутствует. 
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
##  __См. также
#### Ссылки
[FileConverterContext - ](T_Tessa_FileConverters_FileConverterContext.htm)
[FileConverterContext -
перегрузка](Overload_Tessa_FileConverters_FileConverterContext__ctor.htm)
[Tessa.FileConverters - пространство имён](N_Tessa_FileConverters.htm)
