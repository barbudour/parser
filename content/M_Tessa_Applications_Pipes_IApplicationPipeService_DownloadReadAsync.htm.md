# IApplicationPipeService.DownloadReadAsync - метод
##  __Definition
 **Пространство имён:**
[Tessa.Applications.Pipes](N_Tessa_Applications_Pipes.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
    ValueTask<byte[]> DownloadReadAsync(
    	int size,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Function DownloadReadAsync ( 
    	size As Integer,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask(Of Byte())
C++ __Копировать
    ValueTask<array<unsigned char>^> DownloadReadAsync(
    	int size, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     abstract DownloadReadAsync : 
            size : int * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<byte[]> 
#### Параметры
size [Int32](https://learn.microsoft.com/dotnet/api/system.int32)
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<[Byte](https://learn.microsoft.com/dotnet/api/system.byte)[]>
##  __См. также
#### Ссылки
[IApplicationPipeService -
](T_Tessa_Applications_Pipes_IApplicationPipeService.htm)
[Tessa.Applications.Pipes - пространство имён](N_Tessa_Applications_Pipes.htm)
