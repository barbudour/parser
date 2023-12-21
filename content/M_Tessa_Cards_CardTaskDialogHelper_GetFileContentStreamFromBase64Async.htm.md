# CardTaskDialogHelper.GetFileContentStreamFromBase64Async - метод
Возвращает поток содержащий контент файла указанный в виде строки в Base64.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static ValueTask<Stream> GetFileContentStreamFromBase64Async(
    	string base64
    )
VB __Копировать
     Public Shared Function GetFileContentStreamFromBase64Async ( 
    	base64 As String
    ) As ValueTask(Of Stream)
C++ __Копировать
     public:
    static ValueTask<Stream^> GetFileContentStreamFromBase64Async(
    	String^ base64
    )
F# __Копировать
     static member GetFileContentStreamFromBase64Async : 
            base64 : string -> ValueTask<Stream> 
#### Параметры
base64 [String](https://learn.microsoft.com/dotnet/api/system.string)
    Строка содержащая контент файла представленный в Base64.
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<[Stream](https://learn.microsoft.com/dotnet/api/system.io.stream)>  
Поток содержащий контент файла.
##  __См. также
#### Ссылки
[CardTaskDialogHelper - ](T_Tessa_Cards_CardTaskDialogHelper.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
