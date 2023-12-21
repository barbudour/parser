# ScanDialogViewModel.OnClosedAsync - метод
##  __Definition
 **Пространство имён:**
[Tessa.Extensions.Platform.Client.ViewModels](N_Tessa_Extensions_Platform_Client_ViewModels.htm)  
 **Сборка:** Tessa.UI (в Tessa.UI.dll) Версия: 3.6.0.17
C# __Копировать
     protected override ValueTask OnClosedAsync(
    	DeferredEventArgs e,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Protected Overrides Function OnClosedAsync ( 
    	e As DeferredEventArgs,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask
C++ __Копировать
     protected:
    virtual ValueTask OnClosedAsync(
    	DeferredEventArgs^ e, 
    	CancellationToken cancellationToken = CancellationToken()
    ) override
F# __Копировать
     abstract OnClosedAsync : 
            e : DeferredEventArgs * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask 
    override OnClosedAsync : 
            e : DeferredEventArgs * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask 
#### Параметры
e [DeferredEventArgs](T_Tessa_Platform_DeferredEventArgs.htm)
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask)
##  __См. также
#### Ссылки
[ScanDialogViewModel -
](T_Tessa_Extensions_Platform_Client_ViewModels_ScanDialogViewModel.htm)
[Tessa.Extensions.Platform.Client.ViewModels - пространство
имён](N_Tessa_Extensions_Platform_Client_ViewModels.htm)
