# IAppManagerApplication.IsFirstInstanceAsync - метод
Gets a value indicating whether Признак запуска первого экземпляра приложения
## __Definition
 **Пространство имён:** [Tessa.Applications](N_Tessa_Applications.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     ValueTask<bool> IsFirstInstanceAsync(
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Function IsFirstInstanceAsync ( 
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask(Of Boolean)
C++ __Копировать
     ValueTask<bool> IsFirstInstanceAsync(
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     abstract IsFirstInstanceAsync : 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<bool> 
#### Параметры
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)>
##  __См. также
#### Ссылки
[IAppManagerApplication - ](T_Tessa_Applications_IAppManagerApplication.htm)
[Tessa.Applications - пространство имён](N_Tessa_Applications.htm)
