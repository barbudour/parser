# ScanDialogViewModel.DeletePageAsync - метод
##  __Definition
 **Пространство имён:**
[Tessa.Extensions.Platform.Client.ViewModels](N_Tessa_Extensions_Platform_Client_ViewModels.htm)  
 **Сборка:** Tessa.UI (в Tessa.UI.dll) Версия: 3.6.0.17
C# __Копировать
     public ValueTask DeletePageAsync(
    	ScanPageViewModel page,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function DeletePageAsync ( 
    	page As ScanPageViewModel,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask
C++ __Копировать
     public:
    ValueTask DeletePageAsync(
    	ScanPageViewModel^ page, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     member DeletePageAsync : 
            page : ScanPageViewModel * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask 
#### Параметры
page
[ScanPageViewModel](T_Tessa_Extensions_Platform_Client_ViewModels_ScanPageViewModel.htm)
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
