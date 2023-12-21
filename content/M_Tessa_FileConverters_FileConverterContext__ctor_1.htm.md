# FileConverterContext(String, String, IFileConverterRequest, IOperation,
CancellationToken) - конструктор
Создаёт экземпляр класса с указанием значений его свойств.
## __Definition
 **Пространство имён:** [Tessa.FileConverters](N_Tessa_FileConverters.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public FileConverterContext(
    	string inputFilePath,
    	string outputFilePath,
    	IFileConverterRequest request,
    	IOperation operation = null,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Sub New ( 
    	inputFilePath As String,
    	outputFilePath As String,
    	request As IFileConverterRequest,
    	Optional operation As IOperation = Nothing,
    	Optional cancellationToken As CancellationToken = Nothing
    )
C++ __Копировать
     public:
    FileConverterContext(
    	String^ inputFilePath, 
    	String^ outputFilePath, 
    	IFileConverterRequest^ request, 
    	IOperation^ operation = nullptr, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     new : 
            inputFilePath : string * 
            outputFilePath : string * 
            request : IFileConverterRequest * 
            ?operation : IOperation * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _operation = defaultArg operation null
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> FileConverterContext
#### Параметры
inputFilePath [String](https://learn.microsoft.com/dotnet/api/system.string)
    Путь к файлу для пребразования.
outputFilePath [String](https://learn.microsoft.com/dotnet/api/system.string)
    Путь к выходному файлу.
request
[IFileConverterRequest](T_Tessa_FileConverters_IFileConverterRequest.htm)
     Запрос на выполнение операции, в рамках которого выполняется конвертация. Не должен быть равен null. 
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
