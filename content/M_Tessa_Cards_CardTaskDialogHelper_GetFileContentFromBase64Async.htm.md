# CardTaskDialogHelper.GetFileContentFromBase64Async - метод
Возвращает массив байт содержащий контент файла указанный в виде строки в
Base64.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static ValueTask<byte[]> GetFileContentFromBase64Async(
    	string base64,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Shared Function GetFileContentFromBase64Async ( 
    	base64 As String,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask(Of Byte())
C++ __Копировать
     public:
    static ValueTask<array<unsigned char>^> GetFileContentFromBase64Async(
    	String^ base64, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     static member GetFileContentFromBase64Async : 
            base64 : string * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<byte[]> 
#### Параметры
base64 [String](https://learn.microsoft.com/dotnet/api/system.string)
    Строка содержащая контент файла представленный в Base64.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<[Byte](https://learn.microsoft.com/dotnet/api/system.byte)[]>  
Массив байт содержащий контент файла.
##  __См. также
#### Ссылки
[CardTaskDialogHelper - ](T_Tessa_Cards_CardTaskDialogHelper.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
