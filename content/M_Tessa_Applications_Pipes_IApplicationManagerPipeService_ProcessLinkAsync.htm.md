# IApplicationManagerPipeService.ProcessLinkAsync - метод
##  __Definition
 **Пространство имён:**
[Tessa.Applications.Pipes](N_Tessa_Applications_Pipes.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     ValueTask ProcessLinkAsync(
    	string link,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Function ProcessLinkAsync ( 
    	link As String,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask
C++ __Копировать
     ValueTask ProcessLinkAsync(
    	String^ link, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     abstract ProcessLinkAsync : 
            link : string * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask 
#### Параметры
link [String](https://learn.microsoft.com/dotnet/api/system.string)
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask)
##  __См. также
#### Ссылки
[IApplicationManagerPipeService -
](T_Tessa_Applications_Pipes_IApplicationManagerPipeService.htm)
[Tessa.Applications.Pipes - пространство имён](N_Tessa_Applications_Pipes.htm)
