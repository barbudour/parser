# IAsyncInitializable.InitializeAsync - метод
##  __Definition
 **Пространство имён:** [Chronos.Platform](N_Chronos_Platform.htm)  
 **Сборка:** Chronos.Platform (в Chronos.Platform.dll) Версия: 3.6.0.17
C# __Копировать
     ValueTask InitializeAsync(
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Function InitializeAsync ( 
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask
C++ __Копировать
     ValueTask InitializeAsync(
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     abstract InitializeAsync : 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask 
#### Параметры
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask)
##  __См. также
#### Ссылки
[IAsyncInitializable - ](T_Chronos_Platform_IAsyncInitializable.htm)
[Chronos.Platform - пространство имён](N_Chronos_Platform.htm)
